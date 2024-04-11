

import numpy as np
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import seaborn as sns

path = os.getcwd() +'\\data'
all_files = glob.glob((path+ "/*.csv"))
all_f = []
file_type = ["Friday_DDOS", "Friday_PCAP", "Friday_Morning", "Monday_PCAP", "Thu_PCAP_Afternoon", "Thu_PCAP_Morning","TUE_PCAP", "WED_PCAP"]
i=0
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df["type"] = file_type[i]
    all_f.append(df)
    i += 1

data = pd.concat(all_f, axis=0, ignore_index=True)
data.to_csv(path+'data_all.csv', index=False)







fig, ax = plt.subplots(3, 3, figsize=(30, 30))
for var, subplot in zip(numerical_features, ax.flatten()):
    sns.boxplot(x='NObeyesdad', y=var, data=train_df, ax=subplot, palette='viridis')
    for ax in fig.axes:
        plt.sca(ax)
        plt.xticks(rotation=45)


fig, ax = plt.subplots(4, 2, figsize=(40, 20))
for var, subplot in zip(numerical_features, ax.flatten()):
    sns.histplot(x=var,  data=train_df, ax=subplot, hue='NObeyesdad', kde=True ,  palette='viridis')

sns.pairplot(train_df[numerical_features + ["NObeyesdad"]].sample(n=2000), hue="NObeyesdad", palette='viridis')







