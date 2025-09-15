# Fuel consumption dataset 
This dataset centralizes fuel consumption ratings for different cars, collected by the Canadian government. 
It provides data for different car models between 1995 and 2014.


Original data can be downloaded [here](https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64/resource/29bcf157-9297-4d6a-9695-dfd816bc32ca).

## Data Description
| Column header | Description | Additional notes 
| ---- | ---- | ---- | 
| Model year | The year used by the manufacturer to designate a model of vehicle | To help you compare vehicles from different model years, fuel consumption ratings for 1995 to 2014 vehicles have been adjusted to reflect the 5-cycle testing procedure. Note that these are approximate values that were generated from the original ratings, not from vehicle testing.
| Make | The manufacturer of the vehicle | n/a
| Model | The model name of the vehicle | AWD = All-wheel drive – vehicle designed to operate with all wheels powered 4WD/4X4 = Four-wheel drive – vehicle designed to operate with either two wheels or four wheels powered FFV = Flexible-fuel vehicle – vehicle designed to operate on gasoline and ethanol blends of up to 85% ethanol (E85) CNG = Compressed natural gas; NGV = Natural gas vehicle SWB = Short wheelbase; LWB = Long wheelbase; EWB = Extended wheelbase # = High output engine
| Vehicle class | Classification of the vehicle based on interior volume for cars and gross vehicle weight rating for light trucks | For details, visit [this page](https://natural-resources.canada.ca/energy-efficiency/transportation-alternative-fuels/personal-vehicles/choosing-right-vehicle/buying-electric-vehicle/understanding-the-tables/21383)
| Engine size (L) | Total displacement of all cylinders (in litres) | n/a 
| Cylinders | Number of engine cylinders | n/a 
| Transmission | The type of transmission and number of gears/speeds | A = Automatic; AM = Automated manual; AS = Automatic with select shift; AV = Continuously variable; M = Manual
| Fuel type | The type of fuel used to power the vehicle | X = Regular gasoline; Z = Premium gasoline; D = Diesel; E = E85; N = Natural Gas For FFVs, consumption values are provided for both gasoline and E85.
| City (L/100 km) | City fuel consumption rating shown in litres per 100 kilometres | The city rating represents urban driving in stop-and-go traffic.
| Highway (L/100 km) | Highway fuel consumption rating shown in litres per 100 kilometres | The highway rating represents a mix of open highway and rural road driving, typical of longer trips.
| Combined (L/100 km) | Combined fuel consumption rating shown in litres per 100 kilometres | The combined rating reflects 55% city driving and 45% highway driving.
| Combined (mpg) | The combined rating expressed in miles per imperial gallon | n/a 
| CO2 emissions (g/km) | The vehicle's tailpipe emissions of carbon dioxide shown in grams per kilometre for combined city and highway driving | n/a 
| CO2 rating | The vehicle's tailpipe emissions of carbon dioxide rated on a scale from 1 (worst) to 10 (best) | n/a 
| 
