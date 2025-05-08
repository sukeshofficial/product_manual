from openai import OpenAI

client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = "<your OpenAI_KEY>"
)

def token(messages, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model = model,
        messages=[
            {
                "role": "system",
                "content": '''
                    Your name is 'Fixer AI'. You are a helpful Product Manual Assistant.
                    Use emojis, neat answers, and avoid markdown. Don't guess answers.
                    Use tables, bullet points, or code blocks if asked.
                    If unrelated to product manuals, say: "Search the web, my knowledge is limited to the product information."
                '''
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": messages
                    }
                ]
            }
        ],
        stream=True
    )
    
    for chunk in response:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content