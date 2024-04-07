import streamlit as st

st.set_page_config(layout='wide')

# Title
st.title('Gemini\'s Article Generator')
st.subheader('Crafting a blog article with Gemini')

article = """
  In the realm of artificial intelligence (AI), the emergence of large language models (LLMs) such as GPT-3, BERT, and LLaMA 2 has revolutionized the way we approach data processing, analysis, and interpretation. These models, pre-trained on vast datasets, have the innate capability to predict words in a sequence, effectively acting as sophisticated document completers. However, the journey from a raw, unrefined algorithm to a polished, application-specific tool involves a crucial process known as fine-tuning.

What is Model Fine-Tuning?
Fine-tuning is a process that involves adjusting the internal parameters of a pre-trained model—its weights or biases—to better align it with specific use cases. This is analogous to refining a raw diamond to fit perfectly in a ring; it's about taking a general-purpose model like GPT-3 and optimizing it to perform specific tasks, transforming it into versions like GPT-3.5 Turbo or the instructive ChatGPT.
"""

# Sidebar
with st.sidebar:
    st.title('Blog Details')
    st.subheader('What are we writing about today?')

    # Blog Title
    blog_title = st.text_input('Title', 'My First Blog Post')

    keywords = st.text_area('Keywords', 'Gemini, Streamlit, Python')

    num_words = st.slider('Word Count', min_value = 250, max_value = 1000, step = 250)

    num_images = st.number_input('Number of Images', min_value = 1, max_value = 5, step = 1)

    submit_button = st.button('Generate Article')

if submit_button:
    st.image('https://images.unsplash.com/photo-1674027444485-cec3da58eef4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwxOHx8YWl8ZW58MHx8fHwxNzEyMDA3NDM1fDA&ixlib=rb-4.0.3&q=80&w=1080')

    st.write(article)