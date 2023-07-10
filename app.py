from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie



st.set_page_config(
    page_title="My WebPage", 
    page_icon="\U0001F600", 
    layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

#---load assests---
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_w51pcehl.json")
img_contact_form = Image.open("images/pngwing.com.png")
img_second = Image.open("images/Ducati_side_shadow.png")

#---header section ----
with st.container():
    st.subheader("Hi, I am Soumya :tada:")
    st.title("An Intern at TVSM")
    st.write("Hi! I am a fourth year computer science engineer at vit-v")
    st.markdown("[Learn More >](https://github.com/coder-skr?tab=repositories)")

#---What i do ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what I do")
        st.write("##") #to insert some space between 2 elements here 2 spaces below the header
        st.write(
            """
            My name is Soumya Kumar:
            - I am a web developer
            - I am exploring data science fields as well
            """
        )
        st.write("[my profile >](https://www.linkedin.com/in/soumya-kumar-400875219/)")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#---some of the project works---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2)) #the text-column will be twice as big as image_column
    with image_column:
        st.image(img_contact_form)
        
    with text_column:
        st.subheader("Integrate Lottie animation")
        st.write(
            """
            Lottie is a file format for vector graphics animation
            and is named after Charlotte "Lotte" Reiniger, 
            a German pioneer of silhouette animation.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/jL-pjuojMfs)")

#--using local css file---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

#---contatct---
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

    contact_form="""
    <form action="https://formsubmit.co/soumykumar24@gmail.com" method="POST">
     <input type="hidden" name="captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
 """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

