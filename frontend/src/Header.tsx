import React, { useState, useEffect } from 'react'
import { Navbar, Nav, Container, NavDropdown } from 'react-bootstrap';
import { Link, Router } from "react-router-dom";
import './App.css'
import logo from './assets/next.svg'
import AddFoods from './AddFoods'
import App from './App'

function Header() {
    return (
            <Navbar bg="light" expand="lg">
                <Container>
                    <Navbar.Brand href="/">
                        <img
                            alt=""
                            src={logo}
                            width="50"
                            height="50"
                        />{' '}
                        Sukkertoppens kantine
                    </Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <Nav.Link as={Link} to={"/"}>Hjem</Nav.Link>
                            <Nav.Link as={Link} to={"/"}>Ugensmenu</Nav.Link>
                            <Nav.Link as={Link} to={"/add"}>tilføj</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
    );
}

export default Header;
