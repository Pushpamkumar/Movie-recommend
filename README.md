# 🎬 Movie Recommender System Using Machine Learning

A **Movie Recommender System** that suggests movies based on user preferences using **Machine Learning** techniques such as **Cosine Similarity**.
The project uses **content-based**, **collaborative**, and **hybrid filtering** approaches to recommend movies effectively.

---

## 🧠 Workflow & Motivation

In today’s fast-paced world, users are often overwhelmed by choices — whether it’s movies, music, or online content.
**Recommendation systems** solve this problem by automatically suggesting relevant items based on the user's interests and behavior.

This system is built using **Machine Learning algorithms** that analyze movie metadata and compute similarity between films to generate personalized recommendations.

---

## ⚙️ Types of Recommendation Systems

### 1️⃣ Content-Based Filtering

* Uses item attributes (like genre, cast, director, etc.) to recommend similar movies.
* Example: YouTube, Twitter.
* Works by creating **feature embeddings** for items and finding similar vectors.
* Drawback: Tends to overfit user preferences (“narrow recommendations”).

### 2️⃣ Collaborative Filtering

* Based on **user-item interactions** such as ratings and reviews.
* Identifies clusters of users with similar preferences.
* Example: Amazon, Netflix.
* Drawback: Struggles with **new users/items** and can be computationally expensive due to large matrices.

### 3️⃣ Hybrid Filtering

* Combines both Content-Based and Collaborative methods.
* Reduces limitations of individual systems.
* Uses techniques like **Word2Vec** or **embedding-based similarity**.
* Modern systems (like Spotify and Netflix) rely on this hybrid approach.

---

## 📊 Dataset

* **Source:** [Kaggle Movie Dataset](https://www.kaggle.com/)
* **Purpose:** Train the recommender model.
* **Model Generation:** The system uses `cosine_similarity` to compute similarity between movie vectors.

### 🧩 Concept Used: Cosine Similarity

Cosine similarity measures how similar two movies are based on their feature vectors.

```
cosine_similarity(A, B) = (A · B) / (||A|| * ||B||)
```

* Value ranges between **0 and 1**
* `1` → Movies are identical
* `0` → Movies are completely dissimilar

For more: [Learn DataSci - Cosine Similarity](https://www.learndatasci.com/glossary/cosine-similarity/)

---

## 🖥️ Installation & Setup Guide

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Pushpamkumar/Movie-recommend.git
cd Movie-recommend
```

### 2️⃣ Create a Virtual Environment

Using **conda**:

```bash
conda create -n movie python=3.7.10 -y
conda activate movie
```

Or using **venv**:

```bash
python -m venv .venv
source .venv/bin/activate   # for Linux/Mac
.venv\Scripts\activate      # for Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Generate Model Files

Run the notebook to generate similarity data and models:

```bash
jupyter notebook "Movie Recommender System Data Analysis.ipynb"
```

### 5️⃣ Launch the Web App

Once models are ready:

```bash
streamlit run app.py
```

The app will open in your browser at
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 🧩 Key Files

| File                                           | Description                                 |
| ---------------------------------------------- | ------------------------------------------- |
| `app.py`                                       | Streamlit frontend for movie recommendation |
| `Movie Recommender System Data Analysis.ipynb` | Model training & feature engineering        |
| `movie_dict.pkl`, `similarity.pkl`             | Precomputed data for faster recommendations |
| `requirements.txt`                             | Python dependencies list                    |

---

## 🚧 Issues Faced & Debugging Journey

### ❌ Problem 1: SSL Connection Error

While fetching movie posters via TMDB API, I faced this error:

```
requests.exceptions.SSLError: EOF occurred in violation of protocol (_ssl.c:1129)
```

**Cause:**
The SSL certificate verification was failing in my local environment due to outdated CA bundles.

**Fix:**

1. Verified SSL path using:

   ```bash
   python -m certifi
   ```
2. Updated the request code to use:

   ```python
   data = requests.get(url, verify=certifi.where(), timeout=10)
   ```
3. Added fallback to retry with `verify=False` if SSL failed.
4. Installed latest certificates:

   ```bash
   pip install --upgrade certifi
   ```

✅ **Result:** Posters started loading correctly and the app fetched TMDB data securely.
---

## 🧾 Output Preview

The web app allows users to:

* Search for a movie 🎥
* View similar movies with posters 🖼️
* Get clean recommendations using the trained ML model ⚡

---

## 💡 Future Enhancements

* Add **user authentication** to personalize recommendations.
* Integrate **sentiment analysis** for reviews.
* Deploy using **Streamlit Cloud** or **AWS EC2**.
* Switch from static `.pkl` models to a real-time API-based system.

---

## 🧑‍💻 Author

**Pushpam Kumar**
🎓 B.Tech CSE | Data Science & AI Enthusiast
📍 Lovely professional University | Punjab
🔗 [GitHub Profile](https://github.com/Pushpamkumar)

---

✨ *“Movies recommend stories; we recommend movies.”*

<img width="1848" height="364" alt="image" src="https://github.com/user-attachments/assets/e0f68943-a58a-43ff-9aa3-6b215cd520e3" />



<img width="1851" height="764" alt="image" src="https://github.com/user-attachments/assets/e689ee52-e698-457c-a842-6e8178cfe658" />

