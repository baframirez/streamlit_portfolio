import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# configure page
st.set_page_config(page_title="Portfolio Bruno Figueroa", layout="wide")

# sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "About", "Contact"])

if page == "Home":
    st.title("Welcome to my Data Science Portfolio")
    st.write("This site showcases my projects, interactive demos, and contact info.")
    st.image("static/images.png", width="content")

elif page == "Projects":
    st.header("Projects")
    # sample project metadata; in a real app this could be loaded from a JSON or database
    projects = [
        {
            "title": "Customer Churn Analysis",
            "description": "Analyzed telecom customer churn with logistic regression and dashboarded insights.",
            "tech": "Python, scikit-learn, Streamlit",
            "link": "https://github.com/username/churn-analysis"
        },
        {
            "title": "Interactive COVID-19 Dashboard",
            "description": "Visualization of global case data using Plotly and live API feeds.",
            "tech": "Python, Plotly, Pandas",
            "link": "https://github.com/username/covid-dashboard"
        },
        {
            "title": "NLP Sentiment Classifier",
            "description": "Built a sentiment analysis pipeline on movie reviews with transformers.",
            "tech": "Python, Hugging Face, Streamlit",
            "link": "https://github.com/username/sentiment-nlp"
        }
    ]
    cols = st.columns(2)
    for i, proj in enumerate(projects):
        with cols[i % 2]:
            st.subheader(proj["title"])
            st.write(proj["description"])
            st.write(f"Tech: {proj['tech']}")
            st.markdown(f"[View on GitHub]({proj['link']})")
    
    # simple interactive demo
    st.markdown("---")
    st.subheader("Sample Demo: Random Scatter Plot")
    n = st.slider("Points", 10, 500, 100)
    df = pd.DataFrame({
        "x": np.random.randn(n),
        "y": np.random.randn(n),
        "category": np.random.choice(["A", "B", "C"], size=n)
    })
    fig = px.scatter(df, x="x", y="y", color="category")
    st.plotly_chart(fig, use_container_width=True)

elif page == "About":
    st.header("About Me")
    st.write("I'm a data scientist with experience in machine learning, data visualization, and web apps.")
    st.markdown("Download my [CV](static/CV.pdf)")

elif page == "Contact":
    st.header("Contact")
    st.write("Feel free to reach out via email or LinkedIn.")
    st.write("**Email:** example@example.com")
    st.write("**LinkedIn:** [profile](https://www.linkedin.com/in/username)")
