from google.adk.agents.llm_agent import Agent

# Import your reasoning agents (proof of integration)
from agents.emotion_agent import emotion_agent
from agents.motivation_agent import motivation_agent
from agents.analytics_agent import analytics_agent
from agents.resource_agent import resource_agent
from agents.reminder_agent import reminder_agent


root_agent = Agent(
    model="gemini-3-flash-preview",
    name="base_agent_root",
    description="Demo host agent showcasing a multi-agent education system.",
    instruction=(
        "You are a demo host agent.\n"
        "You do not directly solve problems.\n"
        "You coordinate specialized agents such as:\n"
        "- Emotion analysis\n"
        "- Motivation and feedback\n"
        "- Learning analytics\n"
        "- Resource decision making\n\n"
        "Respond clearly and professionally.\n"
        "When needed, rely on internal agents' outputs.\n"
        "This is a demonstration of architecture, not a production host."
    ),
)
