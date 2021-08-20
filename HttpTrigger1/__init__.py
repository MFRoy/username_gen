import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    rand_num = requests.get('http://localhost:7071/api/HttpTrigger2')
    rand_letter = requests.get('http://localhost:7071/api/HttpTrigger3')
    
    return func.HttpResponse(
        str(rand_num.text+rand_letter.text),
        status_code=200
    )
