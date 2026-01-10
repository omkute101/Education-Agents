from agents.emotion_agent import detect_emotion, map_to_learning_state

def main():
    print("Base Agent – Local Demo Mode")
    print("Type 'exit' to quit\n")

    while True:
        msg = input("User: ")
        if msg.lower() == "exit":
            break

        emotion_data = detect_emotion(msg)
        learning_state = map_to_learning_state(emotion_data["emotion"])

        print("\n[Emotion Detection]")
        print(emotion_data)
        print("Learning State:", learning_state)
        print("-" * 40)

if __name__ == "__main__":
    main()
