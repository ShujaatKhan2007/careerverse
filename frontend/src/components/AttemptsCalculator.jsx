import { useState, useEffect } from 'react'
import Icon from './Icon'
import { calculateExamAttempts, formatAge } from '../utils/attemptsCalculator'
import './AttemptsCalculator.css'

const STORAGE_KEY = 'cv_dob'

export default function AttemptsCalculator({ exams }) {
  const [dob, setDob] = useState(() => localStorage.getItem(STORAGE_KEY) || '')
  const [results, setResults] = useState(null)

  useEffect(() => {
    if (dob) {
      localStorage.setItem(STORAGE_KEY, dob)
      const dobDate = new Date(dob)
      if (!isNaN(dobDate)) {
        setResults(exams.map((exam) => ({ exam, ...calculateExamAttempts(dobDate, exam) })))
      }
    } else {
      setResults(null)
    }
  }, [dob, exams])

  const today = new Date().toISOString().split('T')[0]

  return (
    <div className="attempts-calc card">
      <div className="attempts-calc__header">
        <div className="attempts-calc__header-icon">
          <Icon name="target" size={20} color="#fff" />
        </div>
        <div>
          <h3 style={{ margin: 0, fontSize: 17 }}>
            Attempts Calculator
            <span className="attempts-calc__badge-new">New</span>
          </h3>
          <p style={{ margin: '4px 0 0', fontSize: 13 }}>
            Enter your date of birth to see roughly how many valid attempts you have left for each exam.
          </p>
        </div>
      </div>

      <div className="attempts-calc__input-row">
        <label className="label" htmlFor="dob-input" style={{ marginBottom: 0 }}>Date of Birth</label>
        <input
          id="dob-input"
          type="date"
          className="input"
          value={dob}
          max={today}
          onChange={(e) => setDob(e.target.value)}
          style={{ maxWidth: 220 }}
        />
      </div>

      {results && (
        <div className="attempts-calc__results fade-in">
          {results.map(({ exam, status, age, message, attemptsRemaining }) => (
            <div key={exam.name} className={`attempts-calc__row attempts-calc__row--${status}`}>
              <div className="attempts-calc__row-top">
                <span className="attempts-calc__exam-name">{exam.name}</span>
                {attemptsRemaining !== null && (
                  <span className={`attempts-calc__badge attempts-calc__badge--${status}`}>
                    {status === 'aged-out' ? 'Not eligible' : `${attemptsRemaining} attempt${attemptsRemaining === 1 ? '' : 's'} left`}
                  </span>
                )}
                {attemptsRemaining === null && status === 'not-yet-eligible' && (
                  <span className="attempts-calc__badge attempts-calc__badge--not-yet-eligible">Not yet eligible</span>
                )}
              </div>
              <p className="attempts-calc__message">
                Your age: <strong>{formatAge(age)}</strong> — {message}
              </p>
              {exam.note && <p className="attempts-calc__note"><Icon name="bell" size={12} /> {exam.note}</p>}
            </div>
          ))}
          <p className="attempts-calc__disclaimer">
            These are best-effort estimates for General category based on typical age/session rules and do not
            account for reserved-category relaxations or exact per-notification cutoff dates. Always verify
            against the exam's official current-year notification before relying on this for a real decision.
          </p>
        </div>
      )}
    </div>
  )
}
