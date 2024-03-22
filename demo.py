import csv
import os
import serpapi

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('SERPAPI_KEY')

client = serpapi.Client(api_key=api_key)
results = client.search({
    'engine': 'google_maps',
    'q': 'pizza',
    'll': '@10.762622,106.660172,15.1z',
    'type': 'search',
})

local_results = results['local_results']

with open('demo.csv', 'w',  encoding='utf-8', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the headers
    csv_writer.writerow(["Title", "Address", "Phone Number", "Website"])

    # Write the data
    for result in local_results:
        csv_writer.writerow(
            [result["title"], result["address"], result["phone"] if "phone" in result else ""])

print('Done writing to CSV file.')