import sys
sys.path.append('./')

from system import lorenz
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from utils import create_folder_if_not_exists

def noise(idx):
    if idx == 0:
        return np.random.normal(0, 1.5)
    if idx == 1:
        return np.random.normal(0, 2)
    if idx == 2:
        return np.random.normal(0, 2.5)
    
if __name__ == '__main__':
    
    T = 20 # Simulation time
    delta_t = 0.0001 # Sampling period
    nb_integration_step = int(T / delta_t)
    nb_simulation = 100
    seed = 42

    # System parameters
    beta = 8/3
    sigma = 10
    rho = 28

    folder_letter = ['a', 'b', 'c']
    
    intial_conditions = (np.random.rand(nb_simulation, 3) - 0.5) *  20

    for idx in range(3):

        # np.random.seed(seed)
        folder_path = f'./simulation/lorenz_simulation_{folder_letter[idx]}/'
        create_folder_if_not_exists(folder_path)

        for n in range(nb_simulation):

            t = 0

            results = {'x' : [], 'y':[], 'z':[], 'x_' : [], 'y_':[], 'z_':[], 'xdt' : [], 'ydt':[], 'zdt':[], 'xdt_' : [], 'ydt_':[], 'zdt_':[]}

            X = intial_conditions[n]

            for i in range(nb_integration_step):

                results['x'].append(X[0] + noise(idx)) 
                results['y'].append(X[1] + noise(idx))
                results['z'].append(X[2] + noise(idx))

                results['x_'].append(X[0])
                results['y_'].append(X[1])
                results['z_'].append(X[2])
                
                Xdt = lorenz(X, beta=beta, sigma=sigma, rho=rho)

                X = np.asarray(Xdt) * delta_t + X
                t += delta_t

                results['xdt'].append(Xdt[0])
                results['ydt'].append(Xdt[1])
                results['zdt'].append(Xdt[2])
                results['xdt_'].append(Xdt[0])
                results['ydt_'].append(Xdt[1])
                results['zdt_'].append(Xdt[2])

            data = pd.DataFrame(results)
            data.to_csv(folder_path+f'simulation_{n}.csv')