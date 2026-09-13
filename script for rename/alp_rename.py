import os

folder = os.path.dirname(os.path.abspath(__file__))

image_extensions = {
    ".jpg", ".jpeg", ".png", ".webp",
    ".gif", ".bmp", ".tiff", ".tif"
}

def to_letters(n):
    """
    Convert a positive integer to a bijective base-26 letter sequence:
    1 -> a, 2 -> b, ..., 26 -> z, 27 -> aa, 28 -> ab, ..., 52 -> az, 53 -> ba ...
    """
    letters = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        letters = chr(97 + remainder) + letters
    return letters

all_images = [
    f for f in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, f))
    and os.path.splitext(f)[1].lower() in image_extensions
]

# Sort alphabetically first (change to mtime sort below if you prefer capture order)
all_images.sort()
# all_images.sort(key=lambda f: os.path.getmtime(os.path.join(folder, f)))

# Two-phase rename to avoid filename conflicts
temp_files = []
for i, filename in enumerate(all_images, start=1):
    old_path = os.path.join(folder, filename)
    ext = os.path.splitext(filename)[1].lower()
    temp_name = f"__temp_letter_{i}{ext}"
    temp_path = os.path.join(folder, temp_name)
    os.rename(old_path, temp_path)
    temp_files.append((temp_path, ext))

for i, (temp_path, ext) in enumerate(temp_files, start=1):
    new_name = f"{to_letters(i)}{ext}"
    new_path = os.path.join(folder, new_name)
    os.rename(temp_path, new_path)

print(f"Done! {len(all_images)} image(s) renamed using letters (a, b, ..., z, aa, ab, ...).")