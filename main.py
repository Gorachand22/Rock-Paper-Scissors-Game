import streamlit as st
from accessories import image_list
import random
import base64
def play_game(user_choice):
    computer_choice = random.randint(0, 2)
    
    # Display GIF for user's choice
    with open(image_list[user_choice], "rb") as f:
        contents = f.read()
        data_url_user = base64.b64encode(contents).decode("utf-8")
        st.markdown(f'<img src="data:image/gif;base64,{data_url_user}" alt="Your Choice">', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size: 20px; font-weight: bold; color:pink;">Your Choice</p>', unsafe_allow_html=True)

    # Display GIF for computer's choice
    with open(image_list[computer_choice], "rb") as f:
        contents = f.read()
        data_url_computer = base64.b64encode(contents).decode("utf-8")
        st.markdown(f'<img src="data:image/gif;base64,{data_url_computer}" alt="Computer\'s Choice">', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size: 20px; font-weight: bold; color: pink;">Computer\'s Choice</p>', unsafe_allow_html=True)

    if user_choice == computer_choice:
        st.markdown(f'<p style="font-size: 30px; font-weight: bold; color: orange;">It\'s a tie!</p>', unsafe_allow_html=True)
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        st.markdown(f'<p style="font-size: 30px; font-weight: bold; color: blue;">You win!</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p style="font-size: 30px; font-weight: bold; color: red;">You lose!</p>', unsafe_allow_html=True)

# Streamlit App
st.title('Welcome To Rock-Paper-Scissors Game')

st.sidebar.title('RPS Game')

# Sidebar options
ln = st.sidebar.selectbox('Check this out', ['Tap to play', 'how to play', 'about'])
if ln == 'Tap to play':
    # Create clickable buttons for each option
    st.image('images/OIG.png', caption="Rock-Paper-Scissors", width=300)
    user_choice = st.radio("Choose your move:", ["Rock🪨", "Paper📃", "Scissors✂️"], key='game_choice')
    if st.button('Play'):
        if user_choice == "Rock🪨":
            play_game(0)
        elif user_choice == "Paper📃":
            play_game(1)
        elif user_choice == "Scissors✂️":
            play_game(2)

elif ln == 'how to play':
    st.image('images/OIG1.png', caption="Rock-Paper-Scissors", width=300)
    st.write("Instructions on how to play the game:")
    st.markdown("- <span style='font-size: 30px; font-weight: bold; color: blue;'>Rock beats scissors.</span>", unsafe_allow_html=True)
    st.markdown("- <span style='font-size: 30px; font-weight: bold; color: orange;'>Scissors beats paper.</span>", unsafe_allow_html=True)
    st.markdown("- <span style='font-size: 30px; font-weight: bold; color: pink;'>Paper beats rock.</span>", unsafe_allow_html=True)

elif ln == 'about':
    st.image('images/OIG3.png', caption="Rock-Paper-Scissors", width=300)
    st.markdown("- <span style='font-size: 30px; font-weight: bold; color: blue;'>This is a simple Rock-Paper-Scissors game.</span>", unsafe_allow_html=True)
    st.markdown("- <span style='font-size: 30px; font-weight: bold; color: green;'>You can choose between Rock, Paper, and Scissors.</span>", unsafe_allow_html=True)
