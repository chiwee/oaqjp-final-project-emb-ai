import requests
import json

# =========================
# CONFIG (change if needed)
# =========================
BASE_URL = "http://127.0.0.1:5000/detect"


# =========================
# Test cases
# =========================
TEST_CASES = [
    "I am very happy today because I got an A grade.",
    "I feel sad and disappointed about my result.",
    "I am extremely angry and frustrated.",
    "I am scared about the upcoming exam.",
    "This is disgusting and terrible experience."
]


def test_emotion_api():
    print("\n=== EMOTION DETECTION API TEST ===\n")

    for i, text in enumerate(TEST_CASES, 1):
        print(f"Test Case {i}: {text}")

        response = requests.post(
            BASE_URL,
            headers={"Content-Type": "application/json"},
            json={"text": text}
        )

        # Check HTTP status
        print("Status Code:", response.status_code)

        try:
            data = response.json()
        except Exception:
            print("Invalid JSON response")
            print(response.text)
            continue

        # Print result
        print("Response:")
        print(json.dumps(data, indent=4))
        print("-" * 50)


# =========================
# Run test
# =========================
if __name__ == "__main__":
    test_emotion_api()
