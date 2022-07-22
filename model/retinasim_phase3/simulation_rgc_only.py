from brian2 import *
import numpy as np
from model.retinasim_phase3.simulation_utils import save_delta_ve, SimulationParam
from model.retinasim_phase3.retina_network_rgc_only import retina_simulation

# sp can be either the path to a txt file containing the simulation parameters or a SimulationParam object

def estim_to_retina_output(time_in_ms, sp, estim, light_intensity=0.5, delta_ve_folder="delta_ve_workspace", dt=0.01, debug=False, gpu=True, select_GPU=None, genn_directory=None):
    
    start = time.time()
    
    if isinstance(sp, str):
        sp = SimulationParam(sp)
    
    save_delta_ve(sp.imped, estim, sp.electrode_x, sp.electrode_y, sp.electrode_z, sp.electrode_diam, sp.xy_coord_folder, sp.z_coord_folder, delta_ve_folder, sp.implant_mode, dt=dt)
    data = retina_simulation(time_in_ms, sp, delta_ve_folder=delta_ve_folder, delta_ve_dt=dt, simulation_timestep=dt, debug=debug, gpu=gpu, select_GPU=select_GPU, genn_directory=genn_directory)

    end = time.time()
    print("simulation time: {}".format(end-start))
    
    return data