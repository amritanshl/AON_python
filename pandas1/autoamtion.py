import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def  automate_analysis(file_path,output_folder = "reports11"):
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            logging.info(f"Created folder: {output_folder}")
        df = pd.read_csv(file_path)
        logging.info(f"Loaded {len(df)} rows from {file_path}")
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df.dropna(subset=['Date'], inplace=True)
        df['Calories'] = df['Calories'].fillna(df['Calories'].median())
        df = df[df['Duration'] <= 180]
        
        # Remove duplicates
        df.drop_duplicates(inplace=True)
        logging.info("Data cleaning complete.")

        # --- STAGE 3: AUTOMATED INSIGHTS ---
        summary = df.describe()
        summary.to_csv(f"{output_folder}/statistical_summary.csv")
        
        # Calculate Correlation
        correlation = df[['Pulse', 'Maxpulse', 'Calories']].corr()
        logging.info("Insights generated and saved to CSV.")

        # --- STAGE 4: AUTOMATED VISUALIZATION ---
        sns.set_theme(style="darkgrid")
        
        # Trend Chart
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df, x='Date', y='Calories')
        plt.title('Calorie Burn Trend')
        plt.savefig(f"{output_folder}/calorie_trend.png")
        plt.close() # Close to free up memory
        
        # Distribution Chart
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x='Pulse', kde=True)
        plt.title('Pulse Distribution')
        plt.savefig(f"{output_folder}/pulse_distribution.png")
        plt.close()

        logging.info(f"Analysis complete. Find your reports in the '{output_folder}' directory.")
    except Exception as ex:
        logging.error(f"An error occurred: {ex}")

if __name__ == "__main__":
    automate_analysis('fitness_data.csv')