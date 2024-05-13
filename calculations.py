#def calculate():
#    # Calculate duty cycle
#    duty_cycle = (Vout + self.voltage_ripple) / self.v_in_min
#
#    # Calculate inductance
#    L = (self.v_in_min * (self.v_in_max - self.v_in_min)) / (self.switch_frequency * self.voltage_ripple * self.load_resistance)
#
#    # Calculate capacitor
#    C = (self.load_resistance * (self.v_in_max - self.v_in_min)) / (self.voltage_ripple * self.switch_frequency * duty_cycle * Vout)
#
#    # Update result labels
#    result_label_L.config(text="Inductance (L): {:.4f} μH".format(L * 1e6))
#    result_label_C.config(text="Capacitance (C): {:.4f} μF".format(C * 1e6))
#
#    # Plot the duty cycle
#    x = [self.v_in_min, self.v_in_max]
#    y = [duty_cycle] * 2
#
#    plt.figure(figsize=(5, 4))
#    plt.plot(x, y, marker='o')
#    plt.xlabel('Input Voltage (V)')
#    plt.ylabel('Duty Cycle')
#    plt.title('Duty Cycle vs Input Voltage')
#    plt.grid(True)
#
#    # Display the plot
#    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
#    canvas.draw()
#    canvas.get_tk_widget().grid(row=9, columnspan=2)

class BuckBoost():
    def __init__(self) -> None:
        self.v_in_min=0
        self.v_in_max=0
        self.v_out=0
        self.load_resistance=0
        self.load_current=0
        self.switch_frequency=0
        self.voltage_ripple=0
        self.current_ripple=0
        self.inductor=0
        self.capacitor=0
        self.duty_cycle_min=0
        self.duty_cycle_max=0

    def calculate_data(self):
        self.duty_cycle_min=(self.v_out - self.v_in_max) / self.v_out
        self.duty_cycle_max=(self.v_out - self.v_in_min) / self.v_out
        self.inductor = (self.v_in_min * (self.v_in_max - self.v_in_min)) / (self.switch_frequency * self.voltage_ripple * self.load_resistance)
        self.capacitor= (self.load_resistance * (self.v_in_max - self.v_in_min)) / (self.voltage_ripple * self.switch_frequency * self.duty_cycle_min * self.v_out)