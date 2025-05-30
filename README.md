---
layout: default
title: warp-bubble-coordinate-spec
---

# warp-bubble-coordinate-spec

Specification of coordinate system and symmetry assumptions for the warp-bubble metric ansatz.

## Overview

This repository defines the coordinate chart and symmetries used to simplify the spacetime metric for warp-bubble candidates. It provides both theoretical foundations and automated tools for generating metric ansätze from warp-bubble shape profiles.

**🌐 Live Documentation:** [https://arcticoder.github.io/warp-bubble-coordinate-spec/](https://arcticoder.github.io/warp-bubble-coordinate-spec/)

## Key Features

- **Standardized Coordinate System**: Spherical coordinates $(t, r, \theta, \phi)$ with symmetry assumptions
- **Reduced Metric Ansatz**: Simplified line element for warp-bubble spacetimes
- **Automated Shape Processing**: Scripts to fetch and process warp-bubble profiles
- **LaTeX Generation**: Automatic generation of metric ansätze from shape data
- **Multiple Data Formats**: Support for both NPZ (high precision) and CSV data sources

## Repository Structure

```
warp-bubble-coordinate-spec/
├── coordinate_spec.tex           # Complete LaTeX specification
├── index.md                      # Website content with math rendering
├── scripts/                      # Automation tools
│   ├── fetch_shape.py           # Download and convert shape data
│   ├── generate_ansatz.py       # Generate LaTeX metric ansätze
│   ├── requirements.txt         # Python dependencies
│   └── shapes/                  # Downloaded shape data (JSON)
├── metrics/                     # Generated LaTeX snippets
├── _layouts/                    # Jekyll layout templates
└── .github/workflows/           # GitHub Actions for deployment
```

## Quick Start

### 1. Install Dependencies

```bash
pip install -r scripts/requirements.txt
```

### 2. Fetch Shape Data

```bash
# Download Alcubierre warp bubble profile
python scripts/fetch_shape.py --shape alcubierre

# Download Natario profile using CSV format
python scripts/fetch_shape.py --shape natario --format csv
```

### 3. Generate Metric Ansatz

```bash
python scripts/generate_ansatz.py \
  --shape alcubierre \
  --out metrics/alcubierre_ansatz.tex
```

## Available Shapes

- **alcubierre**: Classic Alcubierre warp drive spacetime
- **natario**: Natario warp drive variant

Data is sourced from the [warp-bubble-shape-catalog](https://arcticoder.github.io/warp-bubble-shape-catalog/) repository, available in:
- **NPZ format**: Higher precision (500 data points)
- **CSV format**: Compatibility fallback (100 data points)

## Mathematical Framework

The coordinate system uses standard spherical coordinates with imposed symmetries:

1. **Axial symmetry** about the z-axis (no φ-dependence)
2. **Equatorial reflection symmetry** (θ ↦ π−θ invariance)  
3. **Compact support** (warp profiles vanish for r > R)

This reduces the metric to:

$$ds^2 = -A(r)dt^2 + B(r)dr^2 + C(r)r^2d\theta^2 + D(r)r^2\sin^2\theta d\phi^2$$

with boundary conditions ensuring asymptotic flatness.

## Development

### Building the Documentation

```bash
# Install Jekyll dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# Build for production
bundle exec jekyll build
```

### GitHub Actions

The repository includes automated CI/CD that:
- Builds and deploys the Jekyll site to GitHub Pages
- Supports both Windows and Linux platforms
- Handles MathJax rendering for mathematical content

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the build locally
5. Submit a pull request

## License

This project is open source. See the repository for license details.
