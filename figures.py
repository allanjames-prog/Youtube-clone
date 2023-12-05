# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the data
# Replace these with your actual data
flow_rate = np.array([4.75, 9, 13.6, 19.6])  # Flow rate in L/min
pressure_drop_venturi = np.array([127.6, 294.1, 441.8, 637.3])  # Pressure drop for venturi meter in Pa
pressure_drop_orifice = np.array([294.1, 686.4, 1028.6, 1470.8])  # Pressure drop for orifice plate in Pa
pressure_drop_nozzle = np.array([196.1, 441.8, 686.4, 1028.6])  # Pressure drop for nozzle in Pa

# Create a new figure for the pressure drop plot
plt.figure()

# Plot the pressure drop against the flow rate for each device
plt.plot(flow_rate, pressure_drop_venturi, 'o-', label='Venturi Meter')
plt.plot(flow_rate, pressure_drop_orifice, 'o-', label='Orifice Plate')
plt.plot(flow_rate, pressure_drop_nozzle, 'o-', label='Nozzle')

# Label the x-axis as 'Flow rate (L/min)'
plt.xlabel('Flow rate (L/min)')

# Label the y-axis as 'Pressure drop (Pa)'
plt.ylabel('Pressure drop (Pa)')

# Add a legend
plt.legend()

# Display the plot
plt.show()
