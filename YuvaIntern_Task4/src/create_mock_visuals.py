"""Create illustrative Task 4 presentation visuals.
These values are mock examples only and must not be represented as real results.
"""
import matplotlib.pyplot as plt

segments=["Month-to-month","One-year","Two-year"]
illustrative=[32,18,9]

plt.figure(figsize=(8,5))
plt.bar(segments,illustrative)
plt.ylabel("Illustrative churn rate (%)")
plt.title("Illustrative Churn Rate by Contract Type")
plt.tight_layout()
plt.savefig("diagrams/illustrative_churn_by_contract.png",dpi=160)
plt.close()

tenure=[3,9,18,30,42,54]
risk=[35,29,23,17,13,10]
plt.figure(figsize=(8,5))
plt.plot(tenure,risk,marker="o")
plt.xlabel("Illustrative tenure (months)")
plt.ylabel("Illustrative churn risk (%)")
plt.title("Illustrative Relationship Between Tenure and Churn Risk")
plt.tight_layout()
plt.savefig("diagrams/illustrative_tenure_risk.png",dpi=160)
plt.close()
