from google.adk.agents.llm_agent import Agent

resource_agent = Agent(
    model="gemini-3-flash-preview",
    name="resource_agent",
    description="Decides what learning resource should be provided.",
    instruction=(
        "You are a resource decision agent.\n\n"

        "Based on the user query and context, decide:\n"
        "- Is a learning resource needed?\n"
        "- What type (notes, pdf, explanation)?\n"
        "- Should RAG (user documents) be used?\n\n"

        "Constraints:\n"
        "- Do NOT generate content\n"
        "- Do NOT fetch documents\n\n"

        "Return ONLY JSON with keys:\n"
        "- need_resource (true/false)\n"
        "- resource_type (notes/pdf/explanation)\n"
        "- topic\n"
        "- level (beginner/intermediate/advanced)\n"
        "- source (rag/general)"
    ),
)
