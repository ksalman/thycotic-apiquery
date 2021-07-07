import requests
import os
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


USER = os.environ["TUSER"]
PASS = os.environ["TPASS"]
URL = os.environ["TURL"]
TOKENURL = URL + "/SecretServer/oauth2/token"
APIURL = URL + "/SecretServer/api/v1"

payload = {"username": USER, "password": PASS, "grant_type": "password"}
response = requests.post(TOKENURL, data=payload, verify=False)
ACCESS_TOKEN = response.json()["access_token"]

headers = {"Authorization": "Bearer {}".format(ACCESS_TOKEN)}

# response = requests.get(APIURL + "/users/current", headers=headers, verify=False)
# print(response.json())

hasNext = True
nextSkip = 0
while hasNext == True:
    response = requests.get(
        # APIURL + "/secrets?filter.folderId=47&filter.includeSubFolders=True",
        APIURL + "/folders?filter.parentFolderId=47&take=100&skip={}".format(nextSkip),
        headers=headers,
        verify=False,
    )
    for r in response.json()["records"]:
        if r["inheritPermissions"] == False:
            print(r["folderPath"])
    #    print(response.json()["skip"])
    hasNext = response.json()["hasNext"]
    nextSkip = response.json()["nextSkip"]
#    break
