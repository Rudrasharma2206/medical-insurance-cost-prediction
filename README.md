# 🏥 Medical Insurance Cost Predictor

A machine learning web application that predicts medical insurance charges based on personal health and demographic factors.

🔗 **Live Demo:** http://localhost:8501

---

## 📸 Screenshots

> Add screenshots of your Streamlit app here after deployment

---

## 📌 Problem Statement

Medical insurance costs vary significantly based on factors like age, BMI, smoking habits, and region. This project builds a machine learning model to **predict insurance charges** based on these factors, helping individuals estimate their medical expenses.

---

## 🗂️ Dataset

- **Source:** [Kaggle - Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Size:** 1338 rows × 7 columns
- **Features:**

| Feature | Type | Description |
|---------|------|-------------|
| age | Numerical | Age of the person |
| sex | Categorical | male / female |
| bmi | Numerical | Body Mass Index |
| children | Numerical | Number of dependents |
| smoker | Categorical | yes / no |
| region | Categorical | northeast / northwest / southeast / southwest |
| charges | Numerical | 🎯 Target — Medical insurance cost |

---

## 🧠 ML Models Used

| Model | R² Score |
|-------|----------|
| Linear Regression | ~0.74 |
| Gradient Boosting Regressor | ~0.89 |
| Random Forest Regressor | ~0.87 |

> ✅ **Gradient Boosting Regressor** was selected as the final model based on best R² score.

---

## 📊 Key Insights from EDA

- 🚬 **Smokers** pay **3-4x more** than non-smokers
- 📈 **BMI above 30** significantly increases charges
- 👴 **Age** has a strong positive correlation with cost
- 🌍 **Region** has minimal impact on charges

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **ML Libraries:** Scikit-learn, Pandas, NumPy
- **Web App:** Streamlit
- **Visualization:** Matplotlib, Seaborn
- **Model Saving:** Pickle

---

## 📁 Project Structure

```
medical-insurance-cost-prediction/
│
├── data/
│   └── insurance.csv          # Dataset
│
├── cost-predictor.ipynb       # ML notebook (EDA + model training)
├── app.py                     # Streamlit web app
├── requirements.txt           # Dependencies
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Rudrasharma2206/medical-insurance-cost-prediction.git
cd medical-insurance-cost-prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```

### 4. Open in browser
```
http://localhost:8501
```

---

## 📦 Requirements

```
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
```

---

## 🔮 Future Improvements

- [ ] Deploy on Streamlit Cloud
- [ ] Add more ML models (XGBoost, CatBoost)
- [ ] Add SHAP values for model explainability
- [ ] Add interactive EDA charts in the web app
- [ ] Collect real-world insurance data

---

## 👤 Author

**Rudra Sharma**
- GitHub: [@Rudrasharma2206](https://github.com/Rudrasharma2206)
- LinkedIn: [Add your LinkedIn here]

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
