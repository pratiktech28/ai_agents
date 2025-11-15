def health_response(query):
    query = query.lower()
    if "fever" in query:
        return "Drink fluids, rest, and monitor temperature. Consult a doctor if it persists."
    elif "headache" in query:
        return "Try hydration and rest. If severe or frequent, seek medical advice."
    else:
        return "I'm a basic health agent. Please consult a professional for serious concerns."
