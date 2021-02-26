import pandas as pd
from DataVisualization.Visualization.UserDataObjects.BarClass import BarClass

class DataFrameActions():
    dataFrame = None

    @staticmethod
    def PrepareDataFrame(bars):
        ids = []
        names = []
        manual = []
        automated = []

        for bar in bars:
            ids.append(bar.folderID)
            names.append(bar.headFolderdName)
            manual.append(bar.countManualTestCases)
            automated.append(bar.countAutomatedTestCases)

        DataFrameActions.dataFrame = pd.DataFrame({
            'ids': ids,
            'names': names,
            'manual': manual,
            'automated': automated
        })

        #tidyData = df.melt(id_vars='Factor').rename(columns=str.title)
        tidyData = DataFrameActions.dataFrame.melt(id_vars='names', value_vars=['manual', 'automated'])
        return tidyData

    @staticmethod
    def getDataFrame():
        return DataFrameActions.dataFrame

    @staticmethod
    def getMaxValueOfTestCasesInTidyData(tidyDataFrame):
        listValuesOfTestCases = []

        for folder in tidyDataFrame:
            for cases in folder:
                pass

    def prepareDataForAllTestCasesChartPie(tidyData):
        m = 0
        a = 0

        for bar in tidyData.iloc:
            if bar["variable"] == "manual":
                m = m + int(bar["value"])
            else:
                a = a + int(bar["value"])

        allTestCasesForChartPie = {"manual": m, "automated": a}
        return allTestCasesForChartPie