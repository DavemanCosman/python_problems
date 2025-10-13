import json
import requests
from datetime import datetime

def load_test_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def call_inference_api(payload, token):
    url = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    try:
        response = requests.post(url, headers=headers, json={"inputs": payload}, timeout=10)
        response.raise_for_status()
        print(response.text) # for debugging
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during inference: {e}")
        return None

def log_result(prediction):
    timestamp = datetime.utcnow().isoformat()
    with open("inference_results.log", "a") as log_file:
        log_file.write(f"{timestamp} | prediction: {prediction}\n")

if __name__ == "__main__":
    test_data = load_test_data("test_payload_detailed.json")
    # TODO: Call inference API and log results
    token = "<your_token_here>" #TODO replace with actual token or load from secure place
    
    for item in test_data:
        record_id = item["id"]
        vin = item["vin"]
        year = item["year"]
        result = call_inference_api(item["text"], token)
        if result:
            for prediction in result[0]:
                label = prediction["label"]
                score = prediction["score"]
                log_result(f"record_id: {record_id}, VIN: {vin}, label: {label}, confidence: {score:.2f}")