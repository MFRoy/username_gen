import logging
import requests
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey


# </create_container_if_not_exists>

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Initialize the Cosmos client
    endpoint = "https://username-gen-db.documents.azure.com:443/"
    key = 'GEWcJCUV4RkpMRorPFh6bNNtK9KqivE9xaU0uUb8ZKYUvH21VaO6DdHWFnTsA47o55AicTQYc7GFihQZrjDQug=='

    # <create_cosmos_client>
    client = CosmosClient(endpoint, key)
    # </create_cosmos_client>

    # Create a database
    # <create_database_if_not_exists>
    database_name = 'username-gen-db'
    database = client.create_database_if_not_exists(
        id=database_name,
        partition_key=PartitionKey(path="/username")
    )
    # </create_database_if_not_exists>

    # Create a container
    # Using a good partition key improves the performance of database operations.
    # <create_container_if_not_exists>
    container_name = 'usernames'
    container = database.create_container_if_not_exists(
        id=container_name, 
        partition_key=PartitionKey(path="/username"),
        offer_throughput=400
    )

    rand_num = requests.get('https://username-gen.azurewebsites.net/api/HttpTrigger2?code=pcOxlN1eyA77/54MLI9yVmnZdiBlnERq2Ds1G/c1hJqVfDQj0eR97w==')
    rand_letter = requests.get('https://username-gen.azurewebsites.net/api/HttpTrigger3?code=QKw757a/HNCVtK7k0lXekabHLNOsMXACzaM8ye/ACn1wNg30vpUEww==')
    logging.info("Requests made")
    username=str(rand_num.text+rand_letter.text)
    container_item={ "id": "username_id","username": username }
    container.create_item(container_item)
    return func.HttpResponse(
        username,
        status_code=200
    )
