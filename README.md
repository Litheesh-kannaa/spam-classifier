# Spam Classifier

Spam Email Classifier — a machine learning-based web app to classify email text as **Spam** or **Not Spam** using Python, Scikit-learn, Flask, and a simple HTML interface.

---

## 🚀 Features

- ✉️ Classifies input email text as Spam or Not Spam  
- 🤖 Trained using Multinomial Naive Bayes and CountVectorizer  
- 📊 Based on a labeled dataset (`spam.csv`)  
- 🌐 Simple frontend using HTML, CSS, and JavaScript  
- ⚙️ Real-time predictions through a Flask backend  

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, Flask  
- **ML Libraries:** Scikit-learn, Pandas  
- **Model:** Multinomial Naive Bayes  
- **Data:** Preprocessed spam dataset (`spam.csv`)

---

## 📁 Project Structure

```bash
Spam_Classifier_Project/
├── model/                # Model + vectorizer files
│   ├── spam_classifier.pkl
│   └── vectorizer.pkl
├── server.py             # Flask backend
├── spam.csv              # Dataset
├── requirements.txt      # Python dependencies
└── ui/                   # Frontend files (HTML, CSS, JS)
```
🧪 Setup Instructions
1. Clone the repo:
bash
Copy
Edit
git clone https://github.com/Litheesh-kannaa/spam-classifier.git
cd spam-classifier
2. Create virtual environment & install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
3. Train the model:
bash
Copy
Edit
cd model
python spam_classifier.py
4. Run the Flask server:
bash
Copy
Edit
cd ..
python server.py
Server will start at: http://localhost:8000

5. Open the frontend:
bash
Copy
Edit
cd ui
python -m http.server 8080
Open browser at: http://localhost:8080

💻 How to Use
Paste any email content into the input box.

Click Classify.

You'll get an immediate response:

"This is a spam email."

"This is not a spam email."

⚠️ Limitations
❌ No actual email service integration (e.g., Gmail API)

📊 Dataset is small (for learning/demo purposes)

💡 Can be improved with more preprocessing and larger data

🔧 UI is basic (no JS framework used)

👤 Author
Litheesh Kannaa (GitHub: @litheesh-kannaa)

