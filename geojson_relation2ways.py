import json


with open('DNP_HIKINR_ROUTES.geojson') as f:
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
    json.dump(data, outfile)
