import requests

facebookId ="YourFacebookId"
accessToken = "yourFacebookToken"
userAccessToken = "YourUserAccessToken"
requestUrl = "https://graph.facebook.com/v3.2/" + facebookId + "?fields=birthday,name,email&access_token=" + userAccessToken
print(requestUrl)
r = requests.get(url=requestUrl)
print(r)
print(r.text)
