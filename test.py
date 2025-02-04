# import os

# path = "notebooks/research.ipynb"

# dir,file = os.path.split(path)

# os.makedirs(dir,exist_ok=True)

# with open(path,"w") as f:
#     pass


from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

customedata_obj = CustomData(2.03,62.0,58.0,8.06,8.12,5.05,"Very Good",'J',"SI2")

df = customedata_obj.get_data_as_dataframe()

print(df)
