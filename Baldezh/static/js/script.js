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

