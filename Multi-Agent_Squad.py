import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  # Fixed typo here

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Configuration Error: GEMINI_API_KEY not found in .env file.")
    exit()

# Initialize the Google GenAI (Gemini) Model
# Since our .env uses GEMINI_API_KEY, we pass it explicitly here.
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.7,
    google_api_key=api_key  # Explicitly map your key here
)

print("Starting the Sequential LangChain Workflow...\n") 

# Phase 1: Defining the Personas & Prompts


# Persona 1: The Senior Research Analyst
researcher_template = """
You are a Senior Research Analyst. Your background is in uncovering deep technical nuances, 
cutting-edge AI trends, and practical enterprise use cases for autonomous systems.

Goal: Investigate and identify exactly 3 specific "Breakthroughs" or "Trends" related to 
AI agents and Agentic Workflows that are projected to dominate by 2026. 

Provide explicit technical details and a brief, impactful real-world use case for each breakthrough.
Structure your findings as a formal "Research Report".
"""

researcher_prompt = ChatPromptTemplate.from_template(researcher_template)

# Persona 2: The Content Strategist
writer_template = """
You are a Content Strategist and a master of digital storytelling, copywriting, and professional networking growth. 
Your expertise lies in taking dense, complex technical jargon and turning it into highly engaging, viral content.

Goal: Take the following "Research Report" provided by the Senior Research Analyst and synthesize it into a viral LinkedIn post.

You MUST strictly follow the Hook-Value-CTA framework:
- Hook: Grab the reader's attention immediately with a bold statement or question about the future of AI.
- Value: Break down the 3 breakthroughs from the report clearly, using emojis, bullet points, and an engaging tone.
- Call to Action (CTA): Conclude with a thought-provoking question to maximize comments and community discussion.

Research Report Data:
{research_report}
"""

writer_prompt = ChatPromptTemplate.from_template(writer_template)


# Phase 2 & 3: Orchestration & Execution (LangChain Expression Language Chain)
#LCEL is better than "Sequential Chain," hence that is used


# Step 1: Execute the Researcher Chain to get the report
print("[Log] Agent 1 (Researcher) is analyzing 2026 Agentic Workflow trends...")
researcher_chain = researcher_prompt | llm | StrOutputParser() #LCEL uses "|" operator to pass data from one step to the next
research_report = researcher_chain.invoke({})

print("\n [Agent Log: Sequential Handoff] ")
print("Researcher has compiled the technical data. Handing report over to the Content Strategist...\n")

# Step 2: Feed the Researcher's output directly into the Writer Chain
print("[Log] Agent 2 (Writer) is converting technical nuances into a high-engagement LinkedIn post...")
writer_chain = writer_prompt | llm | StrOutputParser()
final_linkedin_post = writer_chain.invoke({"research_report": research_report})

# Final Output Display
print("\n")
print(" FINAL LINKEDIN POST OUTPUT")
print("\n")
print(final_linkedin_post)
