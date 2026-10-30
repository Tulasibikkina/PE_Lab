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

# Common function to send prompts to Gemini
def ask_gemini(prompt):
    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )
    return response.text or ""


# =========================================
# LOGIC PUZZLE
# =========================================

puzzle = """
Five students—Asha, Bharat, Charan, Divya and Esha—
are standing in a line from position 1 to position 5.

The following conditions apply:

1. Asha is standing to the left of Bharat.
2. Charan is standing in position 3.
3. Divya is standing immediately to the right of Bharat.
4. Esha is not standing at either end of the line.

Question:
What is the correct order of the five students
from position 1 to position 5?
"""


# =========================================
# 1. DIRECT-ANSWER BASELINE
# =========================================

direct_prompt = f"""
Solve the following logic puzzle and give the final answer.

{puzzle}

Provide the order of the five students from
position 1 to position 5.
"""

direct_output = ask_gemini(direct_prompt)

print("1. DIRECT-ANSWER OUTPUT")
print("=" * 60)
print(direct_output)


# =========================================
# 2. ZERO-SHOT CHAIN-OF-THOUGHT
# =========================================

cot_prompt = f"""
Solve the following logic puzzle.

Let's think step by step.
Give a concise explanation of the key deductions
before providing the final answer.

{puzzle}

Provide the final order of the five students
from position 1 to position 5.
"""

cot_output = ask_gemini(cot_prompt)

print("\n2. ZERO-SHOT CoT OUTPUT")
print("=" * 60)
print(cot_output)


# =========================================
# 3. TASK DECOMPOSITION
# =========================================

# Sub-question 1

sub1_prompt = f"""
Read the following logic puzzle.

{puzzle}

Sub-question 1:
What position is definitely occupied, and by whom?

Give only the answer and a short explanation.
"""

sub1_output = ask_gemini(sub1_prompt)

print("\nSUB-QUESTION 1")
print("=" * 60)
print(sub1_output)


# Sub-question 2

sub2_prompt = f"""
Solve the following logic puzzle.

{puzzle}

Previous result:
{sub1_output}

Sub-question 2:
What possible adjacent positions can Bharat and Divya occupy,
considering that Divya stands immediately to the right of Bharat?

List the possible pairs and eliminate impossible pairs.
"""

sub2_output = ask_gemini(sub2_prompt)

print("\nSUB-QUESTION 2")
print("=" * 60)
print(sub2_output)


# Sub-question 3

sub3_prompt = f"""
Solve the following logic puzzle.

{puzzle}

Previous result 1:
{sub1_output}

Previous result 2:
{sub2_output}

Sub-question 3:
Using all the constraints, determine which remaining
arrangement is possible.

Explain the elimination briefly.
"""

sub3_output = ask_gemini(sub3_prompt)

print("\nSUB-QUESTION 3")
print("=" * 60)
print(sub3_output)


# Sub-question 4 – Combine Results

sub4_prompt = f"""
You are given a logic puzzle and the results of
three previous sub-questions.

Puzzle:
{puzzle}

Sub-question 1 result:
{sub1_output}

Sub-question 2 result:
{sub2_output}

Sub-question 3 result:
{sub3_output}

Sub-question 4:
Combine the previous results and provide the final
order of Asha, Bharat, Charan, Divya and Esha
from position 1 to position 5.

Return only the final order and a one-sentence justification.
"""

decomposed_output = ask_gemini(sub4_prompt)

print("\n4. TASK DECOMPOSITION – FINAL OUTPUT")
print("=" * 60)
print(decomposed_output)


# =========================================
# ACCURACY COMPARISON
# =========================================

correct_answer = [
    "Asha", "Esha", "Charan", "Bharat", "Divya"
]

print("\nACCURACY COMPARISON")
print("=" * 60)

print("Expected correct order:")
print(" -> ".join(correct_answer))

print("\nCompare the outputs of all three methods:")
print("1. Direct Answer")
print(direct_output)
print("\n2. Zero-Shot CoT")
print(cot_output)
print("\n3. Task Decomposition")
print(decomposed_output)

print("\nCheck each result manually against the correct order.")
