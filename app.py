import streamlit as st
import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = "AIzaSyCo58UahbPRuw6iO578VUNeYNMj_Ybe-qs"

def generate_campaign(club_name, club_brief, event_name, event_description, chief_guest, chief_guest_designation, event_date, event_venue, target_audience, tone, additional_notes):
    prompt = f"""
    **Club:** {club_name}
    **Brief:** {club_brief}
    **Event:** {event_name}
    **Description:** {event_description}
    **Chief Guest:** {chief_guest}, {chief_guest_designation}
    **Date:** {event_date}
    **Venue:** {event_venue}
    **Target Audience:** {target_audience}
    **Tone:** {tone}
    **Additional Notes:** {additional_notes}

    Create a compelling invitation campaign statement for this event.
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text  


def main():
    st.title("Campus Event Campaigner")

    with st.form("event_form"):
        club_name = st.text_input("Club Name")
        club_brief = st.text_input("Club Brief")
        event_name = st.text_input("Event Name")
        event_description = st.text_input("Event Description")
        chief_guest = st.text_input("Chief Guest")
        chief_guest_designation = st.text_input("Chief Guest Designation")
        event_date = st.date_input("Event Date")
        event_venue = st.text_input("Event Venue")
        target_audience = st.text_input("Target Audience")
        tone = st.selectbox("Tone", ["Informative", "Exciting", "Persuasive"])
        additional_notes = st.text_area("Additional Notes")

        submitted = st.form_submit_button("Generate Campaign")

    if submitted:
        campaign = generate_campaign(club_name, club_brief, event_name, event_description, chief_guest, chief_guest_designation, event_date, event_venue, target_audience, tone, additional_notes)
        st.success("Campaign Statement Generated:")
        st.markdown(campaign)

if __name__ == "__main__":
    main()
