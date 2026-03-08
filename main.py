from agents.profile_agent import analyze_profile
from agents.retrieval_agent import retrieve_policies
from agents.eligibility_agent import check_eligibility
from agents.recommendation_agent import recommend_schemes

# User input
age = int(input("Enter age: "))
income = int(input("Enter income: "))
occupation = input("Enter occupation: ")
location = input("Enter location: ")

# Step 1: Analyze profile
profile = analyze_profile(age, income, occupation, location)

# Step 2: Retrieve policies using RAG
query = f"government schemes for {occupation}"
policies = retrieve_policies(query)

# Step 3: Check eligibility
eligibility = check_eligibility(income, occupation)

# Step 4: Generate recommendation
result = recommend_schemes(profile, policies, eligibility)

print("\nAI Recommendation:")
print(result)