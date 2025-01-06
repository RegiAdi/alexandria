def get_price_history(db, ticker, interval, period):

    print("START::get_price_history()")

    price_history_repository = db["price_history"]
    history = ticker.history(interval=interval, period=period)

    # insert price history to db
    for row in history.itertuples():
        price_history = {
            "symbol": ticker.ticker,
            "interval": interval,
            "timestamp": row[0].isoformat(),
            "open": row[1],
            "high": row[2],
            "low": row[3],
            "close": row[4],
            "volume": row[5],
        }

        result = price_history_repository.replace_one(
            {"symbol": ticker.ticker, "timestamp": row[0].isoformat()},
            price_history,
            upsert=True,
        )

    print("END::get_price_history()")
