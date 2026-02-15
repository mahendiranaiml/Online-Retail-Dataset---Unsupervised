import pandas as pd 
import logging
from typing import Annotated 
from abc import ABC, abstractmethod
from pathlib import Path
from zenml import step

logging.basicConfig(
     level = logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s"

)
class DataIngestion(ABC):

    """ 
     A class that loads data of CSV type into a DataFrame.

     Attributes:
        filepath : string
        df : pd.DataFrame
    """
    @abstractmethod
    def data_loader(self, filepath : str) -> pd.DataFrame:
        pass

class DataIngestor(DataIngestion):
       
       def __init__(self):
              self.filepath = None
       def data_loader(self, filepath : str) -> pd.DataFrame:
             
            try:
                self.filepath = filepath 
                path = Path(self.filepath)
                df = pd.read_csv(path)
                
                if df.empty:
                     logging.warning("CSV file is empty")
                     return df
                
                logging.info("Data Loaded Successfully")
                logging.info(f"Data has row : {df.shape[0]} and columns : {df.shape[1]}")
                logging.info(f"Data head : \n {df.head(5)}")

                return df
            
            except FileNotFoundError:
                logging.error(f"File Not Found on the path : {path}")
                return None
            
            except PermissionError:
                 logging.error(f"Permission error : {path if path else filepath}")
                 return None
            
            except pd.errors.ParserError as e:
                 logging.error(f"CSV parsing error : {e}")
                 return None
            
            except TypeError as e:
                 logging.error(f"Unexpected error loading dataser : {e}")
                 return None
            
            except Exception  as e:
                logging.error(f"Unable to load Dataset because {e}")
                return None
       

@step
def load_data(filepath : str) ->  Annotated[pd.DataFrame, "Dataset"]:
    DI =  DataIngestor()
    df = DI.data_loader(filepath)
    
    return df