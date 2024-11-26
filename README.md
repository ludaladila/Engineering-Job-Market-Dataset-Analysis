# Engineering Job Market Analysis Dataset
## Table of Contents
1. [Executive Summary](#executive-summary)
   - [Motivation and Potential Applications](#motivation-and-potential-applications)
2. [Description of Data](#description-of-data)
   - [Positions Included in the Dataset](#positions-included-in-the-dataset)
   - [Attributes of the Dataset](#attributes-of-the-dataset)
   - [Link of Dataset](#link-of-dataset)
3. [Data Uniqueness](#data-uniqueness)
4. [Power Analysis Results](#power-analysis-results)
5. [Exploratory Data Analysis (EDA) Report](#exploratory-data-analysis-eda-report)
   - [Geographical Distribution](#1-geographical-distribution)
   - [Skills Demand Analysis](#2-skills-demand-analysis)
   - [Salary Analysis](#3-salary-analysis)
   - [Company Analysis](#4-company-analysis)
   - [Job Description Analysis](#5-job-description-analysis)
6. [Link to code](#link-to-data-sourcing-code)
7. [Ethics Statement](#ethics-statement)
8. [Open Source License](#open-source-license)

---

## Executive Summary

### Motivation and Potential Applications

The rapid advancement of technology has significantly increased the demand for engineering professionals, particularly in computer science and related fields. Understanding current job market trends is crucial for:

- **Job Seekers**: Aligning skills with industry demands to enhance employability and guide career planning.
- **Employers**: Developing effective recruitment strategies to attract top talent.
- **Educational Institutions**: Adjusting curricula to prepare students with in-demand skills.

This dataset project aims to bridge the gap between industry demand and workforce readiness by analyzing job descriptions from Adzuana. By extracting and analyzing common skills, job requirements, salary trends, and geographic differences, the dataset provides valuable insights into the evolving demands of the engineering workforce.

## Description of Data

The dataset comprises approximately **10,000** job descriptions focused on engineering and computer science roles. Each entry includes:

### Positions Included in the Dataset

The dataset focuses on a wide range of engineering and computer science roles, categorized into the following five groups:

| **Group**                | **Positions Included**                                                                                     |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| **Software Development** | Software Engineer, Full Stack Developer, Front End Developer, Back End Developer, Mobile App Developer    |
| **Data Science & Analytics** | Data Scientist, Data Engineer, Machine Learning Engineer, AI Engineer, Business Intelligence Analyst       |
| **Product & Design**     | Product Manager, Business Analyst, Product Analyst, UX/UI Designer, System Analyst                       |
| **IT & Systems**         | DevOps Engineer, Cloud Engineer, Site Reliability Engineer, Security Engineer, Network Engineer           |
| **Other Tech Roles**     | Embedded Systems Engineer, Quality Assurance Engineer, Database Administrator, Solutions Architect, Blockchain Developer |

---
### Attributes of the Dataset
Each entry in the dataset contains the following attributes:
- **Job Title**: Title of the job position (e.g., Software Engineer, Data Scientist).
- **Company Name**: Name of the hiring organization.
- **Description**: Job description of responsibilities and requirements.
- **Location**: City and state where the job is located.
- **Salary Min**: Minimum salary offered.
- **Salary Max**: Maximum salary offered.
- **Date Posted**: Date when the job was posted.
- **URL**: Link to the original job posting.

### Link of Dataset
The dataset is publicly available on Hugging face with th MIT License:

[Hugging face](https://huggingface.co/datasets/yiqing111/Engineering_Jobs_Insight_Dataset)


## Data Uniqueness

This dataset offers a comprehensive and focused view of the engineering job market by:

- **Specialization**:Concentrating specifically on engineering and computer science roles. Unlike generic job market datasets such as O*NET or Kaggle's job datasets, which often provide high-level overviews across all industries, our dataset zeroes in on the technical and engineering domain. It emphasizes the most sought-after roles in the rapidly evolving fields of software development, data science, IT infrastructure, and emerging technologies.

## Power Analysis Results

To ensure the dataset is statistically robust and representative, a power analysis was conducted.

- **Objective**: Determine the minimum sample size required to achieve statistically significant results for the analysis of engineering job postings.
- **Parameters**:
  - **Confidence Level**: 95%
  - **Margin of Error**: 5%
  - **Estimated Proportion (p)**: 0.5 (maximum variability)

- **Calculation**:
  Cochran's formula for determining sample size is given by:

  n₀ = (Z² × p × (1 - p)) / e²

  Where:
  - Z = 1.96 (Z-score for 95% confidence)
  - e = 0.05 (Margin of error)
  - p = 0.5 (Proportion)

  Substitute the values into the formula:

  n₀ = (1.96² × 0.5 × (1 - 0.5)) / 0.05² = 384

The minimum sample size required is approximately **384**.

### Result

The required sample size is approximately **384**.
Therefore, the minimum sample size for a single random sample in this project is **384** job descriptions. 

For the number of subgroups, the project estimates analyzing **25 different job types**. 

The total sample size required is calculated as:

n = 384 × 25 ≈ 10,000

Thus, the project estimates it needs approximately **10,000 job descriptions**.

### Exploratory Data Analysis (EDA) Report

This document summarizes the EDA conducted to analyze job postings, skill demand, salary trends, and geographical distribution within the dataset.

---

### 1. **Geographical Distribution**

**Objective**: Identify the top locations for engineering job postings.

**Methodology**:
- Analyzed the "Location" field to determine state distribution.
- Extracted and visualized the top 20 states with the most job postings.

**Findings**:
- **Top Location**: The **United States** shows the highest volume of postings, Santa Clara, Travis, and Los Angeles are among the most popular hiring regions.

**Visualization**:
![Top 20 States by Job Postings](https://drive.google.com/uc?export=view&id=1dYcWTcaSudGQTQrM88enMA7J_uR5qB4j
)

---

### 2. **Skills Demand Analysis**

#### **Overall Skills Demand**

**Objective**: Understand the most in-demand skills across all job postings.

**Methodology**:
- Used a predefined skill dictionary to extract skills from job descriptions.
- Aggregated and visualized the frequency of skills.

**Findings**:
- **Top Skills**:
  - AI, iOS, and Android dominate the demand.
  - Cloud and DevOps-related skills (e.g., AWS) are increasingly crucial.
  - Soft skills like leadership and communication are also sought after.

**Visualization**:
![Top 20 Most Common Skills](https://drive.google.com/uc?export=view&id=1zAw_WnRqDXFwfKDbcEKZi60DNXUa1wMM
)

---

### 3. **Salary Analysis**

**Objective**: Examine salary distribution for various engineering roles.

**Methodology**:
- Analyzed salary data from the "Salary Min" and "Salary Max" columns.
- Calculated and visualized the average salaries across roles.

**Findings**:
- **Salary Trends**:
  - Average salaries cluster between $80,000 and $130,000 annually.
  - Outliers indicate specialized or senior positions exceeding $150,000.
**Visualization**:
![Salary Distribution](https://drive.google.com/uc?export=view&id=1j-a0DpkVpHmVk_4xsnbTGbruo7pEX-gK
)

---

### 4. **Company Analysis**

#### **Top Hiring Companies**

**Objective**: Highlight companies with the highest number of job postings.

**Methodology**:
- Counted the number of job postings per company.
- Visualized the top 20 companies.

**Findings**:
- **Key Employers**:
  - **Cheez** leads the hiring pool, followed by **Boeing** and **Mr.Cooper**.
- **Notable Trends**:
  - Companies in tech, healthcare, and finance are aggressively hiring.

**Visualization**:
![Top Hiring Companies](https://drive.google.com/uc?export=view&id=1u8iaraVYBKOWZ4dgfXhcvisLO5Wr9WT2
)

---

### 5. **Job Description Analysis**

**Objective**: Extract common themes and requirements from job descriptions.

**Methodology**:
- Combined job descriptions into a single corpus.
- Removed stopwords and generated a word cloud.

**Findings**:
- **Key Themes**:
  - Terms like "solution," "support," and "service" highlight client-focused roles.
  - "Team," "data," and "responsible" suggest collaboration and leadership qualities are valued.

**Visualization**:
![Word Cloud of Job Descriptions](https://drive.google.com/uc?export=view&id=1eqMP95dGiF8Lw3as2hCocZ1VKWjyFKpP
)

---


## Link to Data Sourcing Code

The code used for data sourcing is publicly available on GitHub:

[GitHub Repository Link](https://github.com/ludaladila/Engineering-Job-Market-Analysis/blob/main/adzuna_jobs_fetcher.py)

## Ethics Statement

This project was conducted with careful consideration of ethical standards and legal regulations.

- **Data Privacy**:
  - No personal identifiable information of individuals was collected or stored.
  - Only publicly available job postings were used.
- **Compliance with Terms of Service**:
  - Data collection adhered to the terms and conditions of each job platform.
  - For platforms web scraping, data was accessed via official APIs.
- **Usage Intent**:
  - The dataset is intended for educational and research purposes.
  - Users are encouraged to respect copyright laws and platform policies when utilizing the data.
- **Impact Consideration**:
  - The project aims to positively impact job seekers, employers, and researchers.
  - Potential misuse of the data for discriminatory practices is strongly discouraged.

## Open Source License

This project is licensed under the **MIT License**.

[MIT License Text](https://opensource.org/licenses/MIT)

```
MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction...

[Full license text in the repository]
```

---

**Note**: For the full license text, please refer to the [LICENSE](https://github.com/ludaladila/Engineering-Job-Market-Analysis/blob/main/LICENSE) file in the repository.


