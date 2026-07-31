import { useEffect, useState } from 'react'
import api, { getErrorMessage } from '../services/api'
import { useToast } from '../context/ToastContext'
import Icon from '../components/Icon'
import LoadingSpinner from '../components/LoadingSpinner'
import './AdminDashboard.css'

const TABS = ['Overview', 'Users', 'Careers']

export default function AdminDashboard() {
  const [tab, setTab] = useState('Overview')
  const [stats, setStats] = useState(null)
  const [users, setUsers] = useState([])
  const [careers, setCareers] = useState([])
  const [loading, setLoading] = useState(true)
  const { showToast } = useToast()

  const loadAll = () => {
    setLoading(true)
    Promise.all([
      api.get('/api/admin/stats'),
      api.get('/api/admin/users'),
      api.get('/api/careers'),
    ]).then(([s, u, c]) => { setStats(s.data); setUsers(u.data); setCareers(c.data) })
      .catch((err) => showToast(getErrorMessage(err), 'error'))
      .finally(() => setLoading(false))
  }

  useEffect(() => { loadAll() }, [])

  const deleteUser = async (id) => {
    if (!confirm('Delete this user permanently?')) return
    try {
      await api.delete(`/api/admin/users/${id}`)
      setUsers((prev) => prev.filter((u) => u._id !== id))
      showToast('User deleted')
    } catch (err) {
      showToast(getErrorMessage(err), 'error')
    }
  }

  const deleteCareer = async (slug) => {
    if (!confirm('Delete this career from the platform?')) return
    try {
      await api.delete(`/api/admin/careers/${slug}`)
      setCareers((prev) => prev.filter((c) => c.slug !== slug))
      showToast('Career deleted')
    } catch (err) {
      showToast(getErrorMessage(err), 'error')
    }
  }

  if (loading) return <LoadingSpinner fullPage />

  return (
    <div className="container" style={{ padding: '32px 24px 60px' }}>
      <h1 style={{ fontSize: 26 }}>Admin Dashboard</h1>
      <p style={{ marginBottom: 24 }}>Platform analytics, user management, and content control.</p>

      <div className="admin-page__tabs">
        {TABS.map((t) => (
          <button key={t} className={`admin-page__tab ${tab === t ? 'is-active' : ''}`} onClick={() => setTab(t)}>{t}</button>
        ))}
      </div>

      {tab === 'Overview' && stats && (
        <div className="fade-in">
          <div className="admin-page__stats-grid">
            <StatBlock icon="user" label="Total Users" value={stats.total_users} />
            <StatBlock icon="compass" label="Total Careers" value={stats.total_careers} />
            <StatBlock icon="chart" label="Guidance Requests" value={stats.total_guidance_requests} />
            <StatBlock icon="clock" label="Study Plans" value={stats.total_study_plans} />
            <StatBlock icon="bot" label="Chat Sessions" value={stats.total_chat_sessions} />
          </div>

          <div className="card" style={{ padding: 22, marginTop: 24 }}>
            <h3 style={{ fontSize: 16, marginBottom: 14 }}>Top Requested Careers</h3>
            {stats.top_requested_careers?.length ? (
              <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: 10 }}>
                {stats.top_requested_careers.map((c) => (
                  <li key={c._id} style={{ display: 'flex', justifyContent: 'space-between', fontSize: 14 }}>
                    <span>{c._id || 'Unknown'}</span>
                    <span style={{ fontWeight: 700 }}>{c.count} requests</span>
                  </li>
                ))}
              </ul>
            ) : <p>No data yet.</p>}
          </div>
        </div>
      )}

      {tab === 'Users' && (
        <div className="admin-page__table-wrap fade-in">
          <table className="admin-page__table">
            <thead><tr><th>Name</th><th>Email</th><th>Role</th><th></th></tr></thead>
            <tbody>
              {users.map((u) => (
                <tr key={u._id}>
                  <td>{u.name}</td>
                  <td>{u.email}</td>
                  <td><span className={`badge ${u.role === 'admin' ? 'badge-hard' : 'badge-easy'}`}>{u.role}</span></td>
                  <td>
                    {u.role !== 'admin' && (
                      <button onClick={() => deleteUser(u._id)} style={{ background: 'none', border: 'none' }} aria-label="Delete user">
                        <Icon name="trash" size={16} color="var(--color-error)" />
                      </button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {tab === 'Careers' && (
        <div className="admin-page__table-wrap fade-in">
          <table className="admin-page__table">
            <thead><tr><th>Title</th><th>Category</th><th>Difficulty</th><th></th></tr></thead>
            <tbody>
              {careers.map((c) => (
                <tr key={c.slug}>
                  <td>{c.title}</td>
                  <td>{c.category}</td>
                  <td>{c.difficulty}</td>
                  <td>
                    <button onClick={() => deleteCareer(c.slug)} style={{ background: 'none', border: 'none' }} aria-label="Delete career">
                      <Icon name="trash" size={16} color="var(--color-error)" />
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <p style={{ fontSize: 12.5, color: 'var(--text-secondary)', padding: '14px 4px' }}>
            New careers can be added via the API (<code>POST /api/admin/careers</code>) or by extending <code>app/data/careers_data.py</code> and re-running the seed script.
          </p>
        </div>
      )}
    </div>
  )
}

function StatBlock({ icon, label, value }) {
  return (
    <div className="card admin-page__stat-block">
      <div className="admin-page__stat-icon"><Icon name={icon} size={20} color="var(--color-primary)" /></div>
      <div>
        <div style={{ fontSize: 22, fontWeight: 800, fontFamily: 'var(--font-display)' }}>{value}</div>
        <div style={{ fontSize: 12.5, color: 'var(--text-secondary)' }}>{label}</div>
      </div>
    </div>
  )
}
