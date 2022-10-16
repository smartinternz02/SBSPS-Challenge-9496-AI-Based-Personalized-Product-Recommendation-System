import pickle
import numpy as np
import streamlit as st
import pandas as pd




def recommend(ProductID,df,pt,similarity_scores):
    # index fetch

    index = np.where(pt.index == ProductID)[0][0]
    similar_products = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x, reverse=True)[1:6]

    data = []
    for i in similar_products:
        r_products= []
        temp_df = df[df['ProductID'] == pt.index[i[0]]]
        r_products.extend(list(temp_df.drop_duplicates('ProductID')['ProductName'].values))

        data.append(r_products)
    return data

# Load the files.

#           Electronics Category
Elec_products_dict = pickle.load(open('Pickle_files/Elec_products_dict.pkl','rb'))
Elec_pivot_table = pickle.load(open('Pickle_files/Elec_pivot_table_dict.pkl','rb'))
Elec_similarity_scores = pickle.load(open('Pickle_files/Elec_similarity_scores.pkl','rb'))
Elec_prodcuts = pd.DataFrame(Elec_products_dict)
Elec_pt = pd.DataFrame(Elec_pivot_table)

#           Cell-Phones & Acceseries Categry
Cell_products_dict = pickle.load(open('Pickle_files/Cell_products_dict.pkl','rb'))
Cell_pivot_table = pickle.load(open('Pickle_files/Cell_pivot_table_dict.pkl','rb'))
Cell_similarity_scores = pickle.load(open('Pickle_files/Cell_similarity_scores.pkl','rb'))
Cell_prodcuts = pd.DataFrame(Cell_products_dict)
Cell_pt = pd.DataFrame(Cell_pivot_table)

#           Watches Category
Wat_products_dict = pickle.load(open('Pickle_files/Wat_products_dict.pkl','rb'))
Wat_pivot_table = pickle.load(open('Pickle_files/Wat_pivot_table_dict.pkl','rb'))
Wat_similarity_scores = pickle.load(open('Pickle_files/Wat_similarity_scores.pkl','rb'))
Wat_prodcuts = pd.DataFrame(Wat_products_dict)
Wat_pt = pd.DataFrame(Wat_pivot_table)




st.header('AI Based Personalized Electronic Gadgets Recommendation System')

category = st.radio(
     "select the following category: ",
     ('Electronics','Watches', 'Cell Phone & Accessories'))

if category == 'Electronics':
    pt = Elec_pt
    df = Elec_prodcuts
    similarity_scores = Elec_similarity_scores
    st.subheader('You have selected Electronics Category.')

elif category == 'Watches':
    pt = Wat_pt
    df = Wat_prodcuts
    similarity_scores = Wat_similarity_scores
    st.subheader("You have selected Watches Category.")

elif category == 'Cell Phone & Accessories':
    pt = Cell_pt
    df = Cell_prodcuts
    similarity_scores = Cell_similarity_scores
    st.subheader("You have selected Cell Phone & Accessories Category.")

else:
    st.subheader("Please select a Category!")

selected_product_name = st.selectbox(
    'Select the product that you want to recommend->',
    df
)
select_df = df[df['ProductID'] == selected_product_name]
selected_productid = select_df['ProductID']

st.write(selected_productid)

if st.button('Recommend'):
    recommended_products = recommend(selected_productid,df,pt,similarity_scores)
    product_list = []
    for i in recommended_products:
        product_list.extend(i)

    for i in product_list:
        st.write(i)




