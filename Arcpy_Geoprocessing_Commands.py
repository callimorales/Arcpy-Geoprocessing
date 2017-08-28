##############################
# 1. Read (and print) all files from the LabData folder
##############################
print "\nSection 1"
import  os

folder_path = (r'E:\GEOG 173 - Programming\Unit 2\LabData\LabData')
# acessing correct folder path to download items

file_list = os.listdir(folder_path) # reads files in folder_path
print
print file_list
# print files in the folder path


##############################
# 2. Identify (and print) the number of shapefiles in the file list and their names
##############################

for file_name in file_list:
# loop was used over list using a plain for-in loop
# file_name is assigned to the items in file_list
 if file_name.endswith('shp'):
        #looks for file_names that are shapefiles
        print "Shapefile Name:", file_name
        #if conditions are met shapefile file_names will be printed

num_shapefiles = 0

#starts the count for number of shapefiles at 0
##############################
# 3. Use ArcPy to execute any geoprocessing command
##############################
shapefile_name_list = list()
#creates an empty list

for file_name in file_list: 
    if file_name.endswith('shp'):
        num_shapefiles=num_shapefiles+1
        #adds 1 to the count everytime a .shp file is found
        shapefile_name_list.append(file_name)
        #if conditons are met: file_name that are .shp files will be appended to the empty list
        
print "\nNumber of Shapefiles:", num_shapefiles #prints number of shapefiles
print "\nShapefile Name List:", shapefile_name_list #prints shapefile name list

##############################
# 3. Use ArcPy to execute any geoprocessing command
##############################

print "\nSection 3"

import arcpy
# imports arcpy to use geoprocessing codes
arcpy.env.overwiteOutput = True
# sets environment workspace to the 'folder_path'
# allows oen to replace create an output with the same name as an existing file by overwriting the file
arcpy.Buffer_analysis(folder_path + "\NA_Big_Lakes.shp", folder_path + "\Buffered_NA_Big_Lakes.shp", "75 Kilometers")
# creates a buffer analysis for the Lakes Shapefile of 75 Kilometers
arcpy.Buffer_analysis(folder_path + "\NA_Cities.shp", folder_path + "\Buffered_NA_Cities.shp", "50 Kilometers")
# creates a buffer analysis for the Cities Shapefile of 50 Kilometers
arcpy.Union_analysis ([folder_path + "\NA_Big_Lakes.shp", folder_path + "\North_America.shp"], folder_path + "\union_Lakes_NAmerica1.shp")
# creates a united Shapeile of the Lakes and North America Shapefiles
#print file_list.split("file_list")
#print file_list.sort(reverse = True)

