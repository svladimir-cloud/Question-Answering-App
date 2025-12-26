from fastapi import FastAPI
from pydantic import BaseModel
from ML_model import pipe

class Item(BaseModel):
    question: str
    context: str

pipeline = pipe()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": 
            "Question Answering App.\
            Сервис использует языковую модель для ответа на вопрос по контексту.\
            Модель: `deepset/roberta-base-squad2`"
            }


@app.post("/predict")
async def predict(item: Item):
    '''Give an answer for a question using context'''

    return pipeline(question=item.question, context=item.context)

# def predict(item: Item):
#     return pipeline(question=item.question, context=item.context)

# a = Item(question='fff', context='333')