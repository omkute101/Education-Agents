def get_user_profile(context: dict) -> dict:
    """
    Extracts user profile from injected context.
    """
    return context.get("user_profile", {})

def memory_enabled(profile: dict) -> bool:
    """
    Checks whether user has enabled personalization memory.
    """
    return profile.get("memory_enabled", True)

def get_preferences(profile: dict) -> dict:
    """
    Returns user preferences such as learning style.
    """
    return profile.get("preferences", {})
