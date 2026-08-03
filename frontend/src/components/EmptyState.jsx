import Icon from './Icon'

export default function EmptyState({ icon = 'compass', title, description, action }) {
  return (
    <div className="empty-state">
      <div style={{ display: 'inline-flex', width: 56, height: 56, borderRadius: '50%', background: 'rgba(37,99,235,0.08)', alignItems: 'center', justifyContent: 'center', marginBottom: 16 }}>
        <Icon name={icon} size={26} color="var(--color-primary)" />
      </div>
      <h3 style={{ marginBottom: 6 }}>{title}</h3>
      {description && <p style={{ maxWidth: 380, margin: '0 auto 16px' }}>{description}</p>}
      {action}
    </div>
  )
}
