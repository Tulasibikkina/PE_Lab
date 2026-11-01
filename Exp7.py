#EXPERIMENT 7: CONSTRAINT SPECIFICATION & ITERATIVE REFINEMENT

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
# PREPARE THE ARTICLE
# =========================================

article = """
Cloud computing is a computing model that provides computing
resources such as servers, storage, databases, networking and
software through the Internet. Instead of purchasing and
maintaining physical infrastructure, organizations can access
computing resources when needed.

Cloud computing commonly provides three service models:
Infrastructure as a Service (IaaS), Platform as a Service
(PaaS), and Software as a Service (SaaS). IaaS provides
virtualized computing resources, PaaS provides a platform for
developing and deploying applications, and SaaS provides
software applications through the Internet.

Important benefits of cloud computing include scalability,
flexibility, resource sharing and reduced infrastructure
maintenance. Organizations can increase or decrease resources
according to demand. However, cloud computing also requires
attention to security, privacy, availability and data management.
"""


# =========================================
# PART A: INITIAL PROMPT
# =========================================

prompt_basic = f"""
Summarize the following technical article.

Article:
{article}
"""

response_basic = client.models.generate_content(
    model=model_name,
    contents=prompt_basic
)

output_basic = response_basic.text or ""

print("INITIAL PROMPT OUTPUT")
print("=" * 60)
print(output_basic)


# =========================================
# PART B: REFINEMENT CYCLE 1
# =========================================

prompt_cycle1 = f"""
Summarize the following technical article.

Requirements:
1. Write approximately 100 words.
2. Use exactly five bullet points.
3. Use simple English.
4. Include the definition of cloud computing.
5. Mention the three cloud service models.
6. Mention the benefits of cloud computing.
7. Include scalability and security concerns.

Article:
{article}
"""

response_cycle1 = client.models.generate_content(
    model=model_name,
    contents=prompt_cycle1
)

output_cycle1 = response_cycle1.text or ""

print("\nREFINEMENT CYCLE 1 OUTPUT")
print("=" * 60)
print(output_cycle1)


# =========================================
# PART C: REFINEMENT CYCLE 2
# =========================================

prompt_cycle2 = f"""
Summarize the following technical article.

Follow all the instructions:

1. Create exactly five numbered points.
2. Each point must contain one concise sentence.
3. The complete summary must be between 90 and 110 words.
4. Use simple academic English.
5. Include the definition of cloud computing.
6. Include IaaS, PaaS and SaaS.
7. Include the major benefits of cloud computing.
8. Include scalability, security and privacy.
9. Do not add information that is not in the article.
10. Do not include an introduction or conclusion.

Article:
{article}
"""

response_cycle2 = client.models.generate_content(
    model=model_name,
    contents=prompt_cycle2
)

output_cycle2 = response_cycle2.text or ""

print("\nREFINEMENT CYCLE 2 OUTPUT")
print("=" * 60)
print(output_cycle2)


# =========================================
# FINAL COMPARISON
# =========================================

print("\nFINAL COMPARISON")
print("=" * 60)

print("\n1. INITIAL PROMPT")
print(output_basic)

print("\n2. REFINEMENT CYCLE 1")
print(output_cycle1)

print("\n3. REFINEMENT CYCLE 2")
print(output_cycle2)