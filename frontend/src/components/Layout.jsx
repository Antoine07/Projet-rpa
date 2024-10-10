import { Link, Outlet } from 'react-router-dom'

import './Layout.css'

const Layout = () => {
    return (
        <div className="app">
            <nav>
                <ul className='main-menu'>
                    <li><Link to="/">Accueil</Link></li>
                    <li><Link to="/invoices">Invoices</Link></li>
                </ul>
            </nav>
            <div className="main-content">
                <Outlet />
            </div>
            <footer className="footer">
                &copy; 2024 Mon Site
            </footer>
        </div>
    );
};

export default Layout