document.addEventListener("DOMContentLoaded", function() {
    var modal = document.getElementById("modal");
    var modalImg = document.getElementById("modal-image");
    var captionText = document.getElementById("caption");
    var images = document.getElementsByClassName("gallery-img");
    var closeBtn = document.getElementsByClassName("close")[0];
    var currentImageIndex;

    Array.from(images).forEach((img, index) => {
        img.onclick = function() {
            modal.style.display = "block";
            modalImg.src = this.src;
            captionText.innerHTML = this.alt;
            currentImageIndex = index;
        }
    });

    closeBtn.onclick = function() {
        modal.style.display = "none";
    }

    document.addEventListener('keydown', function(event) {
        if (event.key === "Escape") {
            modal.style.display = "none";
        }
    });

    function navigate(direction) {
        currentImageIndex = (currentImageIndex + direction + images.length) % images.length;
        modalImg.src = images[currentImageIndex].src;
        captionText.innerHTML = images[currentImageIndex].alt;
    }

    document.querySelector('.prev').addEventListener('click', () => navigate(-1));
    document.querySelector('.next').addEventListener('click', () => navigate(1));
});

document.addEventListener("DOMContentLoaded", function() {
    const slides = document.querySelectorAll(".slide");
    let currentIndex = 0;

    function showSlide(index) {
        console.log(`Attempting to show slide at index ${index}`);
        
        slides.forEach((slide, idx) => {
            slide.classList.remove('active');
            slide.style.display = 'none';
            console.log(`Slide ${idx} hidden`);
        });

        if (slides[index]) {
            slides[index].classList.add('active');
            slides[index].style.display = 'flex';
            console.log(`Slide ${index} is now active and displayed`);
        } else {
            console.error('No slide found at index', index);
        }
    }

    showSlide(currentIndex); // Показываем первый слайд при загрузке

    document.querySelector('.prev-service').addEventListener('click', function() {
        console.log('Previous service button clicked');
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(currentIndex);
    });

    document.querySelector('.next-service').addEventListener('click', function() {
        console.log('Next service button clicked');
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    });
});
document.addEventListener("DOMContentLoaded", function() {
    document.body.addEventListener('click', function(event) {
        if (event.target.classList.contains('arrow-icon')) {
            const info = event.target.nextElementSibling;
            const container = event.target.parentNode;

            if (info.style.display === 'none' || info.style.display === '') {
                info.style.display = 'block'; // Показать блок
            } else {
                info.style.display = 'none'; // Скрыть блок
            }
        }
    });
});