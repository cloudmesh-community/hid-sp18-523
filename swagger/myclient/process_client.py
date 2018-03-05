from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.process_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->diskspace_get: %s\n" % e)
