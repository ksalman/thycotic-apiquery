import click
import requests
import os
import urllib3

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


@click.group()
def cli():
    """Tool to query Thycotic Secret Server"""
    pass


@cli.command()
@click.argument("foo")
def test(foo):
    click.echo(foo)


@cli.command()
@click.argument("parent_folder_id")
def folder(parent_folder_id):
    """Show folders that do not inherit from parent"""
    hasNext = True
    nextSkip = 0
    while hasNext == True:
        params = {
            "filter.parentFolderId": parent_folder_id,
            "take": 100,
            "skip": nextSkip,
        }
        response = requests.get(
            APIURL + "/folders",
            params=params,
            headers=headers,
            verify=False,
        )
        for r in response.json()["records"]:
            if r["inheritPermissions"] == False:
                print(r["folderPath"])
        hasNext = response.json()["hasNext"]
        nextSkip = response.json()["nextSkip"]


if __name__ == "__main__":
    cli()
