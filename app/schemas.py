from pydantic import BaseModel
from typing import List

class NoticiaInput(BaseModel):
    texto: str

class ClassificacaoOutput(BaseModel):
    classe: str
    probabilidade: float
    palavras_influentes: List[str]

class HistoricoItem(BaseModel):
    texto: str
    classe: str
    probabilidade: float
