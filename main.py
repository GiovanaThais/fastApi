from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#ROTA RAIZ
@app.get('/')
def source():
    return {"ola": "mundo"}

#criar model
class User(BaseModel):
    id: int
    email: str
    password: str

#criar base de dados
data_bases = [
    User(id=1, email="gio@gmail.com", password="gigitgc123"),
    User(id=2, email="teste@teste.com", password="teste123")
]

#rota get all 
@app.get('/users')
def get_all_users():
    return data_bases

#rota get id
@app.get("/users/{id_user}")
def get_user_id(id_user: int):
    for user in data_bases:
        if(user.id == id_user):
            return user
    return {"Status": 404,
     "Mensagem":"usuario não encontrado"}
    

#rota Insere
@app.post("/users")
def create_user(user: User):
    #criar regras de negocios
    list(user.password)
    if len(user.password) > 8:
        data_bases.append(user)
        return user
    return {"senha deve contar ao menos 8 digitos"}
