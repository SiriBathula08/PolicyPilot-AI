from agents.retrieval_agent import retrieve_policies

def chat_with_policy(user_question):

    policies = retrieve_policies(user_question)

    if not policies:
        return "Sorry, I couldn't find relevant policies."

    answer = "Relevant Government Schemes:\n\n"

    for p in policies:
        answer += f"Scheme: {p['scheme']}\n"
        answer += f"Description: {p['description']}\n"
        answer += f"Target Group: {p['target']}\n\n"

    return answer