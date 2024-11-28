# streamlit run login2.py --server.enableXsrfProtection false

import streamlit as st 
import pandas as pd 
import plotly.express as px 
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
load_dotenv() 
import os
import google.generativeai as genai
import plotly.graph_objects as go
from PIL import Image
from streamlit_lottie import st_lottie

import base64

st.set_page_config(page_title="Health and Nutrition Analyzer", page_icon="🍎", layout="wide")
def app():
    link="https://lottie.host/cb8ef2f3-bd57-4112-afe4-0d8b8289b61a/064ArtjIGg.json"
    link3="https://lottie.host/d1974fc2-cfbc-44bb-8923-11df75cf13de/tBmbzf2JwH.json"
    with st.sidebar:
        option = option_menu(
                "Menu",
                options=['Home', 'Nutrient Mapping', 'BMI Calculator', 'Food Genie'],
                icons=['house', 'bar-chart', 'calculator', 'magic'],  # Corresponding FontAwesome icons
                menu_icon="cast",  # Optional menu icon
                default_index=0  # Default selected option
            )


    with open('nutrients.pkl', 'rb') as f:
        df = pickle.load(f)
        
    if option=='Home':
        css_animation = """
        <style> 
        .typewriter h1 {
            text-align: center;
            overflow: hidden;
            white-space: nowrap;
            margin: 0 auto;
            letter-spacing: .15em;
            animation: 
            typing 3.5s steps(40, end),
            blink-caret .75s step-end 15,
            color-change 3.5s infinite;
        }

        @keyframes typing {
            from { width: 20% }
            to { width: 50% }
        }

        @keyframes blink-caret {
            from, to { opacity: 1 }
            50% { opacity: 0 }
        }

        @keyframes color-change {
            0% { color: #f00; }
            20% { color: #0f0; }
            40% { color: #00f; }
            60% { color: #ff0; }
            80% { color: #0ff; }
            100% { color: #f0f; }
        }

        .blinking-effect {
            animation: blink 1s step-end infinite;
        }

        @keyframes blink {
            0%, 49% { opacity: 1; }
            50%, 100% { opacity: 0; }
        }
        </style>
        """

        # HTML for the text
        html_content = """
        <style> .headline {text-align: center;}
        </style>
        <div class="typewriter">
        <h1 class="blinking-effect">    Food Nutrition profile    </h1>
        </div>
        """
        st.markdown(css_animation + html_content, unsafe_allow_html=True)

   
        st_lottie(link, key="user",height=300)
        html_content = """
        <style>
        .subheadline {
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            color: #FFFFFF; /* white */
            background: linear-gradient(to right, #FF69B4, #33CC33, #0066FF, #FFC107); /* rainbow colors */
            background-size: 400px 100%; /* wave effect */
            animation: wave 3s infinite;
            padding: 10px;
            border-radius: 10px;
        }

        @keyframes wave {
            0% {
            background-position: 0% 50%;
            }
            100% {
            background-position: 100% 50%;
            }
        }
        </style>

        <h3 class="subheadline">
        Explore our features to know more about your food habits and nutrition intake.
        """

        st.markdown(html_content, unsafe_allow_html=True)
        col1, col2,col3 = st.columns((1,1,1),gap='large')
        with col1:
            st.markdown("<p style='color: #DAA520'><strong>Nutrition Mapping</strong> </p>", unsafe_allow_html=True)
            st.success("allows you to get insights into the nutritional content of your favorite foods and discover new ones that fit your dietary needs.")
            # st.markdown("<p style='color: #D2B48C'>allows you to get insights into the nutritional content of your favorite foods and discover new ones that fit your dietary needs.</p>", unsafe_allow_html=True)
        with col2:
            st.markdown("<p style='color: #DAA520'><strong>BMI calculator</strong></p>", unsafe_allow_html=True)
            st.success("Calculate you weight type and provides personalized recommendations for a healthy lifestyle") 
            # st.markdown("<p style='color: #D2B48C'>provides personalized recommendations for a healthy lifestyle.</p>", unsafe_allow_html=True)
        with col3:
            st.markdown("<p style='color: #DAA520'><strong>Food Genie</strong></p>", unsafe_allow_html=True)
            st.success("feature allows you to upload an image of a dish and get instant nutrition information and recipe suggestions.")
            # st.markdown("<p style='color: #D2B48C'> feature allows you to upload an image of a dish and get instant nutrition information and recipe suggestions.</p>", unsafe_allow_html=True)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    if option=='BMI Calculator':
                html_content = """
                    <style>
                    .subheadline {
                        font-size: 18px;
                        font-weight: bold;
                        text-align: center;
                        color: #33CC33; /* green */
                        text-shadow: 0px 0px 10px #33CC33; /* glow effect */
                        background: linear-gradient(to bottom, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.5)); /* dark gradient */
                        padding: 10px;
                        border-radius: 10px;
                        box-shadow: 0px 0px 10px #33CC33; /* glow effect */
                        animation: pulse 2s infinite;
                    }

                    @keyframes pulse {
                        0% {
                        transform: scale(1);
                        }
                        50% {
                        transform: scale(1.1);
                        }
                        100% {
                        transform: scale(1);
                        }
                    }
                    </style>

                    <h3 class="subheadline">
                    BMI CALCULATOR
                    </h3>
                    """

                st.markdown(html_content, unsafe_allow_html=True)
                # st.markdown("<h1 style='text-align: center; font-size: 36px; color:green'; font-weight: bold'>BMI CALCULATOR</h1", unsafe_allow_html=True)
                

# CSS for typewriter effect and blinking cursor
                css_animation = """
                <style>
                .typewriter h3 {
                    overflow: hidden;
                    border-right: .15em solid orange;
                    white-space: nowrap;
                    margin: 0 auto;
                    letter-spacing: .15em;
                    animation: 
                    typing 3.5s steps(40, end),
                    blink-caret .75s step-end infinite;
                }

                @keyframes typing {
                    from { width: 0 }
                    to { width: 100% }
                }

                @keyframes blink-caret {
                    from, to { border-color: transparent }
                    50% { border-color: black }
                }
                </style>
                """

                # HTML for the text
                html_content = """
                <div class="typewriter">
                <h3>Here you can checkout your BMI and
                <br>
                know how you can work out on it...</h3>
                </div>
                """

                # Display in Streamlit
                st.markdown(css_animation + html_content, unsafe_allow_html=True)

                # st.subheader("Here you can checkout your BMI and know how you can work out on it...")
                col1, col2 = st.columns(2)
                with col1:
                    height = st.slider("Your height(in metres)", 0.55, 2.72)
                    weight = st.slider("Your weight(in kilograms)", 5, 120)

                    bmi = weight / (height * height)

                    if st.button("Submit"):
                        result = f"Hi , your BMI is {bmi:.2f}"
                        st.text(result)
                        
                        if bmi < 18.5:
                                st.warning("You are underweight!!!")
                                if st.expander("Click here to know how to improve your BMI."):
                                        st.info("1.) Eat more frequently.")
                                        st.info("2.) Choose nutrient-rich foods.")
                                        st.info("3.) Try smoothies and shakes.")
                                        st.info("4.) Watch when you drink.")
                        elif 18.5 <= bmi <= 24.9:
                                    st.success("You have an acceptable BMI")
                                    st.balloons()
                                    if st.expander("Click here to know how to maintain a good BMI."):
                                        st.info("1.) Try to make physical activity a regular part of your day.")
                                        st.info("2.) Stay hydrated and eat a balanced diet.")
                                        st.info("3.) Avoid random snacking.")
                        elif 25 <= bmi <= 29.9:
                                    st.warning("You are overweight!!!")
                                    if st.expander("Click here to know how to improve your BMI."):
                                        st.info("1.) Follow a healthy, balanced diet.")
                                        st.info("2.) Be physically active.")
                                        st.info("3.) Monitor your progress.")
                        else:
                                    st.warning("You are obese!!!")
                                    if st.expander("Click here to know your eating habits."):
                                        st.info("1.) Drink at least 8-10 glasses of water a day to help control hunger and boost metabolism.")
                                        st.info("2.) Aim to eat 5-6 small, balanced meals throughout the day to regulate blood sugar and reduce cravings.")
                                        st.info("3.) Make weight gainer shakes by mixing oats, milk, banana, peanut butter, and whey protein in your blender.")
                                        st.info("4.) Incorporate more fiber-rich foods like fruits, vegetables, and whole grains into your diet to feel fuller longer.")


                        

                        
                with col2:
                    fig = go.Figure(go.Indicator(
                            mode="gauge+number",
                            value=bmi,
                            title={'text': "BMI"},
                            gauge={
                                'axis': {'range': [0, 50]},
                                'steps': [
                                    {'range': [0, 18.5], 'color': "lightblue"},
                                    {'range': [18.5, 24.9], 'color': "green"},
                                    {'range': [25, 29.9], 'color': "yellow"},
                                    {'range': [30, 34.9], 'color': "orange"},
                                    {'range': [35, 50], 'color': "red"}
                                ],
                                'threshold': {
                                    'line': {'color': "black", 'width': 4},
                                    'thickness': 0.75,
                                    'value': bmi
                                }
                            }
                        ))

                    st.plotly_chart(fig)    
    
    if option=='Nutrient Mapping':
        st.markdown("""
                        <h1 class='animated' style='
                        animation: pulse 2s infinite;
                        text-align: center;
                        font-size: 40px;
                        color: yellow;
                        font-weight: bold;
                        text-shadow: 2px 2px 4px #cccccc;
                        font-family: Lucida Fax, sans-serif;
                        letter-spacing: 2px;
                        word-spacing: 5px;
                        '>
                        <span style='font-style: italic'>Nutrient <span style='font-style: italic'>Mapping</span></span>
                        </h1>
                        """, unsafe_allow_html=True)

        cat= df.Category.unique()
        cat= cat.tolist()    
        cat1 = ['Select']
        cat1 = cat1 + cat
        select_cat = st.selectbox("Select Food Category",options=cat1)
        if select_cat == 'Select':
            pass
        else:
            con= df[df['Category']==select_cat]
        select_col= st.selectbox("Select Nutrient", options=['Select','Calories','Protein','Fat','Sat.Fat','Fiber','Carbs'])
        if select_cat=="Select" or select_col=="Select":
            # st_lottie(link, key="user",height=300)
            st_lottie(link3, key="user",height=300)
        else:
            protein_rich= df.sort_values(by='Protein', ascending= False)
            fig1 = px.bar(con, x='Food', y=select_col, color='Protein', title=' Top 10 protein rich foods')

            # for calories
            calories_rich= df.sort_values(by='Calories', ascending= False)
            fig2 = px.bar(con, x='Food', y=select_col, color='Calories', title=' Top 10 Calories rich foods')

            #for fat
            fat_rich= df.sort_values(by='Fat', ascending= False)
            fig3 = px.bar(con, x='Food', y=select_col, color='Fat', title=' Top 10 Fat rich foods')

            #for sat.fat
            sat_rich= df.sort_values(by='Sat.Fat', ascending= False)
            fig4 = px.bar(con, x='Food', y=select_col, color='Sat.Fat', title=' Top 10 Saturated Fat rich foods')

            #for fibres
            fib_rich= df.sort_values(by='Fiber', ascending= False)
            fig5 = px.bar(con, x='Food', y=select_col, color='Fiber', title=' Top 10 Fiber rich foods')

            #for carbs
            carb_rich= df.sort_values(by='Carbs', ascending= False)
            fig6 = px.bar(con, x='Food', y=select_col, color='Carbs', title=' Top 10 Carbs rich foods')

            if select_col=='Protein':
                st.plotly_chart(fig1)
            elif select_col=='Calories':
                st.plotly_chart(fig2)
            elif select_col=='Fat':
                st.plotly_chart(fig3)
            elif select_col=='Sat.Fat':
                st.plotly_chart(fig4)
            elif select_col=='Fibre':
                st.plotly_chart(fig5)
            else:
                st.plotly_chart(fig6)

    if option=='Food Genie':
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API And get response

            def get_gemini_repsonse(input,image,prompt):
                model=genai.GenerativeModel('gemini-1.5-flash')
                response=model.generate_content([input,image[0],prompt])
                return response.text

            def input_image_setup(uploaded_file):
                # Check if a file has been uploaded
                if uploaded_file is not None:
                    # Read the file into bytes
                    bytes_data = uploaded_file.getvalue()

                    image_parts = [
                        {
                            "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                            "data": bytes_data
                        }
                    ]
                    return image_parts
                else:
                    raise FileNotFoundError("No file uploaded")
                

            video_file = "vecteezy_burst-of-strawberry-blueberry-in-black-background_26656716.mp4"  # Replace with your local MP4 file

            # Encode the video file in base64
            video_base64 = base64.b64encode(open(video_file, "rb").read()).decode()

            # Create the HTML code for the video background
            video_html = """
            <style>
                body {{
                    margin: 0;
                    background-color: #f0f0f0;
                }}
                video {{
                    position: fixed;
                    right: 0;
                    bottom: 0;
                    min-width: 100%;
                    min-height: 100%;
                }}
                .content {{
                    position: fixed;
                    bottom: 0;
                    background: rgba(0, 0, 0, 0.5);
                    color: #f1f1f1;
                    width: 100%;
                    padding: 20px;
                }}
            </style>
            <video autoplay muted loop>
                <source src="data:video/mp4;base64,{video_base64}">
                Your browser does not support HTML5 video.
            </video>

            """.format(video_base64=video_base64)

            # Add the video background to the Streamlit app
            st.markdown(video_html, unsafe_allow_html=True)



            st.markdown("""
            <style>
                .animated {
                    animation: bounce 2s, grow 2s, turn 2s, zoom 2s;
                    animation-fill-mode: forwards;
                    animation-iteration-count: 1;
                }
                @keyframes bounce {
                    0% {
                        transform: translateY(0);
                    }
                    50% {
                        transform: translateY(-10px);
                    }
                    100% {
                        transform: translateY(0);
                    }
                }
                @keyframes grow {
                    0% {
                        transform: scale(0.5);
                    }
                    100% {
                        transform: scale(1);
                    }
                }
                @keyframes turn {
                    0% {
                        transform: rotate(0deg);
                    }
                    100% {
                        transform: rotate(360deg);
                    }
                }
                @keyframes zoom {
                    0% {
                        transform: scale(0.1);
                    }
                    100% {
                        transform: scale(1);
                    }
                }
            </style>
            """, unsafe_allow_html=True)


            st.markdown("""
                        <h1 class='animated' style='
                        text-align: center;
                        font-size: 40px;
                        color: yellow;
                        font-weight: bold;
                        text-shadow: 2px 2px 4px #cccccc;
                        font-family: Lucida Fax, sans-serif;
                        letter-spacing: 2px;
                        word-spacing: 5px;
                        '>
                        <span style='font-style: italic'>Food <span style='font-style: italic'>Genie</span></span>
                        </h1>
                        """, unsafe_allow_html=True)

            # link='https://lottie.host/e631d8d5-cbf7-4b92-8536-e237af9027f3/o0b9qnpglO.json'
            # st_lottie(link, key="user",height=300)


            # st.header(":blue[Health App]")
            input=st.text_input("Ask Here!!: ",key="input")
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
            image=""   
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image.",width=150)


            submit=st.button("Click to get your answer!!")

            input_prompt="""
            You are an expert in nutritionist where you need to see the food items from the image
                        and calculate the total nutrients and state that the item is healthy or unhealthy in bold letters, also provide the details of every food items with calories and energy intake
                        is below format

                        1. Item 1 - *no of calories, energy
                                        no of proteins
                                        no of fats
                        2. Item 2 - no of calories, energy
                                    no of proteins
                                    no of fats
                        ----
                        ---- 
                        answer to question.
            """
            ## If submit button is clicked

            if submit:
                image_data=input_image_setup(uploaded_file)
                response=get_gemini_repsonse(input_prompt,image_data, input)
                st.markdown("<h2 class='animated' style='text-align: center; font-size: 40px; color: #3498db; font-weight: bold'>Here, You Go!!</h2>", unsafe_allow_html=True)
                # st.subheader("The Response is")
                st.write(response)


    # st.markdown(css, unsafe_allow_html=True)
app()








