import tkinter as tk
import pandas as pd
from tkinter import filedialog

class Form:
    def __init__(self, master):
        self.master = master
        self.master.title("Formulario de Entrada")
        self.master.geometry("500x400") # set a fixed window size for better layout control

        # create a frame to hold the form fields
        self.form_frame = tk.Frame(master, padx=20, pady=20) # add padding to the frame
        self.form_frame.pack(pady=20) # add padding to the bottom of the frame

        # create the form fields with some padding
        self.company_label = tk.Label(self.form_frame, text="Nombre de la empresa", padx=10, pady=5)
        self.company_label.grid(row=0, column=0, sticky="w")
        self.company_entry = tk.Entry(self.form_frame, bd=2, relief="solid")
        self.company_entry.grid(row=0, column=1, sticky="w", padx=10, pady=5)

        self.plant_label = tk.Label(self.form_frame, text="Planta", padx=10, pady=5)
        self.plant_label.grid(row=1, column=0, sticky="w")
        self.plant_entry = tk.Entry(self.form_frame, bd=2, relief="solid")
        self.plant_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)

        self.line_label = tk.Label(self.form_frame, text="Línea de producción", padx=10, pady=5)
        self.line_label.grid(row=2, column=0, sticky="w")
        self.line_entry = tk.Entry(self.form_frame, bd=2, relief="solid")
        self.line_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)

        self.oven_label = tk.Label(self.form_frame, text="Número de horno", padx=10, pady=5)
        self.oven_label.grid(row=3, column=0, sticky="w")
        self.oven_entry = tk.Entry(self.form_frame, bd=2, relief="solid")
        self.oven_entry.grid(row=3, column=1, sticky="w", padx=10, pady=5)

        self.material_label = tk.Label(self.form_frame, text="Material", padx=10, pady=5)
        self.material_label.grid(row=4, column=0, sticky="w")
        self.material_entry = tk.Entry(self.form_frame, bd=2, relief="solid")
        self.material_entry.grid(row=4, column=1, sticky="w", padx=10, pady=5)

        self.first_observation_label = tk.Label(self.form_frame, text="Fecha de la primera observación", padx=10, pady=5)
        self.first_observation_label.grid(row=5, column=0, sticky="w")
        self.first_observation_entry = tk.Entry(self.form_frame, bd=2, relief="solid")
        self.first_observation_entry.grid(row=5, column=1, sticky="w", padx=10, pady=5)

        self.last_observation_label = tk.Label(self.form_frame, text="Fecha de la última observación", padx=10, pady=5)
        self.last_observation_label.grid(row=6, column=0, sticky="w")
        self.last_observation_entry = tk.Entry(self.form_frame, bd=2, relief="solid")
        self.last_observation_entry.grid(row=6, column=1, sticky="w", padx=10, pady=5)

        # create a separate frame for the buttons
        self.button_frame = tk.Frame(master, padx=20, pady=20)
        self.button_frame.pack(pady=20)

        self.file_button = tk.Button(self.button_frame, text="Seleccionar archivo Excel", padx=10, pady=5, command=self.select_file)
        self.file_button.grid(row=0, column=0, sticky="w")

        self.submit_button = tk.Button(self.button_frame, text="Enviar", padx=10, pady=5, command=self.submit)
        self.submit_button.grid(row=0, column=1, sticky="w")

        self.data = None

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            self.data = pd.read_excel(file_path)

    def submit(self):
        if self.data is None:
            print("No se ha seleccionado un archivo Excel.")
            return

        data = {
            "company": self.company_entry.get(),
            "plant": self.plant_entry.get(),
            "line": self.line_entry.get(),
            "oven": self.oven_entry.get(),
            "material": self.material_entry.get(),
            "first_observation": self.first_observation_entry.get(),
            "last_observation": self.last_observation_entry.get(),
        }

        new_row = pd.DataFrame([data])
        self.data = pd.concat([self.data, new_row], ignore_index=True)

        print(self.data)

root = tk.Tk()
form = Form(root)
root.mainloop()