# HR Analytics Dashboard with Employee Attrition Prediction

## Project Overview

The HR Analytics Dashboard project focuses on analyzing employee data to identify factors contributing to employee attrition. The project uses Python for data analysis and visualization, Power BI for dashboard creation, and Machine Learning for attrition prediction.

The objective is to help HR departments make data-driven decisions to improve employee retention and workforce management.

---

## Business Problem

Employee attrition is a major challenge for organizations as it increases recruitment costs, training expenses, and productivity loss.

This project aims to:

- Analyze employee demographics and workforce trends.
- Identify factors influencing attrition.
- Visualize HR metrics using interactive dashboards.
- Build a machine learning model to predict employee attrition.

---

## Dataset Information

Dataset: IBM HR Analytics Employee Attrition Dataset

### Dataset Summary

- Total Employees: 1470
- Total Features: 35
- Numerical Features: 26
- Categorical Features: 9
- Missing Values: 0

---

## Technology Stack

### Programming & Analysis

- Python
- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-Learn

### Dashboarding

- Power BI

### Version Control

- Git
- GitHub

---

## Project Structure

```text
HR_Analytics_Dashboard
│
├── dataset
│   └── HR_Analytics.csv
│
├── notebooks
│   └── hr_analysis.py
│
├── images
│
├── model
│
├── powerbi
│
├── sql
│
├── README.md
│
└── requirements.txt
```

---

# Exploratory Data Analysis (EDA)

## 1. Employee Attrition Distribution

### Objective

Analyze the overall attrition trend within the organization.

### Key Findings

- Total Employees: 1470
- Employees Retained: 1233
- Employees Left: 237
- Attrition Rate: 16.12%
- Retention Rate: 83.88%

### Business Insight

Approximately 1 out of every 6 employees leaves the organization. HR teams should focus on identifying the key drivers behind employee turnover.

### Visualization

![Attrition Distribution](images/.png)

---

## 2. Department-wise Attrition Analysis

### Objective

Identify departments with the highest employee turnover.

### Key Findings

- Research & Development has the largest workforce.
- Research & Development and Sales departments contribute the highest number of attrition cases.
- Human Resources has the lowest workforce and lowest attrition count.

### Business Insight

Departments with higher attrition require focused retention strategies and employee engagement programs.

### Visualization

![Department Attrition](images/Department_Wise_Attrition.png)

---

## 3. Gender-wise Attrition Analysis

### Objective

Analyze attrition trends across gender groups.

### Business Insight

Understanding gender-based attrition patterns helps organizations build inclusive workplace policies and improve retention strategies.

### Visualization

![Gender Attrition](images/gender_attrition.png)

---

## 4. Overtime vs Attrition Analysis

### Objective

Determine whether overtime impacts employee turnover.

### Key Findings

- Employees working overtime show significantly higher attrition rates.
- Work-life balance plays an important role in employee retention.

### Business Insight

Reducing excessive overtime may improve employee satisfaction and lower attrition.

### Visualization

![Overtime Attrition](images/overtime_attrition.png)

---

## 5. Age Distribution Analysis

### Objective

Understand workforce age demographics.

### Business Insight

Age distribution helps HR teams design targeted employee development and retention programs.

### Visualization

![Age Distribution](images/age_distribution.png)

---

## 6. Salary Distribution Analysis

### Objective

Analyze employee income patterns.

### Business Insight

Salary distribution analysis helps determine whether compensation influences employee turnover.

### Visualization

![Salary Distribution](images/salary_distribution.png)

---

## 7. Salary vs Attrition Analysis

### Objective

Evaluate the relationship between salary and employee attrition.

### Business Insight

Lower compensation levels may contribute to higher attrition rates among employees.

### Visualization

![Salary vs Attrition](images/salary_vs_attrition.png)

---

## 8. Job Satisfaction Analysis

### Objective

Analyze employee satisfaction levels.

### Business Insight

Employees with lower satisfaction scores are more likely to leave the organization.

### Visualization

![Job Satisfaction](images/job_satisfaction.png)

---

## 9. Work Experience Analysis

### Objective

Analyze employee tenure and experience.

### Business Insight

Employee retention tends to vary across different experience levels.

### Visualization

![Years At Company](images/years_at_company.png)

---

# Machine Learning Model

## Objective

Predict whether an employee is likely to leave the organization.

### Algorithms Used

- Logistic Regression
- Random Forest Classifier

### Workflow

1. Data Cleaning
2. Data Preprocessing
3. Label Encoding
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Feature Importance Analysis

---

## Model Performance

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Feature Importance

Top factors influencing employee attrition:

- OverTime
- MonthlyIncome
- Age
- JobRole
- YearsAtCompany
- JobSatisfaction
- WorkLifeBalance

### Visualization

![Feature Importance](images/feature_importance.png)

---

# Power BI Dashboard

The Power BI dashboard consists of three main pages:

## Dashboard 1: Executive Summary

### KPI Cards

- Total Employees
- Attrition Rate
- Employees Left
- Average Age
- Average Salary

---

## Dashboard 2: Attrition Analysis

### Visualizations

- Department-wise Attrition
- Gender-wise Attrition
- Overtime vs Attrition
- Job Role vs Attrition
- Education Field vs Attrition

---

## Dashboard 3: Employee Insights

### Visualizations

- Age Distribution
- Salary Distribution
- Job Satisfaction
- Years at Company
- Work-Life Balance

---

# Key Business Recommendations

- Reduce excessive overtime to improve employee retention.
- Conduct employee satisfaction surveys regularly.
- Improve career growth opportunities in high-attrition departments.
- Develop department-specific retention strategies.
- Enhance work-life balance initiatives.

---

# Conclusion

This project demonstrates how data analytics and machine learning can be used to understand workforce behavior and predict employee attrition. The insights generated through Python, Power BI, and machine learning models can help organizations improve employee retention and optimize HR decision-making.

---

## Author

**Yashika Garg**

B.E. CSE (AI & ML)

Chitkara University"# IBM-HR-Analytics-Employee-Attrition-Performance" 
