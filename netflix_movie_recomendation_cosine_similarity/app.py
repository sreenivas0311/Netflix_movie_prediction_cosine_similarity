import pickle
import streamlit as st

# ----------------------------
# Load saved artifacts
# ----------------------------
with open('df_cleaned.pkl', 'rb') as f:
    df = pickle.load(f)

with open('cosine_sim.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)

# ----------------------------
# Recommendation function
# ----------------------------
def recommend(title, df, cosine_sim, top_n=5):
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n + 1]
    indices = [i[0] for i in sim_scores]
    return df['title'].iloc[indices]

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Netflix Recommender", layout="centered")
st.title("🎬 Netflix Content Recommendation System")

# Searchable auto-suggest dropdown (Google-like)
selected_title = st.selectbox(
    "Search and select a movie or TV show",
    sorted(df['title'].values)
)

top_n = st.slider("Number of recommendations", 3, 10, 5)

if st.button("Recommend"):
    results = recommend(selected_title, df, cosine_sim, top_n=top_n)
    st.subheader("Recommended for you:")
    for r in results:
        st.write(f"- {r}")
