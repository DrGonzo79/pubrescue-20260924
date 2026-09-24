from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def payload():
    return {"files":[{"name":"yearbook.pub","pages":64,"size_mb":118.4,"fonts":7,"linked_images":42},
                     {"name":"handbook.pub","pages":18,"size_mb":12.8,"fonts":3,"linked_images":5}],
            "output_format":"pdf","include_visual_qa":True}

def test_health():
    assert client.get("/health").json() == {"status":"ok"}

def test_audits_batch_and_flags_complex_file():
    response = client.post("/audit", json=payload())
    assert response.status_code == 200
    body = response.json()
    assert body["total_pages"] == 82
    assert body["high_risk_files"] == 1
    assert body["recommendation"] == "Pilot high-risk files first"
    assert body["estimated_price_usd"] == 195

def test_docx_warns_about_reflow():
    data = payload(); data["output_format"] = "docx"
    assert any("reflow" in warning for warning in client.post("/audit", json=data).json()["warnings"])

def test_rejects_invalid_and_duplicate_files():
    data = payload(); data["files"][0]["name"] = "yearbook.pdf"
    assert client.post("/audit", json=data).status_code == 422
    data = payload(); data["files"][1]["name"] = "YEARBOOK.PUB"
    assert client.post("/audit", json=data).status_code == 422
