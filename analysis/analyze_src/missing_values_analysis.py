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


#concrete class for missing value identification.
class SimpleMissingValueAnalysis(MissingValueAnalysisTemplate):
    def identify_missing_values(self, df: pd.DataFrame):
        """
        Purpose: missing value analysis
        Parameter: Dataframe
        Returns: none. prints missing value 
        """
        print("\nMissing Values Count by Column: ")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values>0])

    def visualize_missing_values(self, df:pd.DataFrame):
        """
         Purpose: visualizes missging values using heat maps
        Parameter: The Dataframe to be visualized
        Returns: none. displays heatmap

        """
        print("\nVisualizing Missing Values..")
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(),cbar=False, cmap="viridis")
        plt.title("Missing Values Heatmap")
        plt.show()

if __name__ == "__main__":
    pass