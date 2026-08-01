import { useEffect, useState } from 'react'
import api, { getErrorMessage } from '../services/api'
import { useToast } from '../context/ToastContext'
import Icon from '../components/Icon'
import LoadingSpinner from '../components/LoadingSpinner'
import EmptyState from '../components/EmptyState'
import './CareerCompare.css'

const ROWS = [
  { key: 'category', label: 'Category' },
  { key: 'difficulty', label: 'Difficulty' },
  { key: 'min_education', label: 'Min. Education' },
  { key: (c) => c.salary_range.entry, label: 'Entry Salary' },
  { key: (c) => c.salary_range.mid, label: 'Mid-Career Salary' },
  { key: (c) => c.salary_range.senior, label: 'Senior Salary' },
  { key: (c) => c.entrance_exams.map((e) => e.name).join(', '), label: 'Entrance Exams' },
  { key: 'career_growth', label: 'Career Growth' },
]

export default function CareerCompare() {
  const [allCareers, setAllCareers] = useState([])
  const [selectedSlugs, setSelectedSlugs] = useState([])
  const [comparison, setComparison] = useState(null)
  const [loading, setLoading] = useState(false)
  const { showToast } = useToast()

  useEffect(() => {
    api.get('/api/careers').then(({ data }) => setAllCareers(data)).catch(() => {})
  }, [])

  const toggleSlug = (slug) => {
    setSelectedSlugs((prev) => {
      if (prev.includes(slug)) return prev.filter((s) => s !== slug)
      if (prev.length >= 4) {
        showToast('You can compare up to 4 careers at a time')
        return prev
      }
      return [...prev, slug]
    })
  }

  const runComparison = async () => {
    if (selectedSlugs.length < 2) {
      showToast('Select at least 2 careers to compare')
      return
    }
    setLoading(true)
    try {
      const { data } = await api.post('/api/careers/compare', { career_slugs: selectedSlugs })
      setComparison(data.careers)
    } catch (err) {
      showToast(getErrorMessage(err), 'error')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container" style={{ padding: '32px 24px 80px' }}>
      <div style={{ marginBottom: 24 }}>
        <h1 style={{ fontSize: 26 }}>Compare Careers</h1>
        <p>Select 2-4 careers to compare salary, difficulty, exams, and growth side-by-side.</p>
      </div>

      <div className="compare-page__chips">
        {allCareers.map((c) => (
          <button
            key={c.slug}
            className={`compare-page__chip ${selectedSlugs.includes(c.slug) ? 'is-selected' : ''}`}
            onClick={() => toggleSlug(c.slug)}
          >
            <Icon name={c.icon} size={15} /> {c.title}
          </button>
        ))}
      </div>

      <button className="btn btn-primary" style={{ marginTop: 20 }} onClick={runComparison} disabled={loading}>
        {loading ? <span className="spinner" /> : `Compare Selected (${selectedSlugs.length})`}
      </button>

      {comparison && (
        <div className="compare-page__table-wrap fade-in">
          <table className="compare-page__table">
            <thead>
              <tr>
                <th>Attribute</th>
                {comparison.map((c) => (
                  <th key={c.slug}>
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6 }}>
                      <Icon name={c.icon} size={22} color="var(--color-primary)" />
                      {c.title}
                    </div>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {ROWS.map((row) => (
                <tr key={row.label}>
                  <td className="compare-page__row-label">{row.label}</td>
                  {comparison.map((c) => (
                    <td key={c.slug}>{typeof row.key === 'function' ? row.key(c) : c[row.key]}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {!comparison && !loading && (
        <div style={{ marginTop: 40 }}>
          <EmptyState icon="chart" title="No comparison yet" description="Select careers above and click Compare to see a full side-by-side breakdown." />
        </div>
      )}
    </div>
  )
}
