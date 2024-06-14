let currentIndex = 0;
const images = document.querySelectorAll('.thumbnails img');
const mainImage = document.getElementById('currentImage');

function showImage(index) {
    currentIndex = index;
    mainImage.src = images[currentIndex].src;
    highlightThumbnail(currentIndex);
}

function changeSlide(step) {
    currentIndex += step;
    if (currentIndex >= images.length) {
        currentIndex = 0;
    } else if (currentIndex < 0) {
        currentIndex = images.length - 1;
    }
    showImage(currentIndex);
}

function highlightThumbnail(index) {
    images.forEach(img => img.classList.remove('active'));
    images[index].classList.add('active');
}

document.addEventListener('DOMContentLoaded', () => {
    showImage(currentIndex);
});


document.addEventListener('DOMContentLoaded', () => {
    const tagInput = document.getElementById('tag-input');
    const suggestions = document.getElementById('suggestions');
    const selectedTags = document.getElementById('selected-tags');

    tagInput.addEventListener('input', () => {
        const inputValue = tagInput.value.toLowerCase();
        suggestions.innerHTML = '';
        if (inputValue) {
            fetchCategories(inputValue);
        } else {
            suggestions.style.display = 'none';
        }
    });

    function fetchCategories(query) {
        fetch(`/catalog/get-categories/?query=${encodeURIComponent(query)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(categories => {
                suggestions.innerHTML = '';
                categories.forEach(category => {
                    const li = document.createElement('li');
                    li.textContent = category.name;
                    li.addEventListener('click', () => {
                        addCategory(category.name);
                        tagInput.value = '';
                        suggestions.innerHTML = '';
                    });
                    suggestions.appendChild(li);
                });
                suggestions.style.display = 'block';
            })
            .catch(error => {
                console.error('Error fetching categories:', error);
            });
    }

    function addCategory(category) {
        if (![...selectedTags.children].some(child => child.firstChild.textContent === category)) {
            const tagElement = document.createElement('div');
            tagElement.className = 'tag';
            tagElement.innerHTML = `<span>${category}</span><button class="remove-tag">&times;</button>`;
            tagElement.querySelector('.remove-tag').addEventListener('click', () => {
                selectedTags.removeChild(tagElement);
            });
            selectedTags.appendChild(tagElement);
        }
    }

    document.addEventListener('click', (e) => {
        if (!tagInput.contains(e.target) && !suggestions.contains(e.target)) {
            suggestions.style.display = 'none';
        }
    });
});
