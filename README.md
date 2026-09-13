<p align="center">
  <em>A curated personal archive of Desktop & Mobile wallpapers — organized, numbered, and ready to use.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Desktop-198%20images-blue?style=for-the-badge&logo=windows11&logoColor=white">
  <img src="https://img.shields.io/badge/Mobile-238%20images-green?style=for-the-badge&logo=android&logoColor=white">
  <img src="https://img.shields.io/badge/Total-436%20wallpapers-orange?style=for-the-badge&logo=googlephotos&logoColor=white">
</p>

---

## 📂 Repository Structure

```
My-Wallpaper-Collection/
│
├── Desktop/              # 198 desktop wallpapers (16:9 / widescreen)
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── ...
│   └── 198.jpg
│
├── Mobile/               # 238 mobile wallpapers (portrait / AMOLED-friendly)
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── ...
│   └── 238.jpg
│
├── script for rename/    # Python utilities used to keep files sequentially numbered
│
└── README.md
```

All files are renamed sequentially (`1`, `2`, `3`, ...) using custom Python scripts, so the collection stays clean and easy to browse or script against.

---

## 🖥️ Desktop Showcase

A quick preview of 10 wallpapers from the **Desktop** collection:

<table>
  <tr>
    <td><img src="Desktop/1.jpg" width="100%"></td>
    <td><img src="Desktop/2.jpg" width="100%"></td>
    <td><img src="Desktop/3.jpg" width="100%"></td>
  </tr>
  <tr>
    <td><img src="Desktop/4.jpg" width="100%"></td>
    <td><img src="Desktop/5.jpg" width="100%"></td>
    <td><img src="Desktop/6.png" width="100%"></td>
  </tr>
  <tr>
    <td><img src="Desktop/7.png" width="100%"></td>
    <td><img src="Desktop/8.jpeg" width="100%"></td>
    <td><img src="Desktop/9.png" width="100%"></td>
  </tr>
  <tr>
    <td><img src="Desktop/10.png" width="100%"></td>
    <td><img src="Desktop/11.jpg" width="100%"></td>
    <td><img src="Desktop/12.jpg" width="100%"></td>
  </tr>
</table>

> 📁 [Browse the full Desktop folder →](./Desktop)

---

## 📱 Mobile Showcase

A quick preview of 10 wallpapers from the **Mobile** collection:

<table>
  <tr>
    <td><img src="Mobile/1.jpg" width="100%"></td>
    <td><img src="Mobile/2.jpg" width="100%"></td>
    <td><img src="Mobile/3.jpg" width="100%"></td>
  </tr>
  <tr>
    <td><img src="Mobile/4.jpg" width="100%"></td>
    <td><img src="Mobile/5.jpg" width="100%"></td>
    <td><img src="Mobile/6.jpg" width="100%"></td>
  </tr>
  <tr>
    <td><img src="Mobile/7.jpg" width="100%"></td>
    <td><img src="Mobile/8.jpg" width="100%"></td>
    <td><img src="Mobile/9.jpg" width="100%"></td>
  </tr>
  <tr>
    <td><img src="Mobile/10.jpg" width="100%"></td>
    <td><img src="Mobile/11.jpg" width="100%"></td>
    <td><img src="Mobile/12.jpg" width="100%"></td>
  </tr>
</table>

> 📁 [Browse the full Mobile folder →](./Mobile)

---

## ✨ Features

- ✅ **Sequentially numbered files** — easy to reference, script, or randomize (`1.jpg` → `n.jpg`)
- ✅ **Separated by device type** — Desktop (widescreen) and Mobile (portrait) kept apart for correct aspect ratios
- ✅ **Automated maintenance scripts** — see [`script for rename/`](./script%20for%20rename) for the Python tools used to keep numbering clean whenever new wallpapers are added
- ✅ **Growing collection** — new wallpapers get appended without breaking existing numbering

---

## 🚀 Usage

Clone the repo and grab any wallpaper directly by its number:

```bash
git clone https://github.com/Hafiz-Sakib/My-Wallpaper-Collection.git
cd My-Wallpaper-Collection

# Example: open desktop wallpaper #42
open Desktop/42.jpg

# Example: open mobile wallpaper #100
open Mobile/100.jpg
```

Or grab a random one:

```bash
# Random desktop wallpaper
ls Desktop | shuf -n 1

# Random mobile wallpaper
ls Mobile | shuf -n 1
```

---

## 🛠️ Maintenance Scripts

The [`script for rename/`](./script%20for%20rename) folder contains the Python utilities used to keep this collection organized:

| Script               | Purpose                                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `rename.py`          | Renames all images in a folder to sequential numbers (`1, 2, 3, ...`)                                                               |
| Continuation renamer | Detects the last used sequential number and renames only newly added images, continuing from there                                  |
| Letter-pass renamer  | Temporarily renames files to a letter sequence (`a, b, ..., z, aa, ab, ...`) to safely resolve naming conflicts before re-numbering |

This keeps the collection collision-free even when new wallpapers are dropped in with random filenames from a phone or browser download.

---

## 📸 Source

Wallpapers are collected from various free-to-use sources across the web for personal use.

---

<p align="center">
  Made with 🖤 by <a href="https://github.com/Hafiz-Sakib">Hafiz-Sakib</a>
</p>
