
import os
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables
load_dotenv()

# Step 2: Get API key and model name
api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL")

# Step 3: Check API key
if not api_key:
    raise ValueError("Gemini API key not found in .env file")

# Step 4: Create Gemini client
client = genai.Client(api_key=api_key)

# Step 5: Send a request to Gemini
response = client.models.generate_content(
    model=model_name,
    contents="Explain what Python automation is in 3 simple sentences."
)

# Step 6: Print AI response
print("Gemini Response:")
print(response.text)

# Step 7: Close the client
client.close()
