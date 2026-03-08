from agents.embedding_agent import search_policy

def retrieve_policies(user_query):

    results = search_policy(user_query)

    return results