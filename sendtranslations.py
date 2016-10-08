from twilio.rest import TwilioRestClient
import httplib2
import urllib
import json

translationToPass = ""

# TRANSLATE SCRIPT
def translate(text, lan):

    GOOGLE_API_KEY = "AIzaSyC53IYbS9tHwFv9fYoptruH07RGJtuysT8"
    baseURL = "https://www.googleapis.com"
    pathURL = "/language/translate/v2"
    queryURL = "?key=" + GOOGLE_API_KEY + "&source=en&target=" + lan + "&q="
    text_encoded = urllib.quote_plus(text)
    translateURL = baseURL + pathURL + queryURL + text_encoded

    url = translateURL
    print url

    http = httplib2.Http()
    response, body = http.request(url, "GET")
    print response
    print body

    # Error handling
    try:
        parsed_body = json.loads(body)
    except Exception as e:
        print 'Translation failed with no JSON response from Google'

    parsed_body = json.loads(body)

    data = parsed_body['data']
    translations = data['translations']
    firstTranslation = translations[0]
    translatedText = firstTranslation['translatedText']

    # another way of parsing, this one is a little advanced
    # translatedText = data['data']['translations'][0]['translatedText']
    # print translatedText == translatedText2
    # print type(translatedText)
    print translatedText
    return translatedText
    translationToPass = translatedText



translate("Hey brother", "es")


account_sid = "ACa326d844b6f8edd861dc1488531d9efe"
auth_token = "dbd22909483217c1f1c23a2aa6a7e4a5"

# We instantiate a REST Client and pass it our accout ID and token as arguments
client = TwilioRestClient(account_sid, auth_token)

""" We use the 'TwilioRestClient' object, access it's messages object, and then
 then it's 'create method' """

client.messages.create(to="+13477920858",
                       from_="+19145945181",
                       body=translationToPass)
