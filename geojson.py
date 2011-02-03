import re

id_field = 'Eqid'
lat_field = 'Lat'
lon_field = 'Lon'

num_pat = re.compile('^-?[0-9]*(\.?[0-9]+)?([eE]-?[0-9]+)?$')
def number(value):
    if num_pat.match(value):
        return float(value)
    return value

def row2feature(row):
    feature = {'type': 'Feature',
               'id': row[id_field],
               'properties': {},
               'geometry': {'type': 'Point',
                            'coordinates': [float(row[lon_field]), float(row[lat_field])]}}
    for k in row.keys():
        if not (k in non_props):
            feature['properties'][k] = number(row[k])
    return feature

if __name__ == '__main__':
    import simplejson, csv, optparse

    parser = optparse.OptionParser()
    opts, args = parser.parse_args()

    input_filename = args.pop(0)
    input = csv.DictReader(open(input_filename))

    non_props = [lat_field, lon_field]

    features = map(row2feature, input)
    collection = {'type': 'FeatureCollection',
                  'features': features}
    print simplejson.dumps(collection)
