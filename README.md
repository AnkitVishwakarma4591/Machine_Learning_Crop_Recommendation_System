# 🌾 Crop Recommendation System

## 📘 Project Overview
The **Crop Recommendation System** uses **Machine Learning** to suggest the most suitable crop for cultivation based on soil and environmental conditions such as Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, and rainfall.  
It helps farmers and agricultural planners make data-driven decisions to maximize yield and resource efficiency.

---

## 🚀 Features
- Accepts 7 environmental and soil input features.  
- Predicts the best crop using trained ML models.  
- Built using **Streamlit** for an interactive and user-friendly web interface.  
- Supports multiple algorithms like:
- Random Forest Classifier 🌲  
- Gradient Boosting Classifier 🌿  
- XGBoost Classifier ⚡

---

## 🧠 Technologies Used
- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**
- **XGBoost**
- **Streamlit**
- **Joblib** (for model serialization)

---

## 📊 Dataset
The dataset used contains 2200 samples with the following features:

| Column | Description |
|---------|--------------|
| N | Nitrogen content in soil |
| P | Phosphorus content in soil |
| K | Potassium content in soil |
| Temperature | Ambient temperature (°C) |
| Humidity | Relative humidity (%) |
| pH | Soil pH value |
| Rainfall | Rainfall (mm) |
| Label | Target crop name |

---

## ⚙️ How to Run

1. **Clone this repository**
```bash
   git clone https://github.com/AnkitVishwakarma4591/Machine-Learning-Crop_Recommendation_System.git
````

2. **Navigate to the project directory**

   ```bash
   cd Machine-Learning-Crop_Recommendation_System
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

5. **Enter values** for N, P, K, temperature, humidity, pH, and rainfall →
   The system will predict the most suitable crop.

---

## 🧩 Model Training

1. The dataset is scaled using **StandardScaler**.
2. The target variable (`label`) is encoded using **LabelEncoder**.
3. Models such as RandomForest, GradientBoosting, and XGBoost are trained.
4. The best-performing model is saved using **Joblib** as `disease_model.pkl`.

---

## 📈 Example Prediction

| N  | P  | K  | Temp | Humidity | pH  | Rainfall | Predicted Crop |
| -- | -- | -- | ---- | -------- | --- | -------- | -------------- |
| 90 | 42 | 43 | 21.5 | 80.2     | 6.4 | 202.9    | rice           |

---

## 👨‍💻 Developer Information

**📧 Email:** [ankitvishwakarma4591@gmail.com](mailto:ankitvishwakarma4591@gmail.com)<br>
**📞 Phone:** 9060782203<br>
**🔗 LinkedIn:** [Ankit Vishwakarma](https://www.linkedin.com/in/ankit-vishwakarma-324baa2a6/)<br>
**Portfolio:** [Ankit's Portfolio](https://ankit-portfolio-7d8377.netlify.app/)

---

### 🌟 “Empowering farmers through data-driven crop intelligence.”

```
