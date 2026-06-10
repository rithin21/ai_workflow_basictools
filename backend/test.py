import requests

def ask_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model":"llama3.2:1b",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }
    )

    return response.json()["message"]["content"]

print("before")

print(ask_llm("what is ai"))

print("after")