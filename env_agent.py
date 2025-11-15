def env_response(query):
    query = query.lower()
    if "plastic" in query:
        return "Use reusable bags, bottles, and avoid single-use plastics."
    elif "save water" in query:
        return "Fix leaks, use low-flow fixtures, and turn off taps when not needed."
    else:
        return "I'm an environment agent. Ask me about eco-friendly habits!"
