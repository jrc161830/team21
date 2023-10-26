from azure.storage.blob import BlobClient
import time

while True:

    blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=iotprojectce4201;AccountKey=qoldchKLxrTD10m/gKzSH7Y1VmDsOoB1vpz9WqYGEZXa0r2+09N+ZbyU/mX2h81eBVOaUef9rs/F+AStF+UfXA==;EndpointSuffix=core.windows.net", container_name="project", blob_name="my_blob.txt")

    with open("./data.txt", "wb") as my_blob:
        blob_data = blob.download_blob()
        blob_data.readinto(my_blob)

    time.sleep(1500)
