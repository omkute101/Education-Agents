import streamlit as st
from agent import root_agent
from agent import get_memory, set_memory

USER_ID = "default_user"

st.title("🎓 AI Mentor Agent")

# Load memory
memory = get_memory(USER_ID)
if "experience_level" not in memory:
    memory["experience_level"] = None
if "learning_goal" not in memory:
    memory["learning_goal"] = None

# Step 1: Ask user goal (free text)
if not memory["learning_goal"]:
    st.subheader("Welcome! What would you like help with today?")
    goal_input = st.text_input("Type your learning goal here:")
    if st.button("Confirm Goal") and goal_input.strip():
        memory["learning_goal"] = goal_input.strip()
        set_memory(USER_ID, memory)
        st.experimental_rerun()
elif memory["learning_goal"]:
    st.success(f"Learning Goal: {memory['learning_goal']}")

# Step 2: Ask experience level
if memory["learning_goal"] and not memory["experience_level"]:
    st.subheader("Select your experience level")
    level_choice = st.radio(
        "Your experience level:",
        ["Beginner", "Intermediate", "Advanced"]
    )
    if st.button("Confirm Level"):
        memory["experience_level"] = level_choice
        set_memory(USER_ID, memory)
        st.experimental_rerun()
elif memory["experience_level"]:
    st.success(f"Experience Level: {memory['experience_level']}")

# Step 3: Agent response with guided options
if memory["learning_goal"] and memory["experience_level"]:
    st.subheader("AI Mentor Response")
    user_input = f"My goal is {memory['learning_goal']} and my experience is {memory['experience_level']}."
    response = root_agent.respond(user_input)

    # Display agent text
    st.text(response.get("text", ""))

    # If agent returns buttons/options, display them
    buttons = response.get("buttons", [])
    if buttons:
        st.write("Choose one of the options:")
        for b in buttons:
            if st.button(b):
                st.success(f"You selected: {b}")
                # Optionally, update memory or pass input to agent for next step
