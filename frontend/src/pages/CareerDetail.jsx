import { useEffect, useState } from 'react'
import { useParams, useNavigate, Link } from 'react-router-dom'
import api, { getErrorMessage } from '../services/api'
import { useToast } from '../context/ToastContext'
import Icon from '../components/Icon'
import LoadingSpinner from '../components/LoadingSpinner'
import EmptyState from '../components/EmptyState'
import './CareerDetail.css'

const DIFFICULTY_CLASS = { Easy: 'badge-easy', Medium: 'badge-medium', Hard: 'badge-hard', 'Very Hard': 'badge-veryhard' }

export default function CareerDetail() {
  const { slug } = useParams()
  const [career, setCareer] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [saved, setSaved] = useState(false)
  const { showToast } = useToast()
  const navigate = useNavigate()

  useEffect(() => {
    setLoading(true)
    setError('')
    api.get(`/api/careers/${slug}`)
      .then(({ data }) => setCareer(data))
      .catch((err) => setError(getErrorMessage(err)))
      .finally(() => setLoading(false))

    api.get('/api/saved-careers').then(({ data }) => {
      setSaved(data.some((s) => s.career.slug === slug))
    }).catch(() => {})
  }, [slug])

  const toggleSave = async () => {
    try {
      if (saved) {
        await api.delete(`/api/saved-careers/${slug}`)
        setSaved(false)
        showToast('Removed from saved careers')
      } else {
        await api.post('/api/saved-careers', { career_slug: slug })
        setSaved(true)
        showToast('Career saved!', 'success')
      }
    } catch (err) {
      showToast(getErrorMessage(err), 'error')
    }
  }

  const createStudyPlan = () => {
    navigate('/study-plans', { state: { prefillCareerSlug: slug, prefillTitle: career?.title } })
  }

  if (loading) return <LoadingSpinner fullPage />
  if (error || !career) return <div className="container" style={{ padding: '60px 24px' }}><EmptyState icon="x" title="Career not found" description={error} action={<Link to="/explorer" className="btn btn-primary">Back to Explorer</Link>} /></div>

  return (
    <div className="container career-detail fade-in" style={{ padding: '32px 24px 80px' }}>
      <div className="career-detail__hero card">
        <div className="career-detail__hero-icon"><Icon name={career.icon} size={30} color="var(--color-primary)" /></div>
        <div style={{ flex: 1 }}>
          <div style={{ display: 'flex', gap: 10, alignItems: 'center', flexWrap: 'wrap' }}>
            <h1 style={{ margin: 0, fontSize: 26 }}>{career.title}</h1>
            <span className={`badge ${DIFFICULTY_CLASS[career.difficulty]}`}>{career.difficulty}</span>
          </div>
          <p style={{ marginTop: 6, maxWidth: 640 }}>{career.short_description}</p>
        </div>
        <div style={{ display: 'flex', gap: 10 }}>
          <button className="btn btn-secondary" onClick={toggleSave}>
            <Icon name="bookmark" size={16} color={saved ? 'var(--color-highlight)' : undefined} /> {saved ? 'Saved' : 'Save'}
          </button>
          <button className="btn btn-primary" onClick={createStudyPlan}>
            <Icon name="plus" size={16} /> Study Plan
          </button>
        </div>
      </div>

      <div className="career-detail__stats-row">
        <StatCard icon="award" label="Entry Salary" value={career.salary_range.entry} />
        <StatCard icon="chart" label="Mid-Career" value={career.salary_range.mid} />
        <StatCard icon="graduation-cap" label="Min. Education" value={career.min_education} />
        <StatCard icon="compass" label="Category" value={career.category} />
      </div>

      <Section title="Overview" icon="compass">
        <p>{career.overview}</p>
      </Section>

      <Section title="Required Qualifications" icon="graduation-cap">
        <ul>{career.required_qualifications.map((q, i) => <li key={i}>{q}</li>)}</ul>
      </Section>

      <Section title="Entrance Exams" icon="award">
        {career.entrance_exams.map((exam) => (
          <div key={exam.name} className="career-detail__exam-card card">
            <h4 style={{ marginBottom: 10 }}>{exam.name}</h4>
            <div className="career-detail__exam-grid">
              <ExamField label="Conducting Body" value={exam.conducting_body} />
              <ExamField label="Eligibility" value={exam.eligibility} />
              <ExamField label="Age Limit" value={exam.age_limit} />
              <ExamField label="Attempts" value={exam.attempts} />
              <ExamField label="Selection Process" value={exam.selection_process} />
              <ExamField label="Exam Pattern" value={exam.exam_pattern} />
            </div>
            <ExamField label="Syllabus" value={exam.syllabus} fullWidth />
          </div>
        ))}
      </Section>

      <Section title="Preparation Strategy" icon="target">
        <ol className="career-detail__ordered">
          {career.preparation_strategy.map((s, i) => <li key={i}>{s}</li>)}
        </ol>
      </Section>

      <div className="career-detail__two-col">
        <Section title="Best Books" icon="book">
          <ul>{career.best_books.map((b, i) => <li key={i}>{b}</li>)}</ul>
        </Section>
        <Section title="Online Resources" icon="globe">
          <ul className="career-detail__resource-list">
            {career.online_resources.map((r) => (
              <li key={r.name}>
                <a href={r.url} target="_blank" rel="noopener noreferrer">{r.name}</a>
                <span className={`badge ${r.type === 'free' ? 'badge-easy' : r.type === 'paid' ? 'badge-hard' : 'badge-medium'}`}>{r.type}</span>
              </li>
            ))}
          </ul>
        </Section>
      </div>

      <div className="career-detail__two-col">
        <Section title="Top Colleges" icon="building">
          <ul>{career.top_colleges.map((c, i) => <li key={i}>{c}</li>)}</ul>
        </Section>
        <Section title="Scholarships" icon="award">
          <ul>{career.scholarships.map((s, i) => <li key={i}>{s}</li>)}</ul>
        </Section>
      </div>

      <Section title="Career Growth" icon="chart">
        <p>{career.career_growth}</p>
      </Section>

      <Section title="Official Websites" icon="globe">
        <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
          {career.official_websites.map((w) => (
            <a key={w} href={w} target="_blank" rel="noopener noreferrer" className="btn btn-secondary btn-sm">{w.replace('https://', '')}</a>
          ))}
        </div>
      </Section>

      <Section title="Frequently Asked Questions" icon="bot">
        <div className="career-detail__faqs">
          {career.faqs.map((f, i) => (
            <details key={i} className="career-detail__faq">
              <summary>{f.q}</summary>
              <p>{f.a}</p>
            </details>
          ))}
        </div>
      </Section>
    </div>
  )
}

function StatCard({ icon, label, value }) {
  return (
    <div className="card career-detail__stat-card">
      <Icon name={icon} size={18} color="var(--color-primary)" />
      <div>
        <div style={{ fontWeight: 700, fontSize: 14 }}>{value}</div>
        <div style={{ fontSize: 12, color: 'var(--text-secondary)' }}>{label}</div>
      </div>
    </div>
  )
}

function Section({ title, icon, children }) {
  return (
    <section className="career-detail__section">
      <h2 className="career-detail__section-title"><Icon name={icon} size={19} color="var(--color-primary)" /> {title}</h2>
      {children}
    </section>
  )
}

function ExamField({ label, value, fullWidth }) {
  return (
    <div style={{ gridColumn: fullWidth ? '1 / -1' : undefined }}>
      <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-secondary)', marginBottom: 2 }}>{label}</div>
      <div style={{ fontSize: 13.5 }}>{value}</div>
    </div>
  )
}
