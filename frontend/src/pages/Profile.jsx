import { useState } from 'react'
import { useAuth } from '../context/AuthContext'
import { useToast } from '../context/ToastContext'
import api, { getErrorMessage } from '../services/api'
import Icon from '../components/Icon'

const EDUCATION_OPTIONS = ['10th', '12th', 'Undergraduate', 'Postgraduate']
const STREAM_OPTIONS = ['Science', 'Commerce', 'Arts', 'Other']

export default function Profile() {
  const { user, updateUserLocal } = useAuth()
  const { showToast } = useToast()
  const [form, setForm] = useState({
    name: user?.name || '',
    age: user?.age || '',
    education: user?.education || '',
    stream: user?.stream || '',
    percentage: user?.percentage || '',
    dream_career: user?.dream_career || '',
    bio: user?.bio || '',
    location: user?.location || '',
  })
  const [saving, setSaving] = useState(false)

  const update = (field) => (e) => setForm((f) => ({ ...f, [field]: e.target.value }))

  const handleSubmit = async (e) => {
    e.preventDefault()
    setSaving(true)
    try {
      const payload = { ...form, age: form.age ? Number(form.age) : undefined, percentage: form.percentage ? Number(form.percentage) : undefined }
      const { data } = await api.put('/api/users/profile', payload)
      updateUserLocal(data)
      showToast('Profile updated!', 'success')
    } catch (err) {
      showToast(getErrorMessage(err), 'error')
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="container" style={{ padding: '32px 24px 60px', maxWidth: 640 }}>
      <h1 style={{ fontSize: 26 }}>Your Profile</h1>
      <p style={{ marginBottom: 24 }}>Keep your details updated for more accurate career recommendations.</p>

      <div className="card" style={{ padding: 26 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 14, marginBottom: 24 }}>
          <div style={{ width: 56, height: 56, borderRadius: '50%', background: 'var(--gradient-primary)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: 22, fontWeight: 700, fontFamily: 'var(--font-display)' }}>
            {user?.name?.[0]?.toUpperCase()}
          </div>
          <div>
            <div style={{ fontWeight: 700, fontSize: 16 }}>{user?.name}</div>
            <div style={{ fontSize: 13, color: 'var(--text-secondary)' }}>{user?.email}</div>
          </div>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label className="label">Full Name</label>
            <input className="input" value={form.name} onChange={update('name')} />
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14, marginBottom: 18 }}>
            <div>
              <label className="label">Age</label>
              <input type="number" className="input" value={form.age} onChange={update('age')} />
            </div>
            <div>
              <label className="label">Percentage (%)</label>
              <input type="number" className="input" value={form.percentage} onChange={update('percentage')} />
            </div>
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14, marginBottom: 18 }}>
            <div>
              <label className="label">Current Education</label>
              <select className="select" value={form.education} onChange={update('education')}>
                <option value="">Select</option>
                {EDUCATION_OPTIONS.map((o) => <option key={o} value={o}>{o}</option>)}
              </select>
            </div>
            <div>
              <label className="label">Stream</label>
              <select className="select" value={form.stream} onChange={update('stream')}>
                <option value="">Select</option>
                {STREAM_OPTIONS.map((o) => <option key={o} value={o}>{o}</option>)}
              </select>
            </div>
          </div>
          <div className="form-group">
            <label className="label">Dream Career</label>
            <input className="input" value={form.dream_career} onChange={update('dream_career')} />
          </div>
          <div className="form-group">
            <label className="label">Location</label>
            <input className="input" value={form.location} onChange={update('location')} />
          </div>
          <div className="form-group">
            <label className="label">Bio</label>
            <textarea className="textarea" rows={3} value={form.bio} onChange={update('bio')} maxLength={500} />
          </div>

          <button type="submit" className="btn btn-primary" disabled={saving}>
            {saving ? <span className="spinner" /> : <><Icon name="check" size={16} /> Save Changes</>}
          </button>
        </form>
      </div>
    </div>
  )
}
