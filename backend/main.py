from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ollama import chat
import os
from pydantic import BaseModel

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']

)


class UserQuery(BaseModel):
    query:str

def sleep_pc():
    os.system(
        "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
    )
    return 'pc sleeping'

def shutdown_pc():
    os.system('shutdown /s /t 0')
    return 'pc shutting down' 

@app.post('/')
def sendquery(data:UserQuery):
    user_query=data.query

    if 'sleep' in user_query.lower():
        return {
            #'response':sleep_pc()
            'response':'sleep called'
        }
    
    elif 'shutdown' in user_query.lower() or 'shut down' in user_query.lower():
        return {'response': 'shutdown called'}
    
    else:
        response = chat(
            model='llama3.2:1b',
            messages=[
                {
                    'role': 'user',
                    'content': data.query
                }
            ]
        )

        return {
            'response': response['message']['content']
        }