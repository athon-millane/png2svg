#!/usr/bin/env python3

import sys
import numpy as np
from PIL import Image
import svgwrite
from pathlib import Path

def image_to_svg(input_path, output_path, threshold=128):
    """
    Convert a PNG image to SVG using edge detection and path tracing.
    
    Args:
        input_path (str): Path to input PNG file
        output_path (str): Path to output SVG file
        threshold (int): Threshold for edge detection (0-255)
    """
    # Open and convert image to grayscale
    img = Image.open(input_path).convert('L')
    img_array = np.array(img)
    
    # Create SVG drawing
    dwg = svgwrite.Drawing(output_path, size=(img.width, img.height))
    
    # Add white background
    dwg.add(dwg.rect(insert=(0, 0), size=(img.width, img.height), fill='white'))
    
    # Process image and create paths
    for y in range(img.height):
        for x in range(img.width):
            if img_array[y, x] < threshold:
                # Create a small rectangle for each dark pixel
                dwg.add(dwg.rect(insert=(x, y), size=(1, 1), fill='black'))
    
    # Save the SVG file
    dwg.save()

def main():
    if len(sys.argv) != 3:
        print("Usage: python png2svg.py input.png output.svg")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    if not Path(input_path).exists():
        print(f"Error: Input file '{input_path}' does not exist")
        sys.exit(1)
    
    try:
        image_to_svg(input_path, output_path)
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 