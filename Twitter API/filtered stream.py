bearer_token = 'AAAAAAAAAAAAAAAAAAAAAI7bhAEAAAAAXFbXlYNurx1fRppFCVVGXDvzN%2Fg%3DNhhRAsbFWklw6dD2LVzhKJuCMmVzsn37l4t7JmlJN07UpEYjAw'

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r
def set_rules(delete):
    # You can adjust the rules if needed
    sample_rules = [
        {"value": "dog has:images", "tag": "dog pictures"},
        {"value": "cat has:images -grumpy", "tag": "cat pictures"},
    ]
    payload = {"add": sample_rules}
    import requests
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    import json
    print(json.dumps(response.json()))