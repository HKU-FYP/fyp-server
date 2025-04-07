from fastapi import APIRouter, Depends, status

from src.domain.di_container import stock_info_service
from src.domain.stock.application.dto.request.GetStockInfoDetailRequestDto import (
    GetStockInfoDetailRequestDto,
)
from src.domain.stock.application.dto.response.get_stock_info_response import (
    GetStockInfoResponseDto,
)
from src.shared.database.session import get_session
from src.shared.utils.auth_util import get_current_user_id

router = APIRouter(tags=["Stock Info"])


@router.get("/all-stock-ticker-info", status_code=status.HTTP_200_OK, response_model=GetStockInfoResponseDto)
def get_all_stock_ticker_info(
    session=Depends(get_session), user_id: int = Depends(get_current_user_id)
) -> GetStockInfoResponseDto:
    return stock_info_service.get_all_stock_info(session)


@router.get("/stocks/info/detail", status_code=status.HTTP_200_OK)
def get_stock_info_detail(ticker: str, user_id: int = Depends(get_current_user_id)):
    # return stock_info_service.get_stock_info_detail_by_ticker(ticker=ticker)

    if (ticker == "AAPL") :
        return {
            "exchange": "NASDAQ",
            "mic_code": "XNGS",
            "currency": "USD",
            "datetime": "2025-04-04",
            "open": 193.89,
            "high": 199.88,
            "low": 187.34,
            "close": 188.38,
            "volume": 125569000,
            "previous_close": 203.19,
            "change": -14.81,
            "percent_change": -7.28874,
            "is_market_open": False,
            "stock_history": [
                {
                    "datetime": "2025-04-04",
                    "open": 193.89,
                    "high": 199.88,
                    "low": 187.34,
                    "close": 188.38,
                    "volume": 125569000
                },
                {
                    "datetime": "2025-04-03",
                    "open": 205.53999,
                    "high": 207.49001,
                    "low": 201.25,
                    "close": 203.19,
                    "volume": 103419000
                },
                {
                    "datetime": "2025-04-02",
                    "open": 221.32001,
                    "high": 225.19,
                    "low": 221.020004,
                    "close": 223.89,
                    "volume": 35905900
                },
                {
                    "datetime": "2025-04-01",
                    "open": 219.81,
                    "high": 223.67999,
                    "low": 218.89999,
                    "close": 223.19,
                    "volume": 36412700
                },
                {
                    "datetime": "2025-03-31",
                    "open": 217.0099945,
                    "high": 225.62,
                    "low": 216.23,
                    "close": 222.13,
                    "volume": 65299300
                },
                {
                    "datetime": "2025-03-28",
                    "open": 221.67,
                    "high": 223.81,
                    "low": 217.67999,
                    "close": 217.89999,
                    "volume": 39818600
                },
                {
                    "datetime": "2025-03-27",
                    "open": 221.39,
                    "high": 224.99001,
                    "low": 220.56,
                    "close": 223.85001,
                    "volume": 37094800
                },
                {
                    "datetime": "2025-03-26",
                    "open": 223.50999,
                    "high": 225.020004,
                    "low": 220.47,
                    "close": 221.53,
                    "volume": 34466100
                },
                {
                    "datetime": "2025-03-25",
                    "open": 220.77,
                    "high": 224.10001,
                    "low": 220.080002,
                    "close": 223.75,
                    "volume": 34493600
                },
                {
                    "datetime": "2025-03-24",
                    "open": 221.0,
                    "high": 221.48,
                    "low": 218.58,
                    "close": 220.73,
                    "volume": 44299500
                },
                {
                    "datetime": "2025-03-21",
                    "open": 211.56,
                    "high": 218.84,
                    "low": 211.28,
                    "close": 218.27,
                    "volume": 94127800
                },
                {
                    "datetime": "2025-03-20",
                    "open": 213.99001,
                    "high": 217.49001,
                    "low": 212.22,
                    "close": 214.10001,
                    "volume": 48862900
                },
                {
                    "datetime": "2025-03-19",
                    "open": 214.22,
                    "high": 218.75999,
                    "low": 213.75,
                    "close": 215.24001,
                    "volume": 54385400
                },
                {
                    "datetime": "2025-03-18",
                    "open": 214.16,
                    "high": 215.14999,
                    "low": 211.49001,
                    "close": 212.69,
                    "volume": 42432400
                },
                {
                    "datetime": "2025-03-17",
                    "open": 213.31,
                    "high": 215.22,
                    "low": 209.97,
                    "close": 214.0,
                    "volume": 48073400
                },
                {
                    "datetime": "2025-03-14",
                    "open": 211.25,
                    "high": 213.95,
                    "low": 209.58,
                    "close": 213.49001,
                    "volume": 60107600
                },
                {
                    "datetime": "2025-03-13",
                    "open": 215.95,
                    "high": 216.84,
                    "low": 208.42,
                    "close": 209.67999,
                    "volume": 61368300
                },
                {
                    "datetime": "2025-03-12",
                    "open": 220.14,
                    "high": 221.75,
                    "low": 214.91,
                    "close": 216.98,
                    "volume": 62547500
                },
                {
                    "datetime": "2025-03-11",
                    "open": 223.81,
                    "high": 225.84,
                    "low": 217.45,
                    "close": 220.84,
                    "volume": 76137400
                },
                {
                    "datetime": "2025-03-10",
                    "open": 235.53999,
                    "high": 236.16,
                    "low": 224.22,
                    "close": 227.48,
                    "volume": 72071200
                },
                {
                    "datetime": "2025-03-07",
                    "open": 235.11,
                    "high": 241.37,
                    "low": 234.75999,
                    "close": 239.070007,
                    "volume": 46273600
                },
                {
                    "datetime": "2025-03-06",
                    "open": 234.44,
                    "high": 237.86,
                    "low": 233.16,
                    "close": 235.33,
                    "volume": 45170400
                },
                {
                    "datetime": "2025-03-05",
                    "open": 235.42,
                    "high": 236.55,
                    "low": 229.23,
                    "close": 235.74001,
                    "volume": 47227600
                },
                {
                    "datetime": "2025-03-04",
                    "open": 237.71001,
                    "high": 240.070007,
                    "low": 234.67999,
                    "close": 235.92999,
                    "volume": 53798100
                },
                {
                    "datetime": "2025-03-03",
                    "open": 241.78999,
                    "high": 244.029999,
                    "low": 236.11,
                    "close": 238.029999,
                    "volume": 47184000
                },
                {
                    "datetime": "2025-02-28",
                    "open": 236.95,
                    "high": 242.089996,
                    "low": 230.2,
                    "close": 241.84,
                    "volume": 56833400
                },
                {
                    "datetime": "2025-02-27",
                    "open": 239.41,
                    "high": 242.46001,
                    "low": 237.059998,
                    "close": 237.3,
                    "volume": 41153600
                },
                {
                    "datetime": "2025-02-26",
                    "open": 244.33,
                    "high": 244.98,
                    "low": 239.13,
                    "close": 240.36,
                    "volume": 44433600
                },
                {
                    "datetime": "2025-02-25",
                    "open": 248.0,
                    "high": 250.0,
                    "low": 244.91,
                    "close": 247.039993,
                    "volume": 48013300
                },
                {
                    "datetime": "2025-02-24",
                    "open": 244.92999,
                    "high": 248.86,
                    "low": 244.42,
                    "close": 247.10001,
                    "volume": 51326400
                }
            ]
        }
    else:
        return {
                "exchange": "NASDAQ",
                "currency": "USD",
                "datetime": "2025-01-10",
                "open": 240.0099945,
                "high": 240.16,
                "low": 233.0,
                "close": 236.85001,
                "volume": 61679400,
                "previous_close": 242.7,
                "change": -5.84999,
                "percent_change": -2.41038,
                "is_market_open": False,
                "stock_history": [
                    {
                        "datetime": "2025-01-10",
                        "open": 240.0099945,
                        "high": 240.16,
                        "low": 233.0,
                        "close": 236.85001,
                        "volume": 61679400,
                    },
                    {
                        "datetime": "2025-01-08",
                        "open": 241.92,
                        "high": 243.71001,
                        "low": 240.050003,
                        "close": 242.7,
                        "volume": 37628900,
                    },
                    {
                        "datetime": "2025-01-07",
                        "open": 242.98,
                        "high": 245.55,
                        "low": 241.35001,
                        "close": 242.21001,
                        "volume": 40856000,
                    },
                    {
                        "datetime": "2025-01-06",
                        "open": 244.31,
                        "high": 247.33,
                        "low": 243.2,
                        "close": 245.0,
                        "volume": 45045600,
                    },
                    {
                        "datetime": "2025-01-03",
                        "open": 243.36,
                        "high": 244.17999,
                        "low": 241.89,
                        "close": 243.36,
                        "volume": 40244100,
                    },
                    {
                        "datetime": "2025-01-02",
                        "open": 248.92999,
                        "high": 249.10001,
                        "low": 241.82001,
                        "close": 243.85001,
                        "volume": 55740700,
                    },
                    {
                        "datetime": "2024-12-31",
                        "open": 252.44,
                        "high": 253.28,
                        "low": 249.42999,
                        "close": 250.42,
                        "volume": 39480700,
                    },
                    {
                        "datetime": "2024-12-30",
                        "open": 252.23,
                        "high": 253.5,
                        "low": 250.75,
                        "close": 252.2,
                        "volume": 35557500,
                    },
                    {
                        "datetime": "2024-12-27",
                        "open": 257.82999,
                        "high": 258.70001,
                        "low": 253.059998,
                        "close": 255.59,
                        "volume": 42355300,
                    },
                    {
                        "datetime": "2024-12-26",
                        "open": 258.19,
                        "high": 260.10001,
                        "low": 257.63,
                        "close": 259.019989,
                        "volume": 27237100,
                    },
                    {
                        "datetime": "2024-12-24",
                        "open": 255.49001,
                        "high": 258.20999,
                        "low": 255.28999,
                        "close": 258.20001,
                        "volume": 23234700,
                    },
                    {
                        "datetime": "2024-12-23",
                        "open": 254.77,
                        "high": 255.64999,
                        "low": 253.45,
                        "close": 255.27,
                        "volume": 40858800,
                    },
                    {
                        "datetime": "2024-12-20",
                        "open": 248.039993,
                        "high": 255.0,
                        "low": 245.69,
                        "close": 254.49001,
                        "volume": 147495300,
                    },
                    {
                        "datetime": "2024-12-19",
                        "open": 247.5,
                        "high": 252.0,
                        "low": 247.089996,
                        "close": 249.78999,
                        "volume": 60882300,
                    },
                    {
                        "datetime": "2024-12-18",
                        "open": 252.16,
                        "high": 254.28,
                        "low": 247.74001,
                        "close": 248.050003,
                        "volume": 56774100,
                    },
                    {
                        "datetime": "2024-12-17",
                        "open": 250.080002,
                        "high": 253.83,
                        "low": 249.78,
                        "close": 253.48,
                        "volume": 51356400,
                    },
                    {
                        "datetime": "2024-12-16",
                        "open": 247.99001,
                        "high": 251.38,
                        "low": 247.64999,
                        "close": 251.039993,
                        "volume": 51694800,
                    },
                    {
                        "datetime": "2024-12-15",
                        "open": 247.99001,
                        "high": 251.37891,
                        "low": 247.75,
                        "close": 251.039993,
                        "volume": 46018060,
                    },
                    {
                        "datetime": "2024-12-13",
                        "open": 247.82001,
                        "high": 249.28999,
                        "low": 246.24001,
                        "close": 248.13,
                        "volume": 33155300,
                    },
                    {
                        "datetime": "2024-12-12",
                        "open": 246.89,
                        "high": 248.74001,
                        "low": 245.67999,
                        "close": 247.96001,
                        "volume": 32777500,
                    },
                    {
                        "datetime": "2024-12-11",
                        "open": 247.96001,
                        "high": 250.8,
                        "low": 246.25999,
                        "close": 246.49001,
                        "volume": 45205800,
                    },
                    {
                        "datetime": "2024-12-10",
                        "open": 246.89,
                        "high": 248.21001,
                        "low": 245.34,
                        "close": 247.77,
                        "volume": 36914800,
                    },
                    {
                        "datetime": "2024-12-09",
                        "open": 241.83,
                        "high": 247.24001,
                        "low": 241.75,
                        "close": 246.75,
                        "volume": 44649200,
                    },
                    {
                        "datetime": "2024-12-08",
                        "open": 241.83,
                        "high": 247.24001,
                        "low": 241.75,
                        "close": 246.75,
                        "volume": 44649232,
                    },
                    {
                        "datetime": "2024-12-06",
                        "open": 242.91,
                        "high": 244.63,
                        "low": 242.080002,
                        "close": 242.84,
                        "volume": 36870600,
                    },
                    {
                        "datetime": "2024-12-05",
                        "open": 243.99001,
                        "high": 244.53999,
                        "low": 242.13,
                        "close": 243.039993,
                        "volume": 40033900,
                    },
                    {
                        "datetime": "2024-12-04",
                        "open": 242.87,
                        "high": 244.11,
                        "low": 241.25,
                        "close": 243.0099945,
                        "volume": 44383900,
                    },
                    {
                        "datetime": "2024-12-03",
                        "open": 239.81,
                        "high": 242.75999,
                        "low": 238.89999,
                        "close": 242.64999,
                        "volume": 38861000,
                    },
                    {
                        "datetime": "2024-12-02",
                        "open": 237.27,
                        "high": 240.78999,
                        "low": 237.16,
                        "close": 239.59,
                        "volume": 48137100,
                    },
                    {
                        "datetime": "2024-11-29",
                        "open": 234.81,
                        "high": 237.81,
                        "low": 233.97,
                        "close": 237.33,
                        "volume": 28481400,
                    },
                ],
            }
