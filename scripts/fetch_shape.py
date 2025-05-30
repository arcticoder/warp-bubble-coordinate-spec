#!/usr/bin/env python3
import argparse
import os
import requests
import csv
import json
import numpy as np
from io import BytesIO

def fetch_shape_csv(shape, output_dir="scripts/shapes"):
    """Fetch shape data from CSV format"""
    csv_url = "https://raw.githubusercontent.com/arcticoder/warp-bubble-shape-catalog/refs/heads/main/data/profile_data.csv"
    resp = requests.get(csv_url)
    resp.raise_for_status()
    
    # Parse CSV and extract the requested shape
    csv_data = resp.text.strip().split('\n')
    
    # Check if the shape exists in the CSV
    headers = csv_data[0].split(',')
    if shape not in headers:
        available_shapes = [h for h in headers if h != 'r']
        raise ValueError(f"Shape '{shape}' not found. Available shapes: {available_shapes}")
    
    # Extract r and shape data
    reader = csv.DictReader(csv_data)
    r_values = []
    shape_values = []
    
    for row in reader:
        r_values.append(float(row['r']))
        shape_values.append(float(row[shape]))
    
    return r_values, shape_values, f"CSV data for {shape} with {len(r_values)} points"

def fetch_shape_npz(shape, output_dir="scripts/shapes"):
    """Fetch shape data from NPZ format"""
    npz_url = "https://github.com/arcticoder/warp-bubble-shape-catalog/raw/refs/heads/main/data/profiles.npz"
    resp = requests.get(npz_url)
    resp.raise_for_status()
    
    # Load NPZ data
    data = np.load(BytesIO(resp.content))
    
    # Check if the shape exists in the NPZ
    if shape not in data.files:
        available_shapes = [f for f in data.files if f != 'r']
        raise ValueError(f"Shape '{shape}' not found in NPZ. Available shapes: {available_shapes}")
    
    r_values = data['r'].tolist()
    shape_values = data[shape].tolist()
    
    return r_values, shape_values, f"NPZ data for {shape} with {len(r_values)} points"

def fetch_shape(shape, output_dir="scripts/shapes", format_preference="npz"):
    """Fetch shape data from the warp-bubble-shape-catalog"""
    
    # Try the preferred format first, then fallback
    try:
        if format_preference == "npz":
            r_values, shape_values, description = fetch_shape_npz(shape, output_dir)
        else:
            r_values, shape_values, description = fetch_shape_csv(shape, output_dir)
    except Exception as e:
        print(f"Failed to fetch from {format_preference}: {e}")
        print(f"Trying alternative format...")
        
        # Try the other format
        try:
            if format_preference == "npz":
                r_values, shape_values, description = fetch_shape_csv(shape, output_dir)
            else:
                r_values, shape_values, description = fetch_shape_npz(shape, output_dir)
        except Exception as e2:
            raise ValueError(f"Failed to fetch from both formats. NPZ error: {e}, CSV error: {e2}")
    
    # Create JSON structure compatible with existing generate_ansatz.py
    shape_data = {
        "name": shape,
        "description": description,
        "f": f"interpolated_{shape}(r)",
        "r_values": r_values,
        "f_values": shape_values,
        "parameters": {
            "description": f"Shape function data for {shape} profile",
            "r_min": min(r_values),
            "r_max": max(r_values),
            "num_points": len(r_values),
            "f_min": min(shape_values),
            "f_max": max(shape_values)
        }
    }
    
    # Save to JSON file
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{shape}.json")
    with open(out_path, "w") as f:
        json.dump(shape_data, f, indent=2)
    
    print(f"Saved shape data to {out_path}")
    print(f"Shape function: {description}")
    print(f"r range: [{shape_data['parameters']['r_min']:.6f}, {shape_data['parameters']['r_max']:.6f}]")
    print(f"f(r) range: [{shape_data['parameters']['f_min']:.6f}, {shape_data['parameters']['f_max']:.6f}]")
    
    return out_path

def main():
    parser = argparse.ArgumentParser(description="Fetch warp-bubble shape profile from CSV or NPZ data and convert to JSON")
    parser.add_argument('--shape', required=True, help="Name of the shape (e.g., alcubierre, natario)")
    parser.add_argument('--output', default="scripts/shapes", help="Directory to save JSON")
    parser.add_argument('--format', choices=['csv', 'npz'], default='npz', 
                       help="Preferred data format (npz has higher precision)")
    args = parser.parse_args()
    
    try:
        fetch_shape(args.shape, args.output, args.format)
    except Exception as e:
        print(f"Error: {e}")
        
        # List available shapes
        try:
            print("\nTrying to list available shapes...")
            import numpy as np
            from io import BytesIO
            
            # Try NPZ first
            try:
                resp = requests.get("https://github.com/arcticoder/warp-bubble-shape-catalog/raw/refs/heads/main/data/profiles.npz")
                resp.raise_for_status()
                data = np.load(BytesIO(resp.content))
                available = [f for f in data.files if f != 'r']
                print(f"Available shapes in NPZ: {available}")
            except:
                # Fallback to CSV
                resp = requests.get("https://raw.githubusercontent.com/arcticoder/warp-bubble-shape-catalog/refs/heads/main/data/profile_data.csv")
                resp.raise_for_status()
                headers = resp.text.split('\n')[0].split(',')
                available = [h for h in headers if h != 'r']
                print(f"Available shapes in CSV: {available}")
        except Exception as list_error:
            print(f"Could not list available shapes: {list_error}")
        
        exit(1)

if __name__ == "__main__":
    main()
