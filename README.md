# online-shopper-purchase-prediction
Machine Learning-based classification project that predicts online shopper purchase intention using customer browsing behavior. Includes data preprocessing, exploratory data analysis (EDA), feature engineering, model comparison, Random Forest classification, and Streamlit deployment for real-time prediction.

# Online Shopper Purchase Prediction using Machine Learning

# project Description

A Machine Learning classification project that predicts whether an online visitor will make a purchase based on browsing behavior and session characteristics. The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model comparison, Random Forest classification, and Streamlit deployment for real-time purchase prediction.

---

# Project Overview

Online businesses receive thousands of website visitors every day, but only a small percentage complete a purchase. Understanding customer purchase intention can help businesses optimize marketing strategies, improve customer engagement, and increase conversion rates.

This project uses Machine Learning techniques to predict whether a customer is likely to make a purchase based on their browsing behavior during an online shopping session.

The solution covers the complete Machine Learning lifecycle including data preprocessing, exploratory data analysis, feature selection, model training, evaluation, and deployment through a Streamlit web application.

---

# Problem Statement

E-commerce platforms struggle to identify potential buyers among website visitors.

The goal of this project is to build a predictive model that can classify customer sessions into:

- Purchase (Revenue = 1)
- No Purchase (Revenue = 0)

This enables businesses to:

- Improve marketing efficiency
- Increase conversion rates
- Personalize customer experiences
- Support data-driven decision making

---

# Business Objective

The project helps organizations:

* Identify high-value visitors

* Improve customer targeting

* Increase sales opportunities

* Reduce marketing costs

* Optimize conversion strategies

* Enhance customer engagement

---

# Dataset Information

Dataset: Online Shoppers Purchasing Intention Dataset

The dataset contains customer browsing and session information

### Key Features

- Administrative
- Administrative_Duration
- Informational
- Informational_Duration
- ProductRelated
- ProductRelated_Duration
- BounceRates
- ExitRates
- PageValues
- SpecialDay
- Month
- OperatingSystems
- Browser
- Region
- TrafficType
- VisitorType
- Weekend

### Target Variable

Revenue

- 1 → Customer Purchased
- 0 → Customer Did Not Purchase

---

# Project Workflow

## Phase 1: Problem Understanding

- Defined business problem
- Identified target variable
- Understood dataset structure
- Established project objectives

---

## Phase 2: Data Collection & Loading

- Imported dataset
- Loaded data into Pandas DataFrame
- Inspected rows and columns
- Reviewed data types

---

## Phase 3: Data Preprocessing

- Missing Value Check
- Duplicate Value Removal
- Data Type Verification
- Label Encoding
- Feature Selection

Encoded Features:

- Month
- VisitorType

---

## Phase 4: Exploratory Data Analysis (EDA)

Performed:

- Purchase Distribution
- Visitor Type Distribution
- Monthly Traffic Analysis
- Purchase vs Visitor Type
- Purchase vs Month
- Purchase vs Page Value

### Correlation Analysis

- Correlation Heatmap
- Feature Relationship Analysis

---

## Phase 5: Feature Engineering

Selected the most influential features:

- ProductRelated
- ProductRelated_Duration
- PageValues
- BounceRates
- ExitRates
- VisitorType
- Month
- Weekend

---

## Phase 6: Machine Learning Model Building

Implemented and compared multiple classification algorithms:

### 1. Logistic Regression

Linear classification model used as baseline.

### 2. Decision Tree Classifier

Rule-based classification model.

### 3. Random Forest Classifier

Ensemble learning algorithm using multiple decision trees.

### 4. Gradient Boosting Classifier

Boosting-based ensemble model.

### 5. XGBoost Classifier

Advanced boosting algorithm for classification tasks.

---

## Phase 7: Model Evaluation

Evaluation Metrics Used:

- Accuracy Score
- Precision Score
- Recall Score
- F1 Score
- ROC-AUC Score
- Confusion Matrix

---

## Phase 8: Hyperparameter Tuning

Optimized model performance using:

 - GridSearchCV
---

## Phase 9: Best Model Selection

After comparing all algorithms, Random Forest Classifier achieved the highest overall performance and was selected for deployment.

### Advantages

- Better generalization
- Reduced overfitting
- High prediction accuracy
- Strong feature importance interpretation

---

# Key Business Insights

* Customers who spend more time on product pages are significantly more likely to make a purchase.
* Returning visitors have a higher conversion rate than new visitors.
* PageValues strongly influence purchase decisions.
* High Bounce Rates negatively affect purchasing behavior.
* Product engagement is one of the strongest indicators of customer buying intention.

---

# Streamlit Web Application

An interactive Streamlit application was developed to provide real-time purchase predictions.

### User Inputs

- Product Pages Visited
- Product Page Duration
- Page Value
- Bounce Rate
- Exit Rate
- Visitor Type
- Month
- Weekend Visit

### Application Outputs

- Purchase Prediction
- Purchase Probability
- Customer Conversion Analysis
- Business Recommendations

---

# Technologies Used

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-Learn
- XGBoost

### Model Persistence

- Joblib

### Deployment

- Streamlit

### Development Environment

- Jupyter Notebook

---

# Future Enhancements

- Real-Time API Integration
- Cloud Deployment (AWS/Azure)
- Customer Segmentation Module
- Deep Learning Models
- Recommendation System
- Marketing Campaign Optimization

---

# Key Achievements

- Developed an end-to-end Machine Learning classification pipeline.
- Performed comprehensive exploratory data analysis and feature engineering.
- Compared multiple machine learning algorithms for performance evaluation.
- Selected Random Forest as the best-performing model.
- Built an interactive Streamlit application for real-time prediction.
- Generated actionable business insights from customer browsing behavior.
- Created a scalable solution for customer conversion prediction.
