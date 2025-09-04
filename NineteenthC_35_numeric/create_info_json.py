import os
import json

# Path to the folder containing zoom subfolders
output_folder = r"C:\cantaloupe-5.0.7\images\NineteenthC_35_numeric"

# GitHub Pages URL for this folder
github_base_url = "https://brandonhurst01.github.io/iiif_images/NineteenthC_35_numeric"

# Get the zoom levels (folders named 0,1,...)
zoom_levels = sorted([int(d) for d in os.listdir(output_folder) if d.isdigit()])

# Determine scaleFactors based on zoom levels
scale_factors = [2 ** z for z in zoom_levels]

# Image dimensions (from your earlier script)
width = 2248
height = 3648
tile_size = 512

info = {
    "@context": "http://iiif.io/api/image/2/context.json",
    "@id": github_base_url,
    "protocol": "http://iiif.io/api/image",
    "width": width,
    "height": height,
    "tiles": [
        {
            "width": tile_size,
            "scaleFactors": scale_factors
        }
    ],
    "profile": ["http://iiif.io/api/image/2/level2.json"]
}

# Save info.json
with open(os.path.join(output_folder, "info.json"), "w", encoding="utf-8") as f:
    json.dump(info, f, indent=2)

print("Mirador-compatible info.json created!")
print("Zoom levels:", zoom_levels)
print("scaleFactors:", scale_factors)
