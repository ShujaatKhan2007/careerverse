import { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import api from '../services/api'
import Icon from '../components/Icon'
import LoadingSpinner from '../components/LoadingSpinner'
import './Dashboard.css'

const QUICK_ACTIONS = [
  { to: '/guidance', icon: 'compass', title: 'Find My Career', desc: 'Get personalized career guidance', color: '#2563EB' },
  { to: '/explorer', icon: 'search', title: 'Explore Careers', desc: 'Browse all career paths', color: '#4F46E5' },
  { to: '/compare', icon: 'chart', title: 'Compare Careers', desc: 'Side-by-side comparison', color: '#10B981' },
  { to: '/assistant', icon: 'bot', title: 'Ask AI Assistant', desc: 'Get instant answers', color: '#F59E0B' },
]

function timeAgo(dateStr) {
  const diff = (Date.now() - new Date(dateStr)) / 1000
  if (diff < 60) return 'just now'
  if (diff < 3600) return `${Math.floor(diff / 60)}m ago`
  if (diff < 86400) return `${Math.floor(diff / 3600)}h ago`
  return `${Math.floor(diff / 86400)}d ago`
}

export default function Dashboard() {
  const { user } = useAuth()
  const [summary, setSummary] = useState(null)
  const [savedCareers, setSavedCareers] = useState([])
  const [loading, setLoading] = useState(true)
  const [search, setSearch] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    let mounted = true
    Promise.all([
      api.get('/api/users/dashboard-summary'),
      api.get('/api/saved-careers'),
    ]).then(([sRes, savedRes]) => {
      if (!mounted) return
      setSummary(sRes.data)
      setSavedCareers(savedRes.data.slice(0, 3))
    }).catch(() => {}).finally(() => mounted && setLoading(false))
    return () => { mounted = false }
  }, [])

  const handleSearch = (e) => {
    e.preventDefault()
    if (search.trim()) navigate(`/explorer?search=${encodeURIComponent(search.trim())}`)
  }

  if (loading) return <LoadingSpinner fullPage />

  return (
    <div className="container dashboard fade-in">
      <div className="dashboard__greeting">
        <div>
          <h1 style={{ fontSize: 28, marginBottom: 4 }}>
            {getGreeting()}, {user?.name?.split(' ')[0]} 👋
          </h1>
          <p>Let's continue building your future today.</p>
        </div>
      </div>

      <form onSubmit={handleSearch} className="dashboard__search">
        <Icon name="search" size={18} color="var(--text-secondary)" />
        <input
          className="dashboard__search-input"
          placeholder="Search careers — e.g. 'data scientist', 'doctor', 'lawyer'..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <button type="submit" className="btn btn-primary btn-sm">Search</button>
      </form>

      <div className="dashboard__quick-actions">
        {QUICK_ACTIONS.map((a) => (
          <Link to={a.to} key={a.to} className="card card--hover dashboard__quick-card">
            <div className="dashboard__quick-icon" style={{ background: `${a.color}18` }}>
              <Icon name={a.icon} size={22} color={a.color} />
            </div>
            <div>
              <h3 style={{ fontSize: 15 }}>{a.title}</h3>
              <p style={{ fontSize: 13 }}>{a.desc}</p>
            </div>
          </Link>
        ))}
      </div>

      <div className="dashboard__grid">
        <div className="card dashboard__progress">
          <div className="section-title"><h3 style={{ fontSize: 16 }}>Your Progress</h3></div>
          <div className="dashboard__stats">
            <Stat label="Careers Explored" value={summary?.careers_explored_count ?? 0} icon="compass" />
            <Stat label="Saved Careers" value={summary?.saved_careers_count ?? 0} icon="bookmark" />
            <Stat label="Study Plans" value={summary?.study_plans_count ?? 0} icon="clock" />
          </div>
          <div style={{ marginTop: 18 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 13, marginBottom: 6 }}>
              <span>Overall study progress</span>
              <span style={{ fontWeight: 700 }}>{summary?.overall_progress_pct ?? 0}%</span>
            </div>
            <div className="progress-track"><div className="progress-fill" style={{ width: `${summary?.overall_progress_pct ?? 0}%` }} /></div>
          </div>
        </div>

        <div className="card">
          <div className="section-title">
            <h3 style={{ fontSize: 16 }}>Recent Activity</h3>
          </div>
          {summary?.recent_activity?.length ? (
            <ul className="dashboard__activity-list">
              {summary.recent_activity.map((a) => (
                <li key={a._id}>
                  <Icon name="compass" size={15} color="var(--color-primary)" />
                  <span>Explored guidance for <strong>{a.input?.dream_career}</strong></span>
                  <span className="dashboard__activity-time">{timeAgo(a.created_at)}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p style={{ fontSize: 13.5 }}>No activity yet. Try the career guidance flow to get started!</p>
          )}
        </div>
      </div>

      <div className="section-title" style={{ marginTop: 32 }}>
        <h3 style={{ fontSize: 18 }}>Saved Careers</h3>
        <Link to="/saved" style={{ fontSize: 13.5, fontWeight: 600 }}>View all →</Link>
      </div>
      {savedCareers.length ? (
        <div className="dashboard__saved-grid">
          {savedCareers.map((s) => (
            <Link to={`/career/${s.career.slug}`} key={s.saved_id} className="card card--hover dashboard__saved-card">
              <Icon name={s.career.icon} size={20} color="var(--color-primary)" />
              <span>{s.career.title}</span>
            </Link>
          ))}
        </div>
      ) : (
        <p style={{ fontSize: 13.5 }}>You haven't saved any careers yet. <Link to="/explorer">Browse the Career Explorer</Link>.</p>
      )}
    </div>
  )
}

function Stat({ label, value, icon }) {
  return (
    <div className="dashboard__stat">
      <Icon name={icon} size={18} color="var(--color-primary)" />
      <div>
        <div className="dashboard__stat-value">{value}</div>
        <div className="dashboard__stat-label">{label}</div>
      </div>
    </div>
  )
}

function getGreeting() {
  const hour = new Date().getHours()
  if (hour < 12) return 'Good morning'
  if (hour < 18) return 'Good afternoon'
  return 'Good evening'
}
