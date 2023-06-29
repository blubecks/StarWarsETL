import re, requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def make_a_request(url: str):
    response = requests.get(url, verify=False)
    print(f"gathering info at url: {url}")
    if response.ok:
        return response.json()
    else:
        print(response.status_code)
        raise Exception(f"Error in request {url}")


def get_id_by_url(url: str):
    return url.rsplit('/', 2)[-2]


def send_data_to_bucket(filename):
    file_payload = open(filename, "rb")
    response = requests.post("http://httpbin.org/post", files={"upload_file": file_payload})
    if response.ok:
        print("Upload completed successfully!")
        print(response.text)
    else:
        print("Something went wrong!")
