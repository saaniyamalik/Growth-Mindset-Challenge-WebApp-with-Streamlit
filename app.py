#Streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project")
st.title("Growth Midset Challenge: Web App With Streamlit ")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace the Challenge, Stop Waiting for Tomorrow Start Now🏅")

#---------------------------------------------------------------------------------#
#Quote Section
st.header("💡 Today's Growth Mindset Quote")
st.write("ALLAH is your protector, and He is the best of helpers")

st.header("🔧 What's Your Challenge Today?")
user_input = st.text_input (" Describe a Challenge You're facing ")

#----------------------------------------------------------------------------------#
#Condition
if user_input:
    st.success(f"💪🏻 You're facing: {user_input}. Keep pushing forward towords your goal!")
else:
    st.warning("Tell us about your challenge to get started! ")    

#-----------------------------------------------------------------------------------#
 #Reflexing 
st.header(" Reflect on your learning ")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"⭐️Great Inside! your reflection {reflection}")
else:
    st.info("Reflection on past experience help your grow ! share your difficulties")     

#--------------------------------------------------------------------------------------#
#Acheivments
st.header("🏆Celebrate your wins ")
acheivment = st.text_input("Share something you've recently accomplished")

if acheivment:
    st.success(f"🏅Amazing! you acheived")
else:
    st.info("Big or small, every acheivment counts! share one now 🤩")    

#--------------------------------------------------------------------------------------#
#Footer
st.write("-----")    
st.write("🌌Keep believing in yourself.Growth is a Journey not a destination⭐️")
st.write(" *****Created by Saniya Malik***** ")

