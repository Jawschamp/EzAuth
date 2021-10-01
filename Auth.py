#import json
import requests


from base64 import b64encode


id_secret = "ec684b8c687f479fadea3cb2ad83f5c6:e1f31c211f28413186262d37a13fc84d"
#code = input("Go to https://www.epicgames.com/id/api/redirect?clientId=ec684b8c687f479fadea3cb2ad83f5c6&responseType=code"

class AuthMethods():
    def get_access_token(code):
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

AuthMethods.get_access_token(code="ddc3671d11da420e9985e0c4147eb49c")