from google.adk.agents.llm_agent import Agent
from .resource.agent import resource_fetching_agent
from .quizy.agent import quiz_agent
from .evaluator.agent import evaluator_agent

import json
import os

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "memory.json")

# Memory helpers
def get_memory(user_id="default_user"):
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)
    return data.get(user_id, {})

def set_memory(user_id="default_user", memory=None):
    if memory is None:
        memory = {}
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}
    data[user_id] = memory
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ✅ Merge tools properly
combined_tools = []
if resource_fetching_agent.tools:
    combined_tools.extend(resource_fetching_agent.tools)
if quiz_agent.tools:
    combined_tools.extend(quiz_agent.tools)
if evaluator_agent.tools:
    combined_tools.extend(evaluator_agent.tools)

# Host / Planning Agent
root_agent = Agent(
    name="PlanningAgent",
    model="gemini-2.5-flash",
    description=(
        "Host (Master Mentor) Agent in a multi-goal Autonomous AI Mentor system. "
        "Plans learning journeys, tracks progress, delegates resource collection, "
        "and triggers evaluation through sub-agents."
    ),
    instruction="""
        You are the Host (Master Mentor) Agent.

        Your responsibilities:
        - Accept the user's goal or intent (study, skill, habit, career, wellness, etc.).
        - Analyze the goal and plan a structured, step-by-step journey.
        - Decide the immediate next actionable step autonomously.
        - Invoke the Resource Agent to fetch learning or support material.
        - Track user progress and store memory across sessions.
        - After completion of any step, trigger Quizy to evaluate learning or progress.

        Rules:
        - The user should NOT ask explicitly for resources or quizzes.
        - You decide when to fetch resources.
        - You decide when a topic or milestone is complete.
        - You decide when Quizy must be triggered.
        """,
    tools=combined_tools,
)
