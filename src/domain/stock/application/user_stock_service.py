from pprint import pprint

from sqlalchemy.orm import Session

from src.domain.news.application.keyword_generator import \
    ExampleKeywordsGenerator
from src.domain.stock.application.dto.response.SaveUserStockResponseDto import SaveUserStockResponseDto
from src.domain.stock.application.dto.response.get_user_stock_ids import \
    GetUserStockIdResponse
from src.domain.stock.application.dto.response.get_user_stocks_response import (
    UserStockInfoDto,
)
from src.domain.stock.domain.model.user_stock import UserStock
from src.domain.stock.domain.stock_info_repository import StockInfoRepository
from src.domain.stock.domain.user_stock_repository import UserStockRepository
from src.shared.exception.base import BaseCustomException
from pymilvus import MilvusClient, model

milvus_client = MilvusClient("milvus_demo.db")
sentence_transformer = model.dense.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2", device="cpu")


class UserStockService:
    def __init__(self, user_stock_repository: UserStockRepository, stock_info_repository: StockInfoRepository, keyword_generator: ExampleKeywordsGenerator):
        self.user_stock_repository = user_stock_repository
        self.stock_info_repository = stock_info_repository
        self.keyword_generator = keyword_generator

    def save_user_stock(self, session: Session, user_id: int, stock_info_ids: list[int]) -> SaveUserStockResponseDto:
        # Check whether the user already input a stock with the same stock_info_id
        user_stocks = self.user_stock_repository.find_all_by_user_id(session, user_id)
        if any(user_stock.stock_info_id == stock_info_id for user_stock in user_stocks):
            raise BaseCustomException(400, f"User already has the stock with stock_info_id: {stock_info_id}")

        saved_user_stocks = []
        for stock_info_id in stock_info_ids:
            user_stock = UserStock(user_id=user_id, stock_info_id=stock_info_id)
            self.user_stock_repository.save(session, user_stock)
            saved_user_stocks.append(user_stock)

        # Add to milvus
        for user_stock in saved_user_stocks:
            stock_info = self.stock_info_repository.find_by_id(session, user_stock.stock_info_id)
            example_keywords = self.keyword_generator.generate_keywords(stock_info.name).keywords
            print(f"Stock Name: {stock_info.name}")
            print("Example Keywords:", example_keywords)
            example_keywords.append(stock_info.name)

            for example_keyword in example_keywords:
                vectors = sentence_transformer.encode_documents([example_keyword])  # convert to embedding

                data = [
                    {
                        "vector": vectors[0],
                        "stock_info_id": stock_info.id,
                        "ticker": stock_info.ticker,
                        "name": stock_info.name,
                        "keyword": example_keyword,
                        "user_id": user_id,
                        "user_stock_id": user_stock.id,
                    }
                ]

                milvus_client.insert(collection_name="dummy_demo1", data=data)
            # res = milvus_client.query(collection_name="dummy_demo1", limit=5)

        return SaveUserStockResponseDto(user_stock_id=[user_stock.id for user_stock in saved_user_stocks])

    def get_user_stocks_by_user_id(self, session: Session, user_id: int) -> list[UserStockInfoDto]:
        user_stocks = self.user_stock_repository.find_all_by_user_id(session, user_id)
        res = []
        for user_stock in user_stocks:
            stock_info = self.stock_info_repository.find_by_id(session, user_stock.stock_info_id)
            res.append(UserStockInfoDto(id=user_stock.stock_info_id, user_stock_id=user_stock.id, ticker=stock_info.ticker, name=stock_info.name))

        return res

