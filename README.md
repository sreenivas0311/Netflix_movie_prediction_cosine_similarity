📦 Model Artifacts & File Size Note

        Due to GitHub’s 100 MB file size limit, the trained model artifacts could not be uploaded to this repository.
        
        The following files were generated during development and are required to run the Streamlit app:
        
        df_cleaned.pkl
        
        tfidf.pkl
        
        cosine_sim.pkl
        
        How to Obtain These Files
        
        Run the Jupyter Notebook provided in the notebook/ folder
        
        The notebook includes code to generate and save all required .pkl files locally
        
        Place the generated files inside the app/ directory before running the app
        
        This approach avoids large file uploads while keeping the repository lightweight and reproducible.

🎬 Netflix Content Recommendation System
📌 Project Overview
    
    This project builds a content-based recommendation system using Netflix movies and TV shows data (Flixable – 2019).
    
    The goal is to recommend similar content based on textual similarity (story, genre, cast) when user interaction data is not available.
    
    The system uses Natural Language Processing (NLP) techniques and unsupervised machine learning to suggest relevant titles.

📊 Dataset Information

    Source: Flixable (Third-party Netflix catalog)
    
    Timeframe: Netflix content available up to 2019
    
    Content Types: Movies & TV Shows
    
    Total Records: ~7,800 titles

🔑 Key Columns Used

      title
      
      description
      
      listed_in (genres)
      
      cast
      
      type
      
      release_year
      
      rating
      
      duration

🎯 Problem Statement

    Netflix-style platforms need to recommend content even when:
    
    ❌ No user ratings exist
    
    ❌ No watch history is available (cold start problem)
    
    This project solves that by building a content-based recommender, which relies purely on item attributes, not users.
    
    🧠 Approach & Methodology
1️⃣ Data Cleaning & Preparation

    Removed non-informative columns (show_id, director)
    
    Handled missing values (country, rating)
    
    Converted date_added to datetime
    
    Extracted numeric values from duration
    
    Created rating groups (Kids / Teens / Adults)

2️⃣ Exploratory Data Analysis (Minimal)

    Movies vs TV Shows distribution
    
    Content growth over years
    
    Rating & duration patterns
    
    Country and genre distribution
    
    EDA was kept minimal since the primary goal is recommendation modeling.

3️⃣ Feature Engineering

    Combined text fields into a single column:
    
    content_text = title + description + listed_in + cast
    
    
    This represents each title as a single document.

4️⃣ Text Vectorization (NLP)

    Applied TF-IDF Vectorization
    
    Removed stopwords
    
    Limited feature size for efficiency

5️⃣ Similarity Computation

    Used Cosine Similarity
    
    Compared each title with every other title
    
    Generated a similarity matrix (N × N)

6️⃣ Recommendation Logic

      User selects a title
      
      System finds the most similar titles
      
      Returns top-N recommendations
      
      This forms a content-based recommendation model.

🤖 Machine Learning Used

    Type: Unsupervised Machine Learning
    
    Techniques:
    
    TF-IDF Vectorization
    
    Cosine Similarity
    
    Model Type: Content-Based Recommendation Model
    
    No supervised learning was used due to lack of user-level labels.

🚀 Deployment

  The system is deployed as a Streamlit web application.

✨ Deployment Highlights

    🔍 Auto-suggest searchable dropdown (Google-like)
    
    🚫 Prevents invalid movie inputs
    
    ⚡ Real-time recommendations
    
    🪶 Lightweight & fast
    
    📦 Saved Artifacts
    
    df_cleaned.pkl
    
    tfidf.pkl
    
    cosine_sim.pkl
    
    These are loaded directly during deployment (no retraining in production).

🛠️ Tech Stack
    
    Python
    
    Pandas
    
    NumPy
    
    Scikit-learn
    
    Streamlit
    
    Pickle

📂 Project Structure
project/

│

├── notebook/

│   └── netflix_recommender.ipynb

│

├── app/

│   ├── app.py

│   ├── df_cleaned.pkl

│   ├── tfidf.pkl

│   ├── cosine_sim.pkl

│   └── requirements.txt

│

└── README.md

▶️ How to Run Locally
pip install -r requirements.txt
streamlit run app.py

📌 Key Takeaways

    Built an end-to-end content-based recommender
    
    Solved the cold start problem
    
    Used NLP + ML in a production-style pipeline
    
    Demonstrated model building, persistence, and deployment

🔮 Future Enhancements

    K-Means clustering for content segmentation
    
    Hybrid recommendation (content + collaborative)
    
    User-based filtering (age, country, release year)
    
    Evaluation metrics with user feedback data

📄 License

This project is for educational and demonstration purposes.
