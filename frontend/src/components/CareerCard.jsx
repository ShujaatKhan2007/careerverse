import { useNavigate } from 'react-router-dom'
import Icon from './Icon'
import './CareerCard.css'

const DIFFICULTY_CLASS = {
  Easy: 'badge-easy',
  Medium: 'badge-medium',
  Hard: 'badge-hard',
  'Very Hard': 'badge-veryhard',
}

export default function CareerCard({ career, onSave, isSaved = false, showSaveButton = true }) {
  const navigate = useNavigate()

  return (
    <div className="career-card card card--hover fade-in">
      <div className="career-card__top">
        <div className="career-card__icon">
          <Icon name={career.icon} size={22} color="var(--color-primary)" />
        </div>
        {showSaveButton && (
          <button
            className={`career-card__save ${isSaved ? 'is-saved' : ''}`}
            onClick={(e) => { e.stopPropagation(); onSave?.(career) }}
            aria-label={isSaved ? 'Remove from saved' : 'Save career'}
            title={isSaved ? 'Saved' : 'Save for later'}
          >
            <Icon name="bookmark" size={17} color={isSaved ? 'var(--color-highlight)' : 'var(--text-secondary)'} />
          </button>
        )}
      </div>

      <h3 className="career-card__title">{career.title}</h3>
      <p className="career-card__desc">{career.short_description}</p>

      <div className="career-card__meta">
        <span className={`badge ${DIFFICULTY_CLASS[career.difficulty] || 'badge-medium'}`}>{career.difficulty}</span>
        <span className="career-card__meta-item">
          <Icon name="award" size={14} /> {career.salary_range?.entry}
        </span>
      </div>

      <div className="career-card__footer">
        <span className="career-card__edu">
          <Icon name="graduation-cap" size={14} /> {career.course_duration ? career.course_duration.split('(')[0].trim() : `${career.min_education}+`}
        </span>
        <button className="btn btn-secondary btn-sm" onClick={() => navigate(`/career/${career.slug}`)}>
          Explore <Icon name="chevronRight" size={14} />
        </button>
      </div>
    </div>
  )
}
