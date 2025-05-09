# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px
import os
import gdown


dataset_path = "aspect_sentiment_dataset.csv"

# Download only if not already downloaded
if not os.path.exists(dataset_path):
    url = "https://drive.google.com/uc?id=1n-Nv39QKVpi8FTF4WEB9iB76SpDybTEa"
    gdown.download(url, dataset_path, quiet=False)

# Load the dataset into a DataFrame
df = pd.read_csv(dataset_path)

st.set_page_config(page_title="Aspect-Based Sentiment Analysis for MOOCs", layout="wide")

st.title("🎓 MOOC Aspect-Based Sentiment Dashboard")
st.markdown("Analyze learner feedback across aspects like videos, quizzes, instructors, and content.")

# Sidebar filters
aspects = sorted(df['aspect'].unique())
selected_aspect = st.sidebar.selectbox("Select Aspect", aspects)
filtered_df = df[df['aspect'] == selected_aspect]

# Pie chart of sentiment distribution
sentiment_counts = filtered_df['sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['Sentiment', 'Count']
fig_pie = px.pie(sentiment_counts, names='Sentiment', values='Count',
                 title=f"Sentiment Distribution for Aspect: {selected_aspect}",
                 color_discrete_sequence=px.colors.qualitative.Set3)

# Bar chart: frequency of each aspect overall
aspect_counts = df['aspect'].value_counts().reset_index()
aspect_counts.columns = ['Aspect', 'Count']
fig_bar = px.bar(aspect_counts, x='Aspect', y='Count',
                 title="Most Discussed Aspects in Reviews",
                 color='Count', color_continuous_scale='Blues')

# Layout
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_pie, use_container_width=True)
with col2:
    st.plotly_chart(fig_bar, use_container_width=True)

# Show sample comments
st.subheader(f"💬 Sample Comments for '{selected_aspect}' by Sentiment")

tabs = st.tabs(["👍 Positive", "😐 Neutral", "👎 Negative"])
for sentiment, tab in zip(["positive", "neutral", "negative"], tabs):
    with tab:
        samples = filtered_df[filtered_df["sentiment"] == sentiment]["sentence"].head(5).tolist()
        if samples:
            for s in samples:
                st.write(f"- {s}")
        else:
            st.info("No samples available for this sentiment.")
