from io import BytesIO
import logging
import json
import pandas as pd
import azure.functions as func 



def predict(data, user_id, rs_type="content_based"):
    # Prediction:
    result_pred = list(data[data["user_id"]==str(user_id)]["article_id"]) 
    return result_pred   

#@func.BlobStorageInput("prediction_content_based.pickle", "azure-webjobs-hosts")
def main(req: func.HttpRequest, inputblob: func.InputStream) : #-> func.HttpResponse:
#def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    user_id = req.params.get("user_id")
    if not (user_id):
        user_id="0"
    else :
        user_id = str(user_id)

    blob_bytes = inputblob.read()
    blob_stream = BytesIO(blob_bytes)
    blob_stream.seek(0)
    data = pd.read_pickle(blob_stream)
    recomandations = predict(data, user_id, rs_type="content_based") 
    result = json.dumps({"user_id":recomandations}) 
    print(recomandations)
    
    return  func.HttpResponse(result, status_code=200)