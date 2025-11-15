def edu_response(query):
    query = query.lower()
    if "coding" in query or "programming" in query:
        return "Try freeCodeCamp, Khan Academy, or Coursera’s free tracks."
    elif "math" in query:
        return "Check out Brilliant.org or Khan Academy’s math section."
    else:
        return "I'm an education agent. Let me know what subject you're interested in!"
