# 🤖 Placement Operations Copilot


## 📌 Project Overview

The **Placement Operations Copilot** is a **local, offline, agentic AI system** designed to support placement readiness evaluation and role suitability analysis for students.

The system:
- Breaks placement evaluation into **logical agent-based steps**
- Applies **rule-based, explainable reasoning**
- Produces **structured recommendations** for readiness, roles, and preparation plans
- Runs entirely **offline** with **no external APIs or cloud services**

---

## 🎯 Objectives

- Evaluate **candidate readiness** using performance data
- Recommend **best-fit roles** based on skill thresholds
- Identify **skill gaps** blocking role eligibility
- Generate a **day-wise 7-day preparation plan**
- Provide a **clear “Next Actions” summary**

---

## 🧠 Agentic Workflow Architecture

The system follows a **multi-agent architecture**:

1. **Data Interpretation Agent**
   - Reads CSV input
   - Identifies skill columns

2. **Readiness Reasoning Agent**
   - Computes average scores
   - Assigns readiness status (Ready / Almost Ready / Not Ready)
   - Generates focused improvement suggestions

3. **Role Mapping Agent**
   - Matches skills against predefined role requirements
   - Identifies recommended and non-recommended roles

4. **Feedback & Planning Agent**
   - Extracts strengths and gaps
   - Generates a structured 7-day preparation plan

5. **Next Actions Agent**
   - Summarizes immediate actionable steps

---

## 🖥️ User Interface

The system uses **Streamlit** for a clean, interactive UI:

- CSV file upload (drag & drop)
- Real-time analysis
- Visual sections for:
  - Readiness
  - Role suitability
  - Interview feedback
  - Day-wise preparation plan
  - Next actions

---

## 📂 Project Structure

├── app.py 
├─  README.md # Project documentation
└──candidate_skills.csv

conda create -n placement_copilot python=3.10
conda activate placement_copilot


pip install streamlit pandas

streamlit run app.py


## 👤 Author

Alok Srivastava
AI / ML & Data Science Enthusiast
