import os

# এই script যে folder-এ আছে
folder = os.path.dirname(os.path.abspath(__file__))

# Supported image extensions
image_extensions = {
    ".jpg", ".jpeg", ".png", ".webp",
    ".gif", ".bmp", ".tiff", ".tif"
}

# Image files collect করা
images = [
    f for f in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, f))
    and os.path.splitext(f)[1].lower() in image_extensions
]

# Alphabetical order
images.sort()

# Temporary names দিয়ে rename করা
# এতে 1.jpg -> 2.jpg টাইপ conflict হবে না
temp_files = []

for i, filename in enumerate(images, start=1):
    old_path = os.path.join(folder, filename)
    ext = os.path.splitext(filename)[1].lower()

    temp_name = f"__temp_image_{i}{ext}"
    temp_path = os.path.join(folder, temp_name)

    os.rename(old_path, temp_path)
    temp_files.append((temp_path, ext))

# Final serial names
for i, (temp_path, ext) in enumerate(temp_files, start=1):
    new_name = f"{i}{ext}"
    new_path = os.path.join(folder, new_name)

    os.rename(temp_path, new_path)

print(f"Done! {len(images)} image(s) renamed.")