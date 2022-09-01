from fastapi import FastAPI
from api import api


app = FastAPI()


if __name__ == '__main__':

    app.include_router(api.api_router)
