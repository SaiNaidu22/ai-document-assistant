from google import genai
from google.genai.errors import ServerError
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
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text

    except ServerError:
        return "The AI service is temporarily busy. Please try again in a few moments."

    except Exception as e:
        return f"Unexpected error: {str(e)}"