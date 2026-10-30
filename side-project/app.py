
# Import required libraries
import streamlit as st
import pandas as pd
import joblib
import os

# Load the saved ML models
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

math_model = joblib.load(
    os.path.join(BASE_DIR, "math_score_model.pkl")
)

support_model = joblib.load(
    os.path.join(BASE_DIR, "academic_support_model.pkl")
)

subject_models = joblib.load(
    os.path.join(BASE_DIR, "subject_support_models.pkl")
)

# Configure the app
st.set_page_config(
    page_title="Student Performance AI",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Student Performance AI")
st.write(
    "Predict an estimated math score and identify "
    "where a student may benefit from additional support."
)

# Create two tabs for the two ML features
math_tab, support_tab = st.tabs([
    "📊 Math Score Predictor",
    "🎯 Academic Support Indicator"
])

# ----------------------------------------
# FEATURE 1: MATH SCORE PREDICTOR
# ----------------------------------------
with math_tab:
    st.header("Math Score Predictor")
    st.write("Enter the student's background information.")

    gender = st.selectbox(
        "Gender", ["female", "male"], key="gender"
    )

    race = st.selectbox(
        "Race/Ethnicity",
        ["group A", "group B", "group C", "group D", "group E"],
        key="race"
    )

    education = st.selectbox(
        "Parental Education",
        [
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree"
        ],
        key="education"
    )

    lunch = st.selectbox(
        "Lunch",
        ["standard", "free/reduced"],
        key="lunch"
    )

    preparation = st.selectbox(
        "Test Preparation Course",
        ["none", "completed"],
        key="preparation"
    )

    if st.button("Predict Math Score"):
        student = pd.DataFrame([{
            "gender": gender,
            "race/ethnicity": race,
            "parental level of education": education,
            "lunch": lunch,
            "test preparation course": preparation
        }])

        prediction = float(math_model.predict(student)[0])
        prediction = max(0, min(100, prediction))

        st.metric("Estimated Math Score", f"{prediction:.1f}/100")
        st.caption(
            "An estimate based on the training data, "
            "not a guaranteed exam result."
        )

# ----------------------------------------
# FEATURE 2: ACADEMIC SUPPORT INDICATOR
# ----------------------------------------
with support_tab:
    st.header("Academic Support Indicator")
    st.write(
        "Enter the student's attendance, study habits, "
        "assignment completion, and previous average."
    )

    attendance = st.slider(
        "Attendance (%)", 0, 100, 75
    )

    study_hours = st.slider(
        "Study Hours per Day", 0.0, 10.0, 2.5, step=0.5
    )

    assignment_completion = st.slider(
        "Assignment Completion (%)", 0, 100, 75
    )

    previous_average = st.slider(
        "Previous Academic Average", 0, 100, 60
    )

    if st.button("Assess Academic Support"):
        student_features = pd.DataFrame([{
            "attendance": attendance,
            "study_hours": study_hours,
            "assignment_completion": assignment_completion,
            "previous_average": previous_average
        }])

        # Predict overall support indicator
        risk = int(support_model.predict(student_features)[0])
        probability = float(
            support_model.predict_proba(student_features)[0][1]
        )

        st.subheader("Assessment Result")

        if risk == 1:
            st.warning("Additional academic support may be helpful.")
        else:
            st.success("The model did not flag this student.")

        st.metric(
            "Estimated Support Probability",
            f"{probability:.1%}"
        )

        # Predict subject-specific risk
        st.subheader("Subject-wise Assessment")

        results = []

        for subject, model in subject_models.items():
            subject_probability = float(
                model.predict_proba(student_features)[0][1]
            )

            results.append({
                "Subject": subject.replace("_score", "").title(),
                "Estimated Risk": subject_probability
            })

        results.sort(
            key=lambda item: item["Estimated Risk"],
            reverse=True
        )

        for result in results:
            st.write(
                f"**{result['Subject']}:** "
                f"{result['Estimated Risk']:.1%} estimated risk"
            )
            st.progress(result["Estimated Risk"])

        st.caption(
            "Educational demonstration using synthetic training data. "
            "Probabilities are not validated real-world risk estimates. "
            "Use actual assessment results and teacher judgment "
            "before making decisions about student support."
        )
