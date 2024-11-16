import os
import zipfile
from abc import ABC, abstractmethod

import pandas as pd

#Factory Design pattern is used.
#Define an abstract class for Data Ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame: 
        """ Abstract method to ingest data from a given file. """
        pass


#Implement a concrete class for ZIP Ingestion
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """ converts a .zip containing (CSV, Excel, JSON)) file to Data frame"""

        #Ensure its a .zip file
        if not file_path.endswith(".zip"):
            raise ValueError("The provided file is not a zip file.")
        
        #Extract the zip file
        with zipfile.ZipFile(file_path,"r") as zip_ref:
            zip_ref.extractall("extracted_data")

        extracted_files = os.listdir("extracted_data")
        supported_files = [f for f in extracted_files if f.endswith((".csv", ".json", ".xlsx", ".xls"))]

        if not supported_files:
            raise FileNotFoundError("No supported files (CSV, JSON, Excel) found in the zip archive")


        file_types={}
        for file_name in supported_files:
            ext = os.path.splitext(file_name)[1]
            file_types.setdefault(ext, []).append(file_name)



        for ext, files in file_types.items():
            if len(files) > 1:
                print(f"Warning: Multiple files with extension '{ext}' found: {files}")

        
        if file_path.endswith(".csv"):
            df=pd.read_csv(file_path)
        elif file_path.endswith(".json"):
            df=pd.read_json
        elif file_path.endswith(".xlsx"):
            df=pd.read_excel
        
        #Return the Dataframe
        return df

#Implement a concrete class for JSON file ingestion 
class JSONDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """"converts a JSON file to Dataframe"""

        #Ensure its a JSON file
        if not file_path.endswith(".json"):
            raise ValueError("The provided file is not a JSON file")

        df = pd.read_json(file_path)

        #Return the Dataframe
        return df

#Implement a concrete class for EXCEL file
class ExcelDataIngestor(DataIngestor):
    def ingest(self,file_path: str)-> pd.DataFrame:
        """"converts an EXCEL file to Dataframe"""

        #Ensure its an EXCEL file
        if not file_path.endswith(".xlsx"):
            raise ValueError("The provided file is not an EXCEL file")

        df = pd.read_excel(file_path)

        return df


#Implement a concrete class for CSV file
class CsvDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """converts a CSV file to Dataframe"""

        #Ensure its a CSV file
        if not file_path.endswith(".csv"):
            raise ValueError("The provided file is not a CSV file")

        df=pd.read_csv(file_path)

        return df




class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) ->DataIngestor:
        """"Returns the appropriate DataIngestor based on file extension."""
        if file_extension == ".zip":
            return ZipDataIngestor()
        elif file_extension == ".json":
            return JSONDataIngestor()
        elif file_extension in [".xls", ".xlsx"]:
            return ExcelDataIngestor()
        else:
            raise ValueError(f"No ingestor available for file extension: {file_extension}")
        

if __name__== "__main__":


  pass  
