import json
from datetime import datetime

import streamlit as st

from real_estate_ai_agent.crew import RealEstate


st.set_page_config(
    page_title="AI Real Estate Research Agent",
    page_icon="🏡",
    layout="wide",
)

if "report_raw" not in st.session_state:
    st.session_state.report_raw = None

if "report_data" not in st.session_state:
    st.session_state.report_data = None


st.title("🏡 AI Real Estate Research Agent")
st.write(
    "Analyze neighborhoods, housing market trends, and investment potential "
    "using multiple AI agents."
)

location = st.text_input("📍 Location", "Charlotte, NC")
budget = st.text_input("💰 Budget", "$450,000")
buyer_goal = st.text_input("🎯 Buyer Goal", "Investment Property")

if st.button("🚀 Run Analysis", use_container_width=True):
    with st.spinner("Researching the real estate market... This may take a minute."):
        inputs = {
            "location": location,
            "budget": budget,
            "buyer_goal": buyer_goal,
            "current_date": str(datetime.now()),
        }

        result = RealEstate().crew().kickoff(inputs=inputs)

        st.session_state.report_raw = result.raw

        try:
            st.session_state.report_data = json.loads(result.raw)
        except Exception:
            st.session_state.report_data = None


if st.session_state.report_raw:
    st.success("Analysis Complete!")

    if st.session_state.report_data:
        data = st.session_state.report_data

        st.header("🏆 Recommended Neighborhood")
        st.success(data["recommended_neighborhood"])
        st.write(data["recommendation_summary"])

        st.divider()

        st.header("📊 Ranked Neighborhoods")

        for i, item in enumerate(data["ranked_neighborhoods"], start=1):
            with st.expander(
                f"#{i} {item['neighborhood_name']} • {item['investment_score']}/10",
                expanded=(i == 1),
            ):
                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Median Home Price", item["median_home_price"])
                    st.metric("Budget Fit", item["budget_fit"])

                with col2:
                    st.metric("Risk Level", item["risk_level"])
                    st.metric("Confidence", item["confidence_score"])

                st.markdown("### ✅ Pros")
                for pro in item["pros"]:
                    st.write(f"• {pro}")

                st.markdown("### ❌ Cons")
                for con in item["cons"]:
                    st.write(f"• {con}")

                st.markdown("### 📝 Why this ranking?")
                st.info(item["reason_for_ranking"])

        st.divider()

        st.header("⚠️ Key Risks")
        for risk in data["key_risks"]:
            st.warning(risk)

        st.divider()

        st.header("➡️ Recommended Next Steps")
        for step in data["next_steps"]:
            st.write(f"✅ {step}")

        download_data = json.dumps(data, indent=2)

        st.download_button(
            label="📥 Download JSON Report",
            data=download_data,
            file_name="real_estate_recommendation.json",
            mime="application/json",
            use_container_width=True,
        )

    else:
        st.subheader("Final Recommendation")
        st.markdown(st.session_state.report_raw)

        st.download_button(
            label="📥 Download Report",
            data=st.session_state.report_raw,
            file_name="real_estate_recommendation.md",
            mime="text/markdown",
            use_container_width=True,
        )