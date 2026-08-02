import { useEffect, useState, useCallback } from 'react'
import { useSearchParams } from 'react-router-dom'
import api, { getErrorMessage } from '../services/api'
import { useToast } from '../context/ToastContext'
import CareerCard from '../components/CareerCard'
import LoadingSpinner from '../components/LoadingSpinner'
import EmptyState from '../components/EmptyState'
import Icon from '../components/Icon'

export default function CareerExplorer() {
  const [searchParams, setSearchParams] = useSearchParams()
  const [careers, setCareers] = useState([])
  const [categories, setCategories] = useState([])
  const [savedSlugs, setSavedSlugs] = useState(new Set())
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const { showToast } = useToast()

  const search = searchParams.get('search') || ''
  const category = searchParams.get('category') || ''

  const loadCareers = useCallback(async () => {
    setLoading(true)
    setError('')
    try {
      const params = {}
      if (search) params.search = search
      if (category) params.category = category
      const { data } = await api.get('/api/careers', { params })
      setCareers(data)
    } catch (err) {
      setError(getErrorMessage(err))
    } finally {
      setLoading(false)
    }
  }, [search, category])

  useEffect(() => {
    api.get('/api/careers/categories').then(({ data }) => setCategories(data.categories)).catch(() => {})
    api.get('/api/saved-careers').then(({ data }) => setSavedSlugs(new Set(data.map((s) => s.career.slug)))).catch(() => {})
  }, [])

  useEffect(() => { loadCareers() }, [loadCareers])

  const handleSave = async (career) => {
    try {
      if (savedSlugs.has(career.slug)) {
        await api.delete(`/api/saved-careers/${career.slug}`)
        setSavedSlugs((prev) => { const next = new Set(prev); next.delete(career.slug); return next })
        showToast('Removed from saved careers')
      } else {
        await api.post('/api/saved-careers', { career_slug: career.slug })
        setSavedSlugs((prev) => new Set(prev).add(career.slug))
        showToast('Career saved!', 'success')
      }
    } catch (err) {
      showToast(getErrorMessage(err), 'error')
    }
  }

  const setFilter = (key, value) => {
    const next = new URLSearchParams(searchParams)
    if (value) next.set(key, value); else next.delete(key)
    setSearchParams(next)
  }

  return (
    <div className="container" style={{ padding: '32px 24px 60px' }}>
      <div style={{ marginBottom: 24 }}>
        <h1 style={{ fontSize: 26 }}>Career Explorer</h1>
        <p>Browse {careers.length} career paths across technology, medicine, law, government, and more.</p>
      </div>

      <div style={{ display: 'flex', gap: 12, marginBottom: 24, flexWrap: 'wrap', alignItems: 'center' }}>
        <div style={{ position: 'relative', flex: '1 1 280px' }}>
          <Icon name="search" size={16} color="var(--text-secondary)" className="" />
          <input
            className="input"
            style={{ paddingLeft: 38 }}
            placeholder="Search careers..."
            defaultValue={search}
            onChange={(e) => setFilter('search', e.target.value)}
          />
          <span style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)' }}>
            <Icon name="search" size={15} color="var(--text-secondary)" />
          </span>
        </div>
        <select className="select" style={{ maxWidth: 220 }} value={category} onChange={(e) => setFilter('category', e.target.value)}>
          <option value="">All Categories</option>
          {categories.map((c) => <option key={c} value={c}>{c}</option>)}
        </select>
      </div>

      {loading ? (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 20 }}>
          {Array.from({ length: 6 }).map((_, i) => <div key={i} className="skeleton" style={{ height: 220, borderRadius: 20 }} />)}
        </div>
      ) : error ? (
        <EmptyState icon="x" title="Couldn't load careers" description={error} />
      ) : careers.length === 0 ? (
        <EmptyState icon="search" title="No careers found" description="Try a different search term or clear your filters." />
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 20 }} className="explorer-grid">
          {careers.map((c) => (
            <CareerCard key={c.slug} career={c} isSaved={savedSlugs.has(c.slug)} onSave={handleSave} />
          ))}
        </div>
      )}

      <style>{`@media (max-width: 900px) { .explorer-grid { grid-template-columns: 1fr !important; } }`}</style>
    </div>
  )
}
