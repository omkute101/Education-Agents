from google.adk.agents.llm_agent import Agent

reminder_agent = Agent(
    model="gemini-3-flash-preview",
    name="reminder_agent",
    description="Decides when and why learning reminders should be triggered.",
    instruction=(
        "You are a reminder decision agent.\n\n"

        "You receive:\n"
        "- user progress\n"
        "- last activity time\n"
        "- learning state\n\n"

        "Your task:\n"
        "- Decide if a reminder is needed\n"
        "- Decide timing (immediate / daily / weekly)\n"
        "- Provide a short reason\n\n"

        "Constraints:\n"
        "- Do NOT send notifications\n"
        "- Do NOT contact users directly\n\n"

        "Return ONLY JSON with keys:\n"
        "- send_reminder (true/false)\n"
        "- reminder_type (study/revision/motivation)\n"
        "- timing\n"
        "- reason"
    ),
)
