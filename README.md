# DASE: Deep Algebraic State Estimator

DASE, short for Deep Algebraic State Estimator, is a tool designed to learn algebraic state estimator of nonlinear dynamical systems using deep learning techniques.

## install requirements

pip install -r requirements.txt

## Generate Dataset

To generate the required dataset for training the DASE model, execute the following commands:

```bash
python ./system/simulate_lorenz.py
python ./system/simulate_vanderpol.py

## Launch Training
To train the DASE model, use the provided run.sh script. This script contains the necessary commands to initiate the training process.

```bash
./run_train.sh

## Evaluate Obtained Models
After training, you can evaluate the performance of the obtained models using the run_evaluate.sh.

```bash
./run_evaluate.sh