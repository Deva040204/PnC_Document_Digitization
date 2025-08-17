# SageMaker inference script for extracting policy data using BERT

from transformers import BertTokenizer, BertForTokenClassification
from transformers import pipeline
import torch
import json

# Load model and tokenizer once
model = BertForTokenClassification.from_pretrained("dslim/bert-base-NER")
tokenizer = BertTokenizer.from_pretrained("dslim/bert-base-NER")
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def predict(text):
    """
    Use a pre-trained BERT NER pipeline to extract named entities from OCR text.
    This can be further fine-tuned or rule-enhanced.
    """
    entities = ner_pipeline(text)
    output = {
        "policy_number": None,
        "vendor": None,
        "date": None,
        "loan_id": None,
        "entities": []
    }

    for ent in entities:
        label = ent['entity_group'].lower()
        word = ent['word']

        if "organization" in label or "vendor" in label:
            output["vendor"] = word
        elif "date" in label:
            output["date"] = word
        elif "number" in label and output["policy_number"] is None:
            output["policy_number"] = word
        output["entities"].append(ent)

    # Heuristic fallback extraction
    lines = text.split("\n")
    for line in lines:
        if "policy" in line.lower():
            output["policy_number"] = output["policy_number"] or line.split(":")[-1].strip()
        elif "loan" in line.lower():
            output["loan_id"] = output["loan_id"] or line.split(":")[-1].strip()

    return output

# For testing locally
if __name__ == "__main__":
    sample_text = '''
    Policy Number: PNC123456
    Vendor: ABC Insurance
    Date: 2023-08-15
    Loan ID: LN987654
    '''
    result = predict(sample_text)
    print(json.dumps(result, indent=2))
