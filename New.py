import tkinter as tk
from tkinter import ttk
from googlesearch import search

def search_professors():
    keywords = keywords_entry.get()
    num_results = int(num_results_entry.get())

    if keywords:
        search_query = f'{keywords} professor (site:.edu OR site:linkedin.com)'
        search_results = search(search_query, num=num_results, stop=num_results, pause=2)
        
        if search_results:
            result_text.delete(1.0, tk.END)
            for index, result in enumerate(search_results, start=1):
                result_text.insert(tk.END, f"{index}. {result}\n")
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "No results found.")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter keywords.")

# Create main window
root = tk.Tk()
root.title("Professor Search")

# Create keyword entry
keywords_label = ttk.Label(root, text="Enter keywords:")
keywords_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
keywords_entry = ttk.Entry(root, width=50)
keywords_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# Create number of results entry
num_results_label = ttk.Label(root, text="Number of results:")
num_results_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
num_results_entry = ttk.Entry(root, width=10)
num_results_entry.grid(row=1, column=1, padx=5, pady=5)

# Create search button
search_button = ttk.Button(root, text="Search", command=search_professors)
search_button.grid(row=1, column=2, padx=5, pady=5)

# Create search result text area
result_text = tk.Text(root, width=70, height=15)
result_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
