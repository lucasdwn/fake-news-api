from fastapi import APIRouter
from app.schemas import NoticiaInput, ClassificacaoOutput, HistoricoItem
from app.models import classificar_texto, get_model_status, historico

router = APIRouter(prefix="/api")

@router.post("/classificar-noticia", response_model=ClassificacaoOutput)
def classificar_noticia(input: NoticiaInput):
    resultado = classificar_texto(input.texto)
    return resultado

@router.get("/historico", response_model=list[HistoricoItem])
def consultar_historico():
    return historico

@router.get("/status")
def status():
    return get_model_status()
