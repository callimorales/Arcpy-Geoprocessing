folder_path = r"E:\GEOG_173_Programming\Unit4\LabData\LabData"

import arcpy

arcpy.env.overwriteOutput = True

# copying NA_Cities shapeile

arcpy.CopyRows_management (folder_path + '\NA_Cities.shp', folder_path +'\NA_Cities_table4.dbf')

fc = folder_path + '\NA_Cities_table4.dbf'

# Name of table
# Fields which will be analyzed = ['FIPS_CNTRY', 'Population']

cursor = arcpy.da.UpdateCursor(fc,['FIPS_CNTRY', 'Population'])

for row in cursor:
    if row[0] == 'US' and row[1] < 8000000:
        cursor.deleteRow()
    elif row[0] == 'MX' and row[1] < 8000000:
        cursor.deleteRow()
    elif row[0] == 'CA' and row[1] < 3000000:
        cursor.deleteRow()

del row, cursor 


print "Done with running code"
