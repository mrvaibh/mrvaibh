import React, { useState } from 'react'


const slidesData = [
    {
        img: "assets/img/slide/slide-1.jpg",
        title: "perfection at peak.",
        para: "We're working to turn our passion 👏 for creations into a booming online store. We hope you enjoy our products as much as we enjoy offering them to you.",
    },
    {
        img: "assets/img/slide/slide-2.jpg",
        title: "Lorem, ipsum dolor.",
        para: "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fugiat saepe ullam quisquam enim corporis consequatur voluptas porro quia vero eligendi.",
    },
    {
        img: "assets/img/slide/slide-3.jpg",
        title: "Lorem ipsum dolor sit.",
        para: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid laborum eligendi delectus corrupti numquam molestiae sit, eveniet quidem vero aperiam cum sequi rem doloribus officiis tempore ab inventore ullam excepturi atque perferendis nemo amet enim! Minima iure ducimus voluptate esse.",
    },
]

export default function HeroSection() {
    // Using HOOK to change slide index
    const [currentSlide, setCurrentSlide] = useState(0)
    // Here length is the length of the slidesData array
    const length = slidesData.length

    // Slider Control functions
    const prevSlide = () => {
        setCurrentSlide(currentSlide === 0 ? length - 1 : currentSlide - 1)
    }
    const nextSlide = () => {
        setCurrentSlide(currentSlide === length - 1 ? 0 : currentSlide + 1)
    }

    /* TODO:
    1. Add a timer
    2. Add a keybinding control for slider 

    // setTimeout(() => {
    //     nextSlide()
    // }, 5000);
    
    */


    // Checking if slideData is not empty
    if (!Array.isArray(slidesData) || length <= 0) {
        return null
    }

    return (
        <section id="hero">
            <div id="heroCarousel" className="slide">

                <ol className="carousel-indicators" id="hero-carousel-indicators">
                    {slidesData.forEach((index) => {

                        {
                            index === currentSlide && (
                                <li data-bs-target='#heroCarousel' data-bs-slide-to={index} key={index} className={index === currentSlide ? "active" : ""} ></li>
                            )
                        }
                    }
                    )}
                </ol>

                <div className="carousel-inner" role="listbox">

                    {/* Slides - iterating through all the objects in the array*/}
                    {slidesData.map((slide, index) => (
                        <div className={index === currentSlide ? "carousel-item active" : "carousel-item"} key={index} style={{ backgroundImage: `url(${slide.img})` }}>

                            {index === currentSlide && (
                                <div className="carousel-container">
                                    <div className="container">
                                        <h2 className="carousel-title animate__animated animate__fadeInDown">{slide.title}</h2>
                                        <p className="carousel-para animate__animated animate__fadeInUp">{slide.para}</p>
                                        <a href="#about" className="btn-get-started animate__animated animate__fadeInUp scrollto">Learn More</a>
                                    </div>
                                </div>
                            )}


                        </div>
                    )
                    )}


                </div>

                {/* Slider Controls */}
                <a className="carousel-control-prev" role="button" onClick={prevSlide}>
                    <span className="carousel-control-prev-icon bi bi-chevron-left" aria-hidden="true"></span>
                </a>

                <a className="carousel-control-next" role="button" onClick={nextSlide}>
                    <span className="carousel-control-next-icon bi bi-chevron-right" aria-hidden="true"></span>
                </a>

            </div>
            <script src="/assets/js/main.js"></script>

        </section>
    )
}
