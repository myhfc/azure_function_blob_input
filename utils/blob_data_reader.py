from io import BytesIO
import pandas as pd
from azure.storage.blob import BlobClient

container_name = "azure-webjobs-hosts"
file_relative_path_in_container = "prediction_content_based.pickle"

def read_file_from_blob(container_name: str, file_relative_path_in_container: str):
    # Créer une connexion au compte de stockage
    CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=rsfunctiontest2;AccountKey=ER8zDu3X6blM7KivqBwrLDbS0oglG8lGXZyNUf9P982LVVNLL2UG3++K4XYOdnL1anNxHJAZYb2P+AStU3b2jw==;EndpointSuffix=core.windows.net"
    blob_client = BlobClient.from_connection_string(CONNECTION_STRING, container_name, file_relative_path_in_container)
    downloader = blob_client.download_blob(0)
    # Lire les données du blob
    blob_bytes = downloader.readall()

    blob_stream = BytesIO(blob_bytes)
    blob_stream.seek(0)
    dataframe = pd.read_pickle(blob_stream)
    print(dataframe.head())
    return dataframe