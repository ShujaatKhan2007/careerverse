import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext'
import { ThemeProvider } from './context/ThemeContext'
import { ToastProvider } from './context/ToastContext'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import ProtectedRoute from './components/ProtectedRoute'

import Landing from './pages/Landing'
import Login from './pages/Login'
import Register from './pages/Register'
import Dashboard from './pages/Dashboard'
import CareerExplorer from './pages/CareerExplorer'
import CareerDetail from './pages/CareerDetail'
import CareerGuidance from './pages/CareerGuidance'
import CareerCompare from './pages/CareerCompare'
import AIAssistant from './pages/AIAssistant'
import SavedCareers from './pages/SavedCareers'
import StudyPlanner from './pages/StudyPlanner'
import Profile from './pages/Profile'
import AdminDashboard from './pages/AdminDashboard'
import NotFound from './pages/NotFound'

function Layout({ children }) {
  return (
    <>
      <Navbar />
      <main style={{ minHeight: 'calc(100vh - 68px)' }}>{children}</main>
      <Footer />
    </>
  )
}

export default function App() {
  return (
    <ThemeProvider>
      <ToastProvider>
        <AuthProvider>
          <BrowserRouter>
            <Layout>
              <Routes>
                <Route path="/" element={<Landing />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />

                <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
                <Route path="/explorer" element={<ProtectedRoute><CareerExplorer /></ProtectedRoute>} />
                <Route path="/career/:slug" element={<ProtectedRoute><CareerDetail /></ProtectedRoute>} />
                <Route path="/guidance" element={<ProtectedRoute><CareerGuidance /></ProtectedRoute>} />
                <Route path="/compare" element={<ProtectedRoute><CareerCompare /></ProtectedRoute>} />
                <Route path="/assistant" element={<ProtectedRoute><AIAssistant /></ProtectedRoute>} />
                <Route path="/saved" element={<ProtectedRoute><SavedCareers /></ProtectedRoute>} />
                <Route path="/study-plans" element={<ProtectedRoute><StudyPlanner /></ProtectedRoute>} />
                <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>} />
                <Route path="/admin" element={<ProtectedRoute adminOnly><AdminDashboard /></ProtectedRoute>} />

                <Route path="*" element={<NotFound />} />
              </Routes>
            </Layout>
          </BrowserRouter>
        </AuthProvider>
      </ToastProvider>
    </ThemeProvider>
  )
}
