# RAINDEER

Analysis of precipitation in Germany. 

This project is done as part of the Research Software Engineering course Group Project. 

* [Problem Description](#problem-description)
* [How to get started and Requirements](#how-to-get-started-requirements)
* [Running the Program](#running-the-program)
  * [CLI](#cli)
* [Dataset](#dataset)
* [Contributing](https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/CONTRIBUTING.md)
* [Code of Conduct](https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/code_of_conduct.md)
* [Licencse](https://gitup.uni-potsdam.de/jubruns/raindeer/main/LICENSE) 
* [Citation](https://gitup.uni-potsdam.de/jubruns/raindeer/main/CITATION.cff)



## Problem Description

### Research questions:
1) 
2)
3)
4)
5)

## How to get Started

## Running the Program

### Downloading Data
Currently with our Download tool you can download any monthly or yearly data from the German weather service
(Deutscher Wetter Dienst. **Seasonal data is not yet implemented)

Use the following function to download the data: 
```python 
download( *URLS*, *MONTHS*, *DIR*)
```
URLS and MONTHS can be lists or a string, internally it will be converted to a list. 

Monthly urls use the following layout: 

https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_01.txt
Replace the 01.txt with a {}.txt at the end of the url. 

In case you use yearly data which has not months as a parameter add a "0" as input for months or any other string. 
Yearly URL do not need to be edited. 

example list: 

```python
   url_list = ['url1', 'url2',..., 'urlx']
   months = ['01','02','03',...'12']
   
```

The directory given will not consider the root of the project instead you need to take the relative path from your CWD into consideration
### CLI

### Jupyter Notebook

### Module


## Datasets


## Getting Involved

[Contributing](https://gitup.uni-potsdam.de/jubruns/raindeer/main/CONTRIBUTING.md)
[Code of Conduct](https://gitup.uni-potsdam.de/jubruns/raindeer/main/CONDUCT.md)


[Licencse](https://gitup.uni-potsdam.de/jubruns/raindeer/main/LICENSE) 
[Citation](https://gitup.uni-potsdam.de/jubruns/raindeer/main/CITATION.cff)
