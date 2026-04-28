
def analyze(state):
    players = state.get("players",[])
    hot = len(players) > 1
    return {
        "risk":"HIGH" if hot else "LOW",
        "suggestion":"avoid cluster" if hot else "safe",
        "hotspots":[f"{p['x']//10},{p['y']//10}" for p in players]
    }
