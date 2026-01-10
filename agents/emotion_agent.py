from transformers import pipeline
from google.adk.agents.llm_agent import Agent

# Load once (important for performance)
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def detect_emotion(text: str) -> dict:
    """
    Pure Python emotion detection using Hugging Face.
    """
    scores = emotion_classifier(text)[0]
    top_emotion = max(scores, key=lambda x: x["score"])

    return {
        "emotion": top_emotion["label"],
        "confidence": round(top_emotion["score"], 3)
    }

def map_to_learning_state(emotion: str) -> str:
    mapping = {
        "anger": "frustrated",
        "fear": "confused",
        "sadness": "frustrated",
        "disgust": "frustrated",
        "surprise": "confused",
        "joy": "motivated",
        "neutral": "calm"
    }
    return mapping.get(emotion.lower(), "calm")

emotion_agent = Agent(
    model="gemini-3-flash-preview",
    name="emotion_agent",
    description="Analyzes user emotion and learning sentiment.",
    instruction=(
        "You receive detected emotion data.\n"
        "Interpret it in a learning context.\n\n"
        "Return ONLY JSON with keys:\n"
        "- emotion\n"
        "- confidence\n"
        "- learning_state (calm/confused/frustrated/motivated)\n"
        "- recommendation\n\n"
        "Do NOT teach content."
    ),
)
if __name__ == "__main__":
    text = "I am really stuck and this is very frustrating"
    result = detect_emotion(text)
    learning_state = map_to_learning_state(result["emotion"])

    print("Detected Emotion:", result)
    print("Mapped Learning State:", learning_state)
