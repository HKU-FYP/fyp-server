from pprint import pprint

import requests

from src.domain.stock.application.dto.response.GetStockDetailInfoByTickerResponseDto import (
    GetStockDetailInfoByTickerResponseDto,
    StockHistoryInfoDto,
)


class StockInfoFetcher:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_stock_info_detail_by_ticker(self, ticker: str) -> GetStockDetailInfoByTickerResponseDto:
        try:
            print("ticker: ", ticker)
            # Fetch Stock Quote Information
            stock_quote_resp = requests.get(
                url="https://api.twelvedata.com/quote", params={"symbol": ticker, "apikey": self.api_key}
            )
            stock_quote_resp.raise_for_status()
            stock_quote_data = stock_quote_resp.json()

            # Fetch Time Series Information
            stock_time_series_resp = requests.get(
                url="https://api.twelvedata.com/time_series",
                params={"symbol": ticker, "interval": "1day", "apikey": self.api_key},
            )
            stock_time_series_resp.raise_for_status()
            stock_time_series_data = stock_time_series_resp.json()

            # Process Time Series Data
            stock_history = [
                StockHistoryInfoDto(
                    datetime=entry["datetime"],
                    open=float(entry["open"]),
                    high=float(entry["high"]),
                    low=float(entry["low"]),
                    close=float(entry["close"]),
                    volume=int(entry["volume"]),
                )
                for entry in stock_time_series_data.get("values", [])
            ]

            # Create and return the response DTO
            return GetStockDetailInfoByTickerResponseDto(
                exchange=stock_quote_data["exchange"],
                mic_code=stock_quote_data["mic_code"],
                currency=stock_quote_data["currency"],
                datetime=stock_quote_data["datetime"],
                open=float(stock_quote_data["open"]),
                high=float(stock_quote_data["high"]),
                low=float(stock_quote_data["low"]),
                close=float(stock_quote_data["close"]),
                volume=int(stock_quote_data["volume"]),
                previous_close=float(stock_quote_data["previous_close"]),
                change=float(stock_quote_data["change"]),
                percent_change=float(stock_quote_data["percent_change"]),
                is_market_open=stock_quote_data["is_market_open"],
                stock_history=stock_history,
            )

        except requests.exceptions.RequestException as e:
            print(f"Error fetching stock info for {ticker}: {e}")
            return None
