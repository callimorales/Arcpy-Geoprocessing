import os
import arcpy
arcpy.env.overwriteOutput = True 
data_path = r'E:\GEOG_173_Programming\Unit7\LabData\LabData'

mxd = arcpy.mapping.MapDocument(data_path + '\LabData.mxd') #name of the mxd file used
dataframe = arcpy.mapping.ListDataFrames(mxd)[0]
tempPDF = data_path + r'\temp.pdf'
# temporary PDF to be appedned to Final

finalPDF_fname = data_path + '\Morales_C_Mapbook.pdf'
final_PDF = arcpy.mapping.PDFDocumentCreate(finalPDF_fname)
tempPDF = data_path + r'\temp.pdf'

inputRows = arcpy.SearchCursor(data_path + '\NA_Big_Lakes.shp')

Total_Area = 0
Lake_Total = 0

for row in inputRows:
    Total_Area += round(row.Area_km2,2)
    # round function goes in and delineates the total area of lakes is the summation of the field Area_km2,
    # The 2 is used to round up to 2 decimal places
    Lake_Total += 1

averageLakeSize = round(Total_Area/Lake_Total,2)

titlePageinfo = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[0]
#text file of our name and text boxes are numbered in the order you put them in


titlePageinfo.text = 'Lab 7 Map Document' + '\r' + 'Calli Morales' + '\r' + \
                     'Total Number of lakes; ' + str(Lake_Total) + '\r' + 'Average Lake Area: ' + str(averageLakeSize) +\
                     '\r' + 'Total Lake Area: ' + str(Total_Area)

#Legend = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT", "Legend")[0]
#Legend = elementPositionX = 6.8169
#Legend = elementPositionY = 9.4106
#Legend = elementHeight = 0.5831
#Legend = elementWidth = 0.595

#ScaleBar = arcpy.mapping.ListLayoutElements (mxd, "MAPSURROUND_ELEMENT", "ScaleBar")[0]
#ScaleBar.elementPositionX = 2.127
#ScaleBar.elementPositionY = 0.1

arcpy.mapping.ExportToPDF(mxd, data_path + r'\temp.pdf')
final_PDF.appendPages(data_path + r'\temp.pdf')

print 'Cover Page Done'

#############################


North_Arrow = arcpy.mapping.ListLayoutElements(mxd, "MAPSURROUND_ELEMENT", "North Arrow")[0]

North_Arrow = elementPositionX = 6.8169 
North_Arrow = elementPositionY = 9.4106 
North_Arrow = elementHeight = 0.595
North_Arrow = elementWidth = 0.5831

layerList = arcpy.mapping.ListLayers(mxd, "", dataframe) #places items from first data frame in this layer list

for layer in layerList:
        if layer.name == 'NA_Cities':
            layer.showLabels = True
        elif layer.name == 'NA_Big_Lakes':
            layer.showLabels = False

inputRows2 = arcpy.SearchCursor(data_path + '/NA_Big_Lakes.shp')
# used to display information for each of the lakes pdf pages we append to our final pdf

titleinfo = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")[0]

for row2 in inputRows2: # this for loop replaces the title information we had previously with what is used inside of it
    Area_New = round(row2.Area_km2, 2) # rounds field Area_km2 by two decimal places
    titleinfo.text = "Lake FID: " + str(row2.FID) + '\n' + "Lake Area: " + str(Area_New) 
    titleinfo.elementPositionX = 4.0229
    titleinfo.elementPositionY = 9.4191
    feature = row2.getValue(arcpy.Describe(data_path + "\NA_Big_Lakes.shp").ShapeFieldName)
    dataframe.extent = feature.extent
    dataframe.scale = dataframe.scale*1.2
    arcpy.mapping.ExportToPDF(mxd, data_path + r'\temp.pdf')
    final_PDF.appendPages(data_path + r'\temp.pdf')

final_PDF.saveAndClose()
print "done running my code"
