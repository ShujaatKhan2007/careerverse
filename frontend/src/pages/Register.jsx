import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { useToast } from '../context/ToastContext'
import { getErrorMessage } from '../services/api'
import './AuthPages.css'

export default function Register() {
  const [form, setForm] = useState({ name: '', email: '', password: '', confirmPassword: '' })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const { register } = useAuth()
  const { showToast } = useToast()
  const navigate = useNavigate()

  const update = (field) => (e) => setForm((f) => ({ ...f, [field]: e.target.value }))

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')

    if (form.password !== form.confirmPassword) {
      setError('Passwords do not match')
      return
    }
    if (form.password.length < 8) {
      setError('Password must be at least 8 characters long')
      return
    }

    setLoading(true)
    try {
      await register(form.name, form.email, form.password)
      showToast('Account created! Welcome to CareerVerse.', 'success')
      navigate('/dashboard')
    } catch (err) {
      setError(getErrorMessage(err))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="auth-page">
      <div className="card auth-card fade-in">
        <h1 style={{ fontSize: 24 }}>Create your account</h1>
        <p style={{ marginBottom: 24 }}>Start discovering the right career path for you.</p>

        <form onSubmit={handleSubmit} noValidate>
          <div className="form-group">
            <label className="label" htmlFor="name">Full name</label>
            <input id="name" type="text" className="input" required minLength={2} value={form.name}
              onChange={update('name')} placeholder="Jane Doe" />
          </div>
          <div className="form-group">
            <label className="label" htmlFor="email">Email</label>
            <input id="email" type="email" className="input" required value={form.email}
              onChange={update('email')} placeholder="you@example.com" />
          </div>
          <div className="form-group">
            <label className="label" htmlFor="password">Password</label>
            <input id="password" type="password" className="input" required minLength={8} value={form.password}
              onChange={update('password')} placeholder="At least 8 characters" />
          </div>
          <div className="form-group">
            <label className="label" htmlFor="confirmPassword">Confirm password</label>
            <input id="confirmPassword" type="password" className="input" required value={form.confirmPassword}
              onChange={update('confirmPassword')} placeholder="Re-enter password" />
          </div>

          {error && <p className="form-error">{error}</p>}

          <button type="submit" className="btn btn-primary btn-block" disabled={loading}>
            {loading ? <span className="spinner" /> : 'Create Account'}
          </button>
        </form>

        <p style={{ textAlign: 'center', marginTop: 20, fontSize: 13.5 }}>
          Already have an account? <Link to="/login">Log in</Link>
        </p>
      </div>
    </div>
  )
}
