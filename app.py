

from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from TextSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI(
    title="Text Summarization API",
    description="API for generating summaries using trained model",
    version="1.0"
)

pipeline = PredictionPipeline()


class TextRequest(BaseModel):
    text: str

@app.get("/", tags=["Home"])
async def home():
    return RedirectResponse(url="/docs")


@app.post("/predict", tags=["Prediction"])
async def predict(request: TextRequest):
    try:
        summary = pipeline.predict(request.text)

        return {
            "status": "success",
            "input_text": request.text,
            "summary": summary
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "API is running"}


# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)