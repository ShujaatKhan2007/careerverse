import { Link } from 'react-router-dom'

export default function Footer() {
  return (
    <footer style={{ borderTop: '1px solid var(--border-color)', marginTop: 80, padding: '32px 0' }}>
      <div className="container" style={{ display: 'flex', justifyContent: 'space-between', flexWrap: 'wrap', gap: 16 }}>
        <div>
          <p style={{ margin: 0, fontSize: 13 }}>© {new Date().getFullYear()} CareerVerse. Discover Your Career. Build Your Future.</p>
          <p style={{ margin: '4px 0 0', fontSize: 12, color: 'var(--text-secondary)' }}>Developed by Shujaat Khan</p>
        </div>
        <div style={{ display: 'flex', gap: 20 }}>
          <Link to="/explorer" style={{ fontSize: 13, color: 'var(--text-secondary)' }}>Career Explorer</Link>
          <Link to="/assistant" style={{ fontSize: 13, color: 'var(--text-secondary)' }}>AI Assistant</Link>
        </div>
      </div>
    </footer>
  )
}
