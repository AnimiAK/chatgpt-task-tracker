import streamlit as st
import pandas as pd
import requests

# 🔗 REPLACE this URL with the Raw GitHub link to your tasks.json file
DATA_URL = "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/chatgpt-task-tracker/main/tasks.json"

def fetch_tasks():
    """Fetch the latest task updates from the live JSON data source."""
    try:
        response = requests.get(DATA_URL)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data["tasks"])  # Convert JSON data to DataFrame
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame([], columns=["Project", "Task", "Priority", "Status", "Progress (%)", "ETA"])

# Fetch the latest task updates
df = fetch_tasks()

# Streamlit Dashboard
st.title("ChatGPT Task Manager - Real-Time Progress Tracker")
st.write("This dashboard auto-updates based on live progress.")

# Display tasks dynamically
if not df.empty:
    for index, row in df.iterrows():
        st.subheader(f"📌 {row['Project']} - {row['Task']}")
        st.write(f"**Priority:** {row['Priority']} | **Status:** {row['Status']} | **ETA:** {row['ETA']}")
        st.progress(int(row["Progress (%)"]))
else:
    st.write("⚠ No tasks available. Waiting for live updates...")
