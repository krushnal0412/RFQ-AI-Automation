
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL")

client = genai.Client(api_key=api_key)


def generate_followup_email(rfq_data, missing_fields):

    if missing_fields:

        email_type = "INFORMATION REQUEST"

        instructions = f"""
        Generate a professional email asking the customer
        to provide the following missing information:

        {missing_fields}

        Only ask for the missing information.
        Do not ask for details already provided.
        """

    else:

        email_type = "ACKNOWLEDGMENT EMAIL"

        instructions = """
        Generate a professional acknowledgment email.

        Instructions:
        1. Thank the customer for sharing their RFQ.
        2. Summarize the requested material and quantity.
        3. Confirm that we have received their requirement.
        4. Inform them that our team will check product
           availability, pricing and delivery feasibility.
        5. Tell them we will get back to them with an update.
        6. Do not promise product availability or a delivery date.
        """

    prompt = f"""
    You are a professional procurement assistant.

    Email type: {email_type}

    Available RFQ information:
    {rfq_data}

    {instructions}

    Write a concise and professional email.
    Include a suitable subject line.
    Address the customer by name if available.

    Return only the email draft.
    """

    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )

    return response.text
