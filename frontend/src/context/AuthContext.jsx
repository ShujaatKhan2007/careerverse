import { createContext, useContext, useState, useEffect, useCallback } from 'react'
import api from '../services/api'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  const fetchMe = useCallback(async () => {
    const token = localStorage.getItem('cv_access_token')
    if (!token) {
      setLoading(false)
      return
    }
    try {
      const { data } = await api.get('/api/auth/me')
      setUser(data)
    } catch {
      localStorage.removeItem('cv_access_token')
      localStorage.removeItem('cv_refresh_token')
      setUser(null)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchMe()
  }, [fetchMe])

  const login = async (email, password) => {
    const { data } = await api.post('/api/auth/login', { email, password })
    localStorage.setItem('cv_access_token', data.access_token)
    localStorage.setItem('cv_refresh_token', data.refresh_token)
    await fetchMe()
  }

  const register = async (name, email, password) => {
    const { data } = await api.post('/api/auth/register', { name, email, password })
    localStorage.setItem('cv_access_token', data.access_token)
    localStorage.setItem('cv_refresh_token', data.refresh_token)
    await fetchMe()
  }

  const logout = () => {
    localStorage.removeItem('cv_access_token')
    localStorage.removeItem('cv_refresh_token')
    setUser(null)
  }

  const updateUserLocal = (updates) => setUser((prev) => ({ ...prev, ...updates }))

  return (
    <AuthContext.Provider value={{ user, loading, login, register, logout, updateUserLocal, refetch: fetchMe }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => useContext(AuthContext)
