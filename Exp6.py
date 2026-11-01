#EXPERIMENT 6: ROLE BASED & NEGATIVE PROMPTING

from google import genai
from google.colab import userdata

# =========================================
# API CONFIGURATION
# =========================================

api_key = userdata.get("Gemini_API_Key1")

if not api_key:
    raise ValueError("API key is not configured.")

client = genai.Client(api_key=api_key)
model_name = "gemini-3.5-flash-lite"


# =========================================
# PART A: BASELINE PROMPT
# =========================================

baseline_prompt = """
Explain how a college student can manage monthly expenses.

Give five practical suggestions.
"""

response_baseline = client.models.generate_content(
    model=model_name,
    contents=baseline_prompt
)

baseline_output = response_baseline.text or ""

print("BASELINE OUTPUT")
print("=" * 60)
print(baseline_output)


# =========================================
# PART B: ROLE-BASED PROMPT
# =========================================

role_prompt = """
You are a financial advisor who specializes in helping
college students manage their monthly expenses.

Explain how a college student can manage monthly expenses.

Give five practical suggestions.
Use simple English.
"""

response_role = client.models.generate_content(
    model=model_name,
    contents=role_prompt
)

role_output = response_role.text or ""

print("\nROLE-BASED OUTPUT")
print("=" * 60)
print(role_output)


# =========================================
# PART C: ROLE + NEGATIVE PROMPT
# =========================================

negative_prompt = """
You are a financial advisor who specializes in helping
college students manage their monthly expenses.

Explain how a college student can manage monthly expenses.

Give five practical suggestions.
Use simple English.

Do not mention any brand names.
Do not recommend specific financial products.
Do not include advertisements.
"""

response_negative = client.models.generate_content(
    model=model_name,
    contents=negative_prompt
)

negative_output = response_negative.text or ""

print("\nROLE + NEGATIVE PROMPT OUTPUT")
print("=" * 60)
print(negative_output)