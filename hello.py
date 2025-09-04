from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
class BMIOutPut(BaseModel):
    bmi: float
    message: str


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # أو ضع رابط الصفحة المسموح لها فقط
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def cal(
        weight: float = Query(..., gt=0),
         height: float = Query(..., gt=0)
):
    bmi = weight / (height ** 2)
    message = "مرحبا أكرم"

    return BMIOutPut(bmi=bmi, message=message)
