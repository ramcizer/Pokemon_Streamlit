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

# st.set_page_config(layout="wide")
st.set_page_config(layout="wide")
st.header('Pick a Pokémon for their cry and number of moves comparison')
with st.container(): 
    col2, col3, col4 = st.columns([0.4,1.5,1.5]) 

    # st.session_state

    with col3: 

        pokemon_number = st.slider("Pick a Pokémon",
                                min_value=1,
                                max_value=150
                                )
        audio_url = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{pokemon_number}.ogg"
        st.audio(audio_url, format='audio/mp3', start_time=0)
        pokemon_number2 = st.slider("Pick 2nd Pokémon",
                                min_value=1,
                                max_value=150
                                )
        audio_url2 = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{pokemon_number2}.ogg"
        st.audio(audio_url2, format='audio/mp3', start_time=0)

        pokemon_number3 = st.slider("Pick 3rd Pokémon",
                                min_value=1,
                                max_value=150
                                )
        audio_url3 = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{pokemon_number3}.ogg"
        st.audio(audio_url3, format='audio/mp3', start_time=0)


    name, height, weight, moves = get_details(pokemon_number)
    name2, height2, weight2, moves2 = get_details(pokemon_number2)
    name3, height3, weight3, moves3 = get_details(pokemon_number3)


    height_data = pd.DataFrame({'Pokemon': [name, name2, name3], 'Heights': [height, height2, height3], 'Moves': [moves, moves2, moves3]})
    colours = ['grey', 'blue', 'red']

    # Display image of pokemon! (latest sprite from front!)
    with col2: 
            image_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number}.png'
            # st.image(image_url, caption='Image of Pokemon', use_column_width=True)
            st.image(image_url, use_column_width=False)
            image_url2 = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number2}.png'
            st.image(image_url2, use_column_width=False)
            image_url3 = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number3}.png' 
            st.image(image_url3, use_column_width=False)
    # st.image(image_url, caption='Image of Pokemon', width=400, align='center')


    with col4:
        plt.figure(figsize=(7, 5.5))
        plt.bar(height_data['Pokemon'], height_data['Moves'], color='skyblue')
        plt.title('Moves Comparison of Different Pokémon')
        plt.xlabel('Pokémon')
        plt.ylabel('Moves')
        plt.xticks(rotation=45)
        st.pyplot(plt)

with st.container(): 
        # st.header("Other stats")
        col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,0.61,0.61,0.61]) 
        with col4:
             st.write(f'<span style="font-size: large; line-height: 0.8; padding-bottom: 100px;">Name: {name} <br> Height: {height}  <br> Weight: {weight} <br> Moves: {moves} </span>', unsafe_allow_html=True, use_column_width=True )
        with col5: 
            st.write(f'<span style="font-size: large; line-height: 0.8; padding-bottom: 100px;">Name: {name2} <br> Height: {height2}  <br> Weight: {weight2} <br> Moves: {moves2} </span>', unsafe_allow_html=True, use_column_width=True)
        with col6: 
                 st.write(f'<span style="font-size: large; line-height: 0.8; padding-bottom: 100px;">Name: {name3} <br> Height: {height3}  <br> Weight: {weight3} <br> Moves: {moves3} </span>', unsafe_allow_html=True, use_column_width=True)

# Other ideas
# Stretch version -> display the many sprites from the API!
# Make it look better!
# Add the audio of the latest battle cry!
# Use whole pokedex!
# use the pokemon type to change colour of barchart!
