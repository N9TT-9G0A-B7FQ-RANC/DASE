lorenz_state_variables = ['x', 'y', 'z']
lorenz_observed_state_variables = ['x']
lorenz_control_variables = []

vanderpol_state_variables = ['x', 'y']
vanderpol_observed_state_variables = ['x']
vanderpol_control_variables = []

system_configuration = {
    'vanderpol' : {
        'state' : vanderpol_state_variables,
        'observed_state' : vanderpol_observed_state_variables,
        'control' : vanderpol_control_variables
    },
    'lorenz' : {
        'state' : lorenz_state_variables,
        'observed_state' : lorenz_observed_state_variables,
        'control' : lorenz_control_variables
    },
}

nb_trajectories = 100
seed = 42
device = 'cuda:0'
train_set_pct = 0.7
val_set_pct = 0.2
test_set_pct = 0.1
eval_trajectory_duration = 20.
validation_frequency = 2
nb_epochs = 301
smoothing_parameters = {}