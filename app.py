import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

load_dotenv()

from openai import OpenAI
client = OpenAI(api_key = os.environ['OPENAI_KEY'])


genai.configure(api_key = os.environ['GOOGLE_GEMINI_KEY'])

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

st.set_page_config(layout='wide')

# Title
st.title('Gemini\'s Article Generator')
st.subheader('Crafting a blog article with Gemini')

# Sidebar
with st.sidebar:
    st.title('Blog Details')
    st.subheader('What are we writing about today?')

    # Blog Title
    blog_title = st.text_input('Title', 'Benefits of Machine Learning in Business')

    keywords = st.text_area('Keywords', 'Gemini, Streamlit, Python')

    num_words = st.slider('Word Count', min_value = 250, max_value = 1000, step = 250)

    num_images = st.number_input('Number of Images', min_value = 1, max_value = 5, step = 1)

    convo = model.start_chat(history = [
      {
        "role": "user",
        "parts": [f"Generate a comprehensive, engaging blog post relevant to the given {blog_title} and {keywords}, make sure to incorporate the keywords in the post. The blog post should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."]
      },
      {
        "role": "model",
        "parts": ["Sure, I can help with that. I'll generate a blog post for you."]
      },
    ])

    # print(convo.last.text)

    submit_button = st.button('Generate Article')

if submit_button:
    response = convo.send_message('YOUR_USER_INPUT')

    # image_response = client.images.generate(
    #   model="dall-e-3",
    #   prompt=f"Generate a blog post image for the article titled '{blog_title}'",
    #   size="1024x1024",
    #   quality="standard",
    #   n=1,
    # )
    # image_url = image_response.data[0].url

    # st.image(image_url, caption='Generated Image', use_column_width=True)

    st.title('Generated Article')
    st.write(response.candidates[0].content.parts[0].text)