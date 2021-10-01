import json
import requests

#
from base64 import b64encode
from dotenv import load_dotenv


id_secret = "ec684b8c687f479fadea3cb2ad83f5c6:e1f31c211f28413186262d37a13fc84d"
code = input("Go to https://www.epicgames.com/id/api/redirect?clientId=ec684b8c687f479fadea3cb2ad83f5c6&responseType=code".format(id_secret))

class APIs:
    account_lookup = "https://fortnite-api.com/v1/stats/br/v2"

class Endpoints:
    serviceUrl = "https://account-public-service-prod03.ol.epicgames.com/"
    device_auth_url = "https://account-public-service-prod.ol.epicgames.com/account/api/public/account"
    mcp = "https://account-public-service-prod.ol.epicgames.com/account/"
    channels = "https://channels-public-service-prod.ol.epicgames.com/"
    graphql = "https://graphql.epicgames.com/partyhub/graphql"
    cloudstorage_base = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/"




def Authenticating_Saved_Response():
    headers = {
        "Authorization": "Bearer 0e9f5dcfebbb4cdd940de07a35b4519b" # Not being used
    }
    url = Endpoints.device_auth_url + "/{}/deviceAuth".format(account_id)
    req = requests.post(url, headers=headers)
    with open("device.json", "w") as f:
        res = req.json()
        data = json.dump(res, f, indent=2)
    return req.json()




def device_ios_token_auth():
    headers = {
        "Authorization": "Bearer {}".format(get_access_token()["access_token"])
    }
    url = Endpoints.device_auth_url + "/{}/deviceAuth".format(account_id)
    req = requests.post(url, headers=headers)

    return req.json()



def get_access_token():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"basic {str(b64encode(id_secret.encode('utf-8')), 'utf-8')}"
    }

    body = {
        "grant_type": "authorization_code",
        "code": code
    }

    req = requests.post("https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token",
    headers=headers, data=body)
    print(req.json())
    return req.json()
get_access_token()

def errors(Error):
    if get_access_token()["Errorcode"] == "errors.com.epicgames.account.oauth.authorization_code_not_found":
        print("IDK")