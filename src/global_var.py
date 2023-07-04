"""
CONFIG FILE for DWD_DOWNLOADER, DATAFRAME_HELPER and DATA_HELPER
since webscrapper are blocked by the DWD URLS need to be added manualy

These lists are used as GLOBAL VAR for QOL puproses and are easily editable
"""
## BASE URL FOR ALL DIRECTORIES BY THE DWD
DWD_BASE_URL = "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/"

## AS of July 2023 all possible datasets that are both monthly and annual
MONTHLY_DATA_TYPE= ["air_temperature_mean", "precipitation", "sunshine_duration"]

## all possible intervals

DATA_TYPE= ["air_temperature_mean", "precipitation", "sunshine_duration"]

MONTHLY_DATA_TYPE= ["air_temperature_mean", "precipitation", "sunshine_duration"]

INTERVAL = ["annual", "monthly"]

## URLS to all txt files
URLS =["https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/air_temperature_mean/regional_averages_tm_year.txt",
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/precipitation/regional_averages_rr_year.txt",
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/sunshine_duration/regional_averages_sd_year.txt",
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/tropical_nights_tminGE20/regional_averages_tnes_year.txt",
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/summer_days/regional_averages_txas_year.txt",
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/precipGE20mm_days/regional_averages_rrsgs_year.txt",
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/precipGE10mm_days/regional_averages_rrsfs_year.txt",
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/ice_days/regional_averages_txcs_year.txt",
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/hot_days/regional_averages_txbs_year.txt",
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/frost_days/regional_averages_tnas_year.txt",
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/air_temperature_mean/regional_averages_tm_year.txt",
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_{}.txt", 
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/precipitation/regional_averages_rr_{}.txt",
       "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/sunshine_duration/regional_averages_sd_{}.txt"]

## Headers use for cleaning up dataframes and creating the CSV
HEADERS= ['Jahr;Monat', 'Brandenburg/Berlin', 'Brandenburg', 'Baden-Wuerttemberg',
          'Bayern', 'Hessen','Mecklenburg-Vorpommern', 'Niedersachsen',
          'Niedersachsen/Hamburg/Bremen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz',
          'Schleswig-Holstein', 'Saarland', 'Sachsen','Sachsen-Anhalt',
          'Thueringen/Sachsen-Anhalt', 'Thueringen', 'Deutschland']

## DEFAULT PATH if run from within ROOT
ROOT_DATA = "data"

# Months not hardcoded anywhere but for DEBUG purposes
MONTHS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

