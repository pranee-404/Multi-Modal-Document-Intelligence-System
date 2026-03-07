import easyocr
import re

reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image):
    results = reader.readtext(image, detail=0)
    return "\n".join(results)


def extract_fields(text):
    fields = {}

    invoice_no = re.search(r'Invoice\s*Number[:\s]*([A-Za-z0-9\-]+)', text, re.IGNORECASE)
    date = re.search(r'Date[:\s]*([\d\/\-\.]+)', text, re.IGNORECASE)
    total = re.search(r'Total[:\s]*\$?([\d,\.]+)', text, re.IGNORECASE)

    if invoice_no:
        fields["invoice_number"] = invoice_no.group(1)
    if date:
        fields["date"] = date.group(1)
    if total:
        fields["total_amount"] = total.group(1)

    return fields