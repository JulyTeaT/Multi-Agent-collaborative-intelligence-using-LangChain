# Multi-Agent-collaborative-intelligence-using-LangChain

The project (using a researcher and a content specialist) gives a framework idea of Multi-Agent use to obtain collaborative intelligence, hence prompting multiple AI instances to "speak" to each other, delegate tasks, and refine outputs. This mimics a real-world workplace where a specialist gathers data and a creative professional packages it for an audience. The same can be implemented and executed using CrewAI

Key Learning Objectives: Focus on the Agent-Task-Crew hierarchy, how to define Agent Goals, and the process of Sequential execution, and modern LangChain Expression Language (LCEL).



*Phase 1: Defining the Personas

Focus: Specialization & Authority
Agent 1 (The Researcher): Role: Senior Research Analyst.
Goal: Uncover the latest developments in "Agentic Workflows" for 2026.
Backstory: An expert at finding technical nuances and industry use cases.
Agent 2 (The Writer): Role: Content Strategist.
Goal: Synthesize technical research into a viral, engaging LinkedIn post.
Backstory: A master of digital storytelling and professional networking growth.


*Phase 2: Orchestrating the Workflow

Focus: Task Delegation
The Research Task: Instruct the Researcher to find 3 specific "Breakthroughs" or "Trends" related to AI agents.
The Writing Task: Instruct the Writer to take the Researcher's output and format it using the Hook-Value-CTA framework (Hook to grab attention, Value for the meat, and a Call to Action).
Handoff Logic: Use a sequential process where the Writer cannot start until the Researcher provides the "Research Report."


*Phase 3: Execution & Output

Focus: Implementation
The Crew/Chain: Initialize your framework (CrewAI, LangGraph, or LangChain) and kick off the process.
The Result: Print the final LinkedIn post to the console or save it to a file.
Observation: Note how the "Writer" interprets the technical data differently than the "Researcher."


Tech Stack: LangChain, Google Gemini API (gemini-2.5-flash), Python, python-dotenv.
