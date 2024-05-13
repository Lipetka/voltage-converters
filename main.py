import tkinter
import tkinter.messagebox
from tkinter import filedialog, END, font
import customtkinter
from pyfiglet import fonts
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from calculations import BuckBoost

boost_calculations=BuckBoost()

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        # create log file

        # configure window
        self.title("Buck Boost calculator")    # Window title
        self.geometry(f"{1600}x{800}")  # Default window size
        self.minsize(1100,800)           # minimum window size
        self.resizable(1,1)             # Enable resizing

        # configure grid layout (2x2)
        # DONT TOUCH THIS!
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(2, weight=0)

        ################################################### SETUP FRAMES ###################################################
        self.data_entry_frame = customtkinter.CTkFrame(self, width=280,corner_radius=10)
        self.data_entry_frame.grid(row=0, column=0, rowspan=1, columnspan=1,  sticky="ew", padx=(20, 20), pady=(20, 20))
        self.data_entry_frame.grid_rowconfigure(10, weight=1)
        self.data_entry_frame.grid_columnconfigure(5, weight=1)

        self.results_frame = customtkinter.CTkFrame(self, width=280,corner_radius=10)
        self.results_frame.grid(row=1, column=0, rowspan=1, columnspan=1,  sticky="ew", padx=(20, 20), pady=(20, 20))
        self.results_frame.grid_rowconfigure(10, weight=1)
        self.results_frame.grid_columnconfigure(1, weight=1)

        self.graphs_frame = customtkinter.CTkFrame(self, width=280,corner_radius=10)
        self.graphs_frame.grid(row=0, column=1, rowspan=1, columnspan=1,  sticky="n", padx=(20, 20), pady=(20, 20))
        self.graphs_frame.grid_rowconfigure(10, weight=1)
        self.graphs_frame.grid_columnconfigure(1, weight=1)

        ################################################### ENTRY BOXES ###################################################
        row_counter = 0
        self.v_in_min_text=customtkinter.CTkLabel(self.data_entry_frame, text="In Voltage min. [V]: ")
        self.v_in_min_text.grid(row=row_counter,column=0, padx=(20, 20), pady=(5, 5))
        self.v_in_min_entry = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="In Voltage min. [V]: ")
        self.v_in_min_entry.grid(row=row_counter,column=1, padx=(20, 20), pady=(20, 5))
        row_counter += 1

        self.v_in_max_text=customtkinter.CTkLabel(self.data_entry_frame, text="In Voltage max. [V]: ")
        self.v_in_max_text.grid(row=row_counter,column=0, padx=(20, 20), pady=(5, 5))
        self.v_in_max_entry = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="In Voltage max. [V]: ")
        self.v_in_max_entry.grid(row=row_counter,column=1, padx=(20, 20), pady=(5, 5))
        row_counter += 1

        self.v_out_text=customtkinter.CTkLabel(self.data_entry_frame, text="Out Voltage [V]: ")
        self.v_out_text.grid(row=row_counter,column=0, padx=(20, 20), pady=(5, 5))
        self.v_out_entry = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="Out Voltage [V]: ")
        self.v_out_entry.grid(row=row_counter,column=1, padx=(20, 20), pady=(5, 5))
        row_counter += 1

        self.load_resistance_text=customtkinter.CTkLabel(self.data_entry_frame, text="Load Resistance [ohm]: ")
        self.load_resistance_text.grid(row=row_counter,column=0, padx=(20, 20), pady=(5, 5))
        self.load_resistance_entry = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="Load Resistance [ohm]: ")
        self.load_resistance_entry.grid(row=row_counter,column=1, padx=(20, 20), pady=(5, 5))
        row_counter += 1

        self.load_current_text=customtkinter.CTkLabel(self.data_entry_frame, text="Load current [A]: ")
        self.load_current_text.grid(row=row_counter,column=0, padx=(20, 20), pady=(5, 5))
        self.load_current_entry = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="Load current [A]: ")
        self.load_current_entry.grid(row=row_counter,column=1, padx=(20, 20), pady=(5, 5))
        row_counter += 1

        self.switch_frequency_text=customtkinter.CTkLabel(self.data_entry_frame, text="Switching frequency [kHz]: ")
        self.switch_frequency_text.grid(row=row_counter,column=0, padx=(20, 20), pady=(5, 5))
        self.switch_frequency_entry = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="Switching frequency [kHz]: ")
        self.switch_frequency_entry.grid(row=row_counter,column=1, padx=(20, 20), pady=(5, 5))
        row_counter += 1

        self.voltage_ripple_text=customtkinter.CTkLabel(self.data_entry_frame, text="Voltage ripple [%]: ")
        self.voltage_ripple_text.grid(row=row_counter,column=0, padx=(20, 20), pady=(5, 5))
        self.voltage_ripple_entry = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="Voltage ripple [%]: ")
        self.voltage_ripple_entry.grid(row=row_counter,column=1, padx=(20, 20), pady=(5, 5))
        row_counter += 1

        self.current_ripple_text=customtkinter.CTkLabel(self.data_entry_frame, text="Current ripple [%]: ")
        self.current_ripple_text.grid(row=row_counter,column=0, padx=(20, 20), pady=(5, 5))
        self.current_ripple_entry = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="Current ripple [%]: ")
        self.current_ripple_entry.grid(row=row_counter,column=1, padx=(20, 20), pady=(5, 20))
        row_counter += 1

        self.calculate_button=customtkinter.CTkButton(self.data_entry_frame, text="Calculate", command=self.enter_data)
        self.calculate_button.grid(row=row_counter,column=0, columnspan=2, padx=(20, 20), pady=(5, 5))
        row_counter += 1

        ################################################### RESULTS BOXES ###################################################
        row_counter = 0
        self.inductor_size_text = customtkinter.CTkLabel(self.results_frame, text="Inductor [mH] = N/A")
        self.inductor_size_text.grid(row=row_counter,column=0,padx=(20, 20), pady=(5, 5))
        row_counter += 1

        self.capacitor_size_text = customtkinter.CTkLabel(self.results_frame, text="Capacitor [uF] = N/A")
        self.capacitor_size_text.grid(row=row_counter,column=0,padx=(20, 20), pady=(5, 5))
        row_counter += 1

        ################################################### RESULT GRAPHS ###################################################


        # generate the figure and plot object which will be linked to the root element
        fig = Figure(figsize=(6, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        self.graph1 = FigureCanvasTkAgg(fig, master=self.graphs_frame)
        self.graph1.draw()
        self.graph1.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



        # Loop function (DON'T TOUCH THIS!)
        self.after(200, self.infinite_loop)

    def infinite_loop(self):
        """This function runs in infinite loop
        DONT INITIALIZE OR CALCULATE ANYTHING HERE, JUST CHECK STUFF AND CHANGE ALREADY EXISTING STUFF
        """
        if self.load_resistance_entry.get() != "":
            self.load_current_entry.configure(state = 'disabled')
            self.load_current_text.configure(state = 'disabled')
        else:
            self.load_current_entry.configure(state = 'normal')
            self.load_current_text.configure(state = 'normal')

        if self.load_current_entry.get() != "":
            self.load_resistance_entry.configure(state = 'disabled')
            self.load_resistance_text.configure(state = 'disabled')
        else:
            self.load_resistance_entry.configure(state = 'normal')
            self.load_resistance_text.configure(state = 'normal')


        self.after(1000, self.infinite_loop) # Call this function again every 1000 ms

    def enter_data(self):

        # assign numbers
        try:
            boost_calculations.v_in_min=   float(self.v_in_min_entry.get())
            boost_calculations.v_in_max=   float(self.v_in_max_entry.get())
            boost_calculations.v_out=  float(self.v_out_entry.get())
            if self.load_resistance_entry.get() != "":
                boost_calculations.load_resistance=    float(self.load_resistance_entry.get())
            if self.load_current_entry.get() != "":
                boost_calculations.load_current=   float(self.load_current_entry.get())
            boost_calculations.switch_frequency=   float(self.switch_frequency_entry.get())
            boost_calculations.voltage_ripple= float(self.voltage_ripple_entry.get())
            boost_calculations.current_ripple= float(self.current_ripple_entry.get())

        except ValueError:
            print("Incorrect data type")
            return

        boost_calculations.calculate_data()

        self.inductor_size_text.configure(text=f"Inductor [mH] = {boost_calculations.inductor}")
        self.capacitor_size_text.configure(text=f"Capacitor [uF] = {boost_calculations.capacitor}")



if __name__ == "__main__":
    app = App()
    app.mainloop()
