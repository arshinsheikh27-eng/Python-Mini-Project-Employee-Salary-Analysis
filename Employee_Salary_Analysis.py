import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Employee_Salary.csv")
print("\n", df.head())
# print(df)
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
# print("\n")
print("-----------------------------------------------------------------------")
# Q1. What is the average salary?
print("Average Salary =", df["Salary"].mean())
print("-----------------------------------------------------------------------")
# Q2. What is the highest salary?
print("Highest Salary =", df["Salary"].max())
print("-----------------------------------------------------------------------")
# Q3. What is the lowest salary?
print("Lowest Salary =", df["Salary"].min())
print("-----------------------------------------------------------------------")
# Q4. How many employees are there in each department?
print(df["Department"].value_counts())
print("-----------------------------------------------------------------------")
# Q5. What is the avaerage salary for each department? 
print(df.groupby("Department")["Salary"].mean())
print("-----------------------------------------------------------------------")
# Q6. Which employee has the highest salary?

highest_salary = df["Salary"].max()
print(df[df["Salary"] == highest_salary])
# print(df[df["Salary"] == highest_salary][["Employee_Name","Salary"]])

print("-----------------------------------------------------------------------")
# Q7. Which employee have more than 5 years of experience?

# print(df[df["Experience"] > 5])
print(df[df["Experience"] > 5][["Employee_Name","Experience"]])

print("-----------------------------------------------------------------------")
# Q8. Which department has highest avaerage salary?

department_salary = df.groupby("Department")["Salary"].mean()
print(department_salary) 

print("\nDepartment with Highest Average Salary:")
print(department_salary.idxmax())

print("-----------------------------------------------------------------------")
# Q9. Which department has the most employee?

department_count = df["Department"].value_counts()
print(department_count)

print("\nDepartment with Maximum Employees:")
print(department_count.idxmax())

#Q. Show the average salary by departmnet bar graph

plt.figure(figsize=(8,5), facecolor = "ghostwhite")
department_salary.plot(kind="bar", color="teal", width = 0.6)
plt.title("\n Avaerage Salary Across Departments \n", fontsize = 16)
plt.xlabel("Department", fontsize = 12)
plt.ylabel("Average Salary", fontsize = 12)
plt.grid(axis = "y", linestyle = "--")
ax = plt.gca()
ax.set_facecolor("ghostwhite")
plt.show()

# Q. Show the Employees by department pie chart

plt.figure(figsize=(8,5), facecolor = "ghostwhite")
colors = ["seagreen","teal","darkorange","olive"]
department_count.plot(kind="pie", autopct = "%1.1f%%", startangle = 90, colors = colors)
plt.title("Employee Distribution Across Departments", fontsize = 16)
plt.ylabel("")
plt.show()
