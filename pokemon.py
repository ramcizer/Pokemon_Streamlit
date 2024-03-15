import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_details(poke_number):
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
        response = requests.get(url)
        pokemon = response.json()
        print(pokemon['types'])
        return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves'])
    except:
        return 'Error', np.NAN, np.NAN, np.NAN

pokemon_number, pokemon_number2, pokemon_number3 = 1, 2, 3

container_style = """
    <style>
        .container1 {
            border: 2px solid #3498db;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 20px;
        }
        .container2 {
            /* Add styles for Container 2 if needed */
        }
    </style>
"""

# Display the CSS styles
# st.markdown(container_style, unsafe_allow_html=True)

# Use the styled containers
# with st.container() as container1:
# st.set_page_config(layout="wide")
st.header('Pick a Pokemon for their cry and number of moves comparison')

name, height, weight, moves = get_details(1)
name2, height2, weight2, moves2 = get_details(2)
name3, height3, weight3, moves3 = get_details(3)

with st.container():
    col1, col2, col3 = st.columns([3,3,3], gap='small') 
 
    with col1: 
        with st.container(border=True):
            cont_col_1, cont_col_2 = st.columns([2,2], gap='medium') 
            pokemon_number = st.slider("Pick a pokemon",
                                        min_value=1,
                                        max_value=150
                                        )
            name, height, weight, moves = get_details(pokemon_number)
            with cont_col_1:
                image_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number}.png'
                st.image(image_url, use_column_width=True)                
            
            with cont_col_2:
                st.write(f'<span style="font-size: 11px; line-height: 0.8; padding-bottom: 10px;">Name: {name} <br> Height: {height}  <br> Weight: {weight} <br> Moves: {moves} </span>', unsafe_allow_html=True, use_column_width=True )
            # with st.markdown("<div style='border: 2px solid #e6e6e6; padding: 10px;'>", unsafe_allow_html=True):
                
                

            
            # st.write("Check out their cry")       
            audio_url = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{pokemon_number}.ogg"
            st.audio(audio_url, format='audio/mp3', start_time=0)
            

    with col2:
        with st.container(border=True):
            cont_col_1, cont_col_2 = st.columns([2,2], gap='medium') 
            pokemon_number2 = st.slider("Pick 2nd pokemon",
                                        min_value=1,
                                        max_value=150
                                        )
            name2, height2, weight2, moves2 = get_details(pokemon_number2)
            with cont_col_1: 
    # with st.markdown("<div style='border: 2px solid #e6e6e6; padding: 10px;'>", unsafe_allow_html=True):
                image_url2 = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number2}.png'
                st.image(image_url2, use_column_width=True)

            with cont_col_2: 
                st.write(f'<span style="font-size: 11px; line-height: 0.8; padding-bottom: 10px;">Name: {name2} <br> Height: {height2}  <br> Weight: {weight2} <br> Moves: {moves2} </span>', unsafe_allow_html=True, use_column_width=True)
            
            audio_url2 = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{pokemon_number2}.ogg"
            st.audio(audio_url2, format='audio/mp3', start_time=0)
            # st.markdown("</div>", unsafe_allow_html=True)

    with col3: 
        with st.container(border=True):
            cont_col_1, cont_col_2 = st.columns([2,2], gap='medium') 
            pokemon_number3 = st.slider("Pick 3rd pokemon",
                                min_value=1,
                                max_value=150
                                )
            name3, height3, weight3, moves3 = get_details(pokemon_number3)
            with cont_col_1: 
                image_url3 = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number3}.png' 
                st.image(image_url3, use_column_width=True)

            with cont_col_2:        
                 st.write(f'<span style="font-size: 11px; line-height: 0.8; padding-bottom: 10px;">Name: {name2} <br> Height: {height2}  <br> Weight: {weight2} <br> Moves: {moves2} </span>', unsafe_allow_html=True, use_column_width=True)
            audio_url3 = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{pokemon_number3}.ogg"
            st.audio(audio_url3, format='audio/mp3', start_time=0)

    
    
    
                
    height_data = pd.DataFrame({'Pokemon': [name, name2, name3], 'Heights': [height, height2, height3], 'Moves': [moves, moves2, moves3]})
    colours = ['grey', 'blue', 'red']


with st.container(): 
    plt.figure(figsize=(7, 5.5))
    plt.bar(height_data['Pokemon'], height_data['Moves'], color='skyblue')
    plt.title('Moves Comparison of Different Pokémon')
    plt.xlabel('Pokémon')
    plt.ylabel('Moves')
    plt.xticks(rotation=45)
    st.pyplot(plt)
