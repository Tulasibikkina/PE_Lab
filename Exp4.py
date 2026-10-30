#EXPERIMENT 4

# Using Google Gemini API
from google import genai
from google.colab import userdata

# API CONFIGURATION
api_key = userdata.get("Gemini_API_Key1")

if not api_key:
    raise ValueError("Gemini API key is not configured.")

client = genai.Client(api_key=api_key)
model_name = "gemini-3.5-flash-lite"


# CASE 1: AMBIGUITY
prompt_1_bad = """
Explain Python.
"""
response_1_bad = client.models.generate_content(
    model=model_name,
    contents=prompt_1_bad
)

output_1_bad = response_1_bad.text

prompt_1_good = """
You are a Python programming instructor.

Explain the Python programming language to first-year
B.Tech IT students.

Include:
1. Definition of Python
2. Three important features
3. Three common applications

Use simple English and present the answer using
headings and bullet points.
"""

response_1_good = client.models.generate_content(
    model=model_name,
    contents=prompt_1_good
)

output_1_good = response_1_good.text


# CASE 2: MISSING CONTEXT
prompt_2_bad = """
Summarize the project.
"""

response_2_bad = client.models.generate_content(
    model=model_name,
    contents=prompt_2_bad
)

output_2_bad = response_2_bad.text

prompt_2_good = """
Summarize the following project for a B.Tech project report
in approximately 100 words.

Project Title: Smart Campus Attendance System

Project Description:
The project uses face recognition to automatically record
student attendance. A camera captures the student's face,
the system compares it with registered student data,
and attendance is recorded in a database.

Include the objective, basic working process and main benefit.
Use simple academic English.
"""

response_2_good = client.models.generate_content(
    model=model_name,
    contents=prompt_2_good
)

output_2_good = response_2_good.text


# CASE 3: FORMAT ERROR
prompt_3_bad = """
Give information about three programming languages.
"""

response_3_bad = client.models.generate_content(
    model=model_name,
    contents=prompt_3_bad
)

output_3_bad = response_3_bad.text

prompt_3_good = """
Create a Markdown table comparing exactly three programming
languages: Python, Java and C++.

Use the following columns:
Language | Main Use | Key Feature | Difficulty Level

Provide exactly one row for each programming language.
Do not add information outside the table.
"""

response_3_good = client.models.generate_content(
    model=model_name,
    contents=prompt_3_good
)

output_3_good = response_3_good.text


# DISPLAY RESULTS
print("=" * 70)
print("CASE 1 - AMBIGUITY")
print("=" * 70)

print("\nFAULTY OUTPUT:")
print(output_1_bad)

print("\nREFINED OUTPUT:")
print(output_1_good)

print("\n")

print("=" * 70)
print("CASE 2 - MISSING CONTEXT")
print("=" * 70)

print("\nFAULTY OUTPUT:")
print(output_2_bad)

print("\nREFINED OUTPUT:")
print(output_2_good)

print("\n")

print("=" * 70)
print("CASE 3 - FORMAT ERROR")
print("=" * 70)

print("\nFAULTY OUTPUT:")
print(output_3_bad)

print("\nREFINED OUTPUT:")
print(output_3_good)

print("\nResult: All three prompt failure cases were executed.")
