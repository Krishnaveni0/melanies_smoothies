# # =================================================================
# import streamlit as st
# # from snowflake.snowpark.context import get_active_session
# from snowflake.snowpark.functions import col
# import requests


# st.title('my parents new healthy diner')

# # write directly to app


# st.write(":cup_with_straw:customize your Smoothies! :cup_with_straw:")
# st.write(
#     """ Choose the fruits you want in your custom smoothie!
#     """)

# name_on_order=st.text_input("Name of Smoothie:")
# st.write('The name of Smoothie will be',name_on_order)

# # session = get_active_sessio()
# cnx=st.connection("Snowflake")
# session=cnx.session()
# my_dataframe = session.table("smoothies.public.fruit_options").select(
#     col("FRUIT_NAME"), col("SEARCH_ON")
# )
# # st.dataframe(data=my_dataframe, use_container_width=True)

# pd_df=my_dataframe.to_pandas()
# # st.dataframe(pd_df)
# # st.stop()

# ingredients_list=st.multiselect(
#     'Choose up to 5 ingredients:',
#     my_dataframe,
#     max_selections=5
# )
#  # Create the INGREDIENTS_STRING Variable 
# if ingredients_list:
#     # add space 
#     ingredients_string=' '
 
#     for fruit_chosen in ingredients_list:
#         ingredients_string += fruit_chosen+' '
#         search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
#         st.write('The search value for ', fruit_chosen,' is ', search_on, '.')

        
#         st.subheader(fruit_chosen+"nutrition information")
#         smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/"+fruit_chosen)
#         sf_df=st.dataframe(data=smoothiefroot_response.json(),use_container_width=True)
#     # st.write(ingredients_string)
# # Build a SQL Insert Statement & Test It
#     my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
#             values ('""" + ingredients_string +"""','""" + name_on_order+ """')"""
#     st.write(my_insert_stmt)
#     # st.stop()
#     time_to_insert =st.button("Submit Order")
#     if time_to_insert:
#         session.sql(my_insert_stmt).collect()
#         st.success('Your Smoothie is ordered!', icon="✅")



# =================================================================
import streamlit as st
from snowflake.snowpark.functions import col
import requests
import pandas as pd

st.title("My Parents' New Healthy Diner")
st.write(":cup_with_straw: Customize your Smoothies! :cup_with_straw:")
st.write("Choose the fruits you want in your custom smoothie!")

# Name input
name_on_order = st.text_input("Name of Smoothie:")
st.write("The name of Smoothie will be", name_on_order)

# Connect to Snowflake
cnx = st.connection("snowflake")  # must match [connections.snowflake] in secrets.toml
session = cnx.session()

# Query fruits
my_dataframe = session.table("smoothies.public.fruit_options").select(
    col("FRUIT_NAME"), col("SEARCH_ON")
)
pd_df = my_dataframe.to_pandas()
pd_df.columns = pd_df.columns.str.lower()  # normalize casing

# Prepare dropdown list and search mapping
fruit_options = pd_df["fruit_name"].tolist()
fruit_lookup = dict(zip(pd_df["fruit_name"], pd_df["search_on"]))

# Multiselect
ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
    fruit_options,
    max_selections=5
)

if ingredients_list:
    ingredients_string = ", ".join(ingredients_list)

    for fruit_chosen in ingredients_list:
        search_term = fruit_lookup.get(fruit_chosen, fruit_chosen)
        st.write(f"The search value for **{fruit_chosen}** is **{search_term}**.")

        st.subheader(f"{fruit_chosen} Nutrition Information")

        response = requests.get(f"https://my.smoothiefroot.com/api/fruit/{search_term}")

        if response.status_code == 200:
            st.dataframe(pd.json_normalize(response.json()), use_container_width=True)
        else:
            st.error(f"Could not fetch data for {fruit_chosen} ({search_term})")

    # Insert order
    my_insert_stmt = f"""
        INSERT INTO smoothies.public.orders (ingredients, name_on_order)
        VALUES ('{ingredients_string}', '{name_on_order}')
    """
    st.write(my_insert_stmt)

    if st.button("Submit Order"):
        session.sql(my_insert_stmt).collect()
        st.success("Your Smoothie is ordered!", icon="✅")

