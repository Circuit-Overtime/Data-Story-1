from google.colab import files
dataload = files.uplaod()
import csv 
import plotly.graph_objects as go
import pandas as pd
import statistics
import plotly.express as px

df = pd.read_csv("savings_data.csv")
fig1 = px.scatter(df,y = "quant_saved", color = "blue")
fig1.show()


with open("savings_data.csv", newline="") as f:
    reader = csv.reader(f)
    savings_data = (list(reader))

savings_data.pop(0)

total_entries = len(savings_data)
total_female = 0

for data in savings_data:
    if int(data[1]) == 1:
        total_female += 1

fig = go.Figure(go.Bar[x = ["Female", "Male"], y = [total_female, (total_entries - total_female)]])
fig.show()


all_savings = []
for data in savings_data:
    all_savings.append(float(data[0]))

print(f"Mean of Savings = |{statistics.mean(all_savings)}")
print(f"Mode of Savings = |{statistics.mode(all_savings)}")
print(f"Median of Savings = |{statistics.median(all_savings)}")


