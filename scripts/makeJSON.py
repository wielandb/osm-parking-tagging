import json
import os
import sys
import re

# Read the file ..\parking_new.md
with open(os.path.join('..', 'parking_new.md'), 'r') as f:
    data = f.read()

# Split the file into lines
lines = data.splitlines()

# Create a list of dictionaries
parkingJSON = []
parkingTXTWay = {}
parkingTXTArea = {}
for line in lines:
    # skip the first and second line
    if "-------" in line or "                                                            " in line:
        continue
    if "|" not in line:
        continue
    # Split the line into fields
    fields = line.split('|')
    print(fields)
    # Create a dictionary
    # the first field is the image
    # the second field is the tagging for an area
    # the third field is the tagging for a way
    image = fields[1].strip()
    # regex to get the part between []
    print(image)
    sign_identifier = re.search(r'\[(.*?)\]', image).group(1)
    print(sign_identifier)
    # get the way the osm traffic sign key would be tagged, by replacing _ with ,
    osm_traffic_sign = sign_identifier.replace("_", ",")
    # regex to get the part between ()
    url_1 = "https://raw.githubusercontent.com/wielandb/osm-parking-tagging/main/"
    url_2 = re.search(r'\((.*?)\)', image).group(1)
    img_url = url_1 + url_2
    area = fields[2].strip()
    areaTagList = area.split('<br />')
    areaTagList = [x.strip().replace("`", "") for x in areaTagList]
    # Create a dictionary where the key is everything before = and the value is everything after =
    areaTags = {}
    for tag in areaTagList:
        if "=" in tag:
            key, value = tag.split('=')
            areaTags[key] = value
    way = fields[3].strip()
    wayTagList = way.split('<br />')
    wayTagList = [x.strip().replace("`", "") for x in wayTagList]
    # Create a dictionary where the key is everything before = and the value is everything after =
    wayTags = {}
    for tag in wayTagList:
        if "=" in tag:
            key, value = tag.split('=')
            wayTags[key] = value
    print(wayTags)
    print(areaTags)
    # Create a dictionary to store the data
    parkingJSON.append({
        'sign_identifier': sign_identifier,
        'img_url': img_url,
        'area_tags': areaTags,
        'way_tags': wayTags
    })
    tmpParkingTxt = ""
    for key, value in areaTags.items():
        tmpParkingTxt += key + "=" + value + "LINEBREAK"
    parkingTXTArea[sign_identifier] = tmpParkingTxt
    tmpParkingTxt = ""
    for key, value in wayTags.items():
        tmpParkingTxt += key + "=" + value + "LINEBREAK"
    parkingTXTWay[sign_identifier] = tmpParkingTxt


# save the parkingJSON data to export/json/parking_new.json
with open(os.path.join('..','export', 'json', 'parking_new.json'), 'w') as f:
    json.dump(parkingJSON, f, indent=2)

# save the parkingTxt data to export/txt/parking_new_[type].json
with open(os.path.join('..', 'export', 'txt', 'parking_new_area.json'), 'w') as f:
    json.dump(parkingTXTArea, f, indent=2)
with open(os.path.join('..', 'export', 'txt', 'parking_new_way.json'), 'w') as f:
    json.dump(parkingTXTWay, f, indent=2)