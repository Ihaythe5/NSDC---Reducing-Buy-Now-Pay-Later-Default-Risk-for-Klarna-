"""'
Klarna Visualizations for BNPL Credit Risk Analysis
Author: Isaiah Haythe 

Notes: 

This is the code that provides visualizations for the default risk charts 
for our project. It includes bar charts for default rates by risk segment, employment type, and 
credit score range, as well as a bar chart for average repayment delay by default status. 
Make sure to adjust the file path when loading the dataset. Make sure Matplotlib & Pandas are
also installed.

"""
import pandas as pd
import matplotlib.pyplot as plt






# Load data (You might have to change your file path)
df = pd.read_csv("/Buy_Now_Pay_Later_BNPL_CreditRisk_Dataset.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Create Default Flag
df["Default_Flag"] = df["default_flag"]

# -------------------------------
# Default Rate by Risk Segment
# -------------------------------
default_by_risk = df.groupby("customer_segment")["Default_Flag"].mean()

plt.figure()
default_by_risk.plot(kind="bar")
plt.title("Default Rate by Risk Segment")
plt.xlabel("Risk Segment")
plt.ylabel("Default Rate")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# -----------------------------------
#  Default Rate by Employment Type
# -----------------------------------
default_by_employment = df.groupby("employment_type")["Default_Flag"].mean()

plt.figure()
default_by_employment.plot(kind="bar")
plt.title("Default Rate by Employment Type")
plt.xlabel("Employment Type")
plt.ylabel("Default Rate")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# -----------------------------------
#  Default Rate by Credit Score Range
# -----------------------------------
def credit_bin(score):
    if score < 580:
        return "Poor"
    elif score < 670:
        return "Fair"
    elif score < 740:
        return "Good"
    else:
        return "Excellent"

df["Credit Score Range"] = df["credit_score"].apply(credit_bin)

default_by_credit = df.groupby("Credit Score Range")["Default_Flag"].mean()

plt.figure()
default_by_credit.plot(kind="bar")
plt.title("Default Rate by Credit Score Range")
plt.xlabel("Credit Score Range")
plt.ylabel("Default Rate")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# ---------------------------------------
#  Avg Repayment Delay by Default Status
# ---------------------------------------
avg_delay = df.groupby("default_flag")["repayment_delay_days"].mean()

plt.figure()
avg_delay.plot(kind="bar")
plt.title("Average Repayment Delay by Default Status")
plt.xlabel("Default Status")
plt.ylabel("Avg Repayment Delay (Days)")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()