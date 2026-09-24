from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field, model_validator

app = FastAPI(title="PubRescue readiness API", version="0.1.0")

class PublisherFile(BaseModel):
    name: str = Field(min_length=5, max_length=120, pattern=r"(?i)^.+\.pub$")
    pages: int = Field(ge=1, le=1000)
    size_mb: float = Field(gt=0, le=500)
    fonts: int = Field(ge=0, le=100)
    linked_images: int = Field(ge=0, le=5000)

class AuditRequest(BaseModel):
    files: list[PublisherFile] = Field(min_length=1, max_length=100)
    output_format: Literal["pdf", "docx", "png"]
    include_visual_qa: bool = True
    @model_validator(mode="after")
    def unique_names(self):
        names = [item.name.lower() for item in self.files]
        if len(names) != len(set(names)):
            raise ValueError("file names must be unique")
        return self

class AuditResponse(BaseModel):
    total_pages: int
    high_risk_files: int
    estimated_minutes: int
    estimated_price_usd: int
    recommendation: str
    warnings: list[str]

def audit_batch(payload: AuditRequest) -> AuditResponse:
    multipliers = {"pdf": 1.0, "docx": 1.55, "png": 1.2}
    total_pages = sum(item.pages for item in payload.files)
    high_risk = sum(item.pages > 50 or item.fonts > 6 or item.linked_images > 30 for item in payload.files)
    warnings = []
    if high_risk:
        warnings.append(f"{high_risk} file(s) require manual visual review.")
    if payload.output_format == "docx":
        warnings.append("Editable DOCX can reflow complex Publisher layouts.")
    minutes = round((len(payload.files) * 4 + total_pages * 0.7 + high_risk * 18) * multipliers[payload.output_format])
    if payload.include_visual_qa:
        minutes += round(total_pages * 0.35)
    price = max(79, round((49 + total_pages * 1.35 + high_risk * 35) * multipliers[payload.output_format]))
    recommendation = "Pilot high-risk files first" if high_risk else "Ready for batch conversion"
    return AuditResponse(total_pages=total_pages, high_risk_files=high_risk, estimated_minutes=minutes,
                         estimated_price_usd=price, recommendation=recommendation, warnings=warnings)

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/audit", response_model=AuditResponse)
def audit(payload: AuditRequest) -> AuditResponse:
    return audit_batch(payload)
