from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import pytesseract


IMAGE_FILE = Path(__file__).parent / "sample_images" / "sample_text.jpeg"
OUTPUT_FILE = Path(__file__).parent / "output" / "extracted_text.txt"
PROCESSED_IMAGE_FILE = Path(__file__).parent / "output" / "preprocessed_image.png"


def load_image(image_path):
    image = Image.open(image_path)
    return image


def preprocess_image(image):
    grayscale_image = ImageOps.grayscale(image)

    enhanced_image = ImageOps.autocontrast(grayscale_image)

    processed_image = enhanced_image.filter(ImageFilter.SHARPEN)

    return processed_image


def extract_text_from_image(image):
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text


def save_extracted_text(text, output_path):
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


def main():
    image = load_image(IMAGE_FILE)

    processed_image = preprocess_image(image)

    processed_image.save(PROCESSED_IMAGE_FILE)

    extracted_text = extract_text_from_image(processed_image)

    print("\nOCR Text Recognition Result:")
    print("-" * 30)
    print(extracted_text)

    save_extracted_text(extracted_text, OUTPUT_FILE)

    print("-" * 30)
    print(f"Extracted text saved to: {OUTPUT_FILE}")
    print(f"Preprocessed image saved to: {PROCESSED_IMAGE_FILE}")


if __name__ == "__main__":
    main()