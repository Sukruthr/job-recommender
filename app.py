import streamlit as st
from src.helper import extract_text_from_pdf, ask_openai
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs

st.set_page_config(page_title="Job Recommender", layout="wide")
st.title("AI Job Recommender")
st.markdown("Upload your resume to get job recommendations based on your skills and experience from Naukri.")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
    st.write(resume_text)

    with st.spinner("Summarizing your Resume..."):
        summary = ask_openai(f"Summarize this resume highlighting skills, education, and experience: \n\n {resume_text}", max_tokens=500)

    with st.spinner("Finding skill gaps in your resume..."):
        skill_gaps = ask_openai(f"""Analayze this resume and highlight missing skills, certification, and experience needed for better job opportunities: \n\n {resume_text}""", 
                            max_tokens=400)
    
    with st.spinner("Creating future road map..."):
        roadmap = ask_openai(f"Based on this person's resume, create a future road map for them to get a better job (include skills to learn, certification needed, and industry exposure ): \n\n {resume_text}", 
                            max_tokens=400)

    # Display nicely formatted results
    st.markdown("---")
    st.header("📑 Resume Summary")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{summary}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.header("🛠️ Skill Gaps & Missing Areas")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{skill_gaps}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.header("🚀 Future Roadmap & Preparation Strategy")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{roadmap}</div>", unsafe_allow_html=True)

    st.success("✅ Analysis Completed Successfully!")


    if st.button("🔎Get Job Recommendations"):
        with st.spinner("Fetching job recommendations..."):
            keywords = ask_openai(
                f"Based on this resume summary, suggest the best job titles and keywords for searching jobs. Give a comma-separated list only, no explanation.\n\nSummary: {summary}",
                max_tokens=100
            )

            search_keywords_clean = keywords.replace("\n", "").strip()

        st.success(f"Extracted Job Keywords: {search_keywords_clean}")

        with st.spinner("Fetching jobs from  Naukri..."):
            # linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean, num_jobs=5)
            naukri_jobs = fetch_naukri_jobs(search_keywords_clean, num_jobs=50)


        # st.markdown("---")
        # st.header("💼 Top LinkedIn Jobs")

        # if linkedin_jobs:
        #     for job in linkedin_jobs:
        #         st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}*")
        #         st.markdown(f"- 📍 {job.get('location')}")
        #         st.markdown(f"- 🔗 [View Job]({job.get('link')})")
        #         st.markdown("---")
        # else:
        #     st.warning("No LinkedIn jobs found.")

        st.markdown("---")
        st.header("💼 Top Naukri Jobs (India)")

        if naukri_jobs:
            for job in naukri_jobs:
                st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}*")
                st.markdown(f"- 📍 {job.get('location')}")
                st.markdown(f"- 🔗 [View Job]({job.get('url')})")
                st.markdown("---")
        else:
            st.warning("No Naukri jobs found.")


