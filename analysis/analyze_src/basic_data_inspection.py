from abc import ABC, abstractmethod
import pandas as pd


#Abstract base class for data inspection strategies

#This class defines a common interface for data inspection startegies 
#Subclasses must implemet the inspect method.

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df :pd.DataFrame):
        """"
        Purpose: Perform a specific type of Data Inspetion

        Parameters: Dataframe

        Returns: none (methods prints the inspection results directly) 
        
        """
        pass


#This stratergy implements the data types of each column
class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Purpose: implements the data types of each column

        Parameters: DataFrame

        Returns: None (prints the results) 

        """

        print("\nData Types and No-null Counts:")
        print(df.info())

#This Strategy implements the summary statistics of both Numerical and Categorical data 
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Purpose: provides a summary statistics
        Parameters:Dataframe
        Returns: None (prints the results)
        """

        print("\Summary Statistics (Numerical Features): ")
        print(df.describe())
        print("\Summary Statistics (Categorical Features): ")
        print(df.describe(include=["0"]))


#This allows you to switch between different data inpsection strategies
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Purpose: Initializes the DataInspector with a specific inspection
        Parameters: strategy (DataInspectionStrategy)
        Returns: none
        """
        self._strategy =  strategy
        
        def set_strategy(self, strategy: DataInspectionStrategy):
            """
            Purpose:
            Parameters:
            Returns:
            
            """
            self._strategy = strategy

        def execute_inspection(self, df: pd.DataFrame):
            """
            Purpose: executes the inspection using the current strategy
            Parameters:Dataframe
            Returns:none (executes the strategies inspection method)
            """
            self._strategy.inspect(df)


