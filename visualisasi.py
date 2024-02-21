import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example with Line chart in the first column and Stacked Bar chart in the second column
st.title("Graphic Visualization")

# Generate some data for the line chart
hours = pd.date_range(start="08:00", end="17:00", freq='h')
values_line = np.random.randint(1, 10, len(hours))

fig_line, ax_line = plt.subplots()
ax_line.plot(hours, values_line, marker='o', linestyle='-')
ax_line.set_title("Line Chart")
ax_line.set_xlabel("Hour")
ax_line.set_ylabel("Qty")
ax_line.set_xticks(hours)
ax_line.set_xticklabels(hours.strftime('%I %p'), rotation=45, ha='right')

# Display the line chart
col1, col2 = st.columns(2)

# Display the line chart in the first column
col1.pyplot(fig_line)

# Generate some data for the stacked bar chart
values_bar1 = np.random.randint(1, 5, len(hours))
values_bar2 = np.random.randint(1, 5, len(hours))
values_bar3 = np.random.randint(1, 5, len(hours))
values_bar4 = np.random.randint(1, 5, len(hours))

fig_stacked_bar, ax_stacked_bar = plt.subplots()
ax_stacked_bar.bar(range(len(hours)), values_bar1, label='Type 1', color='blue')
ax_stacked_bar.bar(range(len(hours)), values_bar2, bottom=values_bar1, label='Type 2', color='green')
ax_stacked_bar.bar(range(len(hours)), values_bar3, bottom=np.array(values_bar1) + np.array(values_bar2), label='Type 3', color='red')
ax_stacked_bar.bar(range(len(hours)), values_bar4, bottom=np.array(values_bar1) + np.array(values_bar2) + np.array(values_bar3), label='Target', color='gray')
ax_stacked_bar.set_title("Stacked Bar Chart")
ax_stacked_bar.set_xlabel("Hour")
ax_stacked_bar.set_ylabel("Qty")
ax_stacked_bar.set_xticks(range(len(hours)))
ax_stacked_bar.set_xticklabels(hours.strftime('%I %p'), rotation=45, ha='right')
ax_stacked_bar.legend()

# Display the stacked bar chart in the second column
col2.pyplot(fig_stacked_bar)

# Add sidebar content with Logo.png
st.sidebar.image("Logo.png", use_column_width=True)
st.sidebar.markdown("<h2 style='text-align: center;'>Data Visualization</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.markdown("You can add any content here.")

# Add a table below the graphs
st.subheader("Visualization Table")
# Replace 'your_file.xlsx' with the actual file path
excel_file_path = 'visualisasi.xlsx'
excel_data = pd.read_excel(excel_file_path, engine='openpyxl')
st.write(excel_data)

# Database connection configuration
db_connection_config = st.secrets["connection.iab"]

# Database connection
conn = st.experimental_connection('iab', **db_connection_config)
smt_line = conn.query('SELECT * FROM smt_line').fetchall
st.dataframe(smt_line)

conn
