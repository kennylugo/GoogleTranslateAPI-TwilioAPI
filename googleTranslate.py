import httplib2
import urllib
import json
from twilio.rest import TwilioRestClient

def sendSMS(messageToSend):
    account_sid = "ACa326d844b6f8edd861dc1488531d9efe"
    auth_token = "dbd22909483217c1f1c23a2aa6a7e4a5"

    client = TwilioRestClient(account_sid, auth_token)


    # catch error
    try:
        client.messages.create(to="+13477920858",
                               from_="+19145945181",
                               body=messageToSend)
    except Exception as e:
        print "The phone number is not valid"

def translate(arrayOfStrings, lan):

    GOOGLE_API_KEY = "AIzaSyC53IYbS9tHwFv9fYoptruH07RGJtuysT8"

    baseURL = "https://www.googleapis.com"
    pathURL = "/language/translate/v2"
    queryURL = "?key=" + GOOGLE_API_KEY + "&source=en&target=" + lan

    http = httplib2.Http()

    for text in arrayOfStrings:
            text_encoded = urllib.quote_plus(text)
            translateURL = baseURL + pathURL + queryURL + "&q=" + text_encoded

            response, body = http.request(translateURL, "GET")

            # Error handling
            try:
                parsed_body = json.loads(body)
                data = parsed_body['data']
                translations = data['translations']
                firstTranslation = translations[0]
                translatedText = firstTranslation['translatedText']
                # get rid of sendSMS and create a new func caled sendTranslatedSMS
                sendSMS(translatedText)
            except Exception as e:
                print 'Translation failed with no JSON response from Google'



arrayOfStrings = ["Hello World", "It's me", "Your girlfriend Jackie"]
translate(arrayOfStrings, "fr")
