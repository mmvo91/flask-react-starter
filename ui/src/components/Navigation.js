import React from 'react'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'

const Navigation = () => {
    return (
        <Navbar collapseOnSelect expand="sm" bg="secondary" variant="dark" className="sticky-top">
            <Navbar.Brand href="/">
                {'App Name'}
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
            <Navbar.Collapse className="text-center" id="responsive-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link href={"/"}>Home</Nav.Link>
                </Nav>
                <Nav>
                    <Nav.Link href={"/"}>Logout</Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    )
};

export default Navigation