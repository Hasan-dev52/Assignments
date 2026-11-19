import pandas as pd

# Create sample data
data = {
    "Name": ["Ali", "Sara", "John", "Ali"],
    "Marks": [85, None, 75, 85],
    "City": ["Pune", "Mumbai", None, "Pune"],
    "Remarks": ["Good", "Average", "Good", "Good"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Display first five rows
print("\nFirst Five Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing marks with the mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill missing cities with the mode
df["City"] = df["City"].fillna(df["City"].mode()[0])

print("\nAfter Filling Missing Values:")
print(df)

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated())

# Remove duplicate records
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# Remove irrelevant column
df = df.drop(columns=["Remarks"])

print("\nAfter Removing Irrelevant Column:")
print(df)

# Select students with marks greater than 80
print("\nStudents Scoring Above 80:")
print(df.loc[df["Marks"] > 80])

# Save cleaned data to CSV
df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned data saved successfully.")
