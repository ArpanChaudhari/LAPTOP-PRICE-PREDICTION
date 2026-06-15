# 💻 Laptop Price Prediction

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

A **Machine Learning web application** that predicts laptop prices based on hardware specifications and brand information. Built with **Streamlit** for an interactive UI and powered by a trained ML pipeline using **scikit-learn**.

---

## 🎯 Project Overview

Choosing the right laptop at the right price can be overwhelming with hundreds of configurations available in the market. This project solves that problem by predicting the price of a laptop based on its specifications using machine learning regression models.

### Key Features
- 🔮 **Real-time price prediction** based on user-selected specifications
- 🖥️ **Interactive web interface** built with Streamlit
- 📊 **Comprehensive EDA** with detailed visualizations
- 🧠 **Multiple ML models** evaluated for best performance
- 🔧 **Feature engineering** on raw hardware specifications

---

## 📁 Project Structure

```
Laptop-Price-Prediction/
│
├── ML PROJECT(148,151).ipynb   # Jupyter notebook with EDA, feature engineering & model training
├── app.py                      # Streamlit web application
├── laptop_data.csv             # Raw dataset (1,303 laptops × 12 features)
├── pipe.pkl                    # Trained ML pipeline (serialized model)
├── df.pkl                      # Processed dataframe for app dropdowns
├── pattern.py                  # Utility script
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

---

## 📊 Dataset

The dataset contains **1,303 laptop entries** with **12 features**:

| Feature | Description |
|---|---|
| `Company` | Laptop manufacturer (Dell, HP, Lenovo, etc.) |
| `TypeName` | Type of laptop (Notebook, Ultrabook, Gaming, etc.) |
| `Inches` | Screen size in inches |
| `ScreenResolution` | Screen resolution with display type info |
| `Cpu` | Processor details |
| `Ram` | RAM size |
| `Memory` | Storage type and capacity (HDD/SSD) |
| `Gpu` | Graphics card information |
| `OpSys` | Operating system |
| `Weight` | Laptop weight |
| `Price` | 💰 Target variable — Price in INR |

---

## 🧪 ML Models Evaluated

The following regression models were trained, evaluated, and compared using **R² Score** and **MAE (Mean Absolute Error)**:

| # | Model | R² Score | MAE | Remarks |
|---|---|---|---|---|
| 1 | **Random Forest** 🏆 | **0.8845** | **0.1637** | ✅ Best performer — used in deployment |
| 2 | Ridge Regression | 0.8536 | 0.1871 | L2 regularization (α=10) |
| 3 | Linear Regression | 0.8499 | 0.1875 | Baseline model |
| 4 | Lasso Regression | 0.8489 | 0.1890 | L1 regularization (α=0.001) |
| 5 | Decision Tree | 0.7954 | 0.2157 | max_depth=8 |
| 6 | KNN | 0.6609 | 0.2843 | k=3 neighbors |
| 7 | SVM (RBF) | 0.0562 | 0.2489 | Poor fit on this dataset |

> **Random Forest Regressor** achieved the highest R² score of **0.8845** with the lowest MAE of **0.1637**, making it the best model for this task. It was selected as the final model for deployment in the Streamlit app.

---

## 🔧 Feature Engineering

Significant feature engineering was performed on the raw data:

- **Screen Resolution** → Extracted `Touchscreen`, `IPS Panel`, `X_res`, `Y_res`, and computed **PPI** (Pixels Per Inch)
- **CPU** → Extracted and categorized CPU brand
- **Memory** → Parsed into separate `HDD` and `SSD` storage columns
- **GPU** → Extracted GPU brand
- **Operating System** → Simplified into major OS categories
- **Log Transformation** on target variable (`Price`) for better model performance

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.8+ installed.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ArpanChaudhari/LAPTOP-PRICE-PREDICTION.git
   cd LAPTOP-PRICE-PREDICTION
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit scikit-learn numpy pandas seaborn matplotlib
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   
   The app will automatically open at `http://localhost:8501`

---

## 🖥️ How to Use

1. Select the **Brand** of the laptop
2. Choose the **Type** (Notebook, Ultrabook, Gaming, etc.)
3. Select **RAM**, **HDD**, **SSD** sizes
4. Enter the **Weight** of the laptop
5. Choose **Touchscreen** and **IPS** display options
6. Adjust the **Screen Size** slider
7. Select **Screen Resolution**, **CPU**, **GPU**, and **OS**
8. Click **"Predict Price"** to get the estimated price! 🎉

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Frontend:** Streamlit
- **ML Libraries:** scikit-learn, NumPy, Pandas
- **Visualization:** Seaborn, Matplotlib
- **Serialization:** Pickle

---

## 📈 Future Improvements

- [ ] Add more laptop data for better predictions
- [ ] Deploy on cloud (Heroku / Streamlit Cloud / AWS)
- [ ] Add model comparison metrics in the UI
- [ ] Implement hyperparameter tuning with GridSearchCV
- [ ] Add price trend analysis over time

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available for educational and personal use.

---

## 👨‍💻 Author

**Arpan Chaudhari**

[![GitHub](https://img.shields.io/badge/GitHub-ArpanChaudhari-181717?style=flat-square&logo=github)](https://github.com/ArpanChaudhari)

---

<p align="center">⭐ If you found this project helpful, please give it a star!</p>
