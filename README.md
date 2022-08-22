### DS-Salary-Estimate-and-Analysis
In this project we have to estimate the salary of data scientists and apply exploratory data analysis on the dataset.

## Dataset
The dataset contains the data about data scientists, data engineers and data analysts roles in USA. 
The data is collected from Glassdoor. 

## Data Cleaning and Preprocessing
- Salary Estimate (in thousands USD)
  - Remove unnecessary words/letters
  - Create min, max and avg salary columns with the help of Salary Estimate column
- Company , Location, Headquarters
  - Configure these columns to find the name of company, location and headquarters
- Type of ownership, Sector
  - Clean the columns
  - Apply One Hot Encoding on Type of Ownership column
  - Apply Label Encoding on Sector column
- Job description
  - Apply nlp techniques on the job description column
    - Apply WordNetLemmatizer
    - Convert to lower
    - Remove stopwords and punctuations
- Senior/Junior
  - Create Senior/Junior column that tells whether the role is senior or junior (with the help of Job Title column)
- Role
  - Create a Role column that categorizes the different jobs as Data Scientist, Data Engineers, Data Analyst and Other data roles
- No of competitors
  - Find the number of competitors for each company
- Loc==HQ
  - Create Loc==HQ column to check if the location of job is same as the location of headquarter of the company
- Skills
  - Create columns for different data science skills
  - Skills are : ['mathematics', 'python', 'r, 'machine learning', 'aws', 'cloud', 'excel']

## Exploratory Data Analysis
### Most used words in the job description
![Most used words in the job description](https://github.com/the-vergil/DS-Salary-Estimate-and-Analysis/blob/master/images/words.png)

### Word cloud of words
![Word cloud of words](https://github.com/the-vergil/DS-Salary-Estimate-and-Analysis/blob/master/images/word_cloud.png)

### Number of job openings in different states
![Number of job openings in different states](https://github.com/the-vergil/DS-Salary-Estimate-and-Analysis/blob/master/images/location.png)

### Company size providing data related roles
![Company size providing data related roles](https://github.com/the-vergil/DS-Salary-Estimate-and-Analysis/blob/master/images/size.png)

### Type of Ownership of different companies providing data roles
![Type of Ownership of different companies providing data roles](https://github.com/the-vergil/DS-Salary-Estimate-and-Analysis/blob/master/images/ownership.png)

### Type of Sectors that provide data related roles
![Type of Sectors that provide data related roles](https://github.com/the-vergil/DS-Salary-Estimate-and-Analysis/blob/master/images/sector.png)

### Different types of data roles
![Different types of data roles](https://github.com/the-vergil/DS-Salary-Estimate-and-Analysis/blob/master/images/role.png)
