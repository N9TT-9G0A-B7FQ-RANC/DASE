#!/bin/bash

python ./run/train.py \
    --training_name lorenz_a \
    --training_parameters lorenz_a \
    --start_index 0 \
    --end_index 16

python ./run/train.py \
    --training_name lorenz_b \
    --training_parameters lorenz_b \
    --start_index 0 \
    --end_index 16

python ./run/train.py \
    --training_name lorenz_c \
    --training_parameters lorenz_c \
    --start_index 0 \
    --end_index 16

python ./run/train.py \
    --training_name vanderpol_a \
    --training_parameters vanderpol_a \
    --start_index 0 \
    --end_index 24

python ./run/train.py \
    --training_name vanderpol_b \
    --training_parameters vanderpol_b \
    --start_index 0 \
    --end_index 24

python ./run/train.py \
    --training_name vanderpol_c \
    --training_parameters vanderpol_c \
    --start_index 0 \
    --end_index 24