import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import api, { getErrorMessage } from '../services/api'
import { useToast } from '../context/ToastContext'
import Icon from '../components/Icon'
import CareerCard from '../components/CareerCard'
import './CareerGuidance.css'

const EDUCATION_OPTIONS = ['10th', '12th', 'Undergraduate', 'Postgraduate']
const STREAM_OPTIONS = ['Science', 'Commerce', 'Arts', 'Other']

export default function CareerGuidance() {
  const { user } = useAuth()
  const { showToast } = useToast()
  const navigate = useNavigate()

  const [form, setForm] = useState({
    name: user?.name || '',
    age: '',
    education: '12th',
    stream: 'Science',
    percentage: '',
    dream_career: '',
  })
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const update = (field) => (e) => setForm((f) => ({ ...f, [field]: e.target.value }))

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)
    setResult(null)
    try {
      const { data } = await api.post('/api/careers/guidance', {
        ...form,
        age: Number(form.age),
        percentage: Number(form.percentage),
      })
      setResult(data)
    } catch (err) {
      setError(getErrorMessage(err))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container guidance-page" style={{ padding: '32px 24px 80px' }}>
      <div style={{ marginBottom: 24 }}>
        <h1 style={{ fontSize: 26 }}>Find Your Career Path</h1>
        <p>Tell us about yourself and your dream career - we'll generate a complete guidance report instantly.</p>
      </div>

      <div className="guidance-page__layout">
        <form onSubmit={handleSubmit} className="card guidance-page__form">
          <div className="form-group">
            <label className="label" htmlFor="name">Name</label>
            <input id="name" className="input" required value={form.name} onChange={update('name')} />
          </div>
          <div className="form-group form-group--row">
            <div>
              <label className="label" htmlFor="age">Age</label>
              <input id="age" type="number" min={10} max={80} className="input" required value={form.age} onChange={update('age')} />
            </div>
            <div>
              <label className="label" htmlFor="percentage">Percentage (%)</label>
              <input id="percentage" type="number" min={0} max={100} step="0.01" className="input" required value={form.percentage} onChange={update('percentage')} />
            </div>
          </div>
          <div className="form-group form-group--row">
            <div>
              <label className="label" htmlFor="education">Current Education</label>
              <select id="education" className="select" value={form.education} onChange={update('education')}>
                {EDUCATION_OPTIONS.map((o) => <option key={o} value={o}>{o}</option>)}
              </select>
            </div>
            <div>
              <label className="label" htmlFor="stream">Stream</label>
              <select id="stream" className="select" value={form.stream} onChange={update('stream')}>
                {STREAM_OPTIONS.map((o) => <option key={o} value={o}>{o}</option>)}
              </select>
            </div>
          </div>
          <div className="form-group">
            <label className="label" htmlFor="dream_career">Dream Career</label>
            <input id="dream_career" className="input" required placeholder="e.g. Software Engineer, Doctor, Lawyer..."
              value={form.dream_career} onChange={update('dream_career')} />
          </div>

          {error && <p className="form-error">{error}</p>}

          <button type="submit" className="btn btn-primary btn-block" disabled={loading}>
            {loading ? <span className="spinner" /> : <>Generate My Career Report <Icon name="chevronRight" size={16} /></>}
          </button>
        </form>

        <div className="guidance-page__result">
          {!result && !loading && (
            <div className="empty-state card" style={{ padding: 60 }}>
              <Icon name="compass" size={30} color="var(--color-primary)" />
              <h3 style={{ marginTop: 14 }}>Your report will appear here</h3>
              <p>Fill out the form to get a personalized career guidance report.</p>
            </div>
          )}

          {loading && (
            <div className="card" style={{ padding: 60, textAlign: 'center' }}>
              <div className="spinner" style={{ margin: '0 auto 12px' }} />
              <p>Matching you to the best career path...</p>
            </div>
          )}

          {result && (
            <div className="fade-in">
              <div className="card guidance-page__match-card">
                <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                  <Icon name={result.career.icon} size={26} color="var(--color-primary)" />
                  <div>
                    <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--color-accent)', textTransform: 'uppercase' }}>Best Match</div>
                    <h2 style={{ margin: 0, fontSize: 22 }}>{result.career.title}</h2>
                  </div>
                </div>
                <p>{result.career.overview}</p>
                <Link to={`/career/${result.career.slug}`} className="btn btn-primary">
                  View Full Report <Icon name="chevronRight" size={15} />
                </Link>
              </div>

              <div className="card guidance-page__eligibility-card">
                <h3 style={{ fontSize: 16 }}>Eligibility Check</h3>
                {result.eligibility.map((e) => (
                  <div key={e.exam_name} className="guidance-page__eligibility-row">
                    <Icon name={e.eligible ? 'check' : 'x'} size={16} color={e.eligible ? 'var(--color-success)' : 'var(--color-error)'} />
                    <div>
                      <strong>{e.exam_name}</strong>
                      <ul>{e.notes.map((n, i) => <li key={i}>{n}</li>)}</ul>
                    </div>
                  </div>
                ))}
              </div>

              {result.related_careers?.length > 0 && (
                <>
                  <h3 style={{ fontSize: 16, margin: '20px 0 12px' }}>You might also like</h3>
                  <div className="guidance-page__related-grid">
                    {result.related_careers.map((c) => <CareerCard key={c.slug} career={c} showSaveButton={false} />)}
                  </div>
                </>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
