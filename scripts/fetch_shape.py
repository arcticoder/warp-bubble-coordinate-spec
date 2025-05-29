#!/usr/bin/env python3
import argparse
import os
import requests

def fetch_shape(shape, output_dir="scripts/shapes"):
    url = f"https://arcticoder.github.io/warp-bubble-shape-catalog/data/{shape}.json"
    resp = requests.get(url)
    resp.raise_for_status()
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{shape}.json")
    with open(out_path, "w") as f:
        f.write(resp.text)
    print(f"Saved shape data to {out_path}")

def main():
    parser = argparse.ArgumentParser(description="Fetch warp-bubble shape JSON profile")
    parser.add_argument('--shape', required=True, help="Name of the shape (e.g., alcubierre)")
    parser.add_argument('--output', default="scripts/shapes", help="Directory to save JSON")
    args = parser.parse_args()
    fetch_shape(args.shape, args.output)

if __name__ == "__main__":
    main()
