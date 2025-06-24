# # Import python packages
# import streamlit as st
# from snowflake.snowpark.context import get_active_session

# # Write directly to the app
# st.title(f"Example Streamlit App :balloon: {st.__version__}")
# st.write(
#   """Replace this example with your own code!
#   **And if you're new to Streamlit,** check
#   out our easy-to-follow guides at
#   [docs.streamlit.io](https://docs.streamlit.io).
#   """
# )
# import streamlit as st

# option = st.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone"),
#     index=None,
#     placeholder="Select contact method...",
# )

# # ---------------------------

# st.write("You selected:", option)




# option = st.selectbox(
#     "what is your favourite fruit?",
#     ("apple", "Strawberries",'Peaches'),
#     index=None,
#     placeholder="Select contact method...",
# )

# st.write("You selected:", option)


# # --------------
# session = get_active_session()
# my_dataframe = session.table("smoothies.public.fruit_options")
# st.dataframe(data=my_dataframe, use_container_width=True)



# ====================================
# # removing select box

# # import py packages
# import streamlit as st
# from snowflake.snowpark.context import get_active_session

# # write directly to app
# st.write(":cup_with_straw:customize your Smoothies! :cup_with_straw:")
# st.write(""" Choose the fruits you want in your custom smoothie!
# """)

# session = get_active_session()
# my_dataframe = session.table("smoothies.public.fruit_options")
# st.dataframe(data=my_dataframe, use_container_width=True)





# 🥋 Focus on the FRUIT_NAME Column


# # import py packages
# import streamlit as st
# from snowflake.snowpark.context import get_active_session

# # write directly to app
# st.write(":cup_with_straw:customize your Smoothies! :cup_with_straw:")
# st.write(""" Choose the fruits you want in your custom smoothie!
# """)
# from snowflake.snowpark.functions import col


# session = get_active_session()
# my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# # st.dataframe(data=my_dataframe, use_container_width=True)

# # ADDING MULTI SELECT
# ingredients_list=st.multiselect(
#     'Choose up to 5 ingredients:',
#     my_dataframe
# )


# # limiting upto 5 ingredients
# # Enforce a 5-ingredient max (soft enforcement)
# if len(ingredients_list) > 5:
#     st.warning("⚠️ Please select no more than 5 ingredients.")
#     ingredients_list = ingredients_list[:5]  # Optional: trim the list to 5

# # Display selected ingredients
# st.write("Your smoothie ingredients:", ingredients_list)


# #  throughs error +=he st.text() function only takes one argument — a single string.
# # st.text("Your smoothie ingredients:", ingredients_list)

# st.text(f"Your smoothie ingredients: {ingredients_list}")


# ===================================

# # CLEANING UP EMPTY BRACKETS
# import streamlit as st
# from snowflake.snowpark.context import get_active_session

# # write directly to app
# st.write(":cup_with_straw:customize your Smoothies! :cup_with_straw:")
# st.write(""" Choose the fruits you want in your custom smoothie!
# """)
# from snowflake.snowpark.functions import col


# session = get_active_session()
# my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# # st.dataframe(data=my_dataframe, use_container_width=True)

# # ADDING MULTI SELECT
# ingredients_list=st.multiselect(
#     'Choose up to 5 ingredients:',
#     my_dataframe
# )
# # if ingredients_list:
# #     st.write(ingredients_list)
# #     st.text(ingredients_list)

#  # Create the INGREDIENTS_STRING Variable 
# if ingredients_list:
#     st.write(ingredients_list)
#     st.text(ingredients_list)

#     ingredients_string=''

#     for fruit_chosen in ingredients_list:
#         ingredients_string += fruit_chosen

#     st.write(ingredients_string)



# ===========================
# # 🥋 Improve the String Output
# import streamlit as st
# from snowflake.snowpark.context import get_active_session

# # write directly to app
# st.write(":cup_with_straw:customize your Smoothies! :cup_with_straw:")
# st.write(""" Choose the fruits you want in your custom smoothie!
# """)
# from snowflake.snowpark.functions import col

# session = get_active_session()
# my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# # st.dataframe(data=my_dataframe, use_container_width=True)

# # ADDING MULTI SELECT
# ingredients_list=st.multiselect(
#     'Choose up to 5 ingredients:',
#     my_dataframe
# )
# # if ingredients_list:
# #     st.write(ingredients_list)
# #     st.text(ingredients_list)

#  # Create the INGREDIENTS_STRING Variable 
# if ingredients_list:
#     # add space 
#     ingredients_string=' '

#     for fruit_chosen in ingredients_list:
#         ingredients_string += fruit_chosen+' '

#     st.write(ingredients_string)
# # Build a SQL Insert Statement & Test It
# my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
#             values ('""" + ingredients_string + """')"""

# st.write(my_insert_stmt)

# # -- 🥋 Insert the Order into Snowflake
# if ingredients_string:
#     session.sql(my_insert_stmt).collect()
#     st.success('Your Smoothie is ordered!', icon="✅")

# ========================================

# 🥋 Add a Submit Button

# import streamlit as st
# from snowflake.snowpark.context import get_active_session

# # write directly to app
# st.write(":cup_with_straw:customize your Smoothies! :cup_with_straw:")
# st.write(""" Choose the fruits you want in your custom smoothie!
# """)
# from snowflake.snowpark.functions import col

# session = get_active_session()
# my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# # st.dataframe(data=my_dataframe, use_container_width=True)

# # ADDING MULTI SELECT
# ingredients_list=st.multiselect(
#     'Choose up to 5 ingredients:',
#     my_dataframe
# )
#  # Create the INGREDIENTS_STRING Variable 
# if ingredients_list:
#     # add space 
#     ingredients_string=' '

#     for fruit_chosen in ingredients_list:
#         ingredients_string += fruit_chosen+' '

#     st.write(ingredients_string)
# # Build a SQL Insert Statement & Test It
#     my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
#             values ('""" + ingredients_string + """')"""

#     time_to_insert =st.button("Submit Order")
#     if time_to_insert:
#         session.sql(my_insert_stmt).collect()
#         st.success('Your Smoothie is ordered!', icon="✅")


# ===================================================

#     # 🥋 Move Your Import COL Function Statement to Top of Code
# import streamlit as st
# from snowflake.snowpark.context import get_active_session
# from snowflake.snowpark.functions import col

# # write directly to app
# st.write(":cup_with_straw:customize your Smoothies! :cup_with_straw:")
# st.write(
#     """ Choose the fruits you want in your custom smoothie!
#     """)

# name_on_order=st.text_input("Name of Smoothie:")
# st.write('The name of Smoothie will be',name_on_order)

# session = get_active_session()
# my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# # st.dataframe(data=my_dataframe, use_container_width=True)

# ingredients_list=st.multiselect(
#     'Choose up to 5 ingredients:',
#     my_dataframe
# )
#  # Create the INGREDIENTS_STRING Variable 
# if ingredients_list:
#     # add space 
#     ingredients_string=' '

#     for fruit_chosen in ingredients_list:
#         ingredients_string += fruit_chosen+' '

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
# ====================================================

#         # ==========================================================================
# # pending
#             # 🥋 Move Your Import COL Function Statement to Top of Code
# import streamlit as st
# from snowflake.snowpark.context import get_active_session
# from snowflake.snowpark.functions import col

# # write directly to app
# st.write(":cup_with_straw:customize your Smoothies! :cup_with_straw:")
# st.write(
#     """ Choose the fruits you want in your custom smoothie!
#     """)

# name_on_order=st.text_input("Name of Smoothie:")
# st.write('The name of Smoothie will be',name_on_order)

# session = get_active_session()
# my_dataframe = session.table("smoothies.public.orders").filter(col("ORDER_FILLED")==0).collect()# st.dataframe(data=my_dataframe, use_container_width=True)

# ingredients_list=st.multiselect(
#     'Choose up to 5 ingredients:',
#     my_dataframe
# )
#  # Create the INGREDIENTS_STRING Variable 
# if ingredients_list:
#     # add space 
#     ingredients_string=' '

#     for fruit_chosen in ingredients_list:
#         ingredients_string += fruit_chosen+' '

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
# from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import requests

st.title('my parents new healthy diner')

# write directly to app


st.write(":cup_with_straw:customize your Smoothies! :cup_with_straw:")
st.write(
    """ Choose the fruits you want in your custom smoothie!
    """)

name_on_order=st.text_input("Name of Smoothie:")
st.write('The name of Smoothie will be',name_on_order)

# session = get_active_sessio()
cnx=st.connection("Snowflake")
session=cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'),col('search_on'))
# st.dataframe(data=my_dataframe, use_container_width=True)
# st.stop()


pd_df=my_dataframe.to_pandas()
# st.dataframe(pd_df)
# st.stop()

ingredients_list=st.multiselect(
    'Choose up to 5 ingredients:',
    my_dataframe,
    max_selections=5
)
 # Create the INGREDIENTS_STRING Variable 
if ingredients_list:
    # add space 
    ingredients_string=' '

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen+' '
        
        search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
        # st.write('The search value for ', fruit_chosen,' is ', search_on, '.')

        
        st.subheader(fruit_chosen + 'Nutition Information')         
        smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon" +fruit_chosen)
        sf_df=st.dataframe(data=smoothiefroot_response.json(),use_container_width=True)
    # st.write(ingredients_string)
# Build a SQL Insert Statement & Test It
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string +"""','""" + name_on_order+"""')"""
    # st.write(my_insert_stmt)
    # st.stop()
    time_to_insert =st.button("Submit Order")
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")


# import requests
# smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
# # st.text(smoothiefroot_response.json())
# sf_df=st.dataframe(data=smoothiefroot_response.json(),use_container_width=True)


