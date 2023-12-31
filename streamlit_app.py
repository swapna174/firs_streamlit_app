import streamlit
import pandas
import requests
import snowflake.connector
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega and Blueberry oats')
streamlit.text('🥗 Kale,Spinach and SMothhie')
streamlit.text('🐔 Hard Boilded Free Caged  Eggs')
streamlit.text('🥑🍞 Avacodo Toast')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#import requests
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = request.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalized(fruitvice_response.json())
  return fruityvice_normalized
  
streamlit.header('Fruityvice Fruit Advice!')
try: 
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit to get info.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)


#import snowflake.connector
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
  my_cur.execute("select *from fruit_load_list")
  return my_cur.fetchall()
  
if streamlit.button('Get Fruit Load List'): 
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = getfruit_load_list()
  streamlit.dataframe(my_data_rows)






streamlit.header("The fruit load list contains:")




streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding jackfruit enjoy! ', fruit_choice)


my_cur.execute("insert into fruit_load_list values ('from streamlit')")



