print("Time Column:")
print("Mean:",df["Time"].mean())
print("Median:",df["Time"].median())
print("Variance:",df["Time"].var())
print("Standard Deviation:",df["Time"].std())
print("\nAmount Column:")
print("Mean:",df["Amount"].mean())
print("Median:",df["Amount"].median())
print("Variance:",df["Amount"].var())
print("Standard Deviation:",df["Amount"].std())
stats=pd.DataFrame({
    "Mean":df.mean(numeric_only=True),
    "Median":df.median(numeric_only=True),
    "Variance":df.var(numeric_only=True),
    "Standard Deviation":df.std(numeric_only=True)
})
print(stats)
