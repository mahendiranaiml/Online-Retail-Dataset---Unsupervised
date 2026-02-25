from zenml import step
from abc import abstractmethod, ABC
import pandas as pd
from typing import Annotated

class Preprocessor(ABC):

    """
    This class cleans the DataSet i.e removing null values, wrong entries and invalid records

    """

    @abstractmethod
    def preprocessor(self, df : pd.DataFrame) -> pd.DataFrame:
        pass



class DataPreprocessor(Preprocessor):

    def preprocessor(self, df : pd.DataFrame) -> pd.DataFrame:
# Remove Null Value
# Remove Cancelled items and -negative units
# Drop Duplicates 
# Column correct DataType : Date
# df4 = df3[~(df3['UnitPrice'] <= 0.00)].copy() 
# df3 = df2[(df2['StockCode'] != "M") & (df2['StockCode'] != "D")  ].copy()
# Quantity less than 0 
# df5 = df4[df4['StockCode'] != 'BANK CHARGES'].copy()

        return df
    

@step
def process(df:pd.DataFrame) -> Annotated[pd.DataFrame, "DataFrame"]:

    dp = DataPreprocessor()
    df = dp.preprocessor(df)
    return df