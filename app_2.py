import streamlit as st
import time
import requests

st.set_page_config(
    page_title='AI-rtsie',
    page_icon='🎨🤖',
    layout ='centered',
    initial_sidebar_state='expanded')

url = 'https://airtsie-ilga65pf7a-ew.a.run.app/image'

st.markdown('''# AI-rtsie''')

st.markdown(
    '''the ✨artsy✨ storyteller'''
)

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
    with st.spinner('🤖   I am generating your images...'):
        time.sleep(3)
        st.image('data:image/jpeg;base64,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')

        st.image('data:image/jpeg;base64,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')
    #     # make a request to OUR api
    #     params = {'text': st.sidebar.text}
    #     result = requests.get(url, params=params).json()

    # # debugging check
    # print(result)

    # # check it response is empty
    # if result['OK'] == 0:
    #     st.markdown("I couldn’t get much out of your text ☹️ Tell me something else.")

    # # check if algorithm did not understand a word
    # if result['OK'] == -1:
    #     word_error = f"I don't know the word {result['wrong_word']} 😬 Try again. "
    #     st.markdown(word_error)

    # # display images
    # elif result['OK'] > 0:
    #     with st.spinner('I am loading your images...'):
    #         n_images = result['OK']

    #         if n_images <= 3:
    #             cols13 = st.beta_columns(n_images)

    #             for i in range(n_images):
    #                 with cols13[i]:

    #                     st.image(result['im_urls'][i])
    #                     with st.beta_expander("See original picture"):
    #                         if result['content'][2][i] == '':
    #                             cont_attr = f"{result['content'][1][i]} / [Pixabay](https://pixabay.com/)"
    #                         else:
    #                             cont_attr = f"[{result['content'][1][i]}]({result['content'][2][i]}) / [Unsplash](https://unsplash.com/)"

    #                         st.image(result['content'][0][i], caption='content image')
    #                         st.markdown(cont_attr)

    #                         style_attr = f"[{result['style'][1][i]}]({result['style'][2][i]}) / [Unsplash](https://unsplash.com/)"
    #                         st.image(result['style'][0][i], caption='style image')
    #                         st.markdown(style_attr)
    #                 time.sleep(2)

    #         else:
    #             cols13 = st.beta_columns(3)
    #             cols46 = st.beta_columns(3)

    #             for i in range(3):
    #                 with cols13[i]:

    #                     st.image(result['im_urls'][i])
    #                     with st.beta_expander("See original picture"):
    #                         if result['content'][2][i] == '':
    #                             cont_attr = f"{result['content'][1][i]} / [Pixabay](https://pixabay.com/)"
    #                         else:
    #                             cont_attr = f"[{result['content'][1][i]}]({result['content'][2][i]}) / [Unsplash](https://unsplash.com/)"

    #                         st.image(result['content'][0][i], caption='content image')
    #                         st.markdown(cont_attr)

    #                         style_attr = f"[{result['style'][1][i]}]({result['style'][2][i]}) / [Unsplash](https://unsplash.com/)"
    #                         st.image(result['style'][0][i], caption='style image')
    #                         st.markdown(style_attr)

    #             # not correct yet
    #             for i in range(3, n_images):
    #                 with cols46[i-3]:

    #                     st.image(result['im_urls'][i])
    #                     with st.beta_expander("See original picture"):
    #                         if result['content'][2][i] == '':
    #                             cont_attr = f"{result['content'][1][i]} / [Pixabay](https://pixabay.com/)"
    #                         else:
    #                             cont_attr = f"[{result['content'][1][i]}]({result['content'][2][i]}) / [Unsplash](https://unsplash.com/)"

    #                         st.image(result['content'][0][i], caption='content image')
    #                         st.markdown(cont_attr)

    #                         style_attr = f"[{result['style'][1][i]}]({result['style'][2][i]}) / [Unsplash](https://unsplash.com/)"
    #                         st.image(result['style'][0][i], caption='style image')
    #                         st.markdown(style_attr)

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
