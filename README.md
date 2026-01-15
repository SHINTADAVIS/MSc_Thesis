# Study of Dynamics of Laser System using Lorenz Model

This repository contains the seminar paper and Python implementation related to my MSc Physics final project:  

**Davis, Shinta & Vinod, G.**  
*Study of dynamics of Laser system using Lorenz Model*  
Seminar Proceedings of the National Seminar **“Recent Trends in Physics and Research”**  
Department of Physics, St. Xavier’s College for Women,  
Aluva, Kerala, India – 686560  
December 2015, pp. 39–46.

This work was submitted as part of the **MSc Physics Final Project** at  
**University of Mahatma Gandhi, Kerala, India.**

## Contents

- `paper.pdf`  
  The published seminar paper.

- `python/`  
  Python programs used to simulate and analyze the Lorenz model for laser dynamics.

## Abstract

A Semi-Classical Model of Laser was proposed, by coupling a Classical Optical Field in a cavity, 
described by Maxwell’s equations, with a system of two-level atoms, described by Optical 
Bloch equations. The resulting Maxwell-Bloch equations, which are isomorphic to the 
equations of the Lorenz model (1963) weather prediction, It was this isomorphism, first pointed 
out by H. Haken in 1975, was made used in the study of dynamics of the Simple Laser Model in 
my project. The simulation of the non-linearity of the laser system is done in  Python using the 
Runge Kutta method, and successfully studied the non-linear behaviour of the laser and 
reproduced the results. It was found that the pumping rate, acts as the control parameter, 
which determines the dynamics of the system. The laser system exhibited a threshold behaviour 
governed by the rate of pumping and the lasing action led to a spontaneous symmetry breaking.

## Requirements

- Python 3.x    
- NumPy    
- SciPy    
- Matplotlib    

Install dependencies using:  
```bash
pip install numpy scipy matplotlib
