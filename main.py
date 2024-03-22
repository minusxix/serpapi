import serpapi
import os
import csv

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('SERPAPI_KEY')
client = serpapi.Client(api_key=api_key)

search = 'sắt'

results = client.search({
    'engine': 'google_maps',
    'type': 'search',
    'q': search,
    'll': '@10.762622,106.660172,3z',
})

local_results = results['local_results']

print(results) #python main.py

# output_file = 'demo.txt'
# with open(output_file, 'w', encoding='utf-8') as file:
#     file.write(str(results))
#
# print(f'Kết quả đã được lưu vào tệp tin: {output_file}')

with open('output.csv', 'w', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(["Title", "Address", "Phone"])

    for result in local_results:
        csv_writer.writerow([result["title"], result["address"] if "address" in result else "", result["phone"] if "phone" in result else ""])

print('Done')