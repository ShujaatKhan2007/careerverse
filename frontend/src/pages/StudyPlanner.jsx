import { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import api, { getErrorMessage } from '../services/api'
import { useToast } from '../context/ToastContext'
import Icon from '../components/Icon'
import LoadingSpinner from '../components/LoadingSpinner'
import EmptyState from '../components/EmptyState'
import './StudyPlanner.css'

export default function StudyPlanner() {
  const location = useLocation()
  const [plans, setPlans] = useState([])
  const [careers, setCareers] = useState([])
  const [loading, setLoading] = useState(true)
  const [showForm, setShowForm] = useState(false)
  const { showToast } = useToast()

  const [form, setForm] = useState({
    career_slug: location.state?.prefillCareerSlug || '',
    title: location.state?.prefillTitle ? `${location.state.prefillTitle} Prep Plan` : '',
    exam_name: '',
    target_date: '',
    tasksText: 'Complete syllabus overview\nGather study material and books\nStart topic-wise revision\nTake first mock test',
  })

  const load = () => {
    setLoading(true)
    Promise.all([api.get('/api/study-plans'), api.get('/api/careers')])
      .then(([plansRes, careersRes]) => { setPlans(plansRes.data); setCareers(careersRes.data) })
      .catch(() => {}).finally(() => setLoading(false))
  }

  useEffect(() => {
    load()
    if (location.state?.prefillCareerSlug) setShowForm(true)
  }, [])

  const update = (field) => (e) => setForm((f) => ({ ...f, [field]: e.target.value }))

  const createPlan = async (e) => {
    e.preventDefault()
    if (!form.career_slug) { showToast('Please select a career'); return }
    try {
      const tasks = form.tasksText.split('\n').map((t) => t.trim()).filter(Boolean)
      await api.post('/api/study-plans', {
        career_slug: form.career_slug,
        title: form.title,
        exam_name: form.exam_name || null,
        target_date: form.target_date || null,
        tasks,
      })
      showToast('Study plan created!', 'success')
      setShowForm(false)
      load()
    } catch (err) {
      showToast(getErrorMessage(err), 'error')
    }
  }

  const toggleTask = async (planId, taskIndex, completed) => {
    try {
      const { data } = await api.patch(`/api/study-plans/${planId}/task`, { task_index: taskIndex, completed: !completed })
      setPlans((prev) => prev.map((p) => (p._id === planId ? data : p)))
    } catch (err) {
      showToast(getErrorMessage(err), 'error')
    }
  }

  const deletePlan = async (planId) => {
    try {
      await api.delete(`/api/study-plans/${planId}`)
      setPlans((prev) => prev.filter((p) => p._id !== planId))
      showToast('Study plan deleted')
    } catch (err) {
      showToast(getErrorMessage(err), 'error')
    }
  }

  if (loading) return <LoadingSpinner fullPage />

  return (
    <div className="container" style={{ padding: '32px 24px 60px' }}>
      <div className="section-title">
        <div>
          <h1 style={{ fontSize: 26 }}>Study Planner</h1>
          <p>Build a task-based roadmap and track your progress toward your dream career.</p>
        </div>
        <button className="btn btn-primary" onClick={() => setShowForm((s) => !s)}>
          <Icon name="plus" size={16} /> New Plan
        </button>
      </div>

      {showForm && (
        <form onSubmit={createPlan} className="card study-planner__form fade-in">
          <div className="form-group form-group--row" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14 }}>
            <div>
              <label className="label">Career</label>
              <select className="select" value={form.career_slug} onChange={update('career_slug')} required>
                <option value="">Select a career</option>
                {careers.map((c) => <option key={c.slug} value={c.slug}>{c.title}</option>)}
              </select>
            </div>
            <div>
              <label className="label">Plan Title</label>
              <input className="input" value={form.title} onChange={update('title')} required />
            </div>
          </div>
          <div className="form-group form-group--row" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14 }}>
            <div>
              <label className="label">Target Exam (optional)</label>
              <input className="input" value={form.exam_name} onChange={update('exam_name')} placeholder="e.g. JEE Main" />
            </div>
            <div>
              <label className="label">Target Date (optional)</label>
              <input type="date" className="input" value={form.target_date} onChange={update('target_date')} />
            </div>
          </div>
          <div className="form-group">
            <label className="label">Tasks (one per line)</label>
            <textarea className="textarea" rows={5} value={form.tasksText} onChange={update('tasksText')} />
          </div>
          <button type="submit" className="btn btn-primary">Create Plan</button>
        </form>
      )}

      {plans.length === 0 ? (
        <EmptyState icon="clock" title="No study plans yet" description="Create your first study plan to start tracking your preparation progress." />
      ) : (
        <div className="study-planner__grid">
          {plans.map((p) => (
            <div key={p._id} className="card study-planner__plan-card">
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div>
                  <h3 style={{ fontSize: 16, marginBottom: 2 }}>{p.title}</h3>
                  {p.exam_name && <p style={{ fontSize: 12.5, margin: 0 }}>Target: {p.exam_name}{p.target_date ? ` • ${p.target_date}` : ''}</p>}
                </div>
                <button onClick={() => deletePlan(p._id)} aria-label="Delete plan" style={{ background: 'none', border: 'none' }}>
                  <Icon name="trash" size={16} color="var(--color-error)" />
                </button>
              </div>

              <div style={{ margin: '12px 0' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12.5, marginBottom: 6 }}>
                  <span>Progress</span><span style={{ fontWeight: 700 }}>{p.progress_pct}%</span>
                </div>
                <div className="progress-track"><div className="progress-fill" style={{ width: `${p.progress_pct}%` }} /></div>
              </div>

              <ul className="study-planner__tasks">
                {p.tasks.map((task, i) => (
                  <li key={i}>
                    <label className="study-planner__task-label">
                      <input type="checkbox" checked={p.task_status[i] || false} onChange={() => toggleTask(p._id, i, p.task_status[i])} />
                      <span className={p.task_status[i] ? 'is-done' : ''}>{task}</span>
                    </label>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
