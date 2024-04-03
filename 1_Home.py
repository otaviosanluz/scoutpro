import streamlit as st
import pandas as pd 
import webbrowser

if 'data' not in st.session_state:
    df_data = pd.read_excel('C:/Users/otavi/rating_players/fbref_data/pro/df_radar_pro.xlsx')
    st.session_state['data'] = df_data

#if 'data' not in st.session_state:
    #df_data = pd.read_excel('C:/Users/otavi/rating_players/fbref_data/df_radar.xlsx')
    #st.session_state['data'] = df_radar

st.write('## ScoutPRO')

st.markdown(
    '''
    Welcome to ScoutPRO! 

    ScoutPRO is a platform dedicated to providing detailed analysis and statistics for the 2023 Brazilian Championship, using data from the fbref website. Our goal is to assist coaches, analysts, and football enthusiasts in better understanding player and team performance, facilitating strategic decision-making.

    **Key features:**

    - Player Percentile Charts: Visualize where players stand in relation to others, allowing for comparative analysis of their performance across different metrics.
    - Player Profiles: Explore comprehensive profiles of each player.
    
    Whether you are a coach seeking valuable insights, an analyst in need of detailed data, or just a curious fan about your favorite team's performance, ScoutPRO is here to provide the necessary tools for a deep and informed analysis of Brazilian football.

    Explore our features and dive into the world of football statistics
    '''
)

st.sidebar.markdown('Developed by [Otavio Santos](https://www.linkedin.com/in/otaviosanluz/)')

bt = st.button('fbref Data')
if bt:
    webbrowser.open_new_tab('https://fbref.com/pt/comps/24/Serie-A-Estatisticas')