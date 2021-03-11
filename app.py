import streamlit as st
import time
import requests

# website configuration
st.set_page_config(
    page_title='AI-rtsie',
    page_icon='🎨🤖',
    layout ='wide',
    initial_sidebar_state='expanded')

# AI-rtsie API URL
url = 'https://airtsie-ilga65pf7a-ew.a.run.app/image'

st.markdown('''# AI-rtsie''')

st.markdown(
    '''the ✨artsy✨ storyteller'''
)
st.markdown('')
st.markdown('')

st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('''

Hey there!\n
I am an artifical intelligence that turns your text into ✨*artsy*✨ images.

''')

st.sidebar.markdown('')
st.sidebar.markdown('')

text = st.sidebar.text_area('Tell me something interesting:')

if st.sidebar.button('Submit'):
    with st.spinner("🤖 Let's see what I come up with..."):
        # make a request to OUR api
        params = {'text': text}
        result = requests.get(url, params=params).json()

    # debugging check
    # print(result)

    # check it response is empty
    if result['OK'] == 0:
        st.markdown("I couldn’t get much out of your text ☹️ Tell me something else.")

    # check if algorithm did not understand a word
    if result['OK'] == -1:
        word_error = f"I don't know the word {result['wrong_word']} 😬 Try again. "
        st.markdown(word_error)

    # display images
    elif result['OK'] > 0:
        with st.spinner('I am loading your images...'):
            n_images = result['OK']

            if n_images <= 3:
                cols13 = st.beta_columns(n_images)

                for i in range(n_images):
                    with cols13[i]:

                        st.image(result['im_urls'][i])
                        with st.beta_expander("See original pictures"):
                            if result['content'][2][i] == '':
                                cont_attr = f"{result['content'][1][i]} / [Pixabay](https://pixabay.com/)"
                            else:
                                cont_attr = f"[{result['content'][1][i]}]({result['content'][2][i]}) / [Unsplash](https://unsplash.com/)"

                            st.image(result['content'][0][i], caption='content image')
                            st.markdown(cont_attr)

                            style_attr = f"[{result['style'][1][i]}]({result['style'][2][i]}) / [Unsplash](https://unsplash.com/)"
                            st.image(result['style'][0][i], caption='style image')
                            st.markdown(style_attr)
                    time.sleep(2)

            else:
                cols13 = st.beta_columns(3)
                # empty space to separate the rows a bit more
                st.markdown('')
                cols46 = st.beta_columns(3)

                for i in range(3):
                    with cols13[i]:

                        st.image(result['im_urls'][i])
                        with st.beta_expander("See original pictures"):
                            if result['content'][2][i] == '':
                                cont_attr = f"{result['content'][1][i]} / [Pixabay](https://pixabay.com/)"
                            else:
                                cont_attr = f"[{result['content'][1][i]}]({result['content'][2][i]}) / [Unsplash](https://unsplash.com/)"

                            st.image(result['content'][0][i], caption='content image')
                            st.markdown(cont_attr)

                            style_attr = f"[{result['style'][1][i]}]({result['style'][2][i]}) / [Unsplash](https://unsplash.com/)"
                            st.image(result['style'][0][i], caption='style image')
                            st.markdown(style_attr)
                    time.sleep(2)

                # empty space to separate the rows a bit more
                st.markdown('')

                for i in range(3, n_images):
                    with cols46[i-3]:

                        st.image(result['im_urls'][i])
                        with st.beta_expander("See original pictures"):
                            if result['content'][2][i] == '':
                                cont_attr = f"{result['content'][1][i]} / [Pixabay](https://pixabay.com/)"
                            else:
                                cont_attr = f"[{result['content'][1][i]}]({result['content'][2][i]}) / [Unsplash](https://unsplash.com/)"

                            st.image(result['content'][0][i], caption='content image')
                            st.markdown(cont_attr)

                            style_attr = f"[{result['style'][1][i]}]({result['style'][2][i]}) / [Unsplash](https://unsplash.com/)"
                            st.image(result['style'][0][i], caption='style image')
                            st.markdown(style_attr)
                    time.sleep(2)

st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown(
    "<h1 style='text-align: center; color: grey; font-size: 10px; font-family: arial;'>Powered by Neural Style Transfer library of TensorFlow with magenta/arbitrary-image-stylization-v1-256</h1>", unsafe_allow_html=True
    )
