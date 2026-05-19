
from groq import Groq

# GROQ_API_KEY = "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"

client = Groq(
    api_key="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"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful virtual assistant named nexus skilled in task like Alexa and Google Cloud."
        },
        {
            "role": "user",
            "content": "What is LLM?",
        }
    ],

    model="llama-3.3-70b-versatile"
)

# Print the completion returned by the LLM.
print(chat_completion.choices[0].message.content)