#!/usr/bin/env python3
import argparse
import json
import os
from jinja2 import Template

TEX_TEMPLATE = r"""
% Auto-generated ansatz for {{ shape }}
\section*{Ansatz: {{ shape | capitalize }} Warp Bubble}
\[
  A(r) = {{ funcs.A }},
  \quad B(r) = {{ funcs.B }},
  \quad C(r) = {{ funcs.C }},
  \quad D(r) = {{ funcs.D }}
\]
"""

def load_shape(shape, shapes_dir="scripts/shapes"):
    path = os.path.join(shapes_dir, f"{shape}.json")
    with open(path) as f:
        return json.load(f)

def render_ansatz(shape, template_path=None):
    data = load_shape(shape)
    f_expr = data.get("f")
    funcs = {
        "A": f"1 - ({f_expr})",
        "B": f"1 / (1 - ({f_expr}))",
        "C": "1",
        "D": "1"
    }
    if template_path:
        with open(template_path) as tf:
            tmpl = Template(tf.read())
    else:
        tmpl = Template(TEX_TEMPLATE)
    return tmpl.render(shape=shape, funcs=funcs)

def main():
    parser = argparse.ArgumentParser(description="Generate LaTeX ansatz from shape JSON")
    parser.add_argument('--shape', required=True, help="Name of the shape (e.g., alcubierre)")
    parser.add_argument('--template', help="Path to coordinate_spec.tex template")
    parser.add_argument('--out', required=True, help="Output .tex file")
    args = parser.parse_args()
    content = render_ansatz(args.shape, args.template)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        f.write(content)
    print(f"Wrote ansatz to {args.out}")

if __name__ == "__main__":
    main()
