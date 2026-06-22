# OCR Text Recognition

## Project Overview

This project is an Artificial Intelligence project that performs basic OCR text recognition.

OCR stands for Optical Character Recognition. It is used to extract readable text from an image and convert it into machine-readable text.

This project uses a pre-trained OCR engine instead of training a model from scratch.

---

## Project Objective

The objective of this project is to:

- Load an image containing text
- Preprocess the image to improve readability
- Extract text from the image using OCR
- Display the extracted text in the terminal
- Save the extracted text into an output file
- Save the preprocessed image as project evidence

---

## Tools and Technologies Used

- Python
- Pillow
- pytesseract
- Tesseract OCR Engine

---

## Project Structure

```text
ocr-text-recognition/
├── sample_images/
│   └── sample_text.jpeg
├── output/
│   ├── extracted_text.txt
│   └── preprocessed_image.png
├── ocr_recognition.py
└── README.md
```

---

## How the Project Works

The project follows this workflow:

1. The input image is loaded from the `sample_images` folder.
2. The image is converted to grayscale.
3. The image contrast is automatically enhanced.
4. A sharpening filter is applied to make the text clearer.
5. The processed image is passed to Tesseract OCR.
6. The extracted text is displayed in the terminal.
7. The extracted text is saved in `output/extracted_text.txt`.
8. The preprocessed image is saved in `output/preprocessed_image.png`.

---

## Installation

Install Tesseract OCR:

```bash
sudo apt update
sudo apt install tesseract-ocr
```

Install the required Python libraries:

```bash
pip install pillow pytesseract
```

---

## How to Run

From inside the project folder, run:

```bash
python ocr_recognition.py
```

---

## Sample Output

The OCR system extracted the following text from the sample image:

```text
IT NEVER
GETS EASIER,

YOU JUST
GET BETTER.
```

The extracted text was saved to:

```text
output/extracted_text.txt
```

The preprocessed image was saved to:

```text
output/preprocessed_image.png
```

---

## Key Concepts Demonstrated

This project demonstrates:

- Basic OCR text recognition
- Image loading using Pillow
- Image preprocessing
- Grayscale conversion
- Automatic contrast enhancement
- Image sharpening
- Text extraction using a pre-trained OCR engine
- Saving output results into files

---

## Limitations

OCR accuracy depends on the quality of the input image.

The OCR result may be less accurate if the image contains:

- Handwritten text
- Blurry text
- Decorative fonts
- Low contrast
- Complex backgrounds
- Very small text
- Tilted or distorted text

---

## Conclusion

This project demonstrates how a basic AI recognition task can be implemented using OCR.

The program successfully loads an image, preprocesses it, extracts text using Tesseract OCR, displays the extracted text, and saves the output files.

This project shows how pre-trained AI tools can be used to recognize text from images without training a model from scratch.