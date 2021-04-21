import React from 'react'

import { Link, NavLink } from 'react-router-dom'

export default function Header(props) {
    return (
        <header id="header" className="fixed-top d-flex align-items-center">
            <div className="container d-flex align-items-center">

                <NavLink to="/" className="logo me-auto"><img src="assets/img/Mr.VaiBH_strip.png" alt="" className="img-fluid" /></NavLink>
                {/* Uncomment below if you prefer to use a text logo */}
                {/* <h1 className="logo me-auto"><NavLink to="index.html">Sailor</NavLink></h1> */}

                <nav id="navbar" className="navbar">
                    <ul>
                        <li><NavLink exact to="/" activeClassName="active">Home</NavLink></li>

                        <li className="dropdown"><Link to="#"><span>About</span> <i className="bi bi-chevron-down"></i></Link>
                            <ul>
                                <li><NavLink to="/about" activeClassName="active">About</NavLink></li>
                                <li><NavLink to="/team" activeClassName="active">Team</NavLink></li>
                                <li><NavLink to="/testimonials" activeClassName="active">Testimonials</NavLink></li>

                                {/* <li className="dropdown"><NavLink to="#"><span>Deep Drop Down</span> <i className="bi bi-chevron-right"></i></NavLink>
                                    <ul>
                                    <li><NavLink to="#" >Deep Drop Down 1</NavLink></li>
                                    <li><NavLink to="#" >Deep Drop Down 2</NavLink></li>
                                    <li><NavLink to="#" >Deep Drop Down 3</NavLink></li>
                                    <li><NavLink to="#" >Deep Drop Down 4</NavLink></li>
                                    <li><NavLink to="#" >Deep Drop Down 5</NavLink></li>
                                    </ul>
                                </li> */}
                            </ul>
                        </li>
                        <li><NavLink to="/services" activeClassName="active">Services</NavLink></li>
                        <li><NavLink to="/portfolio" activeClassName="active">Portfolio</NavLink></li>
                        <li><NavLink to="/pricing" activeClassName="active">Pricing</NavLink></li>
                        <li><NavLink to="/blog" activeClassName="active">Blog</NavLink></li>

                        <li><NavLink to="/contact" activeClassName="active">Contact</NavLink></li>
                        <li><Link to="/" className="getstarted">Get Started</Link></li>
                    </ul>
                    <i className="bi bi-list mobile-nav-toggle"></i>
                </nav> {/* .navbar */}

            </div>
        </header>
    )
}
