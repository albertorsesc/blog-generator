import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key

genai.configure(api_key=google_gemini_api_key)

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

    response = convo.send_message('YOUR_USER_INPUT')
    # print(convo.last.text)

    submit_button = st.button('Generate Article')

if submit_button:
    # st.image('https://images.unsplash.com/photo-1674027444485-cec3da58eef4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzMDAzMzh8MHwxfHNlYXJjaHwxOHx8YWl8ZW58MHx8fHwxNzEyMDA3NDM1fDA&ixlib=rb-4.0.3&q=80&w=1080')

    st.write(response.candidates[0].content.parts[0].text)