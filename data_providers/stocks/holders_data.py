
import pandas as pd
from ticker_data import TickerData

class HoldersData():
    def __init__(self, yfTickerData:TickerData=None):
        self.yfTickerData = yfTickerData

    @property
    def get_major_holders(self)->pd.DataFrame:
        return self.yfTickerData.major_holders
    
    @property
    def get_institutional_holders(self)->pd.DataFrame:
        return self.yfTickerData.institutional_holders
    
    @property
    def get_mutualfund_holders(self)->pd.DataFrame:
        return self.yfTickerData.cashflow
    
    @property
    def get_quarterly_cashflow(self)->pd.DataFrame:
        return self.yfTickerData.mutualfund_holders
    
    @property
    def get_insider_transactions(self)->pd.DataFrame:
        return self.yfTickerData.insider_transactions
    
    @property
    def get_insider_purchases(self)->pd.DataFrame:
        return self.yfTickerData.insider_purchases
    
    @property
    def get_insider_roster_holders(self)->pd.DataFrame:
        return self.yfTickerData.insider_roster_holders
