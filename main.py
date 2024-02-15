import serpapi
import os
import csv

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('SERPAPI_KEY')
client = serpapi.Client(api_key=api_key)

search = 'cửa hàng'

result = client.search({
    'engine': 'google_maps',
    'type': 'search',
    'q': search,
    'll': '@10.762622,106.660172,3z',
})

print(result) #python main.py

output_file = 'demo.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(str(result))

print(f"Kết quả đã được lưu vào tệp tin: {output_file}")

# output_file_csv = 'demo.csv'
# with open(output_file_csv, 'w', newline='', encoding='utf-8') as csv_file:
#     fieldnames = ['Title', 'Address', 'Phone']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#
#     for place in result.get('places', []):
#         title = place.get('title', '')
#         address = place.get('address', '')
#         phone = place.get('phone', '')
#         writer.writerow({'Title': title, 'Address': address, 'Phone': phone})
#
# print(f"Thông tin đã được xuất vào tệp tin CSV: {output_file_csv}")