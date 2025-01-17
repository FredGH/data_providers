# import sys
# sys.path.insert(0, ".")


class Dummy:
    @property
    def get_data(self) -> list:
        return [1, 2, 3]


if __name__ == "__main__":
    # d = Dummy()
    # print(d.get_data)
    # https://github.com/ranaroussi/yfinance/blob/main/doc/source/reference/examples/ticker.py
    import yfinance as yf

    dat = yf.Ticker("MSFT")
    print(dat.analyst_price_targets)
