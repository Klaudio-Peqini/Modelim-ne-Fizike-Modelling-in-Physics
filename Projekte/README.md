# Modelling in Physics (Modelim në Fizikë)

## Overview

This repository contains a comprehensive collection of computational and theoretical materials for the course **"Modelling in Physics"**. The aim is to bridge the gap between **analytical physics**, **numerical methods**, and **modern computational practices**, providing students with both conceptual understanding and production-level coding skills.

---

## Objectives

- Develop intuition for physical modelling
- Transition from equations to computational implementations
- Understand numerical and stochastic methods
- Explore nonlinear dynamics and chaos
- Apply modelling to real-world systems
- Work in structured, collaborative scientific environments

---

## Repository Structure

```
Modelling-in-Physics/
└── Projekte/  # Student group projects
```

---

## The `Projects/` Folder – Philosophy of Assignments

The **Projects/** folder is a central pedagogical component of this repository. It is designed to simulate **real scientific research environments** and to encourage **collaborative, project-based learning**.

### Core Idea

Students are divided into groups, and each group is assigned a **modelling project** that:

- Extends concepts learned in the course
- Requires both **theoretical understanding** and **computational implementation**
- Encourages **independent thinking and problem-solving**

---

### Educational Goals

Each project is designed so that students:

- Translate a physical or real-world problem into a **mathematical model**
- Implement the model using **Python (or other languages when appropriate)**
- Perform **numerical simulations**
- Analyze results scientifically
- Present findings in a **professional format**

---

### Structure of Each Project

Each group project should typically include:

```
project_name/
│
├── README.md              # Description of the problem
├── theory/                # Mathematical formulation
├── code/                  # Simulation scripts
├── data/                  # Input/output datasets
├── results/               # Figures and analysis
└── report/                # Final scientific report (PDF/LaTeX)
```

---

### Types of Projects

Projects may include:

- Physical systems (oscillators, pendula, fluids)
- Epidemiological models (SIR, SEIR extensions)
- Traffic and transport models
- Network models (PageRank, diffusion)
- Stochastic processes
- Data-driven modelling

---

### Collaboration Philosophy

Students are expected to:

- Work in **teams**
- Use **Git/GitHub workflows**
- Divide tasks (theory, coding, analysis)
- Review each other’s work
- Maintain **clear documentation**

This mirrors real-world scientific collaboration.

---

### Evaluation Criteria

Projects are evaluated based on:

- Correctness of the physical and mathematical model
- Quality of the code (structure, readability, robustness)
- Depth of analysis
- Visualization and interpretation of results
- Clarity of the final report
- Team collaboration

---

## Installation

```bash
git clone https://github.com/Klaudio-Peqini/Modelim-ne-Fizike-Modelling-in-Physics.git
cd Modelim-ne-Fizike-Modelling-in-Physics

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Usage

```bash
python3 main.py --model oscillator
python3 main.py --model sir
python3 main.py --model chaos
```

---

## Numerical Methods

- Euler
- Runge-Kutta (RK4)
- Verlet
- Euler-Maruyama
- Stochastic Runge-Kutta

---

## Pedagogical Philosophy

This repository follows a **dual structure**:

- **Notebooks → Understanding**
- **Production Code → Professional Practice**

---

## Author

Klaudio Peqini  
Physicist & Lecturer  

---

## License

Educational and research use.
