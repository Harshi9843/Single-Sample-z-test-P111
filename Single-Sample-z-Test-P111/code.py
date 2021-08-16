import plotly.figure_factory as ff 
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("Population Mean: ", population_mean)

def random_set_of_mean(counter):
	dataset = []

	for i in range(0, counter):
		random_index = random.randint(0, len(data))	
		value = data[random_index]
		dataset.append(value)
	mean = statistics.mean(dataset)

	return mean 

mean_list = []

for i in range(0, 100):
	set_of_means = random_set_of_mean(30)
	mean_list.append(set_of_means)

mean = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)
print("Mean of Sampling Distribution: ", mean)
print("Std Deviation of Sampling Distribution: ", std_deviation)

fig = ff.create_distplot([mean_list], ["Claps"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.7], mode = "lines", name = "MEAN"))
fig.show()

mean_sample = []
for i in range(1, 100):
	set_of_mean = random_set_of_mean(20)
	mean_sample.append(set_of_mean)
	mean_of_sample1 = statistics.mean(mean_sample)
print("Mean of Sample 1: ", mean_of_sample1)

z_score = (mean_of_sample1 - mean)/std_deviation
print("z-score = ", z_score)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
print("std1",first_std_deviation_start, first_std_deviation_end)
print("std2",second_std_deviation_start, second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)

#plotting the graph with traces
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.6], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.6], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.6], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.6], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.6], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0, 0.6], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.6], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
