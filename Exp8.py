# EXPERIMENT 8: STRUCTURED FORMAT PROMPTING
# Using Google Gemini API

from google import genai
from google.colab import userdata

# ==================================================
# STEP 1: CONFIGURE GEMINI API
# ==================================================

api_key = userdata.get("Gemini_API_Key1")

if not api_key:
    raise ValueError(
        "Gemini API key is not configured. "
        "Check Colab Secrets."
    )

client = genai.Client(api_key=api_key)

model_name = "gemini-3.5-flash-lite"

print("Gemini client initialized successfully.")

# ==================================================
# PART A: BULLET LIST PROMPTING
# ==================================================

bullet_prompt = """
List five benefits of daily exercise.

Output requirements:
- Use exactly five bullet points.
- Each bullet point must contain one benefit.
- Use simple English.
- Do not use a table.
"""

response_bullet = client.models.generate_content(
    model=model_name,
    contents=bullet_prompt
)

bullet_output = response_bullet.text or ""

print("\n" + "=" * 60)
print("PART A: BULLET LIST OUTPUT")
print("=" * 60)
print(bullet_output)

# ==================================================
# VERIFY THE BULLET LIST
# ==================================================

bullet_lines = [
    line.strip()
    for line in bullet_output.splitlines()
    if line.strip().startswith(("-", "*", "•"))
]

print("\nNumber of bullet points detected:", len(bullet_lines))

if len(bullet_lines) == 5:
    print("Bullet count requirement: SATISFIED")
else:
    print("Bullet count requirement: CHECK OUTPUT")

# ==================================================
# PART B: MARKDOWN TABLE PROMPTING
# ==================================================

table_prompt = """
Create a Markdown table about three benefits of daily exercise.

The table must contain exactly two columns:
Benefit | Description

Include exactly three rows of benefits.
Do not provide information outside the table.
"""

response_table = client.models.generate_content(
    model=model_name,
    contents=table_prompt
)

table_output = response_table.text or ""

print("\n" + "=" * 60)
print("PART B: MARKDOWN TABLE OUTPUT")
print("=" * 60)
print(table_output)

# ==================================================
# VERIFY THE MARKDOWN TABLE
# ==================================================

table_lines = [
    line.strip()
    for line in table_output.splitlines()
    if "|" in line
]

print("\nNumber of table-related lines:", len(table_lines))

if (
    len(table_lines) >= 5
    and any("---" in line for line in table_lines)
):
    print("Markdown table structure detected.")
else:
    print("Please check the table format manually.")

# ==================================================
# FINAL RESULT
# ==================================================

print("\n" + "=" * 60)
print("EXPERIMENT 8 COMPLETED")
print("=" * 60)

print("Both structured prompting tasks have been executed.")
print("Inspect the outputs and complete the observation table.")
