# streamlit run login2.py --server.enableXsrfProtection false

import streamlit as st 
from streamlit_option_menu import option_menu
import db
import pandas as pd
import app
import base64
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Health and Nutrition Analyzer", page_icon="🍎", layout="wide")

link="https://lottie.host/9e81263e-222a-48d1-bba2-56d3b031a09f/mamwyWiENf.json"
link2="https://lottie.host/34f56ea9-d2a7-4345-93c9-79e373b9e296/GPRJ3LUIx4.json"
def loginpage():
        with open('img1.jpeg','rb') as f:
            data= f.read()
            imgs= base64.b64encode(data).decode()
            css=f""" 
                <style>
                [data-testid="stAppViewContainer"]{{
                    background-image:url('data:image/png;base64,{imgs}');
                    background-size:cover
                }}     
                
                [data-testid='stButton']{{
                    color:green;
                }}
                
                
                </style> 
                
                """
            st.markdown(css, unsafe_allow_html=True)
#         video_file = "3129576-uhd_3840_2160_30fps.mp4"  # Replace with your local MP4 file

# # Encode the video file in base64
#         video_base64 = base64.b64encode(open(video_file, "rb").read()).decode()

#         # Create the HTML code for the video background
#         video_html = """
#         <style>
#             body {{
#                 margin: 0;
#                 background-color: #f0f0f0;
#             }}
#             video {{
#                 position: fixed;
#                 right: 0;
#                 bottom: 0;
#                 min-width: 100%;
#                 min-height: 100%;
#             }}
#             .content {{
#                 position: fixed;
#                 bottom: 0;
#                 background: rgba(0, 0, 0, 0.5);
#                 color: #f1f1f1;
#                 width: 100%;
#                 padding: 20px;
#             }}
#         </style>
#         <video autoplay muted loop>
#             <source src="data:video/mp4;base64,{video_base64}">
#             Your browser does not support HTML5 video.
#         </video>

#         """.format(video_base64=video_base64)

        # Add the video background to the Streamlit app
        # st.markdown(video_html, unsafe_allow_html=True)
        with st.sidebar:
            # option = option_menu("Menu", options=['Login', 'Create User', 'View All', 'Update User'])
            option = option_menu(
                        "Menu",
                        options=['Login', 'Create User'],
                        icons=['box-arrow-in-right', 'person-plus'],  # Corresponding FontAwesome icons
                        menu_icon="cast",  # Optional menu icon
                        default_index=0  # Default selected option
                    )
        if option=='Create User':
            st.markdown("<h1 style='font-style: italic';'text-align: center; font-size: 36px; color: green'; font-weight: bold'>CREATE ACCOUNT </h1",unsafe_allow_html=True)
            col1,col2=st.columns(2)
            with col1:
                with st.form('my-form'):
                    # st.markdown("<h1 style='font-style: italic';'text-align: center; font-size: 36px; color: green'; font-weight: bold'>CREATE ACCOUNT </h1",unsafe_allow_html=True)
                    username= st.text_input('Username')
                    password= st.text_input('Password', type='password')
                    
                    btn=st.form_submit_button("Submit")
                    
                    if btn:
                        data=(username,password)
                        res= db.addUser(data)
                        if res:
                            st_lottie(link, key="user",height=300)
                        # st.success("User Registered Successfully")
            with col2:
                pass
        if option == 'Login':
            st.markdown("<h1 style='font-style: italic';'text-align: center'; font-size: 36px; color: green'; font-weight: bold'>LOGIN PAGE </h1",unsafe_allow_html=True)
            col1,col2=st.columns(2)
            with col1:
                with st.form('login-form'):
                    
                    st.markdown("<h3 style='font-style: italic';'text-align: center; font-size: 20px; color: green'; >Enter details </h3",unsafe_allow_html=True)
                    username = st.text_input('Username')
                    password = st.text_input('Password', type='password')
                    btn = st.form_submit_button("Login")
                    if btn:
                        if db.login(username, password):
                            st.success("Login Successful")
                            st.write("Welcome, " + username)
                            st.session_state.current_page="page2"
                            # st.rerun()
                        else:
                            st.error("Invalid username or password")
            with col2:
                pass
                # st_lottie(link2, key="user",height=300)   
            

        # if option=='View All':
        #     st.markdown("<h1 style='font-style: italic';'text-align: center; font-size: 36px; color: green'; font-weight: bold'>VIEW ALL ACCOUNT </h1",unsafe_allow_html=True)
        #     data= db.getAllUser()
        #     # st.write(data)
        #     # st.table(data)
        #     df= pd.DataFrame(data,columns=['ID','Username','Password'])
            
        #     st.dataframe(df, use_container_width=True)
        # if option == 'Update User':
        #     st.markdown("<h1 style='font-style: italic';'text-align: center; font-size: 36px; color: green'; font-weight: bold'UPDATE ACCOUNT </h1",unsafe_allow_html=True)
        #     # Fetch all user data from the database
        #     data = db.getAllUser()
            
        #     # Create a list of user IDs and names
        #     li = [f"{i[0]}-{i[1]}" for i in data]
            
        #     # Create a DataFrame with the fetched data
        #     df1 = pd.DataFrame(data, columns=['ID', 'Username', 'Password'])
            
        #     # Create a selectbox for selecting a user based on ID and name
        #     select_user = st.selectbox('Select User', options=li)
            
        #     # Ensure a valid user is selected
        #     if select_user:
        #         try:
        #             # Extract the selected user ID
        #             select_id = int(select_user.split('-')[0])
                    
        #             # Filter the DataFrame to get details of the selected user
        #             df_new = df1[df1['ID'] == select_id].reset_index(drop=True)
                    
        #             # Display the selected user's details
        #             st.write(df_new)
                    
        #             # Create a form for updating user details
        #             with st.form('my-form'):
        #                 # Pre-fill the form with the selected user's current details
        #                 name = st.text_input('Username', value=df_new.loc[0, 'Username'])
        #                 password = st.text_input('Password', value=df_new.loc[0, 'Password'], type='password')
                        
        #                 # Submit button for the form
        #                 btn = st.form_submit_button("Submit")
                        
        #                 # If the form is submitted
        #                 if btn:
        #                     # Prepare the data for updating
        #                     data = (name, password, select_id)
                            
        #                     # Update the user in the database
        #                     res = db.updateUser(data)
                            
        #                     # Display a success message if the update was successful
        #                     if res:
        #                         st.success("User Updated Successfully")
        #         except Exception as e:
        #             st.error(f"An error occurred: {e}")
        #     else:
        #         st.warning("Please select a user.")

def page2():
    app.app()

    
            
def main():
    if 'current_page' not in st.session_state:
        st.session_state.current_page="page1"
    if st.session_state.current_page=="page1":
        loginpage()
    elif st.session_state.current_page=="page2":
        page2()
        
if __name__=="__main__":
    main()
        




        