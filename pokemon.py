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
        return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves'])
    except:
        return 'Error', np.NAN, np.NAN, np.NAN

col1, col2 = st.columns([1, 4]) 

with col2: 

    pokemon_number = st.slider("Pick a pokemon",
                            min_value=1,
                            max_value=150
                            )

name, height, weight, moves = get_details(pokemon_number)

height = height + 10

height_data = pd.DataFrame({'Pokemon': ['Needle', name, 'Exaggetor'], 'Heights': [40, height, 200]})
colours = ['grey', 'blue', 'red']

# Display image of pokemon! (latest sprite from front!)
with col1: 
    image_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number}.png'
    # st.image(image_url, caption='Image of Pokemon', use_column_width=True)
    st.image(image_url, use_column_width=True)
# st.image(image_url, caption='Image of Pokemon', width=400, align='center')
with col1: 
    st.write(f'Name: {name}')
    st.write(f'Height: {height}')
    st.write(f'Weight: {weight}')
    st.write(f'Move Count: {moves}')

with col2: 
    audio_url = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{pokemon_number}.ogg"
    st.audio(audio_url, format='audio/mp3', start_time=0)
    # st.markdown("The Pokemon's Battlecry!")

with col2:
    plt.figure(figsize=(8, 6))
    plt.bar(height_data['Pokemon'], height_data['Heights'], color='skyblue')
    plt.title('Height Comparison of Different Pokémon')
    plt.xlabel('Pokémon')
    plt.ylabel('Height')
    plt.xticks(rotation=45)
    st.pyplot(plt)


# Stretch version -> display the many sprites from the API!
# Make it look better!
# Add the audio of the latest battle cry!
# Use whole pokedex!
# use the pokemon type to change colour of barchart!
