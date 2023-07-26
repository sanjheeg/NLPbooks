import streamlit as st
import glob
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px


def get_data():
    filepaths = sorted(glob.glob("diary/*.txt"))
    files = []
    all_pos = []
    all_neg = []
    for filepath in filepaths:
        filename = Path(filepath).stem
        files.append(filename)

        analyzer = SentimentIntensityAnalyzer()
        with open(filepath, "r") as entry:
            content = entry.read()
            scores = analyzer.polarity_scores(content)
            pos = scores["pos"]
            all_pos.append(pos)
            neg = scores["neg"]
            all_neg.append(neg)
    return files, all_pos, all_neg


dates, pos, neg = get_data()

st.title("Diary Tone")
st.subheader("Positivity")
figure = px.line(x=dates, y=pos, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=neg, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(neg_figure)