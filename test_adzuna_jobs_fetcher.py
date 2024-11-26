import unittest
from adzuna_jobs_fetcher import fetch_jobs, save_to_csv

class TestAdzunaJobsFetcher(unittest.TestCase):

    def test_fetch_jobs(self):
        """Test the fetch_jobs function with a valid job title."""
        jobs = fetch_jobs("Software Engineer", max_pages=1)
        self.assertIsInstance(jobs, list)
        self.assertGreater(len(jobs), 0, "No jobs fetched.")

    def test_save_to_csv(self):
        """Test the save_to_csv function."""
        sample_data = [
            {"Job Title": "Test Job", "Company": "Test Company", "Location": "Test Location"}
        ]
        save_to_csv(sample_data, filename="test_jobs.csv")
        with open("test_jobs.csv", "r") as f:
            content = f.read()
        self.assertIn("Test Job", content, "Job title not found in saved CSV.")

if __name__ == "__main__":
    unittest.main()
