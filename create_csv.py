import pandas as pd

# Create data
data = {
    "Name": ["Amit", "Riya", "Rahul", "Priya", "Ankit"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("data.csv", index=False)

print("CSV file created successfully!")
