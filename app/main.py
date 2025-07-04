from fastapi import FastAPI
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure aqui os domínios que podem acessar seu backend
origins = [
    "http://localhost:5173",  # endereço do seu frontend em dev
    "http://127.0.0.1:5173",  # às vezes usa esse também
    # Se quiser liberar geral (não recomendado para produção):
    # "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
