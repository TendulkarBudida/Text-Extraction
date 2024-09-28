import tkinter as tk
from tkinter import filedialog
from tkinter import Label
from PIL import Image, ImageTk
from paddleocr import PaddleOCR, draw_ocr
import os

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Function to upload and display image
def upload_image():
    global img_path, img_label
    img_path = filedialog.askopenfilename()
    img = Image.open(img_path)
    img = img.resize((400, 400), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img

# Function to extract text from image and display the result
def extract_text():
    global img_path, text_label, result_img_label
    result = ocr.ocr(img_path, cls=True)
    extracted_text = '\n'.join([line[1][0] for line in result[0]])
    text_label.config(text=extracted_text)
    
    # Draw OCR results on the image
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result[0]]
    txts = [line[1][0] for line in result[0]]
    scores = [line[1][1] for line in result[0]]
    
    # Use a default font
    font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arial.ttf')
    im_show = draw_ocr(image, boxes, txts, scores, font_path=font_path)
    im_show = Image.fromarray(im_show)
    
    # Calculate the aspect ratio and resize the image dynamically
    max_width, max_height = 1600, 800
    aspect_ratio = min(max_width / im_show.width, max_height / im_show.height)
    new_size = (int(im_show.width * aspect_ratio), int(im_show.height * aspect_ratio))
    im_show = im_show.resize(new_size, Image.LANCZOS)
    
    im_show = ImageTk.PhotoImage(im_show)
    result_img_label.config(image=im_show)
    result_img_label.image = im_show

# Initialize Tkinter window
root = tk.Tk()
root.title("Image Text Extractor")
root.geometry("1200x1200")

# Create a canvas and a scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Create and place widgets inside the scrollable frame
upload_btn = tk.Button(scrollable_frame, text="Upload Image", command=upload_image)
upload_btn.pack(pady=10)

img_label = Label(scrollable_frame)
img_label.pack(pady=10)

extract_btn = tk.Button(scrollable_frame, text="Extract Text", command=extract_text)
extract_btn.pack(pady=10)

text_label = Label(scrollable_frame, text="", wraplength=1000)
text_label.pack(pady=10)

result_img_label = Label(scrollable_frame)
result_img_label.pack(pady=10)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Run the Tkinter main loop
root.mainloop()