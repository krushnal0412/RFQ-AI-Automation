import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL")

client = genai.Client(api_key=api_key)


def extract_rfq(email_text):

    prompt = prompt = f"""
Extract information from this RFQ email.

Return ONLY a valid JSON object.
Do not include markdown formatting.
Do not include explanations or ```json code fences.

Use these exact keys:
material
quantity
unit
delivery_location
delivery_timeline
contact_person
contact_email
contact_phone

If information is unavailable, use null.
Do not invent information.

RFQ Email:
{email_text}
"""

    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )

    print("Gemini raw response:")
    print(repr(response.text))

    rfq_data = json.loads(response.text)

    return rfq_data