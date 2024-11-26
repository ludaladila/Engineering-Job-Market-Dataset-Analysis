import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import re

# -----------------------
# Helper Functions
# -----------------------

def load_data(file_path):
    """Load the dataset."""
    df = pd.read_csv(file_path)
    print("Data loaded successfully. Dataset Info:")
    print(df.info())
    return df

def handle_missing_values(df):
    """Handle missing values in the dataset."""
    print("\nMissing values per column before handling:")
    print(df.isnull().sum())

    # Drop rows with missing salary values
    df = df.dropna(subset=['Salary Min', 'Salary Max'])
    # Drop rows with missing company values (optional)
    df = df.dropna(subset=['Company'])
    df.reset_index(drop=True, inplace=True)

    print("\nMissing values per column after handling:")
    print(df.isnull().sum())
    return df

def clean_salary_columns(df):
    """Convert salary columns to numeric types."""
    df['Salary Min'] = pd.to_numeric(df['Salary Min'], errors='coerce')
    df['Salary Max'] = pd.to_numeric(df['Salary Max'], errors='coerce')
    return df

def process_location_column(df):
    """Split 'Location' into 'City' and 'State', clean up the values."""
    df[['City', 'State']] = df['Location'].str.split(',', n=1, expand=True)
    df['City'] = df['City'].str.strip()
    df['State'] = df['State'].str.strip()
    df['State'] = df['State'].str.replace(r'\bcounty\b$', '', case=False, regex=True).str.strip()
    df.loc[df['State'].isnull(), 'State'] = df.loc[df['State'].isnull(), 'City']
    df.loc[df['State'].isnull(), 'City'] = np.nan
    return df

def calculate_average_salary(df):
    """Calculate the average salary."""
    df['Salary Avg'] = df[['Salary Min', 'Salary Max']].mean(axis=1)
    return df

def extract_skills(df, skills_dict):
    """Extract skills from job descriptions using a predefined dictionary."""
    def extract(description):
        skills_found = []
        if pd.notnull(description):
            text = description.lower()
            for category, skills in skills_dict.items():
                for skill in skills:
                    if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text):
                        skills_found.append(skill)
        return list(set(skills_found))

    df['Skills'] = df['Description'].apply(extract)
    return df

def generate_visualizations(df):
    """Generate visualizations for data analysis."""
    # State distribution
    state_counts = df['State'].value_counts().head(20)
    plt.figure(figsize=(12, 8))
    plt.tight_layout()
    state_counts.plot(kind='bar')
    plt.title('Top 20 States by Job Postings')
    plt.xlabel('State')
    plt.ylabel('Number of Job Postings')
    plt.xticks(rotation=45)
    plt.show()


    # Salary distribution
    if not df['Salary Avg'].isnull().all():
        plt.figure(figsize=(12, 6))
        sns.histplot(df['Salary Avg'], bins=50, kde=True)
        plt.title('Salary Distribution')
        plt.xlabel('Average Salary')
        plt.ylabel('Frequency')
        plt.show()

    # Company distribution
    company_counts = df['Company'].value_counts().head(20)
    if not company_counts.empty:
        plt.figure(figsize=(14, 10))
        company_counts.plot(kind='bar')
        plt.title('Top 20 Companies by Job Postings')
        plt.xlabel('Company')
        plt.ylabel('Number of Job Postings')
        plt.xticks(rotation=45)
        plt.show()

    # Skills demand
    all_skills = df['Skills'].explode().dropna()
    skill_counts = all_skills.value_counts().head(20)
    plt.figure(figsize=(12, 6))
    skill_counts.plot(kind='bar')
    plt.title('Top 20 Most Common Skills')
    plt.xlabel('Skills')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.show()

    # Word Cloud for job descriptions
    text = ' '.join(df['Description'].dropna()).lower()
    stopwords = set(STOPWORDS)
    stopwords.update(['will', 'work', 'company', 'team', 'requirements', 'skills', 'experience'])
    wordcloud = WordCloud(width=1600, height=800, background_color='white', stopwords=stopwords).generate(text)
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


# -----------------------
# Main Script
# -----------------------

if __name__ == "__main__":
    # File paths
    input_file = 'Engineering_Jobs_Insight_Dataset.csv'
    output_file = 'adzuna_jobs_cleaned.csv'

    # Skills dictionary
    skills_dict = {
    'programming_languages': [
        'python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'php', 'swift',
        'kotlin', 'go', 'rust', 'typescript', 'scala', 'r', 'matlab', 'perl',
        'shell', 'assembly', 'dart'
    ],
    'web_technologies': [
        'html', 'css', 'react', 'angular', 'vue.js', 'node.js', 'django',
        'flask', 'spring', 'asp.net', 'jquery', 'bootstrap', 'rest', 'api',
        'graphql', 'sass', 'less', 'webpack', 'tailwind css', 'next.js',
        'nuxt.js'
    ],
    'databases': [
        'sql', 'mysql', 'postgresql', 'mongodb', 'oracle', 'redis', 'cassandra',
        'elasticsearch', 'dynamodb', 'firebase', 'sqlite', 'mariadb',
        'amazon redshift', 'neo4j', 'hbase', 'snowflake'
    ],
    'cloud_platforms': [
        'aws', 'azure', 'google cloud', 'heroku', 'docker', 'kubernetes',
        'jenkins', 'ci/cd', 'devops', 'terraform', 'openshift', 'ibm cloud',
        'cloudflare', 'ansible', 'vagrant', 'openstack', 'cloudformation'
    ],
    'machine_learning': [
        'machine learning', 'ai', 'deep learning', 'tensorflow', 'pytorch',
        'scikit-learn', 'nlp', 'computer vision', 'neural networks', 'keras',
        'reinforcement learning', 'xgboost', 'lightgbm', 'hugging face',
        'data science', 'feature engineering', 'model deployment',
        'anomaly detection', 'time series analysis'
    ],
    'data_processing': [
        'pandas', 'numpy', 'matplotlib', 'seaborn', 'plotly', 'excel',
        'tableau', 'power bi', 'dask', 'apache spark', 'hadoop', 'airflow',
        'etl', 'bigquery', 'snowflake'
    ],
    'networking': [
        'tcp/ip', 'http/https', 'ftp', 'ssh', 'dns', 'load balancing',
        'firewall configuration', 'network security', 'vpn', 'proxy servers'
    ],
    'cybersecurity': [
        'penetration testing', 'vulnerability assessment', 'siem', 'soc',
        'firewalls', 'intrusion detection systems', 'owasp', 'encryption',
        'risk assessment', 'incident response', 'zero trust', 'pki',
        'identity access management'
    ],
    'testing': [
        'unit testing', 'integration testing', 'system testing',
        'automation testing', 'selenium', 'junit', 'testng', 'postman',
        'cucumber', 'load testing', 'performance testing', 'penetration testing'
    ],
    'soft_skills': [
        'communication', 'leadership', 'teamwork', 'problem solving',
        'analytical', 'agile', 'scrum', 'project management', 'time management',
        'negotiation', 'adaptability', 'critical thinking', 'creativity',
        'conflict resolution'
    ],
    'version_control': [
        'git', 'github', 'gitlab', 'bitbucket', 'svn', 'mercurial',
        'version control best practices'
    ],
    'mobile_development': [
        'android', 'ios', 'flutter', 'react native', 'xamarin', 'swiftui',
        'kotlin multiplatform mobile', 'cordova', 'ionic', 'firebase'
    ]
}


    # Load and preprocess data
    df = load_data(input_file)
    df = handle_missing_values(df)
    df = clean_salary_columns(df)
    df = process_location_column(df)
    df = calculate_average_salary(df)
    df = extract_skills(df, skills_dict)

    # Save the preprocessed data
    df.to_csv(output_file, index=False)
    print(f"\nPreprocessed data saved to {output_file}")

    # Generate visualizations
    generate_visualizations(df)
