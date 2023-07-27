# Personal developments over the Swiss Energy Hackdays 2020 

# Work in progress

## Challenge: Optimization of District Heating   
Hightech Zentrum, Brugg, August 28-29, 2020   

[Energy Hack Days 2020](https://hack.opendata.ch/event/31)    
[Optimization of District Heating](https://hack.opendata.ch/project/461)   
[Github source Repo](https://github.com/district-heating-2020/data_analysis)   

## Summary
Heating accounts for more than 40% of Switzerland’s final energy consumption.  
District heating networks facilitate deploying renewable heating on scale and are an essential part of Switzerland's Energy Strategy 2050. 

AEW as operator of more than 80 district heating networks sees a very good opportunity for replicability for this challenge.

## Requirements

**Voice of the customer**
*1. The operator (AEW) would like to know how many kW/h of gas boiler-produced heat per year could be saved through the performance forecast in order to decide whether it would have a significant impact on the climate targets.*

*2. The production engineer needs a forecast of the total power required (in kW) for each hour of the next 24 hours and the ability to visualize it.*

*3. The data scientist needs to know which features significantly influence the required total power (in kW) based on the historical data (e.g., in addition to the outside temperature, the global radiation, wind speed, humidity,...) so that I have the right input data choose for the forecast*

**Goals**
1. Minimize the energy consumption of disctrict heating plants (primary energy use) 
2. Minimize the use of peak load boilers. These boilers typically use fossil fuels, while the main boiler uses an renewable energy source.

**Systems goals**
1. A forecast of the required total power (in kW) for each hour of the next 24 hours, depending on the meteorological forecast for the outside temperature
and other relevant parameters".
2. Enhance the control system to 1) consume as little energy as possible and 2) do so without the use of fossil sources (using the wood boiler and the storage tank in combination).

**Capability deliverables** 
- Load forecasts based on historical consumption data, weather data, etc.
- Performance scheduling within the network by exploiting the thermal mass of the supplied objects or using distributed smaller intermediate storage facilities.

## Data sources
- [Production and usage data of an existing distric heating network for 9 client buildings](https://github.com/district-heating-2020/data_analysis/tree/master/data/energy): 2 years (2018-2019), every 5 minutes 
- [Historical weather data for the area](https://github.com/district-heating-2020/data_analysis/tree/master/data/weather)

## Getting started:
- Install a virtual environment:
```sh
virtualenv -p /usr/bin/python3.10 venv_DHS
```
- Activate virtual environment:
```sh
source venv_DHS/bin/activate
```
- Clone the repository:
```sh
git clone git@github.com:olivier-2018/Optimization-of-District-Heating.git
# then
cd Optimization-of-District-Heating
```
- Install python libraries:
```sh
pip install -r requirements.txt
```
- Run the jupyter notebook using your favorite IDE.


