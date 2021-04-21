import React from 'react'

export default function Footer() {
    return (
        <footer id="footer">
            <div className="footer-top">
                <div className="container">
                    <div className="row">

                        <div className="col-lg-3 col-md-6">
                            <div className="footer-info">
                                <h3>MRVAIBH</h3>
                                <p>
                                    Sec-23, Dwarka <br />
                                    ND - 110077, India<br /><br />
                                    <strong>Phone:</strong> +91 745 795 78XX<br />
                                    <strong>Email:</strong> mrvaibh0@gmail.com<br />
                                </p>
                                <div className="social-links mt-3">
                                    <a href="https://twitter.com/MrVaiBH0" className="twitter"><i className="bx bxl-twitter"></i></a>
                                    <a href="https://www.facebook.com/MrVaiBH0" className="facebook"><i className="bx bxl-facebook"></i></a>
                                    <a href="https://www.instagram.com/mrvaibh0" className="instagram"><i className="bx bxl-instagram"></i></a>
                                    <a href="https://github.com/mr-vaibh" className="google-plus"><i className="bx bxl-github"></i></a>
                                    <a href="https://www.linkedin.com/in/mrvaibh" className="linkedin"><i className="bx bxl-linkedin"></i></a>
                                </div>
                            </div>
                        </div>

                        <div className="col-lg-2 col-md-6 footer-links">
                            <h4>Useful Links</h4>
                            <ul>
                                <li><i className="bx bx-chevron-right"></i> <a href="#">Home</a></li>
                                <li><i className="bx bx-chevron-right"></i> <a href="#">About us</a></li>
                                <li><i className="bx bx-chevron-right"></i> <a href="#">Services</a></li>
                                <li><i className="bx bx-chevron-right"></i> <a href="#">Terms of service</a></li>
                                <li><i className="bx bx-chevron-right"></i> <a href="#">Privacy policy</a></li>
                            </ul>
                        </div>

                        <div className="col-lg-3 col-md-6 footer-links">
                            <h4>Our Services</h4>
                            <ul>
                                <li><i className="bx bx-chevron-right"></i> <a href="#">Web Design</a></li>
                                <li><i className="bx bx-chevron-right"></i> <a href="#">Web Development</a></li>
                                <li><i className="bx bx-chevron-right"></i> <a href="#">Product Management</a></li>
                                <li><i className="bx bx-chevron-right"></i> <a href="#">Marketing</a></li>
                                <li><i className="bx bx-chevron-right"></i> <a href="#">Graphic Design</a></li>
                            </ul>
                        </div>

                        <div className="col-lg-4 col-md-6 footer-newsletter">
                            <h4>Our Newsletter</h4>
                            <p>Get in touch if you like to stay updated with recent news, services, projects and more 🙂</p>
                            <form action="" method="post">
                                <input type="email" name="email" /><input type="submit" value="Subscribe" />
                            </form>

                        </div>

                    </div>
                </div>
            </div>

            <div className="container">
                <div className="copyright">
                    &copy; 2021 <strong><span>MRVAIBH</span></strong>. All Rights Reserved
                </div>
                <div className="credits" style={{display: 'none'}}>
                    {/* All the links in the footer should remain intact. */}
                    {/* You can delete the links only if you purchased the pro version. */}
                    {/* Licensing information: https://bootstrapmade.com/license/ */}
                    {/* Purchase the pro version with working PHP/AJAX contact form: https://bootstrapmade.com/sailor-free-bootstrap-theme/ */}
                    Designed by <a href="https://bootstrapmade.com/">BootstrapMade</a>
                </div>
            </div>
        </footer>
    )
}
