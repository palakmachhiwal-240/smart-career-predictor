import streamlit as st
import joblib
import pandas as pd

# Page Settings
st.set_page_config(
    page_title="Smart Career Predictor",
    page_icon="🚀",
    layout="centered"
)
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
}

.stDownloadButton>button {
    width: 100%;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
# Load Model
model = joblib.load("career_model.pkl")
data = pd.read_csv("dataset.csv")

# Career Skills Dictionary
career_skills = {
    "data scientist": [
        "python",
        "pandas",
        "numpy",
        "statistics",
        "machine learning",
        "data visualization"
    ],
    "web developer": [
        "html",
        "css",
        "javascript",
        "react",
        "backend"
    ],
    "ui ux designer": [
        "figma",
        "wireframing",
        "prototyping",
        "user research"
    ],
    "accountant": [
        "tally",
        "gst",
        "accounting",
        "finance"
    ],
    "digital marketer": [
        "seo",
        "social media",
        "google ads",
        "marketing"
    ],
    "sales executive": [
        "communication",
        "negotiation",
        "sales",
        "customer handling"
    ]
}

# Sidebar
st.sidebar.title("📌 About Project")

st.sidebar.info(
    """
Smart Career Predictor is a Machine Learning based web application.

It predicts suitable career paths based on user skills.

Technologies Used:
- Python
- Pandas
- Scikit-Learn
- Streamlit
"""
)
st.sidebar.markdown("---")

st.sidebar.subheader("📊 Dataset Statistics")

st.sidebar.write(
    f"Total Records: {len(data)}"
)

st.sidebar.write(
    f"Total Careers: {data['career'].nunique()}"
)
st.sidebar.markdown("---")

st.sidebar.subheader("🤖 Model Information")

st.sidebar.write("Algorithm: Naive Bayes")

st.sidebar.write("Training Data: 24 Records")

st.sidebar.write("Career Categories: 6")
# Title
st.markdown(
    """
# 🚀 Smart Career Predictor

### AI Powered Career Recommendation System
"""
)
st.caption("🎯 AI Based Career Guidance for Students")

st.markdown(
    """
### Find the best career path based on your skills

Enter your skills below and our AI model will suggest a suitable career.
"""
)

# User Input
skills = st.text_area(
    "Enter your skills",
    placeholder="Example: python machine learning pandas"
)

# Predict Button
if st.button("Predict Career"):

    if skills.strip() == "":
        st.warning("⚠ Please enter your skills first.")

    else:

        # Prediction
        prediction = model.predict([skills])[0]

        # Confidence Score
        probabilities = model.predict_proba([skills])[0]
        confidence = max(probabilities) * 100

        st.success(f"🎯 Suggested Career: {prediction}")
        # Save History

        with open("history.txt", "a") as file:
            file.write(
                f"Skills: {skills} | Prediction: {prediction}\n"
            )
        report = f"""
        SMART CAREER PREDICTOR REPORT

        Suggested Career: {prediction}

        Confidence Score: {confidence:.2f}%

        Thank you for using Smart Career Predictor.
        """

        st.download_button(
            label="📄 Download Career Report",
            data=report,
            file_name="career_report.txt",
            mime="text/plain"
        )
        st.write(f"📈 Confidence Score: {confidence:.2f}%")

        # Top 3 Career Suggestions
        st.subheader("🏆 Top Career Suggestions")

        careers = model.classes_

        career_scores = list(zip(careers, probabilities))
        career_scores.sort(key=lambda x: x[1], reverse=True)

        for career, score in career_scores[:3]:
            st.write(f"✅ {career} - {score * 100:.2f}%")
        st.subheader("📊 Career Probability Chart")

        chart_data = pd.DataFrame({
        "Career": [career for career, score in career_scores[:3]],
        "Probability": [score * 100 for career, score in career_scores[:3]]
        })

        st.bar_chart(
        chart_data.set_index("Career")
            )

        # Career Roadmap
        st.subheader("🛣 Career Roadmap")

        if prediction == "data scientist":
            st.info(
                """
📘 Learn Python

📘 Learn Pandas & NumPy

📘 Study Machine Learning

📘 Build AI Projects

📘 Learn Data Visualization
"""
            )

        elif prediction == "web developer":
            st.info(
                """
🌐 Learn HTML

🌐 Learn CSS

🌐 Learn JavaScript

🌐 Learn React

🌐 Build Websites
"""
            )

        elif prediction == "ui ux designer":
            st.info(
                """
🎨 Learn Figma

🎨 Learn Wireframing

🎨 Study User Experience

🎨 Build Design Portfolio
"""
            )

        elif prediction == "accountant":
            st.info(
                """
📊 Learn Tally

📊 Learn GST

📊 Study Accounting

📊 Practice Financial Reports
"""
            )

        elif prediction == "digital marketer":
            st.info(
                """
📱 Learn SEO

📱 Learn Social Media Marketing

📱 Learn Google Ads

📱 Create Marketing Campaigns
"""
            )

        elif prediction == "sales executive":
            st.info(
                """
🤝 Improve Communication

🤝 Learn Sales Techniques

🤝 Learn Customer Handling

🤝 Practice Negotiation Skills
"""
            )

        # Skill Gap Analysis
        st.subheader("📚 Skill Gap Analysis")

        user_skills = skills.lower()
        missing_skills = []

        for skill in career_skills[prediction]:
            if skill.lower() not in user_skills:
                missing_skills.append(skill)

        if len(missing_skills) > 0:

            st.warning("Skills you should learn next:")

            for skill in missing_skills:
                st.write(f"✅ {skill}")

        else:
            st.success(
                "🎉 Great! You already have most of the important skills."
            )
        

        st.subheader("🎓 Career Tips & Learning Resources")

        if prediction == "data scientist":

            st.info("""
        📚 Recommended Learning Path

        • Python Programming

        • Pandas & NumPy

        • Machine Learning

        • Data Visualization

        🌐 Useful Websites

        • Kaggle.com

        • Coursera.org

        • freecodecamp.org
        """)

        elif prediction == "web developer":

            st.info("""
        📚 Recommended Learning Path

        • HTML

        • CSS

        • JavaScript

        • React

        🌐 Useful Websites

        • W3Schools.com

        • MDN Web Docs

        • freecodecamp.org
        """)

        elif prediction == "ui ux designer":

            st.info("""
        📚 Recommended Learning Path

        • Figma

        • Wireframing

        • User Research

        • Design Systems

        🌐 Useful Websites

        • Figma.com

        • Behance.net

        • Dribbble.com
        """)

        elif prediction == "accountant":

            st.info("""
        📚 Recommended Learning Path

        • Tally

        • GST

        • Accounting

        • Financial Reporting

        🌐 Useful Websites

        • TallySolutions.com

        • ICAI.org
        """)

        elif prediction == "digital marketer":

            st.info("""
        📚 Recommended Learning Path

        • SEO

        • Social Media Marketing

        • Google Ads

        • Content Marketing

        🌐 Useful Websites

        • Google Skillshop

        • HubSpot Academy

        • Semrush Blog
        """)

        elif prediction == "sales executive":

            st.info("""
        📚 Recommended Learning Path

        • Communication Skills

        • Sales Techniques

        • Negotiation

        • Customer Handling

        🌐 Useful Websites

        • HubSpot Academy

        • Coursera.org
        """)
st.sidebar.markdown("---")

st.sidebar.success(
    """
👨‍🎓 Student Project

Project: Smart Career Predictor

Technology:
Python + Machine Learning + Streamlit
"""
)

st.markdown(
    """
    <div style='text-align:center'>
        <h4>🚀 Smart Career Predictor</h4>
        <p>Built using Python, Scikit-Learn and Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)