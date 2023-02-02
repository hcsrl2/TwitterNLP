import requests
import json
import time
author_ids=set()
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAI7bhAEAAAAAXFbXlYNurx1fRppFCVVGXDvzN%2Fg%3DNhhRAsbFWklw6dD2LVzhKJuCMmVzsn37l4t7JmlJN07UpEYjAw'

def create_url():
    url=(f"https://api.twitter.com/2/tweets/sample/stream?"
         f"tweet.fields=author_id")
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2SampledStreamPython"
    return r


def connect_to_endpoint(url):
    count = 0
    response = requests.request("GET", url, auth=bearer_oauth, stream=True)
    time.sleep(1.5)
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            count = count+1
            if json_response['data']['author_id']:
                author_ids.add(str(json_response['data']['author_id']))
        if count==1000:
            with open('../Other Data/author-ids-to-be-extracted.txt', 'a') as f:
                w=str(author_ids)+"\n"
                f.write(w)
                author_ids.clear()
                break

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )


def main():
#    for i in range(1,3):
    url = create_url()
    timeout = 0
    while True:
        connect_to_endpoint(url)
        timeout += 1
        time.sleep(1)

if __name__ == "__main__":
    main()

