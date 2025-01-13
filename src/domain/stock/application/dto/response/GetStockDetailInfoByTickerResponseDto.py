from pydantic import BaseModel, Field


class StockHistoryInfoDto(BaseModel):
    datetime: str
    open: float
    high: float
    low: float
    close: float
    volume: int


class GetStockDetailInfoByTickerResponseDto(BaseModel):
    exchange: str
    mic_code: str
    currency: str
    datetime: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    previous_close: float
    change: float
    percent_change: float
    is_market_open: bool
    stock_history: list[StockHistoryInfoDto]
