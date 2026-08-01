import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import api, { getErrorMessage } from '../services/api'
import { useToast } from '../context/ToastContext'
import Icon from '../components/Icon'
import LoadingSpinner from '../components/LoadingSpinner'
import EmptyState from '../components/EmptyState'

export default function SavedCareers() {
  const [saved, setSaved] = useState([])
  const [loading, setLoading] = useState(true)
  const { showToast } = useToast()

  const load = () => {
    setLoading(true)
    api.get('/api/saved-careers').then(({ data }) => setSaved(data)).catch(() => {}).finally(() => setLoading(false))
  }

  useEffect(() => { load() }, [])

  const remove = async (slug) => {
    try {
      await api.delete(`/api/saved-careers/${slug}`)
      setSaved((prev) => prev.filter((s) => s.career.slug !== slug))
      showToast('Removed from saved careers')
    } catch (err) {
      showToast(getErrorMessage(err), 'error')
    }
  }

  if (loading) return <LoadingSpinner fullPage />

  return (
    <div className="container" style={{ padding: '32px 24px 60px' }}>
      <div style={{ marginBottom: 24 }}>
        <h1 style={{ fontSize: 26 }}>Saved Careers</h1>
        <p>Careers you've bookmarked for later exploration.</p>
      </div>

      {saved.length === 0 ? (
        <EmptyState icon="bookmark" title="No saved careers yet"
          description="Browse the Career Explorer and tap the bookmark icon on any career to save it here."
          action={<Link to="/explorer" className="btn btn-primary">Explore Careers</Link>} />
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 20 }} className="saved-grid">
          {saved.map((s) => (
            <div key={s.saved_id} className="card card--hover" style={{ padding: 22 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 10 }}>
                <Icon name={s.career.icon} size={22} color="var(--color-primary)" />
                <button onClick={() => remove(s.career.slug)} aria-label="Remove" style={{ background: 'none', border: 'none' }}>
                  <Icon name="trash" size={16} color="var(--color-error)" />
                </button>
              </div>
              <h3 style={{ fontSize: 16 }}>{s.career.title}</h3>
              <p style={{ fontSize: 13, minHeight: 36 }}>{s.career.short_description}</p>
              <Link to={`/career/${s.career.slug}`} className="btn btn-secondary btn-sm btn-block">
                View Details
              </Link>
            </div>
          ))}
        </div>
      )}
      <style>{`@media (max-width: 900px) { .saved-grid { grid-template-columns: 1fr !important; } }`}</style>
    </div>
  )
}
