from typing import List, Dict, Optional
import os
import uuid
from pathlib import Path

from fastapi import FastAPI, Form, Request, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 静的ファイルとテンプレートの設定
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# アップロード用ディレクトリの作成
UPLOAD_DIR = Path("app/static/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


# フォーム表示
@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# 生成結果表示
@app.post("/generate", response_class=HTMLResponse)
async def generate_portfolio(
    request: Request,
    # ─────────── 必須 ───────────
    name: str = Form(...),
    template: str = Form(...),
    university: str = Form(...),
    year: str = Form(...),
    graduation_year: str = Form(...),
    self_intro: str = Form(...),
    # スキル（複数行）― 同名フィールドを配列で受け取る
    skill_name: List[str] = Form(...),
    skill_level: List[int] = Form(...),
    # ─────────── 任意 ───────────
    title: Optional[str] = Form(None),
    achievements: Optional[str] = Form(None),
    certifications: Optional[str] = Form(None),
    # 制作物（複数行）― 同名フィールドを配列で受け取る
    project_title: List[str] = Form(...),
    project_description: List[str] = Form(...),
    project_tech: List[str] = Form(...),
    project_url: List[str] = Form([]),
    contact_email: Optional[str] = Form(None),
    contact_sns: Optional[str] = Form(None),
    contact_github: Optional[str] = Form(None),
    # アイコン画像
    icon_image: Optional[UploadFile] = File(None),
):
    # スキル [{name, level}, …] を生成
    skills: List[Dict[str, int]] = [
        {"name": n.strip(), "level": int(l)}
        for n, l in zip(skill_name, skill_level)
        if n.strip()
    ]

    # 制作物 [{title, description, tech, url}, …] を生成
    projects_data = []
    for i in range(len(project_title)):
        if i < len(project_title) and project_title[i].strip():
            project_data = {
                "title": project_title[i].strip(),
                "description": project_description[i].strip() if i < len(project_description) else "",
                "tech": [t.strip() for t in project_tech[i].split(",") if t.strip()] if i < len(project_tech) else [],
                "url": project_url[i].strip() if i < len(project_url) and project_url[i].strip() else None
            }
            projects_data.append(project_data)

    # 任意フィールドの整形
    sns_links = [s.strip() for s in contact_sns.split(",")] if contact_sns else []

    # アイコン画像の処理
    icon_path = None
    if icon_image and icon_image.filename:
        # ファイル拡張子の検証
        allowed_extensions = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
        file_ext = Path(icon_image.filename).suffix.lower()
        
        if file_ext not in allowed_extensions:
            raise HTTPException(status_code=400, detail="サポートされていない画像形式です")
        
        # ユニークなファイル名を生成
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = UPLOAD_DIR / unique_filename
        
        # ファイルを保存
        with open(file_path, "wb") as buffer:
            content = await icon_image.read()
            buffer.write(content)
        
        icon_path = f"/static/uploads/{unique_filename}"

    return templates.TemplateResponse(
        f"portfolio_{template}.html",
        {
            "request": request,
            # 必須
            "name": name,
            "university": university,
            "year": year,
            "graduation_year": graduation_year,
            "self_intro": self_intro,
            "skills": skills,
            # 任意
            "title": title,
            "achievements": achievements,
            "certifications": certifications,
            "projects": projects_data,
            "contact_email": contact_email,
            "sns_links": sns_links,
            "contact_github": contact_github,
            "icon_path": icon_path,
        },
    )
