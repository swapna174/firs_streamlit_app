import streamlit
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega and Blueberry oats')
streamlit.text('🥗 Kale,Spinach and SMothhie')
streamlit.text('🐔 Hard Boilded Free Caged  Eggs')
streamlit.text('🥑🍞 Avacodo Toast')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
