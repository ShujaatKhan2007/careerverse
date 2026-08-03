import { Link } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import Icon from '../components/Icon'
import './Landing.css'

const FEATURES = [
  { icon: 'compass', title: 'Career Recommendation Engine', desc: 'Tell us your age, education, and dream career - get a full personalized guidance report instantly.' },
  { icon: 'award', title: 'Exam Eligibility Checker', desc: 'Instantly verify whether you meet the age, education, and percentage criteria for entrance exams.' },
  { icon: 'book', title: 'Preparation Roadmaps', desc: 'Step-by-step strategies, best books, and free & paid resources for every career path.' },
  { icon: 'bot', title: 'AI Career Assistant', desc: 'Chat with an AI assistant that knows exam patterns, salaries, colleges, and more.' },
  { icon: 'clock', title: 'Study Planner & Tracker', desc: 'Build a personalized study plan and track your progress toward your dream career.' },
  { icon: 'chart', title: 'Career Comparison', desc: 'Compare salary, difficulty, and growth across multiple careers side-by-side.' },
]

const STEPS = [
  { n: '01', title: 'Share your profile', desc: 'Age, education, stream, percentage, and dream career.' },
  { n: '02', title: 'Get matched instantly', desc: 'Our engine matches you to a detailed career guidance report.' },
  { n: '03', title: 'Plan and prepare', desc: 'Save careers, build a study plan, and track your progress.' },
]

export default function Landing() {
  const { user } = useAuth()

  return (
    <div className="landing">
      <section className="landing__hero">
        <div className="container landing__hero-inner">
          <span className="landing__eyebrow">AI-Powered Career Guidance</span>
          <h1 className="landing__headline">
            Discover Your Career. <br /><span className="landing__headline-accent">Build Your Future.</span>
          </h1>
          <p className="landing__subhead">
            CareerVerse guides students from confusion to clarity - matching your profile to the right career,
            the right exam, and a real preparation roadmap.
          </p>
          <p style={{ fontSize: 12.5, color: 'var(--text-secondary)', marginBottom: 20 }}>Developed by Shujaat Khan</p>
          <div className="landing__cta-row">
            <Link to={user ? '/guidance' : '/register'} className="btn btn-primary">
              {user ? 'Start Career Guidance' : 'Get Started Free'} <Icon name="chevronRight" size={16} />
            </Link>
            <Link to="/explorer" className="btn btn-secondary">Explore Careers</Link>
          </div>
        </div>
      </section>

      <section className="container landing__features">
        <div className="section-title" style={{ display: 'block', textAlign: 'center' }}>
          <h2>Everything you need to choose confidently</h2>
          <p style={{ maxWidth: 520, margin: '0 auto' }}>One platform for career discovery, exam prep, and progress tracking.</p>
        </div>
        <div className="landing__feature-grid">
          {FEATURES.map((f) => (
            <div className="card landing__feature-card" key={f.title}>
              <div className="landing__feature-icon"><Icon name={f.icon} size={22} color="var(--color-primary)" /></div>
              <h3 style={{ fontSize: 16 }}>{f.title}</h3>
              <p style={{ fontSize: 13.5 }}>{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="container landing__steps">
        <h2 style={{ textAlign: 'center' }}>How it works</h2>
        <div className="landing__steps-grid">
          {STEPS.map((s) => (
            <div key={s.n} className="landing__step">
              <span className="landing__step-num">{s.n}</span>
              <h3 style={{ fontSize: 16 }}>{s.title}</h3>
              <p style={{ fontSize: 13.5 }}>{s.desc}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="landing__cta-band">
        <div className="container" style={{ textAlign: 'center' }}>
          <h2 style={{ color: '#fff' }}>Ready to find your path?</h2>
          <p style={{ color: 'rgba(255,255,255,0.85)', maxWidth: 460, margin: '0 auto 20px' }}>
            Join CareerVerse and get a personalized career roadmap in under 2 minutes.
          </p>
          <Link to={user ? '/guidance' : '/register'} className="btn" style={{ background: '#fff', color: 'var(--color-primary)' }}>
            {user ? 'Start Now' : 'Create Free Account'}
          </Link>
        </div>
      </section>
    </div>
  )
}
