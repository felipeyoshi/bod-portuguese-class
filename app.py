import streamlit as st
from llm_utils import LLM
from prompts import chapter_prompts

def generate_chapter(title, prompt, artist, conversation, llm):
    st.header(title)
    try:
        response, conversation = llm.generate_text_with_context(conversation, prompt)
        image_url, prompt_image = llm.generate_image(response, artist)
        st.markdown(response)
        st.image(image_url)
    except Exception as e:
         st.error("An error occurred. Please try again.")
    return conversation

# Streamlit UI
st.title("GenAI Portuguese Tutor")
st.write("What if we could merge Portuguese lessons, travel tips, and GenAI into an unforgettable storytelling experience? Explore the vibrant culture of Brazil while learning Portuguese through captivating stories and visuals.")
st.write("**Disclaimer:** This application uses AI to generate text and images. Please be aware that the content generated may not always be accurate or appropriate.")

st.sidebar.title("Create your own Narative!")
chapters = st.sidebar.multiselect("Select your Plot", ["Introduction", "The Arrival", "The best places in Rio", "Lunch Break"], default=["Introduction"])
artist = st.sidebar.selectbox("Inspired by", ["Realistic", "Tarsila do Amaral", "Candido Portinari", "Romero Britto", "Eduardo Kobra"])

# Use Streamlit secrets for the OpenAI API key
api_key = st.secrets["open_ai"]["api_key"]
if not api_key:
    st.warning("Please configure your OpenAI API key in Streamlit secrets.")
    st.stop()

# Button to trigger generation
if st.button("Generate Story"):
    llm = LLM(api_key)
    conversation = []

    for chapter in chapters:
        conversation = generate_chapter(f"Chapter {chapters.index(chapter) + 1}: {chapter}", chapter_prompts[chapter], artist, conversation, llm)