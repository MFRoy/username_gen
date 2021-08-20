import logging
import random
import string
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
  
    letters=string.ascii_letters
    rand_letter = ''.join((random.choice(letters) for i in range(5)))
    return func.HttpResponse(
        rand_letter,
        status_code=200
    )
