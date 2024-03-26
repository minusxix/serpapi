import serpapi
import os
import csv
from dotenv import load_dotenv
from unidecode import unidecode
import tkinter as tk
from tkinter import messagebox

load_dotenv()

class SearchApp:
    def __init__(self, master):
        self.master = master
        master.title("Serpapi Search App")

        self.label = tk.Label(master, text="Tìm kiếm:")
        self.label.pack()

        self.search_entry = tk.Entry(master)
        self.search_entry.pack()

        self.search_button = tk.Button(master, text="Tìm", command=self.run_search)
        self.search_button.pack()

    def run_search(self):
        search_term = self.search_entry.get()
        if not search_term:
            messagebox.showerror("Lỗi", "Vui lòng nhập từ khóa tìm kiếm!")
            return

        api_key = os.getenv('SERPAPI_KEY')
        client = serpapi.Client(api_key=api_key)

        results = client.search({
            'engine': 'google_maps',
            'type': 'search',
            'q': search_term,
            'll': '@10.762622,106.660172,3z',
        })

        local_results = results['local_results']

        output_file = f'{search_term}.csv'
        with open(output_file, 'w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Title', 'Address', 'Phone'])
            for result in local_results:
                csv_writer.writerow([unidecode(result.get('title', '')), unidecode(result.get('address', '')), result.get('phone', '')])

        messagebox.showinfo("Thành công", f"Xuất ra file thành công: {output_file}")

def main():
    root = tk.Tk()
    app = SearchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
