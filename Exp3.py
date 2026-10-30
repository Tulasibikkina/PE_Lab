#EXPERIMENT 3

# Using Google Gemini API
from google import genai
from google.colab import userdata


# API CONFIGURATION
api_key = userdata.get("Gemini_API_Key1")

if not api_key:
    raise ValueError("Gemini API key is not configured.")

client = genai.Client(api_key=api_key)

model_name = "gemini-3.5-flash-lite"

# ITERATION 1: MINIMAL INSTRUCTION
prompt_1 = """
Summarize the plot of Romeo and Juliet.
"""

response_1 = client.models.generate_content(
    model=model_name,
    contents=prompt_1
)

output_1 = response_1.text

# ITERATION 2: LENGTH AND STYLE
prompt_2 = """
Summarize the plot of Romeo and Juliet in exactly two sentences.
Use simple English and an academic style suitable for B.Tech students.
"""

response_2 = client.models.generate_content(
    model=model_name,
    contents=prompt_2
)

output_2 = response_2.text


# ITERATION 3: SETTING, THEME AND CONTENT
prompt_3 = """
Summarize the plot of Romeo and Juliet in exactly two sentences.

The summary must include:
1. The main conflict between the two families.
2. The setting of Verona.
3. The relationship between Romeo and Juliet.
4. The major theme of love and conflict.
5. The tragic outcome of the story.
"""

response_3 = client.models.generate_content(
    model=model_name,
    contents=prompt_3
)

output_3 = response_3.text

# DISPLAY RESULTS
print("=" * 70)
print("ITERATION 1 - MINIMAL PROMPT")
print("=" * 70)
print("Prompt:")
print(prompt_1)
print("\nOutput:")
print(output_1)

print("\n")

print("=" * 70)
print("ITERATION 2 - LENGTH AND STYLE CONSTRAINTS")
print("=" * 70)
print("Prompt:")
print(prompt_2)
print("\nOutput:")
print(output_2)

print("\n")

print("=" * 70)
print("ITERATION 3 - SETTING, THEME AND CONTENT")
print("=" * 70)
print("Prompt:")
print(prompt_3)
print("\nOutput:")
print(output_3)