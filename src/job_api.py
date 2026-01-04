import os
from dotenv import load_dotenv
from apify_client import ApifyClient


load_dotenv()

os.environ["APIFY_API_KEY"] = os.getenv("APIFY_API_KEY")

client = ApifyClient(os.getenv("APIFY_API_KEY"))

# fetch jobs from linkedin
def fetch_linkedin_jobs(search_query, location="United States", num_jobs=10):
    run_input = {
        "keywords": search_query,
        "location": location,
        "limit": num_jobs,
        "page_number": 1,
    }

    # Run the Actor and wait for it to finish
    run = client.actor("KE649tixwpoRnZtJJ").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    jobs=list(client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs


# fetch jobs from Naukri
def fetch_naukri_jobs(search_query, location="United States", num_jobs=50):

    # Prepare the Actor input
    run_input = {
        "keyword": search_query,
        "maxJobs": num_jobs,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all"
    }

    # Run the Actor and wait for it to finish
    run = client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
    jobs=list(client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs