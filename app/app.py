import streamlit as st
import sys
import os

# Allow imports from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.eligibility_agent import check_eligibility
from agents.recommendation_agent import recommend_schemes
from agents.chat_agent import chat_with_policy

st.title("PolicyPilot AI")
st.write("AI Assistant for Government Policy Recommendations")

# User Inputs
st.subheader("User Information")

income = st.number_input("Annual Income (₹)", min_value=0)
occupation = st.text_input("Occupation")

if st.button("Check Eligibility"):

    score, level = check_eligibility(income, occupation)

    st.subheader("Eligibility Result")
    st.write(f"Eligibility Score: {score}/100")
    st.write(f"Eligibility Level: {level}")

    schemes = recommend_schemes(income, occupation)

    if schemes:
        st.subheader("Recommended Schemes")

        for s in schemes:
            st.write(f"**{s['scheme']}**")
            st.write(f"Eligibility Score: {s['score']}%")
            st.write(f"Reason: {s['reason']}")
            st.write("---")
    else:
        st.write("No schemes found for this profile.")


# Chatbot Section
st.subheader("Ask Policy Assistant")

question = st.text_input("Ask about government policies")

if st.button("Ask"):
    response = chat_with_policy(question)
    st.write(response)