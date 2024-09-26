
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from deep_translator import GoogleTranslator

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/translate", response_class=HTMLResponse)
def translate(request: Request, english_text: str = Form(...), target_language: str = Form(...)):
    translator = GoogleTranslator(source='auto', target=target_language)
    translation = translator.translate(english_text)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "english_text": english_text,
        "translation": translation
    })



