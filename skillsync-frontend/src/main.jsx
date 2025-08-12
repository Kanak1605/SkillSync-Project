import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import './styles.css'
function App(){
  return (
    <BrowserRouter>
      <nav className="nav"><Link to='/'>Dashboard</Link> | <Link to='/login'>Login</Link></nav>
      <Routes>
        <Route path='/' element={<Dashboard/>}/>
        <Route path='/login' element={<Login/>}/>
      </Routes>
    </BrowserRouter>
  )
}
createRoot(document.getElementById('root')).render(<App />)
