import { useEffect, useState } from 'react'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
const MAX_WAIT_MS = 70000       // give up waiting after ~70s and let the app try anyway
const POLL_INTERVAL_MS = 2500   // how often to re-ping while waiting
const PING_TIMEOUT_MS = 5000    // how long a single ping attempt gets before it's considered failed

/**
 * Wraps the whole app. On mount, pings the backend's /api/health endpoint
 * and shows a friendly "waking up" screen until it responds - this covers
 * Render's free-tier cold start (~30-50s after 15 minutes of inactivity),
 * which would otherwise show up to the user as a confusing "Network Error"
 * on their first login/register attempt.
 */
export default function BackendWakeGate({ children }) {
  const [status, setStatus] = useState('checking') // 'checking' | 'ready'
  const [elapsed, setElapsed] = useState(0)

  useEffect(() => {
    let cancelled = false
    const startedAt = Date.now()

    const tick = setInterval(() => {
      if (!cancelled) setElapsed(Math.round((Date.now() - startedAt) / 1000))
    }, 1000)

    async function ping() {
      try {
        const controller = new AbortController()
        const timeoutId = setTimeout(() => controller.abort(), PING_TIMEOUT_MS)
        const res = await fetch(`${API_BASE_URL}/api/health`, { signal: controller.signal })
        clearTimeout(timeoutId)
        if (res.ok) {
          if (!cancelled) setStatus('ready')
          return
        }
        throw new Error('Backend responded but not OK')
      } catch {
        if (cancelled) return
        if (Date.now() - startedAt > MAX_WAIT_MS) {
          // Don't block forever - let the app mount and surface errors normally
          // if something other than a cold start is actually wrong.
          setStatus('ready')
          return
        }
        setTimeout(ping, POLL_INTERVAL_MS)
      }
    }

    ping()
    return () => {
      cancelled = true
      clearInterval(tick)
    }
  }, [])

  if (status === 'checking') {
    return (
      <div
        style={{
          minHeight: '100vh',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          gap: 18,
          textAlign: 'center',
          padding: 24,
          background: 'var(--bg-page)',
        }}
      >
        <div
          style={{
            width: 52,
            height: 52,
            borderRadius: 16,
            background: 'var(--gradient-primary)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#fff',
            fontWeight: 800,
            fontFamily: 'var(--font-display)',
            fontSize: 20,
          }}
        >
          CV
        </div>
        <div className="spinner" style={{ width: 30, height: 30, borderWidth: 3 }} />
        <div>
          <h2 style={{ marginBottom: 6, fontSize: 19 }}>Waking up the server…</h2>
          <p style={{ maxWidth: 380, color: 'var(--text-secondary)', margin: 0 }}>
            Our free hosting plan puts the server to sleep after periods of inactivity.
            This usually takes 20–50 seconds on the first visit - thanks for your patience.
          </p>
          <p style={{ fontSize: 12, color: 'var(--text-secondary)', marginTop: 12 }}>
            {elapsed}s elapsed
          </p>
        </div>
      </div>
    )
  }

  return children
}
