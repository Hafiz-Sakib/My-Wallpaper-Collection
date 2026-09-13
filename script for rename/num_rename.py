import os

folder = os.path.dirname(os.path.abspath(__file__))

image_extensions = {
    ".jpg", ".jpeg", ".png", ".webp",
    ".gif", ".bmp", ".tiff", ".tif"
}

def letters_to_number(s):
    """
    Convert a bijective base-26 letter sequence back to its number:
    a -> 1, b -> 2, ..., z -> 26, aa -> 27, ab -> 28, ...
    """
    n = 0
    for ch in s:
        n = n * 26 + (ord(ch) - ord('a') + 1)
    return n

all_images = [
    f for f in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, f))
    and os.path.splitext(f)[1].lower() in image_extensions
]

# Keep only files whose name (without extension) is purely lowercase letters
lettered_images = []
for f in all_images:
    name, ext = os.path.splitext(f)
    if name.isalpha() and name.islower():
        lettered_images.append(f)

# Sort by the actual letter-sequence value, not plain alphabetical string sort
# (plain string sort would wrongly put "aa" right after "a" instead of after "z")
lettered_images.sort(key=lambda f: letters_to_number(os.path.splitext(f)[0]))

# Two-phase rename to avoid filename conflicts
temp_files = []
for i, filename in enumerate(lettered_images, start=1):
    old_path = os.path.join(folder, filename)
    ext = os.path.splitext(filename)[1].lower()
    temp_name = f"__temp_num_{i}{ext}"
    temp_path = os.path.join(folder, temp_name)
    os.rename(old_path, temp_path)
    temp_files.append((temp_path, ext))

for i, (temp_path, ext) in enumerate(temp_files, start=1):
    new_name = f"{i}{ext}"
    new_path = os.path.join(folder, new_name)
    os.rename(temp_path, new_path)

print(f"Done! {len(lettered_images)} image(s) renamed to sequential numbers (1, 2, 3, ...).")