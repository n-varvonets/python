import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.routing import APIRoute
from starlette.requests import Request
from elasticsearch import AsyncElasticsearch
from logging import getLogger, StreamHandler

from models import CreateUserRequest
from scripts.generate_users_data import MAPPING_FOR_INDEX

logger = getLogger(__name__)
logger.addHandler(StreamHandler())
logger.setLevel("INFO")


async def ping() -> dict:
    return {"success": True}


async def create_index(request: Request) -> dict:
    """Разовая функция для создания нужного индекса ЮЗЕРОВ с КАСТОМНЬІМ мапингом"""
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    await elastic_client.indices.create(index="users", mappings=MAPPING_FOR_INDEX)
    return {"success": True}


async def delete_index(request: Request) -> dict:
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    await elastic_client.indices.delete(index="users")
    return {"success": True}


async def create_user(request: Request, body: CreateUserRequest) -> dict:
    """Пайдентик позволяет как сиарелизатор позволяет прокинуть атррибутьі записи в запрос из модели юзера"""
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    res = await elastic_client.index(index="users", document=body.dict())  # body.dict() - пайдентивскую модель с данньіми переводит в вид словаря
    # index - єто клиент, которьій взаимодействует с документами индекса, а НЕ создает/удалет сам индекс через indices
    logger.info(res)
    return {"success": True, "result": res}


async def get_all_users(request: Request):
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    res = await elastic_client.search(index="users", query={"match_all": {}})  # "match_all": {} - верни мне ВСЕ
    return {"success": True, "result": res}


routes = [
    # ручки create_index, delete_index - нужньі лишь в начале, потом они будут
    # использоваться редко или вообще их спилим.
    # create_index будет   создавать индекст с ОПРЕДЕЛННЬІМ ЗАДАННЬІМ мапингом
    APIRoute(path="/ping", endpoint=ping, methods=["GET"]),
    APIRoute(path="/create_index", endpoint=create_index, methods=["GET"]),
    APIRoute(path="/delete_index", endpoint=delete_index, methods=["GET"]),
    APIRoute(path="/create_user", endpoint=create_user, methods=["POST"]),
    APIRoute(path="/get_all_users", endpoint=get_all_users, methods=["GET"])
]

elastic_client = AsyncElasticsearch()  # создаем обьект клиента для взаимодействия с Еластиком
app = FastAPI()  # создаю само приложение как обьект FastApi
app.state.elastic_client = elastic_client  # обьявляю новьій аттрибут у поля state которьій ссілается на обьект клиента Еластика
# ВАЖНО: теперь  я могу обрашаться к клиенту Еластика через наше приложение(app) для поиска в нем(взаимодействии с ним)
app.include_router(APIRouter(routes=routes))  # приваязьіе к нашему приложение помимо еастик еще и список роутов

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
