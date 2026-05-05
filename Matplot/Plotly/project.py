import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

final_df = pd.read_csv('india.csv')

list_of_state = list(final_df['State'].unique())
list_of_state.insert(0,'OverAll India')

st.sidebar.title("India's Data Visulization")

selected_score = st.sidebar.selectbox('Select the state',list_of_state)
sorted(final_df.columns[5:])
primary = st.sidebar.selectbox('Select primary parameter',sorted(final_df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary parameter',sorted(final_df.columns[5:]))


plot = st.sidebar.button('Plot Graph')

if plot:
    
    st.text('Size represents primary parameter')
    st.text('Size represents secondary parameter')
    if selected_score == 'OverAll India':
        # we are plotting for india
            df = px.data.carshare
            fig = px.scatter_mapbox(final_df,lat='Latitude',lon='Longitude'
                          ,zoom=3,size=primary,size_max=35,color=secondary,mapbox_style='carto-positron',width=1200,height=800,hover_name= 'District')
            st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = final_df[final_df['State'] == selected_score]
        fig = px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude'
                          ,zoom=3,size=primary,size_max=35,color=secondary,mapbox_style='carto-positron',width=1200,height=800,hover_name= 'District')
        st.plotly_chart(fig,use_container_width=True)