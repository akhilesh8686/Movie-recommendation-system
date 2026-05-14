# 🎬 Movie Recommendation System

A content-based movie recommendation web app built with **Python**, **Flask**, and **Machine Learning**. Select any movie and instantly get **5 similar movie recommendations** powered by cosine similarity.

---

## 🚀 Live Demo

> Run locally by following the setup steps below.

---

## 📸 Screenshot

><img width="1208" height="567" alt="image" src="https://github.com/user-attachments/assets/bf0354ef-1945-44e7-9fe2-048067aeba1f" />


---

## 🧠 How It Works

1. The model is trained on the **TMDB Movies Dataset**
2. Movie features (genres, keywords, cast, crew, overview) are combined and vectorized using **CountVectorizer**
3. **Cosine Similarity** is computed between all movie vectors
4. When a user selects a movie, the app finds the top 5 closest matches in the similarity matrix and returns them as recommendations

---

## 🛠️ Tech Stack

| Layer       | Technology                        |
|-------------|-----------------------------------|
| Backend     | Python, Flask                     |
| ML / Data   | Pandas, Scikit-learn, NumPy       |
| Serialization | Pickle                          |
| Frontend    | HTML, CSS, JavaScript             |
| Dataset     | TMDB 5000 Movies Dataset          |

---

## 📁 Project Structure

```
movie-recommender-system/
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend UI
├── movies_dict.pkl         # ⚠️ Not included (see Setup)
├── similarity.pkl          # ⚠️ Not included (see Setup)
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/akhilesh8686/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download model files
The `.pkl` files are too large for GitHub. Download them from the link below and place them in the **root folder** of the project:

📦 **[Download movies_dict.pkl & similarity.pkl](#)**
> *(Replace `#` with your Google Drive link)*

### 4. Run the app
```bash
python app.py
```

### 5. Open in browser
```
http://127.0.0.1:5000
```

---

## ✨ Features

- 🔍 Search and select from **thousands of movies**
- ⚡ Instant recommendations — no page reload
- 🎨 Clean, cinematic dark-themed UI
- 📱 Responsive design

---

## 📊 Dataset

- **Source:** [TMDB 5000 Movie Dataset — Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Contains movie metadata: title, genres, keywords, cast, crew, and overview

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Akhilesh**
- GitHub: [@akhilesh8686](https://github.com/akhilesh8686)
