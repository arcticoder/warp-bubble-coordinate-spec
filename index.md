---
layout: page
title: Coordinate System & Symmetry Specification for Warp-Bubble Metrics
description: Specification of coordinate system and symmetry assumptions for the warp-bubble metric ansatz
author: Arcticoder
date: 2025-05-29
---

# Coordinate Chart

We adopt a standard spherical coordinate system on the background spacetime:

**Coordinates:** $(t, r, \theta, \phi)$

**Domains:**
- $t \in (-\infty, +\infty)$
- $r \in [0, +\infty)$ 
- $\theta \in [0,\pi]$
- $\phi \in [0,2\pi)$

## Symmetry Assumptions

1. **Axial symmetry** about the $z$-axis: no $\phi$–dependence.
2. **Equatorial reflection symmetry**: invariance under $\theta \mapsto \pi-\theta$.
3. **Compact support in $r$**: warp profiles $A,B,C,D$ nontrivial only for $r \leq R$.

## Reduced Metric Ansatz

Imposing the above, the line element becomes

$$ds^2 = -A(r)\,dt^2 + B(r)\,dr^2 + C(r)\,r^2\,d\theta^2 + D(r)\,r^2\sin^2\theta\,d\phi^2$$

with

$$A(r),B(r),C(r),D(r) = \begin{cases}
1, & r>R,\\
\text{warp–bubble profiles}, & r\leq R,
\end{cases}$$

and boundary conditions $A(R)=B(R)=C(R)=D(R)=1$.

## Worked Example (Sketch)

- Eliminate cross‐terms by staticity & symmetry.
- Enforce $\theta$–independence $\Rightarrow$ functions of $r$ only.
- Impose $g_{\mu\nu}=\eta_{\mu\nu}$ for $r>R$.
- Rename $g_{tt}=-A(r)$, $g_{rr}=B(r)$, etc.

## Automation Scripts

To generate, test and document metric ansätze for any warp–bubble profile, include a `scripts/` folder with:

```
warp-bubble-coordinate-spec/
├── coordinate_spec.tex
├── scripts/
│   ├── fetch_shape.py
│   ├── generate_ansatz.py
│   └── requirements.txt
└── metrics/
    └── <generated .tex snippets>
```

### 1. `fetch_shape.py`

- **Purpose:** download shape‐profile JSON from [warp-bubble-shape-catalog](https://arcticoder.github.io/warp-bubble-shape-catalog/).
- **Usage:**
  ```bash
  python scripts/fetch_shape.py --shape alcubierre
  ```
- **Behavior:**
  1. Perform HTTP GET on `https://arcticoder.github.io/warp-bubble-shape-catalog/data/{shape}.json`.
  2. Validate presence of fields `f(r)`, `parameters`.
  3. Save to `scripts/shapes/{shape}.json`.

### 2. `generate_ansatz.py`

- **Purpose:** produce a LaTeX snippet defining $A(r),B(r),C(r),D(r)$ from the fetched shape.
- **Usage:**
  ```bash
  python scripts/generate_ansatz.py \
    --shape alcubierre \
    --template ../coordinate_spec.tex \
    --out metrics/alcubierre_ansatz.tex
  ```
- **Behavior:**
  1. Load `scripts/shapes/{shape}.json`.
  2. Use Jinja2 (or simple string templates) to substitute:
     $$A(r)=1 - f(r),\quad B(r)=\frac{1}{1 - f(r)},\;\dots$$
  3. Emit a standalone TeX fragment in `metrics/`.

### Dependencies & Installation

Add a `scripts/requirements.txt`:
```
requests>=2.25
jinja2>=3.0
sympy>=1.8      # if you extend to symbolic curvature computation
```

Install with:
```bash
pip install -r scripts/requirements.txt
```

Each script implicitly references the "shape catalog" at [https://arcticoder.github.io/warp-bubble-shape-catalog/](https://arcticoder.github.io/warp-bubble-shape-catalog/) as its single source-of-truth. For offline work, you may instead add that repo as a git submodule:

```bash
git submodule add \
  https://github.com/arcticoder/warp-bubble-shape-catalog \
  scripts/warp-bubble-shape-catalog
```
