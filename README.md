# Personal developments over the Swiss Energy Hackdays 2020 
## Challenge: Optimization of District Heating   
Hightech Zentrum in Brugg (August 28 - 29, 2020)   

[Energy Hack Days 2020](https://hack.opendata.ch/event/31)   
[Optimization of District Heating] (https://hack.opendata.ch/project/461)  
[Github source Repo] (https://github.com/district-heating-2020/data_analysis)   


## Summary
Heating accounts for more than 40% of Switzerland’s final energy consumption.  
District heating networks facilitate deploying renewable heating on scale and are an essential part of Switzerland's Energy Strategy 2050. 

AEW as operator of more than 80 district heating networks sees a very good opportunity for replicability for this challenge.

**Goals**
1. Minimize the energy consumption of disctrict heating plants (primary energy use) 
2. Minimize the use of peak load boilers. These boilers typically use fossil fuels, while the main boiler uses an renewable energy source.

**Solution** 
- Load forecasts based on historical consumption data, weather data, etc.
- Performance scheduling within the network by exploiting the thermal mass of the supplied objects or using distributed smaller intermediate storage facilities.

## Requirements

General: 
- **For whom**: control system of a district heating plant, which is operated by a renewable energy source (e.g. wood boiler) and additionally, if necessary, one or more fossil boilers (e.g. gas).
- **What**: A forecast of the required total power (in kW) for each hour of the next 24 hours, depending on the meteorological forecast for the outside temperature
and other relevant parameters".
- **Why**: So that the control system 1) consumes as little energy as possible and 2) can do without the use of fossil sources. The goal is that if possible only the interaction of the wood boiler and the storage tank (a kind of large boiler) are required to cover the heat requirements

Detailed questions: 
*1. As AEW, we would like to know how many kW/h of gas boiler-produced heat per year we could have saved through the performance forecast in order to decide whether it would have a significant impact on the climate targets.*

*2. As production engineer, one needs a forecast of the total power required (in kW) for each hour of the next 24 hours and the ability to visualize it.*

*3. As data scientist, one needs to know which factors significantly influence the required total power (in kW) based on the historical data (e.g., in addition to the outside temperature, the global radiation, wind speed, humidity,...) so that I have the right input data choose for the forecast*

*4. As a data scientist, I want to recognize the fixed operating times of customer boilers from consumption data so that I can add this input to the performance forecast*


## Data sources
- [Production and usage data of an existing distric heating network for 9 client buildings](https://github.com/district-heating-2020/data_analysis/tree/master/data/energy): 2 years (2018-2019), every 5 minutes 
- [Historical weather data for the area](https://github.com/district-heating-2020/data_analysis/tree/master/data/weather)

## Integration into the control system
- Recommender: Unload or fill memory now?
- Recommender: How much heat should the wood boiler produce now?
- Recommender: Should the oil cauldron (#6) be "dropped"?

## Getting started:
- Install a virtual environment:
```sh
virtualenv -p /usr/bin/python3.10 venv
```
- Activate virtual environment:
```sh
source venv/bin/activate
```
- Install python libraries:
```sh
pip install -r requirements.txt
```
- Clone the repository:
```sh
git clone git@github.com:olivier-2018/Adv_ML_techniques_for_imbalanced_dataset.git
# then
cd Adv_ML_techniques_for_imbalanced_dataset
```
- Run the jupyter notebook using your favorite IDE.


