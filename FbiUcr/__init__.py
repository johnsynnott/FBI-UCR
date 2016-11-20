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
    print(headers)
    
    return rows[6:]


def parse_property_crime_quantity(raw_data):
    rows = get_rows(raw_data)
    
    results = {}    
    for row in rows:
        if len(row) == 6:
            td = {}
            #for i in range(1,6):
            #    td[headers[i]] = row[i].strip()

            td['population'] = row[1].strip()
            td['total'] = row[2].strip()
            td['burglary'] = row[3].strip()
            td['larceny_theft'] = row[4].strip()
            td['vehicle_theft'] = row[5].strip()    
            
            results[row[0]] = td
    
    return results


def parse_property_crime_rate(raw_data):
    rows = get_rows(raw_data)
    
    results = {}    
    for row in rows:
        if len(row) == 6:
            td = {}
            #for i in range(1,6):
            #    td[headers[i]] = row[i].strip()

            td['population'] = row[1].strip()
            td['total'] = row[2].strip()
            td['burglary'] = row[3].strip()
            td['larceny_theft'] = row[4].strip()
            td['vehicle_theft'] = row[5].strip()    
            
            results[row[0]] = td
    
    return results
    

def parse_violent_crime_quantity(raw_data):
    rows = get_rows(raw_data)
    
    results = {}
    for row in rows:
        if len(row) == 7:
            td = {}
            #for i in range(1,7):
            #    td[headers[i]] = row[i].strip()

            td['population'] = row[1].strip()
            td['total'] = row[2].strip()
            td['murder'] = row[3].strip()
            td['rape'] = row[4].strip()
            td['robbery'] = row[5].strip()
            td['assault'] = row[6].strip()         
            
            results[row[0]] = td
    
    return results


def parse_violent_crime_rate(raw_data):
    rows = get_rows(raw_data)
    
    results = {}
    for row in rows:
        if len(row) == 7:
            td = {}
            #for i in range(1,7):
            #    td[headers[i]] = row[i].strip()

            td['population'] = row[1].strip()
            td['total'] = row[2].strip()
            td['murder'] = row[3].strip()
            td['rape'] = row[4].strip()
            td['robbery'] = row[5].strip()
            td['assault'] = row[6].strip()         
            
            results[row[0]] = td
    
    return results