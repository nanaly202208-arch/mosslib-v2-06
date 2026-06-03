// 轮播逻辑
const slidesEl = document.getElementById('carouselSlides');
const slideItems = [...document.querySelectorAll('.carousel-slide')];
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const dotsContainer = document.getElementById('dotsContainer');
let currentIdx = 0;
const total = slideItems.length;

function updateDotsUI() {
    const dots = document.querySelectorAll('.carousel-dot');
    dots.forEach((dot, i) => {
        if(i === currentIdx) dot.classList.add('active');
        else dot.classList.remove('active');
    });
}
function goToSlide(idx) {
    if(idx < 0) idx = total - 1;
    if(idx >= total) idx = 0;
    currentIdx = idx;
    slidesEl.style.transform = `translateX(-${currentIdx * 100}%)`;
    updateDotsUI();
}
function buildDots() {
    dotsContainer.innerHTML = '';
    for(let i=0; i<total; i++) {
        const dot = document.createElement('button');
        dot.classList.add('carousel-dot');
        if(i === currentIdx) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(i));
        dotsContainer.appendChild(dot);
    }
}
prevBtn.addEventListener('click', () => goToSlide(currentIdx - 1));
nextBtn.addEventListener('click', () => goToSlide(currentIdx + 1));
buildDots();
let interval = setInterval(() => goToSlide(currentIdx + 1), 5000);
const carousel = document.querySelector('.carousel-container');
carousel.addEventListener('mouseenter', () => clearInterval(interval));
carousel.addEventListener('mouseleave', () => { interval = setInterval(() => goToSlide(currentIdx + 1), 5000); });

// 左侧实体点击反馈
document.querySelectorAll('.entity').forEach(el => {
    el.addEventListener('click', (e) => {
        e.preventDefault();
        const panel = document.querySelector('.detail-panel-light');
        if(panel) {
            panel.style.boxShadow = 'inset 0 0 0 2px #605CE5, 0 0 0 2px rgba(96,92,229,0.2)';
            setTimeout(() => panel.style.boxShadow = '', 800);
        }
    });
});
