import subprocess
import requests
from arcgis2geojson import arcgis2geojson as geoj

# links = ['/agsadaptor/rest/services/park/CarolinaThreadTrail/FeatureServer', '/agsadaptor/rest/services/park/CarolinaThreadTrail/MapServer', '/agsadaptor/rest/services/park/CharlottetoStatesville_SeamTrail/FeatureServer', '/agsadaptor/rest/services/park/CharlottetoStatesville_SeamTrail/MapServer', '/agsadaptor/rest/services/park/ConservationLand/FeatureServer', '/agsadaptor/rest/services/park/ConservationLand/MapServer', '/agsadaptor/rest/services/park/CountyOpenSpace/FeatureServer', '/agsadaptor/rest/services/park/CountyOpenSpace/MapServer', '/agsadaptor/rest/services/park/CrossCharlotteTrail/FeatureServer', '/agsadaptor/rest/services/park/CrossCharlotteTrail/MapServer', '/agsadaptor/rest/services/park/CTT_XCLT_MCT_TrailSystems/FeatureServer', '/agsadaptor/rest/services/park/CTT_XCLT_MCT_TrailSystems/MapServer', '/agsadaptor/rest/services/park/Discgolfcourses/MapServer', '/agsadaptor/rest/services/park/FA_points_trails/MapServer', '/agsadaptor/rest/services/park/GovernmentFacility/FeatureServer', '/agsadaptor/rest/services/park/GovernmentFacility/MapServer', '/agsadaptor/rest/services/park/Greenprint_Parcels/FeatureServer', '/agsadaptor/rest/services/park/Greenprint_Parcels/MapServer', '/agsadaptor/rest/services/park/Greenprint_Park_Gap_Areas/FeatureServer', '/agsadaptor/rest/services/park/Greenprint_Park_Gap_Areas/MapServer', '/agsadaptor/rest/services/park/Greenway_Entrances/FeatureServer', '/agsadaptor/rest/services/park/Greenway_Entrances/MapServer', '/agsadaptor/rest/services/park/Greenway_Masterplan/FeatureServer', '/agsadaptor/rest/services/park/Greenway_Masterplan/MapServer', '/agsadaptor/rest/services/park/Greenway_Mile_Markers/FeatureServer', '/agsadaptor/rest/services/park/Greenway_Mile_Markers/MapServer', '/agsadaptor/rest/services/park/Greenway_Trails_NoSegments/FeatureServer', '/agsadaptor/rest/services/park/Greenway_Trails_NoSegments/MapServer', '/agsadaptor/rest/services/park/Greenway_Trails/FeatureServer', '/agsadaptor/rest/services/park/Greenway_Trails/MapServer', '/agsadaptor/rest/services/park/GreenwayParkPlanning/MapServer', '/agsadaptor/rest/services/park/MecklenburgParkEasements/FeatureServer', '/agsadaptor/rest/services/park/MecklenburgParkEasements/MapServer', '/agsadaptor/rest/services/park/MecklenburgParkParcels/FeatureServer', '/agsadaptor/rest/services/park/MecklenburgParkParcels/MapServer', '/agsadaptor/rest/services/park/MecklenburgParkProperty/FeatureServer', '/agsadaptor/rest/services/park/MecklenburgParkProperty/MapServer', '/agsadaptor/rest/services/park/NaturePreserveTrails/FeatureServer', '/agsadaptor/rest/services/park/NaturePreserveTrails/MapServer', '/agsadaptor/rest/services/park/NR_PlanningViewOnly/MapServer', '/agsadaptor/rest/services/park/NRPlanningMap/MapServer', '/agsadaptor/rest/services/park/Park_NR_trails/MapServer', '/agsadaptor/rest/services/park/ParkAdvisory/FeatureServer', '/agsadaptor/rest/services/park/ParkAdvisory/MapServer', '/agsadaptor/rest/services/park/ParkAmenity/FeatureServer', '/agsadaptor/rest/services/park/ParkAmenity/MapServer', '/agsadaptor/rest/services/park/ParkChapters2017/MapServer', '/agsadaptor/rest/services/park/ParkEasement_ParkParcel_Centroid/FeatureServer', '/agsadaptor/rest/services/park/ParkEasement_ParkParcel_Centroid/MapServer', '/agsadaptor/rest/services/park/ParkInvestments/FeatureServer', '/agsadaptor/rest/services/park/ParkInvestments/MapServer', '/agsadaptor/rest/services/park/ParkLocator/MapServer', '/agsadaptor/rest/services/park/ParkNukeBlocks/MapServer', '/agsadaptor/rest/services/park/ParkRegions/FeatureServer', '/agsadaptor/rest/services/park/ParkRegions/MapServer', '/agsadaptor/rest/services/park/Parks/FeatureServer', '/agsadaptor/rest/services/park/Parks/MapServer', '/agsadaptor/rest/services/park/ParkSurvey/FeatureServer', '/agsadaptor/rest/services/park/ParkSurvey/MapServer', '/agsadaptor/rest/services/park/ParkTrailPlants/MapServer', '/agsadaptor/rest/services/park/ParkTrails_Other/FeatureServer', '/agsadaptor/rest/services/park/ParkTrails_Other/MapServer', '/agsadaptor/rest/services/park/Service_Area_Analysis/FeatureServer', '/agsadaptor/rest/services/park/Service_Area_Analysis/MapServer', '/agsadaptor/rest/services/park/Town_Park_Parcels/FeatureServer', '/agsadaptor/rest/services/park/Town_Park_Parcels/MapServer', '/agsadaptor/rest/services/park/UrbanTrailOpportunityZones/FeatureServer', '/agsadaptor/rest/services/park/UrbanTrailOpportunityZones/MapServer', '/agsadaptor/rest/services/park/Verifresh_Freshlist/FeatureServer', '/agsadaptor/rest/services/park/Verifresh_Freshlist/MapServer']

# errlinks = []

# for i in links:
# 	try:
# 		subprocess.run(["esri2geojson", "https://maps.mecklenburgcountync.gov"+i+"/0", i.split("/")[-2]+"_"+i.split("/")[-1]+".geojson"])
# 	except BaseException:
# 		errlinks.append("https://maps.mecklenburgcountync.gov"+i)

# print(errlinks)





#"C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\Service_Area_Analysis_FeatureServer.geojson"]#,
#"C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\Service_Area_Analysis_MapServer.geojson",
files = [
# "C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\Town_Park_Parcels_MapServer.geojson",
# "C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\Verifresh_Freshlist_FeatureServer.geojson",
# "C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\ConservationLand_FeatureServer.geojson",
# "C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\ConservationLand_MapServer.geojson",
# "C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\Discgolfcourses_MapServer.geojson
# "C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\GreenwayParkPlanning_MapServer.geojson"]
# "C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\MecklenburgParkEasements_FeatureServer.geojson"]
"C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\MecklenburgParkEasements_MapServer.geojson"]
# "C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\MecklenburgParkProperty_MapServer.geojson",
# "C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\ParkChapters2017_MapServer.geojson",
# "C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\ParkNukeBlocks_MapServer.geojson",
# "C:\\Users\\finns\\iCloudDrive\\python\\gis\\park-map\\layers\\ParkTrailPlants_MapServer.geojson"]


for file in files:
	print(file)
	name = file.split("\\")[-1].split(".")[0].split("_")[:-1]
	name = "_".join(name)
	typ = file.split("\\")[-1].split(".")[0].split("_")[-1]
	print(name,typ)
	layer = input("layer: ")
	print("https://maps.mecklenburgcountync.gov/agsadaptor/rest/services/park/"+name+"/"+typ+"/"+layer+"/?f=geojson")
	result = subprocess.run(["curl", "https://maps.mecklenburgcountync.gov/agsadaptor/rest/services/park/"+name+"/"+typ+"/"+layer+"/f=geojson"], capture_output=True, text=True)
	print(result.stdout)
	print(geoj(result.stdout))