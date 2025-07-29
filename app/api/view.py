from fastapi import APIRouter, Request, Form
from starlette.responses import HTMLResponse

from app.permutation import permutation
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="/api", tags=["api"])


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request},
    )


@router.post("/change", response_class=HTMLResponse)
def change(
    request: Request,
    change_list: str = Form(""),
    perm_rule: str = Form(""),
):
    result = permutation(change_list, perm_rule)
    # new_list = "ПОЛУЧИЛОСЬ"
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            # "result": result,
            "result": f"{change_list} {perm_rule}",
        },
    )
