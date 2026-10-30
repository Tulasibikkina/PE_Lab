#EXPERIMENT 2

# Using Google Gemini API
from google import genai
from google.colab import userdata



# API CONFIGURATION

api_key = userdata.get("Gemini_API_Key1")

if not api_key:
    raise ValueError("Gemini API key is not configured.")

client = genai.Client(api_key=api_key)

model_name = "gemini-3.5-flash-lite"


# BASELINE PROMPT

baseline_prompt = """
Write a one-paragraph bio of Ada Lovelace.
"""

response1 = client.models.generate_content(
    model=model_name,
    contents=baseline_prompt
)

baseline_output = response1.text


# ENHANCED PROMPT

enhanced_prompt = """
You are a computer science history teacher.

Write a short biography of Ada Lovelace for first-year
B.Tech students.

Include:
1. Her full name
2. Her contribution to computing
3. Her association with Charles Babbage
4. One important achievement

Requirements:
- Use simple English.
- Write approximately 150 words.
- Use one paragraph.
- Maintain an educational and professional tone.
"""

response2 = client.models.generate_content(
    model=model_name,
    contents=enhanced_prompt
)

enhanced_output = response2.text


# DISPLAY RESULTS

print("=" * 60)
print("BASELINE PROMPT")
print("=" * 60)
print(baseline_prompt)

print("\nBASELINE OUTPUT")
print("=" * 60)
print(baseline_output)

print("\n")

print("=" * 60)
print("ENHANCED PROMPT")
print("=" * 60)
print(enhanced_prompt)

print("\nENHANCED OUTPUT")
print("=" * 60)
print(enhanced_output)

print("\nResult: Both prompts have been executed.")