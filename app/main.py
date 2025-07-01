from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/generate", response_class=HTMLResponse)
async def generate_portfolio(
    request: Request,
    name: str = Form(...),
    bio: str = Form(...),
    skills: str = Form(...),
    template: str = Form(...),
):
    skills_list = [s.strip() for s in skills.split(",")]
    return templates.TemplateResponse(
        f"portfolio_{template}.html",
        {
            "request": request,
            "name": name,
            "bio": bio,
            "skills": skills_list,
        },
    )
