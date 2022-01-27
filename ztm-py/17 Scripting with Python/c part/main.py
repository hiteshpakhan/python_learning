from distutils.log import error
from urllib import request
import requests

# if you get the <Response [400]> then that means you get the error 
# now we get the <Response [200]>


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"err facing {res.status_code}, check the api and try again")
    

def check_pwned_api(password):
    # check password if it exist in the api responce 
    pass


request_api_data("CBFDA")