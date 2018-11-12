import json
import sys

# USAGE: python relation2ways.py in.json out.json
# or in.geojson...

if len(sys.argv) < 3:
    sys.exit("ERROR! run: \"python relation2ways.py in.json out.json\"")

with open(sys.argv[1]) as f:
    data = json.load(f)

for feature in data['features']:
    
    if '@relations' in feature['properties'] and feature['properties']['@relations']:
        
        i = 0
        
        for relation in feature['properties']['@relations']:
                        
            if 'name:en' in relation['reltags']:
                
                if i == 0:
            
                    feature['properties']['name:en'] = relation['reltags']['name:en']
                else:
                    
                    feature['properties']['name:en_'+str(i)] = relation['reltags']['name:en']
                    
            if 'network' in relation['reltags']:
                
                if i == 0:
            
                    feature['properties']['network'] = relation['reltags']['network']
                else:
                    
                    feature['properties']['network_'+str(i)] = relation['reltags']['network']
                
            i += 1

with open('out.geojson', 'w') as outfile:
    print("Writing to " + sys.argv[2])
    json.dump(data, outfile)

print("done.")