import pandas as pd

# =====================================
# READING CSV FILES
# =====================================

df = pd.read_csv("data/students.csv")
df1 = pd.read_csv("data/employee.csv")
df2 = pd.read_csv("data/emp.csv")
df3 = pd.read_csv("data/duplicate.csv")
df4 = pd.read_csv("data/group.csv")
df5 = pd.read_csv("data/salary.csv")
jan = pd.read_csv("data/jan.csv")
feb = pd.read_csv("data/feb.csv")


# =====================================
# DATA EXPLORATION
# =====================================

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())


# =====================================
# COLUMN SELECTION
# =====================================

print(df["Name"])
print(df[["Name", "Age"]])

print(type(df["Age"]))
print(type(df[["Age"]]))

print(df["Name"][0])


# =====================================
# FILTERING DATA
# =====================================

print(df1[df1["Salary"] < 60000])
print(df1[df1["Department"] != "IT"])
print(df1[df1["Experience"] == 2])
print(df1[df1["Salary"] >= 70000])


# =====================================
# MULTIPLE CONDITIONS
# =====================================

print(
    df1[
        (df1["Department"] == "IT") &
        (df1["Salary"] > 50000)
    ]
)

print(
    df1[
        (df1["Department"] != "IT") &
        (df1["Salary"] > 50000)
    ]
)


# =====================================
# SORTING DATA
# =====================================

print(
    df1.sort_values(by="Salary", ascending=False)
)


# =====================================
# ILOC (POSITION-BASED INDEXING)
# =====================================

print(df.iloc[0])
print(df.iloc[3, 2])
print(df.iloc[0:3])


# =====================================
# LOC (LABEL-BASED INDEXING)
# =====================================

print(df1.loc[2, "Salary"])


# =====================================
# ADDING NEW COLUMNS
# =====================================

df1["Bonus"] = df1["Salary"] * 5
df1["Total Salary"] = df1["Salary"] + df1["Bonus"]
df1["Tax"] = df1["Total Salary"] * 0.10

print(df1)


# =====================================
# UPDATING DATA
# =====================================

df1.loc[0, "Salary"] = 100000

df1.loc[df1["Department"] == "IT", "Salary"] += 5000

df1.loc[df1["Department"] == "HR", "Department"] = "Human Resources"

df1.loc[df1["Name"] == "John", "Salary"] += 10000

print(df1)


# =====================================
# DROPPING COLUMNS
# =====================================

df = df.drop("Age", axis=1)
print(df)


# =====================================
# RENAMING COLUMNS
# =====================================

df1 = df1.rename(columns={
    "Salary": "Income",
    "Experience": "Exp"
})

print(df1)


# =====================================
# MISSING VALUES
# =====================================

print(df2.isnull())
print(df2.isnull().sum())

df2 = df2.dropna()
print(df2)

df2 = df2.fillna(0)
print(df2)

mean_salary = df2["Salary"].mean()
print(mean_salary)

df2 = pd.read_csv("data/emp.csv")
df2["Salary"] = df2["Salary"].fillna(mean_salary)
print(df2)


# =====================================
# REMOVING DUPLICATES
# =====================================

print(df3.duplicated())
print(df3.duplicated().sum())

df3 = df3.drop_duplicates()
print(df3)

df3 = df3.drop_duplicates(subset="Name")
print(df3)


# =====================================
# GROUPBY
# =====================================

print(df4.groupby("Department"))
print(df4.groupby("Department")["Salary"].mean())
print(df4.groupby("Department")["Salary"].sum())
print(df4.groupby("Department")["Salary"].max())


print(df4.groupby(["Department", "Experience"])["Salary"].mean())
print(df4.groupby(["Department", "Experience"])["Name"].count())


result = (
    df4.groupby(["Department", "Experience"])["Salary"]
    .mean()
    .reset_index()
)

print(result)


# =====================================
# MERGE DATAFRAMES
# =====================================

result = pd.merge(df4, df5, on="Emp_ID")
print(result)

pd.merge(df4, df5, on="Emp_ID", how="inner")


# =====================================
# CONCAT DATAFRAMES
# =====================================

result = pd.concat([jan, feb])
print(result)

result = pd.concat([jan, feb], ignore_index=True)
print(result)

result = pd.concat([jan, feb], axis=1)
print(result)