# EXPERIMENT 9: JSON/YAML GENERATION AND VALIDATION
# Using Google Gemini API

!pip install -q -U google-genai PyYAML
import json
import yaml
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
# STEP 2: PREPARE THE DATASET
# ==================================================

dataset_description = """
The dataset contains three books:

1. Title: The Alchemist
   Author: Paulo Coelho
   Publication Year: 1988

2. Title: 1984
   Author: George Orwell
   Publication Year: 1949

3. Title: Pride and Prejudice
   Author: Jane Austen
   Publication Year: 1813
"""

# ==================================================
# PART A: BASIC JSON GENERATION
# ==================================================

json_prompt = f"""
Convert the following book dataset into JSON.

{dataset_description}
"""

response_json = client.models.generate_content(
    model=model_name,
    contents=json_prompt
)

json_output = response_json.text or ""

print("\n" + "=" * 60)
print("INITIAL JSON OUTPUT")
print("=" * 60)
print(json_output)

# ==================================================
# STEP 3: VALIDATE INITIAL JSON
# ==================================================

print("\nINITIAL JSON VALIDATION")

try:
    initial_json_data = json.loads(json_output)
    print("Valid JSON")
    print(initial_json_data)

except json.JSONDecodeError as e:
    initial_json_data = None
    print("Invalid JSON")
    print("Error:", e)

# ==================================================
# PART B: REFINED JSON PROMPT
# ==================================================

refined_json_prompt = f"""
Convert the following book dataset into valid JSON.

Dataset:
{dataset_description}

Requirements:
1. Create one JSON object containing a key named "books".
2. The value of "books" must be an array.
3. Each book must contain exactly these fields:
   - title
   - author
   - publication_year
4. Use the exact information provided in the dataset.
5. Return only valid JSON.
6. Do not include Markdown code fences.
7. Do not include explanations or additional text.
"""

response_json_refined = client.models.generate_content(
    model=model_name,
    contents=refined_json_prompt
)

json_output_refined = response_json_refined.text or ""

print("\n" + "=" * 60)
print("REFINED JSON OUTPUT")
print("=" * 60)
print(json_output_refined)

# ==================================================
# STEP 4: VALIDATE REFINED JSON
# ==================================================

print("\nREFINED JSON VALIDATION")

json_data = None

try:
    json_data = json.loads(json_output_refined)
    print("Valid JSON")

except json.JSONDecodeError as e:
    print("Invalid JSON")
    print("Error:", e)

# ==================================================
# STEP 5: VERIFY JSON STRUCTURE
# ==================================================

print("\nJSON STRUCTURE VALIDATION")

if isinstance(json_data, dict) and "books" in json_data:
    print("Key 'books': FOUND")

    if isinstance(json_data["books"], list):
        print("Books is an array.")
        print("Number of books:", len(json_data["books"]))

        required_fields = {
            "title",
            "author",
            "publication_year"
        }

        structure_correct = True

        for index, book in enumerate(json_data["books"], start=1):
            if (
                isinstance(book, dict)
                and set(book.keys()) == required_fields
            ):
                print(f"Book {index}: Structure CORRECT")
            else:
                print(f"Book {index}: Structure INCORRECT")
                structure_correct = False

        if len(json_data["books"]) != 3:
            print("Expected exactly three books.")
            structure_correct = False

        if structure_correct:
            print("Overall JSON structure: CORRECT")
        else:
            print("Overall JSON structure: INCORRECT")

    else:
        print("'books' must be an array.")

else:
    print("Required top-level key 'books' is missing.")

# ==================================================
# PART C: YAML GENERATION
# ==================================================

yaml_prompt = f"""
Convert the following book dataset into valid YAML.

{dataset_description}

Requirements:
- Create a top-level key named "books".
- Represent the three books as a list.
- Each book must contain:
  title
  author
  publication_year
- Return only YAML.
- Do not include Markdown code fences.
- Do not include explanations.
"""

response_yaml = client.models.generate_content(
    model=model_name,
    contents=yaml_prompt
)

yaml_output = response_yaml.text or ""

print("\n" + "=" * 60)
print("GENERATED YAML OUTPUT")
print("=" * 60)
print(yaml_output)

# ==================================================
# STEP 6: VALIDATE YAML
# ==================================================

print("\nYAML VALIDATION")

yaml_data = None

try:
    yaml_data = yaml.safe_load(yaml_output)
    print("Valid YAML")

except yaml.YAMLError as e:
    print("Invalid YAML")
    print("Error:", e)

# ==================================================
# STEP 7: VERIFY YAML STRUCTURE
# ==================================================

print("\nYAML STRUCTURE VALIDATION")

if isinstance(yaml_data, dict) and "books" in yaml_data:
    print("Key 'books': FOUND")

    if isinstance(yaml_data["books"], list):
        print("Books is a list.")
        print("Number of books:", len(yaml_data["books"]))

        required_fields = {
            "title",
            "author",
            "publication_year"
        }

        structure_correct = True

        for index, book in enumerate(yaml_data["books"], start=1):
            if (
                isinstance(book, dict)
                and set(book.keys()) == required_fields
            ):
                print(f"Book {index}: Structure CORRECT")
            else:
                print(f"Book {index}: Structure INCORRECT")
                structure_correct = False

        if len(yaml_data["books"]) != 3:
            print("Expected exactly three books.")
            structure_correct = False

        if structure_correct:
            print("Overall YAML structure: CORRECT")
        else:
            print("Overall YAML structure: INCORRECT")

    else:
        print("'books' must be a list.")

else:
    print("Required top-level key 'books' is missing.")

# ==================================================
# FINAL RESULT
# ==================================================

print("\n" + "=" * 60)
print("EXPERIMENT 9 COMPLETED")
print("=" * 60)
print("Initial JSON, refined JSON and YAML tasks executed.")
print("Review the validation results and record observations.")