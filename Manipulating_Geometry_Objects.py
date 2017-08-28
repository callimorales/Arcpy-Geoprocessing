import arcpy
import math
arcpy.env.overwriteOutput = True
folder_path = r'E:\GEOG_173_Programming\Unit5\LabData\LabData'

import_lake_feature = arcpy.GetParameterAsText(0) #folder_path + '\NA_Big_Lakes.shp'
import_cities_feature = arcpy.GetParameterAsText(1) #folder_path + '\NA_Cities.shp'
output_lakes_feature = arcpy.GetParameterAsText(2) #folder_path + '\New_Lakes.shp'

arcpy.CopyFeatures_management (import_lake_feature, output_lakes_feature)

fields = [
    ('City', 'TEXT'),
    ('Admin', 'TEXT'),
    ('Country', 'TEXT'),
    #('Xcoord', 'FLOAT'),
    #('Ycoord', 'FLOAT'),
    ('Population', 'LONG'),
    ('Dist2Coord', 'FLOAT')
]

for field in fields:
    arcpy.AddField_management(*(output_lakes_feature,) + field)

city_name_list = []
city_admin_list = []
city_country_list = []
city_pop_list = []
#city_xcoord_list = []
#city_ycoord_list = []

city_cursor = arcpy.SearchCursor(import_cities_feature)

# read geometry (lat and long coords) and other data
# from cities shapefile and appends into appropriate lists. Uses geometry info built into arcpy
for city in city_cursor:
    city_name_list.append(city.CITY_NAME)
    city_admin_list.append(city.ADMIN_NAME)
    city_country_list.append(city.CNTRY_NAME)
    city_pop_list.append(city.Population)

lakes_cursor = arcpy.UpdateCursor(output_lakes_feature)
# defines lakes update cursor

city_length = len(city_pop_list)
# can use any of the lists cause it's the same number
# calculates total number of coords in city_list for later use

# read geometry (lat and long coords of centroid) na big lakes shapefile and append into
# appropriate (newly created) distance to centroid lists. calculates the distance
# between each city and each lake's centroid, and appends these distanes to a newly created list
for lake in lakes_cursor:
    #creates empty list
    distance_shore_list = []
    for city in range(0, city_length - 1):
        distance_to_shore = arcpy.Near_analysis(import_cities_feature, import_lake_feature)
        result = distance_to_shore.getOutput(0)
        print result
        distance_shore_list.append(result)

# use Near Distance field result and append it to your list

# finds the city with the shortest distance to each lake's centroid, and finds the index number of said city
    closest_city = min(distance_shore_list)
    print type(closest_city)
    closest_city_index = (distance_shore_list.index(closest_city))
    # grab index number, it is used to add the information that we need
# updates the rows for the 18 closest cities with the variables pulled out from the NA_Cities.shp,

    lake.City = city_name_list[closest_city_index]
    lake.Admin = city_name_list[closest_city_index]
    lake.Shore_Dist = closest_city*(0.001) #converts meters to kilometers
    
    lake.Country = city_country_list[closest_city_index]

    lakes_cursor.updateRow(lake)

del city_cursor, lakes_cursor, city, lake                       

print "done running code"
