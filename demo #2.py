import serpapi
import os
import csv
import subprocess
import pandas as pd
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
from unidecode import unidecode
from tkinter import messagebox

load_dotenv()

def search_and_export(search_term, start_index):
    api_key = os.getenv('SERPAPI_KEY')
    client = serpapi.Client(api_key=api_key)

    try:
        results = client.search({
            'engine': 'google_maps',
            'type': 'search',
            'q': search_term,
            'll': '@10.762622,106.660172,3z',
            'start': start_index,
        })

        local_results = results['local_results']

        output_file = f'{search_term}_{start_index}.csv'
        with open(output_file, 'w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Title', 'Address', 'Phone'])
            for result in local_results:
                csv_writer.writerow([unidecode(result.get('title', '')), unidecode(result.get('address', '')), result.get('phone', '')])

        file_path = f'{search_term}_{start_index}.xlsx'
        df = pd.read_csv(output_file)
        df.to_excel(file_path, index=None, header=True)
        try:
            os.startfile(file_path)
        except AttributeError:
            subprocess.call(['xdg-open', file_path])

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def search_button_clicked():
    search_term = search_entry.get()
    start_index = int(start_entry.get())
    search_and_export(search_term, start_index)

def increase_start():
    current_start = int(start_entry.get())
    new_start = current_start + 20
    start_entry.delete(0, tk.END)
    start_entry.insert(0, str(new_start))

def decrease_start():
    current_start = int(start_entry.get())
    new_start = max(0, current_start - 20)
    start_entry.delete(0, tk.END)
    start_entry.insert(0, str(new_start))

root = tk.Tk()
root.title("Google Maps Search")

search_label = ttk.Label(root, text="Tìm kiếm:")
search_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

search_entry = ttk.Entry(root, width=30)
search_entry.grid(row=0, column=1, padx=5, pady=5)

start_label = ttk.Label(root, text="Bắt đầu:")
start_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

start_entry = ttk.Entry(root, width=10)
start_entry.insert(0, "0")
start_entry.grid(row=1, column=1, padx=5, pady=5)

search_button = ttk.Button(root, text="Tìm kiếm", command=search_button_clicked)
search_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

increase_button = ttk.Button(root, text="Tăng", command=increase_start)
increase_button.grid(row=1, column=2, padx=5, pady=5)

decrease_button = ttk.Button(root, text="Giảm", command=decrease_start)
decrease_button.grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
