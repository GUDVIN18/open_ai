from openai import OpenAI

client = OpenAI(
    api_key="sk-jJvbr5RZqhRAdHOuZ8yDkJZChdveL4N6",
    base_url="https://api.proxyapi.ru/openai/v1",
)

chat_completion = client.chat.completions.create(
    model="gpt-4", messages=[{"role": "user", "content": "Привет"}]
)

answer = chat_completion.choices[0].message.content
print(answer)
