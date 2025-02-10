import streamlit as st
from mira_sdk import MiraClient
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MIRA_API_KEY")
client = MiraClient(config={"API_KEY": api_key})

st.title("Expense Categorizer & Budget Tracker")

expenses = st.text_area("Enter your expenses:", "Groceries: 1000, Rent: 5000, Entertainment: 800")

if st.button("Analyze Budget"):
    if expenses:
        input_data = {"expenses": expenses}
        response = client.flow.execute("eshitaz/expensetracker", input_data)
        st.write(response.get("result", "No response from Mira AI"))
    else:
        st.warning("Please enter expenses.")
