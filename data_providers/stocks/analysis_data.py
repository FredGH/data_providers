
import pandas as pd
from ticker_data import TickerData

class AnalystsData():
    def __init__(self, yfTickerData:TickerData=None):
        self.yfTickerData = yfTickerData

    @property
    def get_ranalyst_price_targets(self)->pd.DataFrame:
        return self.yfTickerData.analyst_price_targets
    
    @property
    def get_earnings_estimate(self)->pd.DataFrame:
        return self.yfTickerData.earnings_estimate
    
    @property
    def get_revenue_estimate(self)->pd.DataFrame:
        return self.yfTickerData.revenue_estimate
    
    @property
    def get_earnings_history(self)->pd.DataFrame:
        return self.yfTickerData.earnings_history
    
    @property
    def eps_trend(self)->pd.DataFrame:
        return self.yfTickerData.eps_trend
    
    @property
    def eps_revisions(self)->pd.DataFrame:
        return self.yfTickerData.eps_revisions
    
    @property
    def growth_estimates(self)->pd.DataFrame:
        return self.yfTickerData.growth_estimates