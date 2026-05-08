import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import (
    LineChart,
    ScatterChart,
    BarChart,
    Reference,
    Series
)
from openpyxl.utils.dataframe import dataframe_to_rows

data = {
    "Duration": [60, 60, 60, 45, 45, 60, 60, 45, 30, 60],
    "Pulse": [110, 117, 103, 109, 117, 102, 110, 104, 109, 98],
    "Maxpulse": [130, 145, 135, 175, 148, 127, 136, 134, 133, 124],
    "Calories": [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 374.0, 253.3, 195.1, 269.0]
}
df = pd.DataFrame(data)
# 2. Create Workbook and Active Sheet
wb = Workbook()
ws = wb.active
ws.title = "Workout Report"

# 3. Write DataFrame to the Sheet
for r in dataframe_to_rows(df, index=False, header=True):
    ws.append(r)

# --- 1. LINE CHART (Calories over Sessions) ---
line = LineChart()
line.title = "Calorie Burn Trend"
line.y_axis.title = "Calories"
line.x_axis.title = "Session"

# Data is in column 4 (Calories), Rows 2 to 11
data_ref = Reference(ws, min_col=4, min_row=1, max_row=11)
line.add_data(data_ref, titles_from_data=True)
ws.add_chart(line, "F2")

# --- 2. BAR CHART (Duration per Session) ---
bar = BarChart()
bar.title = "Workout Duration"
bar.y_axis.title = "Minutes"

# Data is in column 1 (Duration)
bar_ref = Reference(ws, min_col=1, min_row=1, max_row=11)
bar.add_data(bar_ref, titles_from_data=True)
ws.add_chart(bar, "F18")

# --- 3. SCATTER CHART (Pulse vs Maxpulse) ---
scatter = ScatterChart()
scatter.title = "Pulse vs Maxpulse Correlation"
scatter.x_axis.title = "Average Pulse"
scatter.y_axis.title = "Max Pulse"

# X-axis values (Pulse - Col 2), Y-axis values (Maxpulse - Col 3)
x_values = Reference(ws, min_col=2, min_row=2, max_row=11)
y_values = Reference(ws, min_col=3, min_row=2, max_row=11)
series = Series(y_values, x_values, title_from_data=False)
scatter.series.append(series)
ws.add_chart(scatter, "N2")

# --- 4. HISTOGRAM (Frequency of Pulse) ---
# Note: Excel doesn't have a "Histogram" object in openpyxl; 
# we calculate frequencies first and plot as a Bar Chart.
hist_data = df['Pulse'].value_counts().sort_index().reset_index()
hist_data.columns = ['Pulse_Value', 'Frequency']

# Add a new sheet for Histogram data to keep things clean
hist_ws = wb.create_sheet(title="Pulse Distribution")
for r in dataframe_to_rows(hist_data, index=False, header=True):
    hist_ws.append(r)

hist_chart = BarChart()
hist_chart.title = "Pulse Frequency (Histogram)"
h_data = Reference(hist_ws, min_col=2, min_row=1, max_row=len(hist_data)+1)
h_cats = Reference(hist_ws, min_col=1, min_row=2, max_row=len(hist_data)+1)
hist_chart.add_data(h_data, titles_from_data=True)
hist_chart.set_categories(h_cats)
hist_ws.add_chart(hist_chart, "D2")

# 5. Save the Workbook
wb.save("Automated_Excel_Report.xlsx")
print("Report generated successfully!")