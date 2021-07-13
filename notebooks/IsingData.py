import numpy as np
from WolffAlgorithm import WolffMonteCarlo

def generate_Ising_configurations(L, numSamplesPerT, Ts, equilibrationSteps=100):
    ''' Generates training data for the 2D Ising model for a given set of temperatures

    Samples are generated using Wolff cluster updates.

    Parameters:

        * `L`: Linear size of the system
        * `numSamplesPerT`: Number of samples to generate per temperature
        * `Ts`: List of temperatures
        * `equilibrationSteps`: Number of equilibration steps

    Returns:

        * A dictionary with the sampled configurations for each temperature

    '''

    # Initialize a new simulator
    sim = WolffMonteCarlo(L=L, T=5, method="DFS")

    all_data = {}

    # Loop over a fixed set of temperatures
    for T in Ts:
        print("Generating samples for L = %d at T = %.3f"%(L,T))

        # Set temperature
        sim.set_T(T)

        # For storing all of the configurations
        res = []
        for s in range(numSamplesPerT + equilibrationSteps):

            # Keep flipping sites, until we flipped at least L^2 of them
            c = 0
            while c < 1:
                to_flip = sim.step()
                c = c + len(to_flip) / L / L

            # The first half of the flips are to equilibrate, the rest are
            # good samples
            if s >= equilibrationSteps:
                res.append(np.array(-1 + 2 * sim.state.reshape(-1)))


        all_data['%.3f'%(T)] = np.array(res)

    
    return all_data

