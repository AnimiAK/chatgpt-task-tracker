import streamlit as st
import pandas as pd
import time

# Sample task data
tasks = [
    ["Merch Store", "Finalize store banner & mockups", "High", "In Progress", 50, "2025-02-15"],
    ["Digital Products", "Design vanlife budgeting template", "High", "In Progress", 40, "2025-02-14"],
    ["YouTube Automation", "Finish first 'Top 10' script", "High", "In Progress", 60, "2025-02-12"],
    ["Sponsorships", "Finalize media kit & outreach email", "High", "In Progress", 70, "2025-02-13"],
    ["VanFit Respawn", "Develop bodyweight workout plan", "High", "In Progress", 50, "2025-02-14"],
]

# Convert to DataFrame
df = pd.DataFrame(tasks, columns=["Project", "Task", "Priority", "Status", "Progress (%)", "ETA"])

# Streamlit Dashboard
st.title("ChatGPT Task Manager - Real-Time Progress Tracker")
st.write("This dashboard refreshes automatically every time new data is available.")

# Display tasks dynamically
for index, row in df.iterrows():
    st.subheader(f"📌 {row['Project']} - {row['Task']}")
    st.write(f"**Priority:** {row['Priority']} | **Status:** {row['Status']} | **ETA:** {row['ETA']}")
    st.progress(int(row["Progress (%)"]))

# Auto-refresh using session state instead of experimental functions
if "last_refresh" not in st.session_state:
    st.session_state.last_refresh = time.time()

# Force refresh every 30 seconds
if time.time() - st.session_state.last_refresh > 30:
    st.session_state.last_refresh = time.time()
    st.rerun()
