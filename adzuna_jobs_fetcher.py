import requests
import pandas as pd
import urllib.parse
import time
import random

# Constants and Configuration
API_URL = "https://api.adzuna.com/v1/api/jobs/us/search/"  # US region API URL
APP_ID = "6dea1fd6"  
APP_KEY = "a019d9cd3f6c0b817c444a03a582013e"  
MAX_RETRIES = 3  # Maximum number of retries for failed requests
RETRY_DELAY_RANGE = (5, 15)  # Delay range for retries in seconds
MIN_DELAY = 2  # Minimum delay between API calls
MAX_DELAY = 10  # Maximum delay between API calls


def fetch_jobs(job_title, max_pages=50):
    """
    Fetch job postings for a specific job title from the Adzuna API.

    Args:
        job_title (str): The job title to search for.
        max_pages (int): The maximum number of pages to fetch. Default is 50.

    Returns:
        list: A list of job dictionaries with relevant details.
    """
    encoded_job_title = urllib.parse.quote(job_title)
    all_jobs = []
    retries = 0

    for page in range(1, max_pages + 1):
        try:
            # Construct the API URL
            api_url = f"{API_URL}{page}?app_id={APP_ID}&app_key={APP_KEY}&results_per_page=10&title_only={encoded_job_title}&full_time=1"
            response = requests.get(api_url)
            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                if "results" in data and data["results"]:
                    for job in data["results"]:
                        # Extract relevant job information
                        job_info = {
                            "Job Title": job.get("title", "N/A"),
                            "Company": job.get("company", {}).get("display_name", "N/A"),
                            "Description": job.get("description", "N/A"),
                            "Location": job.get("location", {}).get("display_name", "N/A"),
                            "Salary Min": job.get("salary_min", "N/A"),
                            "Salary Max": job.get("salary_max", "N/A"),
                            "Date Posted": job.get("created", "N/A"),
                            "URL": job.get("redirect_url", "N/A"),
                        }
                        all_jobs.append(job_info)
                else:
                    break  # Stop fetching if no results are returned
            else:
                raise Exception(f"HTTP {response.status_code}: {response.text}")
        
            time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

        except Exception as e:
            retries += 1
            if retries > MAX_RETRIES:
                print(f"Max retries reached for {job_title}. Error: {e}")
                break
            # Add a random delay before retrying
            delay = random.uniform(*RETRY_DELAY_RANGE)
            print(f"Retrying {job_title} in {delay:.2f} seconds. Error: {e}")
            time.sleep(delay)

    return all_jobs


def save_to_csv(data, filename="adzuna_jobs.csv"):
    """
    Save job data to a CSV file.

    Args:
        data (list): The job data to save.
        filename (str): The filename for the CSV. Default is "adzuna_jobs.csv".
    """
    if data:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding="utf-8")
        print(f"Job data saved to {filename}")
    else:
        print("No data to save.")


if __name__ == "__main__":
   
    job_titles = [
        # Software Development
        "Software Engineer",
        "Full Stack Developer", 
        "Front End Developer",
        "Back End Developer",
        "Mobile App Developer",
    
        # Data Science & Analytics
        "Data Scientist",
        "Data Engineer", 
        "Machine Learning Engineer",
        "AI Engineer",
        "Business Intelligence Analyst",
    
        # Product & Design
        "Product Manager",
        "Business Analyst",
        "Product Analyst",
        "UX/UI Designer", 
        "System Analyst",
    
        # IT & Systems  
        "DevOps Engineer",
        "Cloud Engineer",
        "Site Reliability Engineer",
        "Security Engineer",
        "Network Engineer",
    
        # Other Tech Roles
        "Embedded Systems Engineer",
        "Quality Assurance Engineer",
        "Database Administrator",
        "Solutions Architect",
        "Blockchain Developer"
    ]

    # Fetch jobs for each job title
    all_jobs = []
    for job_title in job_titles:
        print(f"Fetching jobs for: {job_title}")
        jobs = fetch_jobs(job_title)
        if jobs:
            all_jobs.extend(jobs)

    save_to_csv(all_jobs)
