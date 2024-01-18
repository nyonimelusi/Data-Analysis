#!/usr/bin/env python
# coding: utf-8

# Analyzing Fitness Watch Data entails the examination of information gathered by fitness wearables or smartwatches, providing valuable insights into users' health and activity behaviors. These devices monitor various metrics, including steps taken, calories burned, walking speed, and more. If you're interested in delving into the process of analyzing fitness watch data, this article is designed for you. Within this article, I'll guide you through the steps of conducting Fitness Watch Data Analysis using Python.

# # Analyzing Fitness Watch Data: A Step-by-Step Guide

# Fitness Watch Data Analysis serves as a pivotal tool for businesses operating in the health and wellness sector. Through the examination of user data obtained from fitness wearables, companies can comprehend user behavior, provide personalized solutions, and actively contribute to enhancing overall health and well-being.
# 
# Outlined below is the structured process to follow when addressing the challenge of Fitness Watch Data Analysis:

# 1. Data Collection from Fitness Watches:
# Gather data from fitness watches, ensuring its accuracy and reliability.
# 2. Exploratory Data Analysis (EDA):
#  Conduct EDA to obtain preliminary insights into the collected data.
# 3. Feature Engineering:
# Derive new features from the raw data to uncover more meaningful insights.
# 4. Data Visualization:
# Create visual representations of the data to effectively communicate insights.
# 5. User Activity Segmentation and Analysis:
# Segment users' activity based on time intervals or fitness metric levels.
# Analyze the performance of each segment to draw valuable conclusions.

# 
# The process initiates by acquiring data from a fitness watch, typically connected to a dedicated smartphone app. The data can be extracted from this app, such as Apple's Health app in my case. It's important to note that raw fitness data obtained directly from these apps might not be readily suitable for analysis. 

# Let's commence the Fitness Watch Data Analysis task by importing essential Python libraries and loading the dataset:

# 1. Step 1 of analysis with Python:

# #Import libraries:

# In[1]:


import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"
import plotly.express as px

data = pd.read_csv("Apple-Fitness-Data.csv")
print(data.head())


# Let’s have a look if this data contains any null values or not:

# In[2]:


print(data.isnull().sum())


# The dataset is devoid of any null values. Let's proceed by delving into the analysis of my step count over time:

# In[3]:


# Step Count Over Time
fig1 = px.line(data, x="Time",
               y="Step Count",
               title="Step Count Over Time")
fig1.show()


# 
# Now, let's explore the distance covered over time:

# In[4]:


# Distance Covered Over Time
fig2 = px.line(data, x="Time",
               y="Distance",
               title="Distance Covered Over Time")
fig2.show()


# Now, let's examine my energy burned over time:

# In[5]:


# Energy Burned Over Time
fig3 = px.line(data, x="Time",
               y="Energy Burned",
               title="Energy Burned Over Time")
fig3.show()


# Now, let's observe my walking speed over time:

# In[6]:


# Walking Speed Over Time
fig4 = px.line(data, x="Time",
               y="Walking Speed",
               title="Walking Speed Over Time")
fig4.show()


# Now, let's calculate and examine the average step counts per day:

# In[7]:


# Calculate Average Step Count per Day
average_step_count_per_day = data.groupby("Date")["Step Count"].mean().reset_index()

fig5 = px.bar(average_step_count_per_day, x="Date",
              y="Step Count",
              title="Average Step Count per Day")
fig5.update_xaxes(type='category')
fig5.show()


# Now, let's explore my walking efficiency over time:

# In[8]:


# Calculate Walking Efficiency
data["Walking Efficiency"] = data["Distance"] / data["Step Count"]

fig6 = px.line(data, x="Time",
               y="Walking Efficiency",
               title="Walking Efficiency Over Time")
fig6.show()


# Now, let's examine the variations in step count and walking speed based on different time intervals:

# In[9]:


# Create Time Intervals
time_intervals = pd.cut(pd.to_datetime(data["Time"]).dt.hour,
                        bins=[0, 12, 18, 24],
                        labels=["Morning", "Afternoon", "Evening"], 
                        right=False)

data["Time Interval"] = time_intervals

# Variations in Step Count and Walking Speed by Time Interval
fig7 = px.scatter(data, x="Step Count",
                  y="Walking Speed",
                  color="Time Interval",
                  title="Step Count and Walking Speed Variations by Time Interval",
                  trendline='ols')
fig7.show()


# Now, let's compare the daily averages of all the health and fitness metrics:

# In[10]:


# Reshape data for treemap
daily_avg_metrics = data.groupby("Date").mean().reset_index()

daily_avg_metrics_melted = daily_avg_metrics.melt(id_vars=["Date"], 
                                                  value_vars=["Step Count", "Distance", 
                                                              "Energy Burned", "Flights Climbed", 
                                                              "Walking Double Support Percentage", 
                                                              "Walking Speed"])

# Treemap of Daily Averages for Different Metrics Over Several Weeks
fig = px.treemap(daily_avg_metrics_melted,
                 path=["variable"],
                 values="value",
                 color="variable",
                 hover_data=["value"],
                 title="Daily Averages for Different Metrics")
fig.show()


# The depicted graph illustrates each health and fitness metric through rectangular tiles. The size of each tile corresponds to the metric's value, while the color represents the specific metric. Hovering over the data provides precise average values for each metric, facilitating interactive exploration of the visualization

# The dominance of the Step Count metric in the visualization, owing to its generally higher numerical values compared to other metrics, makes it challenging to effectively visualize variations in the remaining metrics. To address this, let's revisit the visualization without including step counts:

# In[11]:


# Select metrics excluding Step Count
metrics_to_visualize = ["Distance", "Energy Burned", "Flights Climbed", 
                        "Walking Double Support Percentage", "Walking Speed"]

# Reshape data for treemap
daily_avg_metrics_melted = daily_avg_metrics.melt(id_vars=["Date"], value_vars=metrics_to_visualize)

fig = px.treemap(daily_avg_metrics_melted,
                 path=["variable"],
                 values="value",
                 color="variable",
                 hover_data=["value"],
                 title="Daily Averages for Different Metrics (Excluding Step Count)")
fig.show()


# Indeed, this demonstrates the process of analyzing and working with fitness data using Python. 

# # Summary

# 
# Absolutely! This overview showcases how to conduct Fitness Data Analysis using Python. Fitness Watch Data Analysis is indeed a vital tool for businesses in the health and wellness sector. Through the analysis of user data from fitness wearables, companies gain insights into user behavior, enabling them to provide personalized solutions and actively contribute to enhancing users’ overall health and well-being. I trust you found this article on Fitness Watch Data Analysis using Python informative and valuable. If you have any further inquiries or need assistance, feel free to ask!

# In[ ]:




