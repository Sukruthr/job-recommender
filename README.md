# AI Job Recommender

An intelligent job recommendation system powered by AI that analyzes your resume and provides personalized job recommendations, skill gap analysis, and career development roadmaps.

## Features

- **Resume Analysis**: Upload your PDF resume and get an AI-powered summary highlighting your skills, education, and experience
- **Skill Gap Analysis**: Identify missing skills, certifications, and experience needed for better job opportunities
- **Career Roadmap**: Receive personalized recommendations for skills to learn, certifications to pursue, and industry exposure needed
- **Job Recommendations**: Get relevant job listings from Naukri based on your resume profile
- **AI-Powered Matching**: Uses OpenAI GPT-4o to extract job keywords and match them with your profile

## Prerequisites

- Python 3.12 or higher
- OpenAI API key
- Apify API key

## Installation

1. Clone the repository:
```bash
git clone [<repository-url>](https://github.com/Sukruthr/job-recommender)
cd job-recommender
```

2. Install dependencies using `uv` (recommended):
```bash
uv sync
```

Or install using pip:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
APIFY_API_KEY=your_apify_api_key_here
```

## Usage

### Running the Streamlit Application

Start the web application:
```bash
streamlit run app.py
```

The application will open in your default web browser. You can then:
1. Upload your resume (PDF format)
2. View the AI-generated resume summary
3. Review skill gaps and missing areas
4. Check your personalized career roadmap
5. Get job recommendations from Naukri

### Using the MCP Server

The project includes an MCP (Model Context Protocol) server for programmatic job fetching:

```bash
python mcp_server.py
```

## Project Structure

```
job-recommender/
├── app.py                 # Main Streamlit application
├── mcp_server.py         # MCP server for job fetching
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Project configuration
├── src/
│   ├── helper.py         # PDF extraction and OpenAI integration
│   └── job_api.py        # Job fetching APIs (Naukri, LinkedIn)
└── README.md             # Project documentation
```

## Dependencies

- **streamlit**: Web application framework
- **openai**: OpenAI API client for GPT-4o integration
- **pymupdf**: PDF text extraction
- **python-dotenv**: Environment variable management
- **apify-client**: Job scraping from Naukri and LinkedIn

## Configuration

The application requires the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key for GPT-4o access
- `APIFY_API_KEY`: Your Apify API key for job scraping

## How It Works

1. **Resume Upload**: Users upload their resume in PDF format
2. **Text Extraction**: The system extracts text from the PDF using PyMuPDF
3. **AI Analysis**: OpenAI GPT-4o analyzes the resume and generates:
   - Resume summary
   - Skill gap analysis
   - Career roadmap
4. **Job Matching**: The system extracts relevant job keywords from the resume summary
5. **Job Fetching**: Apify scrapes job listings from Naukri based on the extracted keywords
6. **Results Display**: All results are displayed in a clean, user-friendly interface

## Notes

- Currently, the application fetches jobs from Naukri (India-focused)
- LinkedIn job fetching is available but commented out in the code
- The application uses GPT-4o model for all AI-powered analysis
- Job recommendations are limited to 50 results by default


