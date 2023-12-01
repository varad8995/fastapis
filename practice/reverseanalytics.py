import json
import requests


def analyticslookup(domain):
    try:
        response = requests.get("https://api.hackertarget.com/analyticslookup/?q={}".format(domain))
        result1 = None
        result = {
            "domain":response.text.split(",")[0],
            "UA-ID":response.text.split(",")[1]
        }
        result1 = json.dumps(result)

    except:
        # Handle exceptions and create the desired response format as a dictionary
        response = {
            "domain": domain,
            "response": [],
            "extSource": "Hackertarget API"
        }        

    return result1






print(analyticslookup('primehealthcare.com'))






