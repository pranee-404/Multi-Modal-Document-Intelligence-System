import json
import os
from utils import pdf_to_image
from parser import extract_text, extract_fields

INPUT_PATH = "sample_docs/test_invoice.pdf"
OUTPUT_PATH = "outputs/parsed.json"

def main():
    print("Converting PDF to image.")
    image = pdf_to_image(INPUT_PATH)
    text = extract_text(image)
    fields = extract_fields(text)

    output = {
        "document_name": os.path.basename(INPUT_PATH),
        "raw_text": text,
        "extracted_fields": fields
    }

    os.makedirs("outputs", exist_ok=True)

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=4)

    print("Done. Output saved.")


if __name__ == "__main__":
    main()