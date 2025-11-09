from fastapi import FastAPI

app=FastAPI()

@app.get("/predict")
#USING SIMPLE TITANIC DATASET HERE TO SHOWCASE WORKING 
def predict_model(age:int , sex:str):
    if age<15 or sex=='F':
        return{'survived':1}
    else:
        return{'survived':0}
    




    