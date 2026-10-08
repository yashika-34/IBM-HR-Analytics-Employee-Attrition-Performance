from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "dataset" / "HR_Analytics.csv"
IMAGES_PATH = PROJECT_ROOT / "images"


def load_data():
    df = pd.read_csv(DATA_PATH)
    return df


def save_plot(fig, filename):
    IMAGES_PATH.mkdir(exist_ok=True)
    output_path = IMAGES_PATH / filename
    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)
    return output_path


def attrition_summary(df):
    total = len(df)
    retained = (df["Attrition"] == "No").sum()
    left = (df["Attrition"] == "Yes").sum()
    rate = (left / total) * 100

    summary = {
        "Total Employees": total,
        "Employees Retained": retained,
        "Employees Left": left,
        "Attrition Rate (%)": round(rate, 2),
    }
    print("\n=== HR Attrition Summary ===")
    for key, value in summary.items():
        print(f"{key}: {value}")
    return summary


def attrition_by_department(df):
    grouped = (
        df.groupby("Department")["Attrition"]
        .apply(lambda s: (s == "Yes").mean() * 100)
        .sort_values(ascending=False)
        .reset_index(name="AttritionRate")
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=grouped, x="AttritionRate", y="Department", hue="Department", dodge=False, palette="viridis", ax=ax)
    ax.set_title("Attrition Rate by Department")
    legend = ax.get_legend()
    if legend is not None:
        legend.remove()
    ax.set_xlabel("Attrition Rate (%)")
    ax.set_ylabel("Department")
    save_plot(fig, "department_attrition_rate.png")
    print("\nDepartment-wise attrition rate:")
    print(grouped.to_string(index=False))


def attrition_by_role(df):
    grouped = (
        df.groupby("JobRole")["Attrition"]
        .apply(lambda s: (s == "Yes").mean() * 100)
        .sort_values(ascending=False)
        .reset_index(name="AttritionRate")
    )
    fig, ax = plt.subplots(figsize=(11, 7))
    sns.barplot(data=grouped, x="AttritionRate", y="JobRole", hue="JobRole", dodge=False, palette="magma", ax=ax)
    ax.set_title("Attrition Rate by Job Role")
    legend = ax.get_legend()
    if legend is not None:
        legend.remove()
    ax.set_xlabel("Attrition Rate (%)")
    ax.set_ylabel("Job Role")
    save_plot(fig, "job_role_attrition_rate.png")
    print("\nJob role attrition rate:")
    print(grouped.to_string(index=False))


def overtime_analysis(df):
    overtime = (
        df.groupby("OverTime")["Attrition"]
        .apply(lambda s: (s == "Yes").mean() * 100)
        .reset_index(name="AttritionRate")
    )
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.barplot(data=overtime, x="OverTime", y="AttritionRate", hue="OverTime", dodge=False, palette=["#45aaf2", "#f39c12"], ax=ax)
    ax.set_title("Overtime vs Attrition Rate")
    legend = ax.get_legend()
    if legend is not None:
        legend.remove()
    ax.set_xlabel("OverTime")
    ax.set_ylabel("Attrition Rate (%)")
    save_plot(fig, "overtime_attrition_rate.png")
    print("\nOvertime impact:")
    print(overtime.to_string(index=False))


def tenure_analysis(df):
    df_copy = df.copy()
    bins = [0, 2, 5, 10, 15, 20, 40]
    labels = ["0-2", "3-5", "6-10", "11-15", "16-20", "20+"]
    df_copy["TenureBand"] = pd.cut(df_copy["YearsAtCompany"], bins=bins, labels=labels, right=True)
    grouped = (
        df_copy.groupby("TenureBand")["Attrition"]
        .apply(lambda s: (s == "Yes").mean() * 100)
        .reset_index(name="AttritionRate")
    )
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(data=grouped, x="TenureBand", y="AttritionRate", hue="TenureBand", dodge=False, palette="coolwarm", ax=ax)
    ax.set_title("Attrition Rate by Years at Company")
    legend = ax.get_legend()
    if legend is not None:
        legend.remove()
    ax.set_xlabel("Years at Company")
    ax.set_ylabel("Attrition Rate (%)")
    save_plot(fig, "tenure_attrition_rate.png")
    print("\nAttrition by tenure band:")
    print(grouped.to_string(index=False))


def salary_vs_attrition(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=df, x="Attrition", y="MonthlyIncome", hue="Attrition", dodge=False, palette=["#2ecc71", "#e74c3c"], ax=ax)
    ax.set_title("Monthly Income vs Attrition")
    legend = ax.get_legend()
    if legend is not None:
        legend.remove()
    ax.set_xlabel("Attrition")
    ax.set_ylabel("Monthly Income")
    save_plot(fig, "salary_vs_attrition.png")
    print("\nAverage monthly income by attrition:")
    print(df.groupby("Attrition")["MonthlyIncome"].mean().round(2).to_string())


def satisfaction_analysis(df):
    metrics = ["JobSatisfaction", "EnvironmentSatisfaction", "WorkLifeBalance"]
    summary = df.groupby("Attrition")[metrics].mean().round(2)
    fig, ax = plt.subplots(figsize=(8, 6))
    summary.T.plot(kind="bar", ax=ax)
    ax.set_title("Average Satisfaction Metrics by Attrition")
    ax.set_ylabel("Average Score")
    ax.set_xlabel("Metric")
    ax.legend(title="Attrition")
    save_plot(fig, "satisfaction_by_attrition.png")
    print("\nSatisfaction trends by attrition:")
    print(summary.to_string())


def main():
    sns.set_style("whitegrid")
    df = load_data()
    print("HR Analytics Project Started Successfully!")
    attrition_summary(df)
    attrition_by_department(df)
    attrition_by_role(df)
    overtime_analysis(df)
    tenure_analysis(df)
    salary_vs_attrition(df)
    satisfaction_analysis(df)
    print("\nAll HR analysis charts were saved to the images folder.")


if __name__ == "__main__":
    main()
