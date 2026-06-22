# OCR Text Recognition

## Project Overview

This project is a basic Artificial Intelligence project that uses OCR to extract text from an image.

OCR stands for Optical Character Recognition. It allows a program to read text inside images and convert it into machine-readable text.

This project uses a pre-trained OCR engine instead of training a model from scratch.

---

## Project Objective

The objective of this project is to:

- Load an image containing text
- Preprocess the image for better recognition
- Extract text using OCR
- Display the extracted text
- Save the extracted text and preprocessed image as output files

---

## Tools Used

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