#EXPERIMENT 1

#Step 1: Import required libraries
import sys
from google import genai
from google.colab import userdata
# Step 2: Display Python version
print("Python Version:")
print(sys.version)
# Step 3: Retrieve API key from Colab Secrets
api_key = userdata.get("Gemini_API_Key1")

if not api_key:
    raise ValueError("Gemini API key is not configured.")

print("\nGemini API key detected successfully.")

# Step 4: Initialize Gemini client
client = genai.Client(api_key=api_key)

print("Gemini client initialized successfully.")
# Step 5: Define the prompt
prompt = "Hello, world! Introduce yourself in one sentence."
# Step 6: Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

# Step 7: Display the output
print("\n" + "=" * 50)
print("EXPERIMENT 1: ENVIRONMENT & CONNECTIVITY")
print("=" * 50)

print("\nPrompt:")
print(prompt)

print("\nModel Response:")
print(response.text)