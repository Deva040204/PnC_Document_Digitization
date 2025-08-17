def model_fn(model_dir):
    return None  # No model, just logic

def input_fn(input_data, content_type):
    return input_data

def predict_fn(data, model):
    text = data.lower()
    return {
        "policy_number": "P12345678",
        "vendor": "ABC Insurance",
        "date": "2023-09-10",
        "loan_id": "LN998877"
    }

def output_fn(prediction, accept):
    import json
    return json.dumps(prediction)
