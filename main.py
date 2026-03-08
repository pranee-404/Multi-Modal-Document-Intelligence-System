import argparse
import json
import os
import cv2
from utils import pdf_to_image
from parser import extract_text, extract_fields
from llm_engine import analyze_document
from utils import draw_boxes

parser = argparse.ArgumentParser(description="Multi-Modal Document Intelligence System")
parser.add_argument("document", help="PDF Path.")

args = parser.parse_args()
INPUT_PATH = args.document
OUTPUT_PATH = "outputs/result.json"

def main():
    print("Converting PDF to image.")
    image = pdf_to_image(INPUT_PATH)

    text, boxes = extract_text(image)

    visualized = draw_boxes(image.copy(), boxes)
    os.makedirs("outputs", exist_ok=True)
    cv2.imwrite("outputs/ocr_visualization.png", visualized)

    fields = extract_fields(text)

    print("Running LLM reasoning.")
    analysis_raw = analyze_document(text, fields)
    analysis_raw = analysis_raw.strip()

    if analysis_raw.startswith("```"):
        analysis_raw = analysis_raw.replace("```json", "").replace("```", "").strip()

    try:
        analysis = json.loads(analysis_raw)
    except:
        analysis = {"raw_response": analysis_raw}

    output = {
        "document_name": os.path.basename(INPUT_PATH),
        "extracted_data": {
            "fields": fields,
            "raw_text": text
        },
        "llm_analysis": analysis
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=4)

    print("Output saved.")

    print("\nDocument Analysis Complete\n")

    print("Detected Fields:")
    for k, v in fields.items():
        print(f"{k}: {v}")

    print("\nLLM Summary:")
    print(analysis.get("summary", "No summary generated"))


if __name__ == "__main__":
    main()