#%% Get number of pages from api
import requests
res = requests.get("https://hotell.difi.no/api/json/npd/wellbore/exploration?page=0")
pages = res.json()["pages"]

#%% Get all pages from api
data = []
for page_number in range(pages):
    res = requests.get("https://hotell.difi.no/api/json/npd/wellbore/exploration?page={}".format(page_number))
    d = res.json()["entries"]
    data.extend(d)
data

#%% Check if wlbNamePart is usable to decode wellbore names
# Works for wellbores without a reentry 
def print_well_name(d):
    well_parts = d["wlbNamePart1"],d["wlbNamePart2"],d["wlbNamePart3"],d["wlbNamePart4"],d["wlbNamePart5"],d["wlbNamePart6"]
    well_name = "{}/{}-{}{} {}{}".format(*well_parts).strip()
    if well_name==d["wlbWellboreName"]:
        pass
    else:
        print(d["wlbWellboreName"], well_parts, well_name)

for d in data:
    print_well_name(d)

#%%
import re
txt = data[0]["wlbWellboreName"]
txt = "6507/6-4 S"
def parse_well_name(txt):
    mo = re.match("(\d{1,4})\/(\d{1,2})(-\w{1,2})*-(\d{1,2})( \w{1,2})*", txt)
    if mo:
        quadrant, block, wellbore_id, well_number, well_type = mo.groups()
        if quadrant:
            quadrant = int(quadrant)
        if block:
            block = int(block)
        if wellbore_id:
           pass 
        if well_number:
            well_number = int(well_number)
        if well_type:
            well_type = well_type[1:]
        return {
            "quadrant": quadrant,
            "block": block,
            "wellbore_id": wellbore_id,
            "well_number": well_number,
            "well_type": well_type,
        }
    else:
        return None
parse_well_name(txt)

#%%
list(map(lambda f: parse_well_name(f["wlbWellboreName"]), data))

#%%
for d in data:
    parsed_well_name = parse_well_name(d["wlbWellboreName"])
    if str(parsed_well_name["quadrant"]) != d["wlbNamePart1"]:
        print(d["wlbWellboreName"])
    if str(parsed_well_name["block"]) != d["wlbNamePart2"]:
        print(d["wlbWellboreName"])
    if parsed_well_name["wellbore_id"]:
        if str(parsed_well_name["wellbore_id"]) != d["wlbNamePart3"]:
            print(d["wlbWellboreName"])
    if str(parsed_well_name["well_number"]) != d["wlbNamePart4"]:
        print(d["wlbWellboreName"])
    if parsed_well_name["well_type"]:
        if str(parsed_well_name["well_type"]) != d["wlbNamePart5"]:
            print(d["wlbWellboreName"])
