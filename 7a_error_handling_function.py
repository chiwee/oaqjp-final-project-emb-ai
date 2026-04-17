import requests


# =========================
# Error Handling Function
# =========================
def safe_watson_request(text, api_key, url):
    """
    Safely calls IBM Watson NLU API with full error handling.
    Returns:
        dict: emotion result OR error message
    """

    # 1. Input validation
    if not text or not isinstance(text, str):
        return {"error": "Invalid input: text must be a non-empty string"}

    endpoint = f"{url}/v1/analyze?version=2022-04-07"

    payload = {
        "text": text,
        "features": {
            "emotion": {}
        }
    }

    try:
        # 2. API request with timeout protection
        response = requests.post(
            endpoint,
            auth=("apikey", api_key),
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=10
        )

        # 3. HTTP status validation
        if response.status_code != 200:
            try:
                error_data = response.json()
            except Exception:
                error_data = response.text

            return {
                "error": "Watson API request failed",
                "status_code": response.status_code,
                "details": error_data
            }

        # 4. Parse JSON safely
        data = response.json()

        emotions = (
            data.get("emotion", {})
                .get("document", {})
                .get("emotion", {})
        )

        # 5. Check missing emotion output
        if not emotions:
            return {"error": "No emotion data returned from Watson API"}

        return emotions

    # 6. Network / unexpected errors
    except requests.exceptions.Timeout:
        return {"error": "Request timeout - Watson API took too long to respond"}

    except requests.exceptions.ConnectionError:
        return {"error": "Connection error - check internet or API URL"}

    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


# =========================
# Simple test (optional)
# =========================
if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"
    URL = "YOUR_INSTANCE_URL"

    test_text = "I am very happy today!"

    result = safe_watson_request(test_text, API_KEY, URL)

    print("RESULT:")
    print(result)
