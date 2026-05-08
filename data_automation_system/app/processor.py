import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def process_data(file_path, output_dir):
    # Load
    df = pd.read_csv(file_path)
    
    # Clean
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)
    df['Calories'] = df['Calories'].fillna(df['Calories'].median())
    df.drop_duplicates(inplace=True)
    
    # Generate Plot
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="whitegrid")
    sns.lineplot(data=df, x='Date', y='Calories', marker='o')
    
    plot_name = "latest_analysis.png"
    plot_path = os.path.join(output_dir, plot_name)
    plt.savefig(plot_path)
    plt.close()
    
    return {"status": "Success", "rows_processed": len(df), "plot_path": plot_path}