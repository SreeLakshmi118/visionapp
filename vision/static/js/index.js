const header = document.querySelector(".header .header-2");
const searchForm = document.querySelector(".search-form");
const searchBtn = document.getElementById("search-btn");
const loginForm = document.querySelector(".container-form");
const btnShowLoginForm = document.getElementById("login-btn");
const btnCloseLoginForm = document.getElementById("close-btn");
const loader = document.querySelector(".loader-container");

//stickyNav
window.onscroll = () => {
  searchForm.classList.remove("active");
  if (window.scrollY > 80) {
    header.classList.add("active");
  } else {
    header.classList.remove("active");
  }
};

window.onload = () => {
  if (window.scrollY > 80) {
    header.classList.add("active");
  } else {
    header.classList.remove("active");
  }
  fedOut();
};

//boooks swiper
var swiper = new Swiper(".books-slider", {
  loop: true,
  centerSlides: true,
  autoplay: {
    delay: 5500,
    disableOnInteraction: false,
  },
  breakpoints: {
    640: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});
//featured swiper
var swiper = new Swiper(".featured-slider", {
  loop: true,
  centerSlides: true,
  spaceBetween: 10,
  autoplay: {
    delay: 5500,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    450: {
      slidesPerView: 2,
    },
    768: {
      slidesPerView: 3,
    },
    1024: {
      slidesPerView: 4,
    },
  },
});
//arrival slider

var swiper = new Swiper(".arrivals-slider", {
  spaceBetween: 10,
  loop: true,
  centeredSlides: true,
  autoplay: {
    delay: 5500,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});
//client slider
var swiper = new Swiper(".reviews-slider", {
  spaceBetween: 10,
  grabCursor: true,
  loop: true,
  centeredSlides: true,
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});
//blog slider
var swiper = new Swiper(".blogs-slider", {
  spaceBetween: 10,
  grabCursor: true,
  loop: true,
  centeredSlides: true,
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});
//EventListener functions

const webSiteIntro = () => {
  loader.classList.add("active");
};

const fedOut = () => {
  setTimeout(webSiteIntro, 3990);
};
const formToogle = () => {
  searchForm.classList.toggle("active");
};
const showLoginForm = () => {
  loginForm.classList.toggle("active");
};

const closeLoginForm = () => {
  loginForm.classList.remove("active");
};

//EventListener
searchBtn.addEventListener("click", formToogle);
btnShowLoginForm.addEventListener("click", showLoginForm);
btnCloseLoginForm.addEventListener("click", closeLoginForm);
