# Watermark Images

A minimal Python desktop app to add a digital watermark to images using a simple Tkinter GUI.

---

## Features

- Select and preview a `.jpg` image and it work with other images too
- Add a digital watermark with one click
- Saves the result as `watermarked_image.png` or in the destination you choose

---

## Requirements

- Python 3.7+
- [Pillow](https://pypi.org/project/Pillow/)
- [opencv-python](https://pypi.org/project/opencv-python/)
- [imwatermark](https://pypi.org/project/imwatermark/)
- Tkinter (usually included with Python)

Install dependencies:
```sh
pip install requirements.txt
```

---

## Usage

```sh
python main.py
```
1. Click **Open File** and select a `.jpg` image.
2. Click **Add WaterMark**.
3. The watermarked image is saved as `watermarked_image.png` in the current directory.

---

## Customization

- Change the watermark text in `watermark.py` (`watermark_text` variable).
- To support more formats, edit the `filetypes` in `main.py`.

---

##