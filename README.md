# Particle Swarm Optimization

**Basic Overview**
In computational science, particle swarm optimization (PSO) is a computational method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. It solves a problem by having a population of candidate solutions, here dubbed particles, and moving these particles around in the search-space according to simple mathematical formula over the particle's position and velocity.

Using that approach, it is possible to replicate an image using the PSO. Given a JPG image in its 3 RGB channels, the algorithm gives random values to each channel (0-255), changing them in each iteration seeking to minimize the error in each one. This error is the difference between the original image value and the one calculated by the algorithm.


**Installation Options**
---
1. Python 3.4.0 or later is required.
2. Install with [`pip`](https://pypi.org/project/stronghold/)
    + `$ pip install Pillow`
    + `$ pip install matplotlib`
