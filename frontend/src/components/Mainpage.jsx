import React from 'react'
import { useState } from 'react';

export default function Mainpage() {
    const[query,setquery]=useState('')
    const[Response,setResponse]=useState('')

    const handlesubmit=async (e)=>{
        e.preventDefault();

        const response=await fetch('http://localhost:8000',
            {
                method:'POST',
                headers:{'Content-Type':'application/json'},
                body:JSON.stringify({query})
            }
        )
        const data=await response.json();
        console.log(data);
        setResponse(data.response);
    }
  return (
    <div className='container my-5'>
        <h2 className='text-center'>Lets learn something new today!</h2>
        <form className="d-flex my-5" role="search" onSubmit={handlesubmit}>
            <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" value={query} onChange={(e)=>{
                setquery(e.target.value)}}/>
            <button className="btn btn-outline-success" type="submit" >Go</button>
        </form>
        <p>{Response}</p>
    </div>
  )
}
