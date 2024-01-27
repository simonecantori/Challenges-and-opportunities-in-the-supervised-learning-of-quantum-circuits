import numpy as np

N = 30 #Number of qubits

# We load 1000 circuits with N qubits and P layers of gates
thetas = np.load(f'Npys/theta_N18N20_to_N{N}.npy') # array with shape (1000,N,1). They are the N angles of each circuit (repeated P times for each layer)
preds = np.load(f'Npys/pred_N18N20_to_N{N}.npy') # array with shape (1000,1). They are the predicted M_z for each circuit.
