# 🧠 HR Attrition Prediction

A Machine Learning-based web application that predicts employee attrition using classification models trained on real HR datasets. This end-to-end project integrates Data Science, Model Optimization, Visualization, and Full-Stack Web Development.

### 🔗 Live Demo
🚀 [HR Attrition Predictor App (Vercel Hosted)](https://hr-attrition-prediction-git-main-bhaumiks-projects-006c20ba.vercel.app/)

---

## 📁 Table of Contents

- [Project Overview](#-project-overview)
- [Tech Stack](#-tech-stack)
- [EDA & Feature Engineering](#-eda--feature-engineering)
- [Modeling Approach](#-modeling-approach)
- [Frontend Overview](#-frontend-overview)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [How to Run Locally](#-how-to-run-locally)
- [Author](#-author)

---

## 📌 Project Overview

This project predicts whether an employee is likely to **leave or stay** at a company based on HR factors such as job satisfaction, salary hike, distance from home, overtime, etc.  
The solution is built with:

- 🎯 Exploratory Data Analysis in **Jupyter Notebook**
- 🌲 Model training using **Random Forest Classifier**
- 📊 Business analytics via **Power BI Dashboard**
- 🌐 Interactive web frontend built with **HTML, CSS, JS**
- 🧪 Backend API using **Flask**, deployed on **Vercel**

---

## 🛠️ Tech Stack

| Layer          | Tools Used                                       |
|----------------|--------------------------------------------------|
| Language       | Python, HTML5, CSS3, JavaScript                  |
| ML Library     | `scikit-learn`, `pandas`, `numpy`                |
| Visualization  | `seaborn`, `matplotlib`, Power BI                |
| Web Framework  | Flask                                            |
| Deployment     | Vercel                                           |

---

## 📊 EDA & Feature Engineering

Performed in `EDA.ipynb`:
- Encoded categorical features using `LabelEncoder`
- Dropped non-impactful or constant columns like `Over18`, `StandardHours`, etc.
- Scaled and filtered attributes for optimal model performance
- Visualized feature correlation in segments using heatmaps
- Cross-validated the model performance for robustness

### Attributes Used in the Model:
```text
Age, BusinessTravel, DailyRate, Department, DistanceFromHome, Education,
EducationField, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement,
JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate,
NumCompaniesWorked, OverTime, PercentSalaryHike, RelationshipSatisfaction,
StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear,
WorkLifeBalance, YearsInCurrentRole, YearsSinceLastPromotion
```

## 🤖 Modeling Approach

- **Algorithm**: `RandomForestClassifier` from `scikit-learn`  
- **Hyperparameter Tuning**: `GridSearchCV`  
- **Model Evaluation**: Confusion Matrix, Cross-Validation, Accuracy Score  
- **Model Export**: Serialized using `pickle` into `model.pkl`  

✅ The model achieved **robust predictive performance** and **generalized well** across validation sets.

---

## 🖥️ Frontend Overview

The `index.html` serves as a user-friendly, interactive form:

- Fully **responsive** input form for employee attributes  
- **Clean modern UI** with animated prediction bars  
- **Dynamic result panel** showing confidence and outcome  
- **AJAX-based submission** to Flask's `/predict` route  

---

## 📈 Power BI Dashboard

- Built a **Power BI** dashboard to explore attrition metrics
- **Key Visuals**:
  - Department-wise attrition
  - Job Satisfaction impact
  - Monthly Income vs Attrition correlation

📌 *Note: Not publicly deployed but available on request or embeddable.*

---

## 🚀 Deployment

- **Backend**: Flask app deployed on **Vercel**
- **Routing**: Vercel serves `/` and `/predict` using `app.py`
- **Model Loading**: `model.pkl` is loaded once at startup
- **Frontend & Backend**: Served together for seamless UX

🌍 [Live App](https://hr-attrition-prediction-git-main-bhaumiks-projects-006c20ba.vercel.app/)

---

## 📦 Project Structure

├── app.py # Flask application
├── model.py # Model training and export
├── model.pkl # Trained ML model (pickled)
├── templates/
│ └── index.html # Frontend HTML page
├── static/ # (Optional) CSS/JS assets if separated
├── EDA.ipynb # Jupyter notebook for data analysis
├── requirements.txt # Python dependencies
└── README.md # You're here!

## 💡 How to Run Locally

1. **Clone the Repository**

   git clone (https://github.com/bhaumikmango/HR-Attrition-Prediction.git)
   cd HR-Attrition-Prediction

2. **Set up Virtual Environment**

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

3. **Install Dependencies**

pip install -r requirements.txt

4. **Run the App**

python app.py

5. **Open in Browser**

http://127.0.0.1:5000/

👨‍💻 Author -

Bhaumik Mango

💼 GitHub Profile (https://github.com/bhaumikmango)

🌐 Live Demo (https://hr-attrition-prediction-git-main-bhaumiks-projects-006c20ba.vercel.app/)

📊 Passionate about Data Science, ML Engineering, and Full-Stack Apps

📢 Acknowledgments-

📁 IBM HR Analytics Employee Attrition Dataset (https://www.ibm.com/analytics/data-science/predictive-analytics)

🧪 Scikit-learn (https://scikit-learn.org/)

🌍 Vercel for seamless hosting (https://vercel.com/)
 
💡 Inspired by real-world enterprise HR systems

##⭐ If you found this project helpful, feel free to give it a star!
