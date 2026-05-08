import streamlit as st
import pandas as pd
import os
from processor import process_data

# Page Configuration
st.set_page_config(page_title="Workout Data Analytics", layout="wide")

st.title("🏋️ Automated Fitness Data Analysis")
st.markdown("Upload your workout CSV to generate instant reports and insights.")

# Sidebar for configuration
st.sidebar.header("Settings")
theme_choice = st.sidebar.selectbox("Select Theme", ["whitegrid", "darkgrid", "ticks"])

# 1. File Upload Section
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Save the file temporarily
    temp_path = os.path.join("data/uploads", uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    # 2. Trigger Analysis
    if st.button("Generate Analysis Report"):
        with st.spinner('Processing your data...'):
            report_dir = "reports/static"
            results = process_data(temp_path, report_dir)
            
            # 3. Display Results
            st.divider()
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Statistical Summary")
                # Reload for display
                df_display = pd.read_csv(temp_path)
                st.dataframe(df_display.describe())
            
            with col2:
                st.subheader("Visual Analysis")
                # Display the saved Seaborn plot
                st.image(results['plot_path'], use_column_width=True)
                
            st.balloons()