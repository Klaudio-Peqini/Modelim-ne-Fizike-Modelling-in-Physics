
# Population, Epidemic and Traffic Models

This repository contains reference implementations of several classical models used in
population dynamics, epidemiology and traffic modeling.

## Repository Structure

population_epidemic_traffic_models/

models/
- population_growth.py
- logistic_growth.py
- sir_model.py
- seir_model.py
- traffic_flow.py

visualization/
- epidemic_curves.py
- phase_plots.py
- traffic_simulation.py

main.py
requirements.txt

## Install dependencies

python3 -m pip install -r requirements.txt

## Usage

python3 main.py --model population

python3 main.py --model logistic

python3 main.py --model sir

python3 main.py --model seir

python3 main.py --model traffic
