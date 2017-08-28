import os
import arcpy
from arcpy.sa import * #imports spatial analyst module
arcpy.env.overwriteOutput = True

folder_path = r'E:\GEOG_173_Programming\Unit6\LabData\LabData'

arcpy.CheckOutExtension('Spatial') #checks out spatial analyst extension 

Landsat = folder_path + '\Landsat.tif' #sets the variable landsat to the TIFF file in our workspace

description1 = arcpy.Describe(Landsat + '/band_1') 
# use built in function to call out number of rows, colums, spatial height

print 'TIF file is = ' + str(description1.height) + ' by ' + str(description1.width)
#describes number of pixels outputting their value in the format hieght multiplied by width
print 'TIF file is ' + str(description1.meanCellHeight) + 'm' + ' by ' + str(description1.meanCellWidth) + 'm'
#describes the resoultion of the tiff file
print '_____________________________________________'

description2 = arcpy.Describe(Landsat) #describes the entirety of the Landsat tiff file, outputting the total number of bands and datum below

print 'Datum = ' + description2.spatialReference.Name + '\nNumber of Bands = ' + str(description2.bandCount)
#prints out reference information 

NIR = arcpy.Raster(Landsat + '/Band_4') # Near Infrared band is assigned to a variable
Red = arcpy.Raster(Landsat + '/Band_3') # Red band is assigned to a variable
Numerator = arcpy.sa.Float(NIR - Red) # numerator is assigned the value of the NIR variable minus the Red variable 
Denominator = arcpy.sa.Float(NIR + Red) # denominator is assigned the value of the addition of the NIR and the Red variables
NDVI = arcpy.sa.Divide(Numerator, Denominator)
# equation for NDVI is the difference between NIR and Red bands divided by the summation of the NIR and Red bands for the given tiff file

NDVI.save(folder_path + '\NDVI1.tif') #information is saved into a new tiff file with NDVI information

NDVI_Raster = folder_path + '\NDVI1.tif' #variable is assigned the newly created tiff file

Range1 = RemapRange([[-1, 0, 1], [0, 0.3, 2], [0.3, 1, 3]]) # Class is defined for the reclassification scheme specified by the project guidelines

Reclass = Reclassify(NDVI_Raster, 'Value', Range1) #reclassifies the tiff file in accordance to the range presented above

Reclass.save(folder_path + '\_Reclassified.tif') #saves information in a newly created reclassified tiff file


NDVI_Val = arcpy.GetCellValue_management(NDVI_Raster, '349201, 3772463')
# gets the cell value of the NDVI Raster File at specified coordinates and assigns them a variable 
Reclass_Val = arcpy.GetCellValue_management(folder_path + '\_reclassified.tif', '349201, 3772463')
# gets the cell value of the Reclassified raster file at the specified coordinates and assigns them a variable
print 'NDVI Cell Value = ' + str(NDVI_Val) + ' and Reclassified Cell Value = ' + str(Reclass_Val) + ' at coordinates 349201, 3772463'
# prints NDVI cell value plus the reclassified NDVI value from the variable set above

print '_____________________________________________'


#### NDWI ####

NIR2 = arcpy.Raster(Landsat + '/Band_4') # Near Infrared band is assigned to a variable
Green = arcpy.Raster(Landsat + '/Band_2') # Green band is assigned to a variable
Numerator2 = arcpy.sa.Float(NIR2 - Green) #  Numerator2 is assigned the value of the NIR variable minus the Green variable
Denominator2 = arcpy.sa.Float(NIR2 + Green) # Denominator2 is assigned the value of the addition of the NIR and the Green variables
NDWI = arcpy.sa.Divide(Numerator2, Denominator2)
# equation for NDWI is the difference between NIR and Green bands divided by the summation of the NIR and Green bands for the given tiff file


NDWI.save(folder_path + '\NDWI1.tif') # information is saved into a new tiff file with NDWI information

NDWI_Raster = folder_path + '\NDWI1.tif' # variable is assigned the newly created tiff file

Range2 = RemapRange([[-1, 0, 1], [0, 0.3, 2], [0.3, 1, 3]])
# Class is defined for the reclassification scheme specified by user inputted reclassification range

Reclass2 = Reclassify(NDWI_Raster, 'Value', Range2) #reclassifies the tiff file in accordance to the range presented above

Reclass2.save(folder_path + '\_Reclassified2.tif') #saves information in a newly created reclassified tiff file


NDWI_Val = arcpy.GetCellValue_management(NDWI_Raster, '349201, 3772463')
# gets the cell value of the NDWI Raster File at specified coordinates and assigns them a variable
Reclass_Val2 = arcpy.GetCellValue_management(folder_path + '\_reclassified2.tif', '349201, 3772463')
# gets the cell value of the Reclassified raster file at the specified coordinates and assigns them a variable
print 'NDWI Cell Value = ' + str(NDWI_Val) + ' and Reclassified Cell Value = ' + str(Reclass_Val2) + ' at coordinates 349201, 3772463'
# prints NDVI cell value plus the reclassified NDWI value from the variable set above


print 'Done with my code'
