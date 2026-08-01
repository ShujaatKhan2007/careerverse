export default function LoadingSpinner({ fullPage = false, label = 'Loading...' }) {
  const content = (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12, padding: fullPage ? 0 : 40 }}>
      <div className="spinner" style={{ width: 28, height: 28, borderWidth: 3 }} />
      <span style={{ fontSize: 13, color: 'var(--text-secondary)' }}>{label}</span>
    </div>
  )

  if (fullPage) {
    return (
      <div style={{ minHeight: '70vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        {content}
      </div>
    )
  }
  return content
}
