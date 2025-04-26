import { Link } from 'react-router-dom';

function Header() {
    return (
        <header className="fixed top-0 left-0 w-full bg-white shadow-md p-4 flex justify-between items-center z-10">
            <img
                src="/static/images/logo.png"
                alt="HBNB Logo"
                className="h-12"
            />
            <nav>
                <Link
                    to="/login"
                    className="mx-2 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
                >
                    Login
                </Link>
                <Link
                    to="/"
                    className="mx-2 text-blue-600 hover:underline"
                >
                    Main
                </Link>
            </nav>
        </header>
    );
}

export default Header;