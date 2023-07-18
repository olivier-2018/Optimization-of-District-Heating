# -*- coding: utf-8 -*-
"""
This is just a very brief hack (!) to illustrate some of the available data.
"""

import pandas as pd
import matplotlib.pyplot as plt


# Folder (semester)
folder = "Data_Merged_2018_2019"


#%% Furnaces ==================================================================
plant_file_names = ['1901_protWZ.csv',
                    '2901_protWZ.csv',
                    '3901_protWZ.csv',
                    '4901_protWZ.csv']

labels = ['Main Feeder',
          'Wood-fired boiler',
          'Gas-fired boiler 1',
          'Gas-fired boiler 2'
          ]

dfs = []
for f in plant_file_names:
    # Read directly as time series
    df_temp = pd.read_csv(folder + "/" + f, index_col=0, parse_dates=True, infer_datetime_format=True, dayfirst=True)
    dfs.append(df_temp)

#%% Select a column and create an overview plot
column = "WZ Leistung(kW)"

fig = plt.figure(1)
fig.clear()

i = 0
for df in dfs:
    df[column].plot(ax=fig.gca(), label=labels[i], legend=True)
    i = i+1

ax = fig.gca()
ax.set_ylim(0, 2500)
ax.set_ylabel('Power (kW)')
ax.set_xlabel(None)
plt.grid()


#%% Heat store Temperatures ===================================================
plant_file_name = '901_protSPS.csv'

df = pd.read_csv(folder + "/" + plant_file_name, index_col=0, parse_dates=True, infer_datetime_format=True, dayfirst=True)

fig = plt.figure(2)
fig.clear()
df2 = df.iloc[:, 3:13]
df2.plot(ax=fig.gca(), legend=True)
ax = fig.gca()
ax.set_ylabel('Temperature (°C)')
ax.set_xlabel(None)


# Average store temperature and main feeder power
df3 = df2.mean(axis=1)

fig = plt.figure(4)
fig.clear()
ax = fig.gca()
dfs[0][column].plot(ax=ax, label='Main Feeder')
ax.set_ylim(0, 2500)

ax2 = ax.twinx()
df3.plot(ax=ax2, label='Avg. storage temp.', style='r')
plt.grid()
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax.transAxes)

ax.set_ylabel('Power (kW)')
ax.set_xlabel(None)
ax2.set_ylabel('Temperature (°C)')

#%% Consumption ===============================================================

load_file_names =  ['1901_protWZ.csv', 
                    '1_prot.csv',
                    '2_prot.csv',
                    '3_prot.csv',
                    '4_prot.csv',
                    '5_prot.csv',
                    '1006_protWZ.csv',
                    '7_prot.csv',
                    '8_prot.csv',
                    '9_prot.csv']

labels = ['Main Feeder',
          'Load 1', 
          'Load 2', 
          'Load 3', 
          'Load 4', 
          'Load 5', 
          'Load 6', 
          'Load 7', 
          'Load 8', 
          'Load 9', 
          ]

dfs = []
for f in load_file_names:
    # Read directly as time series
    df_temp = pd.read_csv(folder + "/" + f, index_col=0, parse_dates=True, infer_datetime_format=True, dayfirst=True)
    dfs.append(df_temp)
    
#%% Select a column and create an overview plot

column = "WZ Leistung(kW)"

fig = plt.figure(3)
fig.clear()

i = 0
for df in dfs:
    df[column].plot(ax=fig.gca(), label=labels[i], legend=True)
    i = i+1

ax = fig.gca()
ax.set_ylim(0, 2500)
ax.set_ylabel('Power (kW)')
ax.set_xlabel(None)
plt.grid()

# Now sum up all loads and add to plot (to compare with main feeder measurement)
dfs2 = dfs[1:]

i = 0
for df in dfs2:
    df.index = df.index.round('min')
    dfs2[i] = df[column]
    i = i+1
    
test = pd.concat(dfs2, axis=1)
test.dropna(inplace=True)

test.sum(axis=1).plot(ax=fig.gca(), label='Sum of Loads', legend=True, style='k--')