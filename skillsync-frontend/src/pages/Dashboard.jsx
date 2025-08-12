import React, {useState, useEffect} from 'react'
import axios from 'axios'
export default function Dashboard(){
  const [jobs, setJobs] = useState([])
  const [title, setTitle] = useState('')
  const [desc, setDesc] = useState('')
  useEffect(()=>{ fetchJobs() }, [])
  async function fetchJobs(){
    const res = await axios.get('http://localhost:8000/jobs/1').catch(()=>null)
    // simple demo: if job 1 not found, list empty
    if(res && res.data) setJobs([res.data])
  }
  async function createJob(e){
    e.preventDefault()
    try{
      const res = await axios.post('http://localhost:8000/jobs/', {title, description: desc})
      setJobs(prev=>[res.data, ...prev])
      setTitle(''); setDesc('')
    }catch(err){ console.error(err) }
  }
  async function uploadResume(e){
    const f = e.target.files[0]
    if(!f) return
    const fd = new FormData(); fd.append('file', f)
    try{
      const res = await axios.post('http://localhost:8000/resumes/upload', fd, { headers: {'Content-Type':'multipart/form-data'} })
      alert('Uploaded: '+JSON.stringify(res.data.parsed))
    }catch(err){ alert('Upload failed') }
  }
  async function getRecs(jobId){
    try{
      const res = await axios.get(`http://localhost:8000/jobs/${jobId}/recommendations`)
      alert('Recommendations: ' + JSON.stringify(res.data.recommendations))
    }catch(err){
      alert('Failed to get recommendations')
    }
  }
  return (
    <div className="container">
      <h1>SkillSync Dashboard</h1>
      <section className="card">
        <h3>Create Job</h3>
        <form onSubmit={createJob}>
          <input placeholder="title" value={title} onChange={e=>setTitle(e.target.value)} required/>
          <textarea placeholder="description" value={desc} onChange={e=>setDesc(e.target.value)} required/>
          <button>Create</button>
        </form>
      </section>
      <section className="card">
        <h3>Upload Resume</h3>
        <input type="file" onChange={uploadResume}/>
      </section>
      <section className="card">
        <h3>Jobs</h3>
        {jobs.length===0 && <p>No jobs yet (create one). Create a job titled 'Example' to test.</p>}
        <ul>
          {jobs.map(j=>(
            <li key={j.id}>
              <strong>{j.title}</strong>
              <p>{j.description}</p>
              <button onClick={()=>getRecs(j.id)}>Get Recommendations</button>
            </li>
          ))}
        </ul>
      </section>
    </div>
  )
}
