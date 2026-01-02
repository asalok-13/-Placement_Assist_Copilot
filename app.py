"""
Placement Operations Copilot
Local • Offline • Explainable Agentic AI System

Author: Alok Srivastava
"""

import os
import pandas as pd
import streamlit as st

# ============================================================
# AGENT 1: DATA INTERPRETATION AGENT
# ============================================================

class DataInterpretationAgent:
    def load_data(self, uploaded_file):
        return pd.read_csv(uploaded_file)

    def extract_skills(self, df):
        skill_columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
        if not skill_columns:
            raise ValueError("No numeric skill columns found in CSV")
        return skill_columns


# ============================================================
# AGENT 2: READINESS REASONING AGENT
# ============================================================

class ReadinessReasoningAgent:
    def evaluate_readiness(self, df, skills):
        avg_score = df[skills].mean().mean()

        if avg_score >= 75:
            status = "Ready"
            reason = "Consistently strong performance across assessed skills"
        elif avg_score >= 60:
            status = "Almost Ready"
            reason = "Basic understanding present but lacks consistency"
        else:
            status = "Not Ready"
            reason = "Below expected performance in core skills"

        weak_skills = df[skills].mean().sort_values().index.tolist()
        suggestions = []

# Skill-based suggestions
        for skill in weak_skills[:2]:
         suggestions.append(f"Improve proficiency in {skill}")

# Add generic suggestions if needed
        if len(suggestions) < 3:
           suggestions.append("Practice mock interview questions regularly")
        if len(suggestions) < 3:
          suggestions.append("Revise fundamentals and core concepts")

        return {
           "status": status,
           "average_score": round(avg_score, 2),
           "reasoning": reason,
           "suggestions": suggestions
        }

# ============================================================
# AGENT 3: ROLE MAPPING
# ============================================================

class RoleMappingAgent:
    ROLE_SKILL_MAP = {
        "Junior Data Analyst": ["sql"],
        "Backend Developer": ["sql", "python", "dsa"],
        "Data Engineer": ["sql", "python", "etl"]
    }

    def map_roles(self, df, skills):
        skill_scores = df[skills].mean().to_dict()
        recommended = []
        not_recommended = {}

        for role, required in self.ROLE_SKILL_MAP.items():
            missing = [
                skill for skill in required
                if skill not in skill_scores or skill_scores[skill] < 70
            ]
            if not missing:
                recommended.append(role)
            else:
                not_recommended[role] = missing

        return recommended, not_recommended


# ============================================================
# AGENT 4: FEEDBACK & PREPARATION PLANNING AGENT
# ============================================================

class FeedbackPlanningAgent:
    def analyze(self, df, skills):
        scores = df[skills].mean()
        strengths = scores[scores >= 70].index.tolist()
        gaps = scores[scores < 70].index.tolist()

        plan = {
           "Day 1": "Revise fundamentals",
           "Day 2": "Practice basic problems",
           "Day 3": "Learn intermediate concepts",
           "Day 4": "Practice intermediate problems",
           "Day 5": "Advanced queries and scenarios",
           "Day 6": "Mock interview practice",
           "Day 7": "Final revision and confidence building"
        }
        return strengths, gaps, plan

# ============================================================
# AGENT 5: NEXT ACTIONS SYNTHESIS AGENT
# ============================================================

class NextActionsAgent:
    def summarize(self, readiness, gaps):
        if readiness == "Ready":
            return "Start applying for roles and continue mock interview practice"
        elif readiness == "Almost Ready":
            return f"Focus on improving {', '.join(gaps)} and reattempt assessment"
        else:
            return "Build fundamentals before attempting placements"


# ============================================================
# STREAMLIT UI
# ============================================================

st.set_page_config(
    page_title="Placement Operations Copilot",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='text-align:center;'>🤖 Placement Operations Copilot</h1>
    <p style='text-align:center; color:gray;'>
    Local • Offline • Explainable Agentic Decision Support System
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "📌 Upload Candidate Scores (CSV)",
    type=["csv"]
)

if uploaded_file:
    try:
        # Step 1: Data interpretation
        df = DataInterpretationAgent().load_data(uploaded_file)
        skills = DataInterpretationAgent().extract_skills(df)

        # ---------------- INPUT DATA ----------------
        with st.expander("📊 View Uploaded Data", expanded=False):
            st.dataframe(df, use_container_width=True)

        # Step 2: Readiness
        readiness = ReadinessReasoningAgent().evaluate_readiness(df, skills)

        # ---------------- READINESS METRICS ----------------
        col1, col2, col3 = st.columns(3)

        col1.metric("Readiness Status", readiness["status"])
        col2.metric("Average Score", readiness["average_score"])
        col3.metric("Skills Evaluated", len(skills))

        st.markdown("### ✅ Readiness Reasoning")
        st.info(readiness["reasoning"])

        st.markdown("### 🎯 Focused Improvement Suggestions")
        for s in readiness["suggestions"]:
            st.write(f"✔ {s}")

        st.divider()

        # Step 3: Role Mapping
        recommended, not_recommended = RoleMappingAgent().map_roles(df, skills)

        st.markdown("### 🎯 Role Suitability Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### ✅ Recommended Roles")
            if recommended:
                for role in recommended:
                    st.success(role)
            else:
                st.warning("No strong role match")

        with col2:
            st.markdown("#### ❌ Not Recommended Roles")
            for role, gaps in not_recommended.items():
                st.error(f"{role} → Missing: {', '.join(gaps)}")

        st.divider()

        # Step 4: Feedback & Plan
        strengths, gaps, plan = FeedbackPlanningAgent().analyze(df, skills)

        st.markdown("### 🧠 Interview Feedback")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 💪 Strengths")
            if strengths:
                for s in strengths:
                    st.success(s)
            else:
                st.info("No strong skills identified")

        with col2:
            st.markdown("#### ⚠️ Skill Gaps")
            if gaps:
                for g in gaps:
                    st.warning(g)
            else:
                st.success("No critical gaps")

        st.divider()

        # ---------------- DAY-WISE PLAN ----------------
        # ---------- 7-Day Plan ----------
        st.subheader("📅 7-Day Preparation Plan")

       # ---------- Day-wise rendering ----------
        for day, task in plan.items():
          st.markdown(f"**{day}**")
          st.write(task)
          st.divider()

        # Step 5: Next Actions
        next_action = NextActionsAgent().summarize(
            readiness["status"], gaps
        )

        st.markdown("### 🚀 Next Actions")
        st.success(next_action)

    except Exception as e:
        st.error(str(e))

else:
    st.markdown(
        """
        <div style="padding:20px; background-color:#f0f2f6;
        border-radius:10px; text-align:center;">
        👆 Upload a CSV file to begin the analysis
        </div>
        """,
        unsafe_allow_html=True
    )
