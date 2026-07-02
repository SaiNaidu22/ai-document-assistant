from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_answer(question, context):

    prompt = f"""
You are an AI assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}

If the answer is not found in the context,
say "I couldn't find that information in the uploaded document."
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print(f"Gemini Error: {e}")   # Shows error in Render logs
        return f"Gemini Error: {str(e)}"