+++
title = "Prep & Review"
date = 2017-11-08T00:00:00-05:00
lastmod = 2017-11-11T11:24:08-05:00
tags = ["mutiple", "python", "visualization", "matplotlib", "multiple", "prep"]
categories = ["Python"]
weight = 4001
draft = false
+++

First, let's review how to create single chart. We'll use unemployment data from US Bureau of Labor Statistics. Here are the steps

1.  Use pandas to load a csv file to a DataFrame
2.  Use Pandas.to\_datetime to convert the DATE column into a Series of datetime values
3.  Create a line chart that visualize the unemployment from 1948:
    1.  x-values should be the first 12 values in the DATE column
    2.  y-values should be the first 12 values in the VALUE column
4.  Formatting the chart
    1.  use pyplot.xticks() to rotate x-axis tick labels by 90 degrees
    2.  Use pyplot.xlabel() to set the x-axis label to "Month"
    3.  Use pyplot.ylabel() to set the y-axis label to "Unemployment Rate"
    4.  Use pyplot.title() to set the plot title to "Monthly Unemployment Trends, 1948"
5.  Display the plot

```ipython
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

data_path = "../data/unrate.csv"
unrate = pd.read_csv(data_path)
unrate["DATE"] = pd.to_datetime(unrate["DATE"])

plt.plot(unrate["DATE"].iloc[:12], unrate["VALUE"].iloc[:12])

plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
```

{{<figure src="/pyplot/unrate-single.png">}}
