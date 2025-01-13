import pandas as pd
import pymysql

from src.domain.stock.domain.model.stock_info import StockInfo
from src.shared.database.session import get_session


def main():
    df = pd.read_csv("stock_info.csv")
    df = df.dropna(subset=["Symbol", "Company Name"])

    with next(get_session()) as session:
        for _, row in df.iterrows():
            stock = StockInfo(ticker=row["Symbol"], name=row["Company Name"])
            session.add(stock)
            session.commit()


if __name__ == "__main__":
    main()
