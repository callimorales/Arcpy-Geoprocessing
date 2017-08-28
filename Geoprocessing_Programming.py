#folder_path =r"E:\GEOG 173 - Programming\Unit 3\LabData\LabData"

import arcpy

#arcpy.env.workspace = folder_path

arcpy.env.overwriteOutput = True

inp_buff_feature = arcpy.GetParameterAsText(0)
outp_buff_feature = arcpy.GetParameterAsText(1)
buff_distance = arcpy.GetParameterAsText(2)
inp_clip_feature = arcpy.GetParameterAsText(3)
outp_clip_feature = arcpy.GetParameterAsText(4)
out_table = arcpy.GetParameterAsText(5)
statistics_field = [["Population", "SUM"]]

arcpy.Buffer_analysis(inp_buff_feature, outp_buff_feature, buff_distance)

arcpy.Clip_analysis(inp_clip_feature, outp_buff_feature, outp_clip_feature)

arcpy.Statistics_analysis(outp_clip_feature, out_table, statistics_field, "CNTRY_NAME")
