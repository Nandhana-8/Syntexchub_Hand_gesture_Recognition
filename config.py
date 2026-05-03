def get_action(gesture):
    actions = {
        "Play ▶": "Playing Music...",
        "Pause ⏸": "Paused",
        "Like 👍": "Liked!",
        "Volume Up 🔊": "Increasing Volume...",
        "Volume Down 🔉": "Decreasing Volume...",
        "Next ▶▶": "Next Track...",
        "Mute 🔇": "Muted"
    }
    return actions.get(gesture, "Show a clear gesture")