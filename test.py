# import os

# path = "notebooks/research.ipynb"

# dir,file = os.path.split(path)

# os.makedirs(dir,exist_ok=True)

# with open(path,"w") as f:
#     pass


# from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

# customedata_obj = CustomData(2.03,62.0,58.0,8.06,8.12,5.05,"Very Good",'J',"SI2")

# df = customedata_obj.get_data_as_dataframe()

# print(df)

import os

def check_file_exists(file_path):
    if os.path.isfile(file_path):
        print(f"The file '{file_path}' exists in the specified directory.")
    else:
        print(f"The file '{file_path}' does NOT exist in the specified directory.")

# Define the expected path for data_ingestion.py
expected_path = os.path.join("src", "DimondPricePrediction", "components", "data_ingestion.py")

# Check if the file exists in the specified path
check_file_exists(expected_path)

from src.DimondPricePrediction.components.data_ingestion import DataIngestion

