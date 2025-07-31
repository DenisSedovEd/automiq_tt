from pathlib import Path

from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from my_app.permutation import (
    EmptyInputError,
    permutation,
)

BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

router = APIRouter(prefix="/api", tags=["api"])


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Базовый роут, для отображения главной страницы
    :param request:
    :return:
    """
    return templates.TemplateResponse(
        request,
        "index.html",
        {"request": request},
    )


@router.post("/change", response_class=HTMLResponse)
def change(
    request: Request,
    change_list: str = Form(""),
    perm_rule: str = Form(""),
):
    """
    Роут для упорядочивания входных объектов.
    :param request:
    :param change_list:
    :param perm_rule:
    :return:
    """
    try:
        result = permutation(change_list, perm_rule)
        return templates.TemplateResponse(
            request,
            "index.html",
            {
                "request": request,
                "result": result,
            },
        )
    except (ValueError, EmptyInputError, EmptyInputError) as e:  # pragma: no cover
        return templates.TemplateResponse(
            request,
            "index.html",
            {
                "request": request,
                "error": str(e),
                "has_error": True,
            },
        )
