import requests
import json

# =========================
# Flask API endpoint
# =========================
BASE_URL = "http://127.0.0.1:5000/detect"

# =========================
# Test dataset
# =========================
test_data = [
    "I am very happy today because I got good results.",
    "I feel very sad and disappointed.",
    "I am extremely angry about the situation.",
    "I am scared of failing my exam.",
    "This is disgusting and unacceptable."
]

# =========================
# Unit Test Execution
# =========================
print("\n===== 5B UNIT TESTING RESULT =====\n")

passed = 0
failed = 0

for i, text in enumerate(test_data, 1):
    print(f"Test Case {i}")
    print("Input:", text)

    try:
        response = requests.post(
            BASE_URL,
            headers={"Content-Type": "application/json"},
            json={"text": text},
            timeout=10
        )

        if response.status_code == 200:
            result = response.json()
            print("Output:", json.dumps(result, indent=4))
            print("✔ PASS")
            passed += 1
        else:
            print("❌ FAIL - HTTP Error:", response.status_code)
            failed += 1

    except Exception as e:
        print("❌ FAIL - Exception:", str(e))
        failed += 1

    print("-" * 50)

# =========================
# Summary Report
# =========================
print("\n===== SUMMARY =====")
print("Total:", len(test_data))
print("Passed:", passed)
print("Failed:", failed)

if passed + failed > 0:
    print("Success Rate:", f"{(passed/(passed+failed))*100:.2f}%")
