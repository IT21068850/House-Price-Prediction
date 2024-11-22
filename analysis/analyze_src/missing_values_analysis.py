from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#Abstract base class for missing value analysis

#This class defines a template for missing value analysis
class MissingValueAnalysisTemplate(ABC):
    def analyze(self, df: pd.DataFrame):
        """
        Puporse: performs a complete missing value analysis
        Parameter: the dataframe to be analyzed 
        Returns: none.
        """
        self.identify_missing_values(df)
        self.visualize_missing_values(df)

        @abstractmethod
        def identify_missing_values(self, df: pd.DataFrame):
            """
            Purpose: identify missing values in dataframe
            Parameter: The Dataframe to be analyzed
            Returns: none . it displays the missing value
            """
            pass

        @abstractmethod
        def visualize_missing_values(self, df:pd.DataFrame):
            """
            Purpose: visualizes missging values using heat maps
            Parameter: The Dataframe to be visualized
            Returns: none. displays heatmap
            
            """
            pass

        