import streamlit as st
import proj
import about
import sys
from streamlit_option_menu import option_menu
from PIL import Image
st.set_page_config(page_title='diabetesPrediction',page_icon=':mask:',layout='wide')
def bgimg():       
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://cdn.pixabay.com/photo/2016/10/08/20/52/diabetes-1724617_1280.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True)
def home():
    img=Image.open("images/diabetes.jpg")
    with st.container():
        st.title('WELCOME TO DIABETES PREDICTION SYSTEM')
        lcolumn,rcolumn=st.columns((4,4))
        with lcolumn:
            st.subheader("> Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces.")
            st.subheader("> Leveraging machine learning algorithms in medical services has shown promise in accurate disease diagnosis and treatment, thereby alleviating the burden on healthcare professionals.")
        with rcolumn:
            st.image(img)
def diabetes_checking():
    proj.diab()  
def About():
    about.diabeticpredict()
def main():
    if len(sys.argv) > 1:
            username = sys.argv[1]  # Get the username from command line arguments
            st.title("Welcome {}".format(username))
            # Continue with the rest of your main_page.py content
    else:
        st.title("Welcome to the Main Page")
   # with st.sidebar: 
    bgimg()
    selected = option_menu('Diabetes Prediction System using ML',
                            ['Home','Diabetes checking', 'About'],
                            icons = ['house','activity','exclamation',':bar_chart:'],
                            menu_icon="cast",
                            default_index = 0,
                            orientation="horizontal",
                            styles={
                            "container":{"padding":"0!important","background-color":"#ffffff80"},
                            "icon":{"color":"black","font-size":"20px"},
                            "nav-link":{"font-size":"15px","text_align":"left",
                                        "margin":"0px","--hover-color":"#eee",
                            },"nav-link-selected":{"background-color":"#50ABE7"},})
    if selected == 'Home':
        home()
    elif selected == "Diabetes checking":
        diabetes_checking()
    elif selected == "About":
        About()
if __name__ == '__main__':
    main()
