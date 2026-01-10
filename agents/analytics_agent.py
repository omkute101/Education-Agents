from google.adk.agents.llm_agent import Agent

analytics_agent = Agent(
    model="gemini-3-flash-preview",
    name="analytics_agent",
    description="Explains learning progress and analytics insights.",
    instruction=(
        "You are an analytics insight agent.\n\n"
        "You receive structured progress data such as:\n"
        "- attempts\n"
        "- average scores\n"
        "- topic-wise performance\n\n"

        "Your task:\n"
        "- Summarize progress clearly\n"
        "- Highlight strengths\n"
        "- Identify weak areas\n"
        "- Give a short improvement suggestion\n\n"

        "Constraints:\n"
        "- Be concise and clear\n"
        "- Do NOT generate full study plans\n\n"

        "Return ONLY JSON with keys:\n"
        "- summary\n"
        "- strengths\n"
        "- weaknesses\n"
        "- suggestion"
    ),
)
