
# Image Text Extractor

This project is a simple graphical user interface (GUI) application for extracting text from images using Optical Character Recognition (OCR). The application is built using Python's `tkinter` library for the interface and PaddleOCR for the text extraction. The extracted text is displayed on the interface, and a new image with OCR results (bounding boxes and text) is generated.

## Features

- Upload an image from your local file system.
- Display the uploaded image.
- Extract and display text from the image using OCR.
- Display the OCR results, including bounding boxes and recognized text, on the image.

## Requirements

- Python 3.6 or higher
- Required Python libraries:
  - `tkinter`
  - `Pillow`
  - `paddleocr`
  - `numpy`

## Installation

1. Clone the repository or download the source files.
   ```bash
   git clone https://github.com/yourusername/image-text-extractor.git
   cd image-text-extractor
   ```

2. Install the required libraries.
   ```bash
   pip install pillow paddleocr numpy
   ```

3. Ensure that you have the font file `arial.ttf` in the same directory as the script. If you don't have it, you can download it or modify the script to use a different font.

## Usage

1. Run the Python script.
   ```bash
   python ocr_app.py
   ```

2. Click the **"Upload Image"** button to upload an image from your system.

3. After the image is uploaded, click **"Extract Text"** to perform OCR and extract the text from the image.

4. The extracted text will be displayed in the interface.

5. The OCR results (text with bounding boxes) will be drawn on the image and displayed below the extracted text.

## Project Structure

```
.
├── ocr_app.py        # Main Python script
├── README.md         # This readme file
├── arial.ttf         # Font file for rendering text on the image (download separately if not present)
└── requirements.txt  # Optional: list of dependencies
```

## Libraries Used

- **Tkinter**: Python's standard GUI library used to create the graphical interface.
- **Pillow**: A Python Imaging Library used for image processing.
- **PaddleOCR**: A pre-trained OCR model provided by PaddlePaddle for optical character recognition.
- **Numpy**: A library used for handling arrays and matrices (required for PaddleOCR).

## Notes

- Ensure that the image size is manageable to avoid performance issues.
- For custom fonts, modify the `font_path` in the `extract_text` function.
- The result image's dimensions are adjusted dynamically to fit within a maximum size of 1600x800 pixels.