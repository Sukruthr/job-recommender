from mcp.server.fastmcp import FastMCP
# from src.helper import extract_text_from_pdf, ask_openai
from src.job_api import fetch_naukri_jobs

mcp = FastMCP("job-recommender")

@mcp.tool()
async def fetch_naukri_jobs_mcp(list_of_keywords):
    return fetch_naukri_jobs(list_of_keywords)

if __name__ == "__main__":  
    mcp.run(transport="stdio")
