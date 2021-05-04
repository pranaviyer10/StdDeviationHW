import csv

with open('data_.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)

total_numbers = 0
total_entries = len(file_data)

for numbers in file_data:
    total_numbers += float(numbers[1])

mean = total_numbers / total_entries
print("Mean (Average is ->"+str(mean))

import pandas as pd
import plotly.express as px

df = pd.read_csv("data_.csv")

fig = px.scatter(df, x="Numbers",
                     y="Entries"
            )
fig.update_layout(shapes=[
    dict(
        type='line',
        y0= mean, y1= mean,
        x0= 0, x1= total_entries
    )
])

fig.update_yaxes(rangemode="tozero")

fig.show()