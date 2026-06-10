from ollama import generate

response = generate(
    model="qwen3:8b",
    prompt="hello"
)

print(response)