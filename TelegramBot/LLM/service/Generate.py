from TelegramBot.configuration.LLMApiConfig import GROQ_API_KEY, LLM_PROVIDER_API_URL
import openai

from typing import List


client = openai.OpenAI(
    base_url=LLM_PROVIDER_API_URL,
    api_key=GROQ_API_KEY  
)

async def generateResponse(strings: List[str]) -> str:
    prompt = " ".join(strings)

    response = client.chat.completions.create(
        model="llama-3.2-90b-vision-preview",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.1)
    
    return response.choices[0].message.content  # Estrai il contenuto della risposta
