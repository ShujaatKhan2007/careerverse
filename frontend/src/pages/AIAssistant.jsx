import { useEffect, useRef, useState } from 'react'
import api, { getErrorMessage } from '../services/api'
import { useAuth } from '../context/AuthContext'
import { useToast } from '../context/ToastContext'
import Icon from '../components/Icon'
import './AIAssistant.css'

export default function AIAssistant() {
  const { user } = useAuth()
  const { showToast } = useToast()
  const [messages, setMessages] = useState([
    { role: 'assistant', content: `Hi ${user?.name?.split(' ')[0] || 'there'}! I'm your CareerVerse AI assistant. Ask me anything about careers, exams, eligibility, or preparation strategy.` },
  ])
  const [input, setInput] = useState('')
  const [sending, setSending] = useState(false)
  const [suggestions, setSuggestions] = useState([])
  const [sessionId, setSessionId] = useState(null)
  const scrollRef = useRef(null)

  useEffect(() => {
    api.get('/api/chat/suggestions').then(({ data }) => setSuggestions(data.suggestions)).catch(() => {})
  }, [])

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: 'smooth' })
  }, [messages, sending])

  const sendMessage = async (text) => {
    const trimmed = text.trim()
    if (!trimmed || sending) return

    setMessages((prev) => [...prev, { role: 'user', content: trimmed }])
    setInput('')
    setSending(true)

    try {
      const { data } = await api.post('/api/chat/message', { message: trimmed, session_id: sessionId })
      setSessionId(data.session_id)
      setMessages((prev) => [...prev, { role: 'assistant', content: data.reply }])
    } catch (err) {
      showToast(getErrorMessage(err), 'error')
      setMessages((prev) => [...prev, { role: 'assistant', content: "Sorry, I hit an error processing that. Please try again." }])
    } finally {
      setSending(false)
    }
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    sendMessage(input)
  }

  return (
    <div className="container assistant-page" style={{ padding: '28px 24px 40px' }}>
      <div style={{ marginBottom: 18 }}>
        <h1 style={{ fontSize: 24, display: 'flex', alignItems: 'center', gap: 10 }}>
          <Icon name="bot" size={22} color="var(--color-primary)" /> AI Career Assistant
        </h1>
        <p>Ask about exams, eligibility, salaries, books, colleges, or anything career-related.</p>
      </div>

      <div className="card assistant-page__chat-card">
        <div className="assistant-page__messages" ref={scrollRef}>
          {messages.map((m, i) => (
            <div key={i} className={`assistant-page__bubble-row ${m.role === 'user' ? 'is-user' : ''}`}>
              {m.role === 'assistant' && (
                <div className="assistant-page__avatar"><Icon name="bot" size={16} color="#fff" /></div>
              )}
              <div className={`assistant-page__bubble ${m.role === 'user' ? 'assistant-page__bubble--user' : 'assistant-page__bubble--bot'}`}>
                {m.content}
              </div>
            </div>
          ))}

          {sending && (
            <div className="assistant-page__bubble-row">
              <div className="assistant-page__avatar"><Icon name="bot" size={16} color="#fff" /></div>
              <div className="assistant-page__bubble assistant-page__bubble--bot assistant-page__typing">
                <span /><span /><span />
              </div>
            </div>
          )}
        </div>

        {messages.length <= 1 && suggestions.length > 0 && (
          <div className="assistant-page__suggestions">
            {suggestions.map((s) => (
              <button key={s} className="assistant-page__suggestion-chip" onClick={() => sendMessage(s)}>{s}</button>
            ))}
          </div>
        )}

        <form onSubmit={handleSubmit} className="assistant-page__input-row">
          <input
            className="assistant-page__input"
            placeholder="Ask about a career, exam, or preparation strategy..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <button type="submit" className="assistant-page__send-btn" disabled={sending || !input.trim()} aria-label="Send message">
            <Icon name="send" size={17} color="#fff" />
          </button>
        </form>
      </div>
    </div>
  )
}
