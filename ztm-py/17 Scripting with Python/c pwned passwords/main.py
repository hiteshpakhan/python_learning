import requests
import hashlib
import sys

# if you get the <Response [400]> then that means you get the error 
# now we get the <Response [200]>


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"err facing {res.status_code}, check the api and try again")
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            print("h=",h,"count=",count)
            return count
    return 0 # if it not return th count it will return the 0 


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5char, remaningchar = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5char) 
    # print(response)
    return get_password_leaks_count(response, remaningchar)

def main(a):
    for password in a:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times.... you shoud probably change your password")
        else:
            print(f"{password} not found, good work")
    return "done"
    
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))    #sys.exit is very important command it will take our control back to the cammand line after executes the program