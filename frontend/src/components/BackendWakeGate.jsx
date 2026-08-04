import { useEffect, useState } from 'react'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
const MAX_WAIT_MS = 70000       // give up waiting after ~70s and let the app try anyway
const POLL_INTERVAL_MS = 2500   // how often to re-ping while waiting
const PING_TIMEOUT_MS = 5000    // how long a single ping attempt gets before it's considered failed
const QUOTE_ROTATE_MS = 4000    // how often to switch the motivational quote

const QUOTES = [
  { text: "Success is the sum of small efforts, repeated day in and day out.", author: "Robert Collier" },
  { text: "The future belongs to those who prepare for it today.", author: "Malcolm X" },
  { text: "It always seems impossible until it's done.", author: "Nelson Mandela" },
  { text: "Discipline is choosing between what you want now and what you want most.", author: "Abraham Lincoln" },
  { text: "The expert in anything was once a beginner.", author: "Helen Hayes" },
  { text: "Your dream career doesn't require you to have it all figured out today - just the next step.", author: "CareerVerse" },
  { text: "Don't watch the clock; do what it does. Keep going.", author: "Sam Levenson" },
  { text: "Every attempt you prepare for is practice for the one that counts.", author: "CareerVerse" },
  { text: "Consistency beats intensity - a little every day adds up to a lot.", author: "CareerVerse" },
  { text: "The best time to plant a tree was 20 years ago. The second best time is now.", author: "Chinese Proverb" },
]

/**
 * Wraps the whole app. On mount, pings the backend's /api/health endpoint
 * and shows a friendly loading screen (with rotating motivational quotes,
 * rather than a static "waking up" message) until it responds - this covers
 * Render's free-tier cold start (~30-50s after 15 minutes of inactivity),
 * which would otherwise show up to the user as a confusing "Network Error"
 * on their first login/register attempt.
 */
export default function BackendWakeGate({ children }) {
  const [status, setStatus] = useState('checking') // 'checking' | 'ready'
  const [elapsed, setElapsed] = useState(0)
  const [quoteIndex, setQuoteIndex] = useState(() => Math.floor(Math.random() * QUOTES.length))

  useEffect(() => {
    let cancelled = false
    const startedAt = Date.now()

    const tick = setInterval(() => {
      if (!cancelled) setElapsed(Math.round((Date.now() - startedAt) / 1000))
    }, 1000)

    const quoteTick = setInterval(() => {
      if (!cancelled) setQuoteIndex((i) => (i + 1) % QUOTES.length)
    }, QUOTE_ROTATE_MS)

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
      clearInterval(quoteTick)
    }
  }, [])

  if (status === 'checking') {
    const quote = QUOTES[quoteIndex]
    return (
      <div
        style={{
          minHeight: '100vh',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          gap: 22,
          textAlign: 'center',
          padding: 24,
          background:
            'radial-gradient(circle at 20% 20%, rgba(37,99,235,0.08), transparent 45%), radial-gradient(circle at 80% 80%, rgba(16,185,129,0.08), transparent 45%), var(--bg-page)',
        }}
      >
        <div
          style={{
            width: 56,
            height: 56,
            borderRadius: 16,
            background: 'var(--gradient-primary)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#fff',
            fontWeight: 800,
            fontFamily: 'var(--font-display)',
            fontSize: 22,
            boxShadow: '0 10px 28px rgba(37, 99, 235, 0.3)',
          }}
        >
          CV
        </div>
        <div className="spinner" style={{ width: 30, height: 30, borderWidth: 3 }} />

        <div key={quoteIndex} className="fade-in" style={{ maxWidth: 460, minHeight: 90 }}>
          <p style={{ fontSize: 18, fontFamily: 'var(--font-display)', fontWeight: 600, color: 'var(--text-primary)', margin: 0, lineHeight: 1.4 }}>
            "{quote.text}"
          </p>
          <p style={{ fontSize: 13, color: 'var(--color-primary)', fontWeight: 600, marginTop: 10 }}>
            — {quote.author}
          </p>
        </div>

        <div>
          <p style={{ fontSize: 12.5, color: 'var(--text-secondary)', margin: 0 }}>
            Getting things ready - this can take up to a minute on the first visit.
          </p>
          <p style={{ fontSize: 11.5, color: 'var(--text-secondary)', marginTop: 6 }}>
            {elapsed}s elapsed
          </p>
        </div>
      </div>
    )
  }

  return children
}
