import React, {useState} from 'react'
import axios from 'axios'
export default function Login(){
  const [email,setEmail]=useState('')
  const [password,setPassword]=useState('')
  const [msg,setMsg]=useState('')
  async function submit(e){
    e.preventDefault()
    try{
      const res = await axios.post('http://localhost:8000/auth/login', {email, password})
      localStorage.setItem('token', res.data.access_token)
      setMsg('Logged in — token saved to localStorage')
    }catch(err){
      setMsg('Login failed')
    }
  }
  return (
    <div className="card">
      <h2>Login</h2>
      <form onSubmit={submit}>
        <input placeholder="email" value={email} onChange={e=>setEmail(e.target.value)} required/>
        <input placeholder="password" type="password" value={password} onChange={e=>setPassword(e.target.value)} required/>
        <button>Login</button>
      </form>
      <p>{msg}</p>
    </div>
  )
}
