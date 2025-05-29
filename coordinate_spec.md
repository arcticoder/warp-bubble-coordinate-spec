---
layout: default
title: Coordinate System & Symmetry Spec
---

# Coordinate System & Symmetry Specification

## Coordinate Chart

We choose spherical coordinates:
- **Coordinates**: $(t, r, \theta, \phi)$  
- **Domains**:  
  - $t \in (-\infty, +\infty)$  
  - $r \ge 0$  
  - $\theta \in [0, \pi]$  
  - $\phi \in [0, 2\pi)$  

## Symmetry Assumptions

1. **Axial symmetry** about the $z$–axis:  
   Metric components are independent of the azimuthal angle $\phi$.

2. **Reflection symmetry** in the equatorial plane ($\theta = \pi/2$).

3. **Compact radial support**:  
   Non-trivial metric perturbations confined within $r \le R$, where $R$ is the bubble radius.

## Simplified Metric Ansatz

Under these assumptions, a general static, axisymmetric warp-bubble metric can be written as:
\[
ds^2 = -A(r) \, dt^2 + B(r) \, dr^2 + C(r) \, r^2 \, d\theta^2 + D(r) \, r^2 \sin^2\theta \, d\phi^2
\]
where $A(r), B(r), C(r), D(r)$ are functions with support in $r \le R$.
