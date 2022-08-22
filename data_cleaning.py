import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/glassdoor_jobs.csv")

#salary_estimate
df1 = df[df["Salary Estimate"]!="-1"]
df1["Salary Estimate"] = df1["Salary Estimate"].apply(lambda x: x.split("(")[0])
df1["Salary Estimate"] = df1["Salary Estimate"].apply(lambda x: x.lower().replace("k", "").replace("$", ""))

df1["Employer Provided Salary"] = df1["Salary Estimate"].apply(lambda x: 1 if "employer provided salary:" in x else 0)
df1["Salary Per Hour"] = df1["Salary Estimate"].apply(lambda x: 1 if "per hour" in x else 0)

df1["Salary Estimate"] = df1["Salary Estimate"].apply(lambda x: x.lower().replace("employer provided salary:", ""))
df1["Salary Estimate"] = df1["Salary Estimate"].apply(lambda x: x.lower().replace("per hour", ""))

df1["min salary"] = df1["Salary Estimate"].apply(lambda x: int(x.split("-")[0]))
df1["max salary"] = df1["Salary Estimate"].apply(lambda x: int(x.split("-")[1]))
df1["mean salary"] =(df1["min salary"] + df1["max salary"])/2


#company_name and rating
df2 = df1.copy()
df2["Company"] = df2.apply(lambda x: x["Company Name"] if x["Rating"]<0 else x["Company Name"][:-3], axis=1)


#location and company's headquarters
df3 = df2.copy()
df3["Location"] = df3["Location"].apply(lambda x: x.split(",")[1])
df3["Headquarters"] = df3["Headquarters"].apply(lambda x: x.split(",")[1] if "," in x else x)


#age of company
df4 = df3.copy()
df4["age"] = df4["Founded"].apply(lambda x: 2020-x if x!=-1 else -1)


#ownership
ownership_to_keep = df4["Type of ownership"].value_counts().index[:7]
df4["Type of ownership"] = df4["Type of ownership"].apply(lambda x: x if x in ownership_to_keep else "Other Organization")
df_ownership = pd.get_dummies(df4["Type of ownership"], drop_first=True)
o_dummies = pd.concat([df4, df_ownership], axis=1)


#sector
sectors_to_keep = o_dummies.Sector.value_counts().index[:10]
df5 = o_dummies.copy()
df5["Sector"] = df5["Sector"].apply(lambda x: x if x in sectors_to_keep else "Other Sectors")

le = LabelEncoder()
df5["le_sectors"] = le.fit_transform(df5["Sector"])


#removing unnecessary columns
df6 = df5.copy()
df6 = df6.drop(["Unnamed: 0", "Salary Estimate", "Company Name", "Founded", "Industry"], axis=1)


#reset index
df6 = df6.reset_index(drop=True)

#job description
job_description = ""
for i in range(len(df6)) :
    job_description += df6["Job Description"][i]
    
df6.to_csv("data/clean_salary_data.csv")
