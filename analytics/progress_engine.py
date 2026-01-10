def compute_progress(history: list) -> dict:
    """
    history example:
    [
        {"topic": "linked list", "score": 40},
        {"topic": "linked list", "score": 60},
        {"topic": "array", "score": 80}
    ]
    """

    stats = {}

    for entry in history:
        topic = entry.get("topic")
        score = entry.get("score", 0)

        if topic not in stats:
            stats[topic] = {
                "attempts": 0,
                "scores": []
            }

        stats[topic]["attempts"] += 1
        stats[topic]["scores"].append(score)

    for topic, data in stats.items():
        data["average_score"] = sum(data["scores"]) / len(data["scores"])

    return stats
