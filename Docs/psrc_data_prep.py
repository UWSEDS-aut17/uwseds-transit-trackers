#    Python script to process King County GTFS data 
import pandas as pd
import os
import zipfile

#    Reading data and making pandas dataframes 
#    from PSRC xlsx files
get_data ():
    households_df = pd.read_excel('C:/Users/ASUS/Desktop/uwsed/uwseds-group-transit-and-social-science/Data/2014-pr3-hhsurvey-households.xlsx')
    persons_df = pd.read_excel('C:/Users/ASUS/Desktop/uwsed/uwseds-group-transit-and-social-science/Data/2014-pr3-hhsurvey-persons.xlsx')
    trips_df = pd.read_excel('C:/Users/ASUS/Desktop/uwsed/uwseds-group-transit-and-social-science/Data/2014-pr3-hhsurvey-trips.xlsx')

#   Extract trips with origin and destination in King County
extract_trips ():
    king_trips_df = trips_df.loc[(trips_df['ocnty'] == 1) & (trips_df['dcnty'] == 1)]
    king_households_df = households_df.loc[households_df['hhid'].isin( king_trips_df['hhid'])]
    king_persons_df = persons_df.loc[persons_df['personid'].isin( king_trips_df['personID'])]


#   Function to merge 3 datasets

merge_data ():
    trips_households_df = king_trips_df.merge(king_households_df, left_on='hhid', right_on='hhid', how='inner')
    all_df = trips_households_df.merge(king_persons_df, left_on='personID', right_on='personid', how='inner')

#   Drop not needed columns
drop_columns ():
    


