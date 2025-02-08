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

# Refresh mechanism: Streamlit will refresh automatically when any changes are detected
st.write("This dashboard auto-refreshes every 30 seconds.")

# Display tasks dynamically
for index, row in df.iterrows():
    st.subheader(f"📌 {row['Project']} - {row['Task']}")
    st.write(f"**Priority:** {row['Priority']} | **Status:** {row['Status']} | **ETA:** {row['ETA']}")
    st.progress(int(row["Progress (%)"]))

# Auto-refresh method using Streamlit's cache control
st.experimental_memo.clear()  # Clears cache so the data updates
time.sleep(30)  # Forces the app to pause for 30 seconds before the next refresh
st.rerun()
