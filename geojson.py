import csv, simplejson, optparse, re

parser = optparse.OptionParser()
opts, args = parser.parse_args()

input_filename = args.pop(0)
input = csv.DictReader(open(input_filename))

lat_field = 'Lat'
lon_field = 'Lon'
non_props = [lat_field, lon_field]

num_pat = re.compile('^-?[0-9]*(\.?[0-9]+)?([eE]-?[0-9]+)?$')
def number(value):
    if num_pat.match(value):
        return float(value)
    return value

features = []
for row in input:
    feature = {'properties': {},
               'geometry': {'type': 'Point',
                            'coordinates': [float(row[lon_field]), float(row[lat_field])]}}
    for k in row.keys():
        if not (k in non_props):
            feature['properties'][k] = number(row[k])
    features.append(feature)

collection = {'type': 'FeatureCollection',
              'features': features}
print simplejson.dumps(collection)
