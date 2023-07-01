# TODO added into a single list. just for testing seperated!
DWD_BASE_URL = "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/"
MONTHLY_DATA_TYPE= ["air_temperature_mean", "precipitation", "sunshine_duration"]
INTERVAL = ["annual", "monthly"]

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

MONTHS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
ROOT_DATA = "../data"

HEADERS= ['Jahr;Monat', 'Brandenburg/Berlin', 'Brandenburg', 'Baden-Wuerttemberg',
          'Bayern', 'Hessen','Mecklenburg-Vorpommern', 'Niedersachsen',
          'Niedersachsen/Hamburg/Bremen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz',
          'Schleswig-Holstein', 'Saarland', 'Sachsen','Sachsen-Anhalt',
          'Thueringen/Sachsen-Anhalt', 'Thueringen', 'Deutschland']

