import os
import re

folder = os.path.dirname(os.path.abspath(__file__))

image_extensions = {
    ".jpg", ".jpeg", ".png", ".webp",
    ".gif", ".bmp", ".tiff", ".tif"
}

all_images = [
    f for f in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, f))
    and os.path.splitext(f)[1].lower() in image_extensions
]

numbered_pattern = re.compile(r"^\d+$")

existing_numbers = []
new_images = []

for f in all_images:
    name, ext = os.path.splitext(f)
    if numbered_pattern.match(name):
        existing_numbers.append(int(name))
    else:
        new_images.append(f)

# Find the highest existing number (0 if none found)
last_number = max(existing_numbers) if existing_numbers else 0

# Sort new (unnumbered) images by modification time
# so they keep their original capture order.
# Change this to new_images.sort() if you want alphabetical order instead.
new_images.sort(key=lambda f: os.path.getmtime(os.path.join(folder, f)))

# Two-phase rename to avoid conflicts with existing filenames
temp_files = []
for i, filename in enumerate(new_images, start=1):
    old_path = os.path.join(folder, filename)
    ext = os.path.splitext(filename)[1].lower()
    temp_name = f"__temp_new_{i}{ext}"
    temp_path = os.path.join(folder, temp_name)
    os.rename(old_path, temp_path)
    temp_files.append((temp_path, ext))

# Rename temp files to final sequential numbers, continuing from last_number
for i, (temp_path, ext) in enumerate(temp_files, start=last_number + 1):
    new_name = f"{i}{ext}"
    new_path = os.path.join(folder, new_name)
    os.rename(temp_path, new_path)

print(f"Existing max number: {last_number}")
print(f"{len(new_images)} new image(s) renamed starting from {last_number + 1}.")