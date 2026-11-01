# EXPERIMENT 5: ZERO-SHOT Vs ONE-SHOT COMPARISION
 
# Using Google Gemini API
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
# PART A: ZERO-SHOT PROMPTING
# =========================================

zero_shot_prompt = """
Classify the sentiment of each sentence as exactly one of:
Positive, Negative, or Neutral.

Return only the sentiment labels in numbered order.
Do not provide explanations.

Sentences:

1. The laboratory session was very interesting.
2. The software installation failed several times.
3. The class started at 10 AM.
4. The teacher explained the experiment clearly.
5. The computer stopped working during the experiment.
6. The students submitted the record on Thursday.
"""

response_zero = client.models.generate_content(
    model=model_name,
    contents=zero_shot_prompt
)

zero_output = response_zero.text or ""

print("ZERO-SHOT OUTPUT")
print("=" * 50)
print(zero_output)


# =========================================
# PART B: FEW-SHOT PROMPTING
# =========================================

few_shot_prompt = """
Classify the sentiment of each sentence as:
Positive, Negative, or Neutral.

Follow the examples.

Example 1:
Input: The laboratory was excellent.
Output: Positive

Example 2:
Input: The computer was not working.
Output: Negative

Example 3:
Input: The class started at 10 AM.
Output: Neutral

Now classify the following sentences:

1. The laboratory session was very interesting.
2. The software installation failed several times.
3. The class started at 10 AM.
4. The teacher explained the experiment clearly.
5. The computer stopped working during the experiment.
6. The students submitted the record on Thursday.

Return only the numbered sentiment labels.
Do not provide explanations.
"""

response_few = client.models.generate_content(
    model=model_name,
    contents=few_shot_prompt
)

few_output = response_few.text or ""

print("\nFEW-SHOT OUTPUT")
print("=" * 50)
print(few_output)