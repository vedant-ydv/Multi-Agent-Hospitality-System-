import streamlit as st
from crew_setup import crew
from app_logger import log_event

st.set_page_config(page_title="AI Hospitality Planner")

st.title("AI Hospitality Travel Planner")

st.write("Generate travel itineraries using a multi-agent AI system.")

destination = st.text_input("Destination")

days = st.number_input(
    "Number of Days",
    min_value=1,
    max_value=10,
    value=3
)

budget = st.selectbox(
    "Budget Preference",
    ["low", "medium", "luxury"]
)

if st.button("Generate Travel Plan"):

    if destination.strip() == "":
        st.warning("Please enter a destination")

    else:

        log_event(f"User requested travel plan for {destination}")

        with st.spinner("AI agents are planning your trip..."):

            try:

                result = crew.kickoff(
                    inputs={
                        "destination": destination,
                        "days": days,
                        "budget": budget
                    }
                )

                itinerary_text = str(result.raw)

                st.success("Travel plan generated successfully")

                st.subheader("Your Itinerary")

                st.markdown(itinerary_text)

                st.download_button(
                    label="Download Plan",
                    data=itinerary_text,
                    file_name="travel_plan.txt",
                    mime="text/plain"
                )

                log_event("Itinerary generated")

            except Exception as e:

                st.error(str(e))
                log_event(str(e))