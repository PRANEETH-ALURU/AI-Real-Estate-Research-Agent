import streamlit as st
from datetime import datetime
from real_estate_ai_agent.crew import RealEstate

st.title("AI Real Estate Research Agent")

location = st.text_input("Location", "Charlotte, NC")
budget = st.text_input("Budget", "$450,000")
buyer_goal = st.text_input("Buyer Goal", "investment property")

if st.button("Run Analysis"):
    with st.spinner("Researching real estate market..."):
        inputs = {
            "location": location,
            "budget": budget,
            "buyer_goal": buyer_goal,
            "current_date": str(datetime.now()),
        }

        result = RealEstate().crew().kickoff(inputs=inputs)

        st.subheader("Final Recommendation")
        st.markdown(result.raw)

        st.download_button(
            "Download Report",
            result.raw,
            file_name="real_estate_recommendation.md",
            mime="text/markdown",
        )