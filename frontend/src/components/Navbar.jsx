import { useState } from 'react'
import { NavLink, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { useTheme } from '../context/ThemeContext'
import Icon from './Icon'
import './Navbar.css'

const NAV_LINKS = [
  { to: '/dashboard', label: 'Dashboard', icon: 'dashboard' },
  { to: '/explorer', label: 'Career Explorer', icon: 'compass' },
  { to: '/study-plans', label: 'Study Plans', icon: 'clock' },
  { to: '/assistant', label: 'AI Assistant', icon: 'bot' },
  { to: '/saved', label: 'Saved', icon: 'bookmark' },
]

export default function Navbar() {
  const { user, logout } = useAuth()
  const { theme, toggleTheme } = useTheme()
  const [menuOpen, setMenuOpen] = useState(false)
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate('/')
  }

  return (
    <header className="navbar glass">
      <div className="container navbar__inner">
        <NavLink to={user ? '/dashboard' : '/'} className="navbar__logo">
          <span className="navbar__logo-mark">CV</span>
          <span className="navbar__logo-text">CareerVerse</span>
        </NavLink>

        {user && (
          <nav className={`navbar__links ${menuOpen ? 'is-open' : ''}`}>
            {NAV_LINKS.map((link) => (
              <NavLink
                key={link.to}
                to={link.to}
                className={({ isActive }) => `navbar__link ${isActive ? 'is-active' : ''}`}
                onClick={() => setMenuOpen(false)}
              >
                <Icon name={link.icon} size={17} />
                {link.label}
              </NavLink>
            ))}
            {user.role === 'admin' && (
              <NavLink to="/admin" className={({ isActive }) => `navbar__link ${isActive ? 'is-active' : ''}`} onClick={() => setMenuOpen(false)}>
                <Icon name="shield" size={17} /> Admin
              </NavLink>
            )}
          </nav>
        )}

        <div className="navbar__actions">
          <button className="navbar__icon-btn" onClick={toggleTheme} aria-label="Toggle dark mode">
            <Icon name={theme === 'light' ? 'moon' : 'sun'} size={18} />
          </button>

          {user ? (
            <>
              <NavLink to="/profile" className="navbar__icon-btn" aria-label="Profile">
                <Icon name="user" size={18} />
              </NavLink>
              <button className="btn btn-secondary btn-sm" onClick={handleLogout}>
                <Icon name="logout" size={15} /> Logout
              </button>
              <button className="navbar__icon-btn navbar__menu-toggle" onClick={() => setMenuOpen((o) => !o)} aria-label="Toggle menu">
                <Icon name="menu" size={20} />
              </button>
            </>
          ) : (
            <>
              <NavLink to="/login" className="btn btn-ghost btn-sm">Log in</NavLink>
              <NavLink to="/register" className="btn btn-primary btn-sm">Get Started</NavLink>
            </>
          )}
        </div>
      </div>
    </header>
  )
}
