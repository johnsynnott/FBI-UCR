import csv
import requests
from . import Data_Types
from . import States

def get(state, data_type, start_year=1960, end_year=2012):
    r = requests.post(
        'https://ucrdatatool.gov/Search/Crime/State/DownCrimeStatebyState.cfm/CrimeStatebyState.csv',
        data={
            'StateId':   state,
            'YearStart': start_year,
            'YearEnd':   end_year,
            'DataType':  data_type
        }
    )
    
    if data_type == Data_Types.PROPERTY_CRIME_QUANTITY:
        return parse_property_crime_quantity(r.text)
    elif data_type == Data_Types.PROPERTY_CRIME_RATE:
        return parse_property_crime_rate(r.text)
    elif data_type == Data_Types.VIOLENT_CRIME_QUANTITY:
        return parse_violent_crime_quantity(r.text)
    elif data_type == Data_Types.VIOLENT_CRIME_RATE:
        return parse_violent_crime_rate(r.text)
    else:
        return None


def get_rows(raw_data):
    clipped = raw_data.split('National or state offense totals are based on data from all reporting agencies and estimates for unreported areas.')[0].strip()
    
    reader = csv.reader(clipped.split('\n'), delimiter=',')
    rows = list(reader)

    headers = rows[5]
    
    return rows[6:]


def parse_property_crime_quantity(raw_data):
    rows = get_rows(raw_data)
    
    results = {}    
    for row in rows:
        if len(row) == 6:
            td = {}
            #for i in range(1,6):
            #    td[headers[i]] = row[i].strip()

            td['population'] = int(row[1].strip())
            td['total'] = int(row[2].strip())
            td['burglary'] = int(row[3].strip())
            td['larceny_theft'] = int(row[4].strip())
            td['vehicle_theft'] = int(row[5].strip())
            
            results[int(row[0])] = td
    
    return results


def parse_property_crime_rate(raw_data):
    rows = get_rows(raw_data)
    
    results = {}    
    for row in rows:
        if len(row) == 6:
            td = {}
            #for i in range(1,6):
            #    td[headers[i]] = row[i].strip()

            td['population'] = int(row[1].strip())
            td['total'] = float(row[2].strip())
            td['burglary'] = float(row[3].strip())
            td['larceny_theft'] = float(row[4].strip())
            td['vehicle_theft'] = float(row[5].strip())
            
            results[int(row[0])] = td
    
    return results
    

def parse_violent_crime_quantity(raw_data):
    rows = get_rows(raw_data)
    
    results = {}
    for row in rows:
        if len(row) == 7:
            td = {}
            #for i in range(1,7):
            #    td[headers[i]] = row[i].strip()

            td['population'] = int(row[1].strip())
            td['total'] = int(row[2].strip())
            td['murder'] = int(row[3].strip())
            td['rape'] = int(row[4].strip())
            td['robbery'] = int(row[5].strip())
            td['assault'] = int(row[6].strip())
            
            results[int(row[0])] = td
    
    return results


def parse_violent_crime_rate(raw_data):
    rows = get_rows(raw_data)
    
    results = {}
    for row in rows:
        if len(row) == 7:
            td = {}
            #for i in range(1,7):
            #    td[headers[i]] = row[i].strip()

            td['population'] = int(row[1].strip())
            td['total'] = float(row[2].strip())
            td['murder'] = float(row[3].strip())
            td['rape'] = float(row[4].strip())
            td['robbery'] = float(row[5].strip())
            td['assault'] = float(row[6].strip())
            
            results[int(row[0])] = td
    
    return results
