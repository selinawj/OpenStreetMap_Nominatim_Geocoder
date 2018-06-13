from nominatim import Nominatim, NominatimReverse
import json
import csv
import pandas as pd

nom = Nominatim()

with open('neighborhood.csv', 'wb') as neighborhoodFile: #stores neighborhoods as new csv file
    df = pd.read_csv('sample_coords.csv') #parses in these coordinates for geocoding
    # lat = df.ix[:,14]
    # lon = df.ix[:,13]
    for i in range(0, len(df)):
        lat = df.ix[i,1]
        lon = df.ix[i,0]
        coords = str(lon) + ", " + str(lat)
        result = nom.query(coords) #start geocode query for each entry
        neighborhoodDetails = result[0]['display_name'] #obtain first query elements
        neighborhoodList = neighborhoodDetails.split(",") #convert unicode to list elements separated by ","
        neighborhood = neighborhoodList[2]
        if coords != "nan, nan":
            output = neighborhood
            neighborhoodFile.write(output)
            neighborhoodFile.write('\n')
            print i
        else:
            output = " "
            neighborhoodFile.write(output)
            neighborhoodFile.write('\n')
