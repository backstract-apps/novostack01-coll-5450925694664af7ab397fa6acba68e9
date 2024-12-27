from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - novostack01-coll-5450925694664af7ab397fa6acba68e9',debug=False,docs_url='/intelligent-sagar-ee719dbec38411efa7d10242ac12000395/docs',openapi_url='/intelligent-sagar-ee719dbec38411efa7d10242ac12000395/openapi.json')

app.include_router(router, prefix='/intelligent-sagar-ee719dbec38411efa7d10242ac12000395/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()