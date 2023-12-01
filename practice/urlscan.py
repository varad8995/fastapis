import json
import requests
def urlscan(domain):
    try:
        
        
    
    
        url = "https://urlscan.io/api/v1/search/"

        payload = json.dumps({
                "url": domain
                })

        headers = {
                    'x-api-key': "044efb52-4417-4dcd-8ffd-100b8dac3ad2",
                    'Content-Type': 'json'

                }

        response = requests.request("GET",url, headers=headers,data=payload)

        result = response.json()
        result1 = result['results']
        result2 = []
        for i in result1:
            result2.append(i["page"])

                #print(result1)
                #print(result2)
                # Remove 'rrsig' and 'dnskey' keys from result1 if they exist

        if response.status_code == 403:       # API key has expired
            payLoad = {
                "domain": domain,
                "response": [], 
                "extSource": "URLScan API"  #(Expired Key)
                }
        else:






                    # Create the desired response format as a dictionary
            payLoad = {
                        "domain": domain,
                        "response": [result2],
                        "extSource": "URLScan API"
                        }
    except:
        # Handle exceptions and create the desired response format as a dictionary
        payLoad = {
            "domain": domain,
            "response": [],
            "extSource": "URLScan API"
        }        

    return payLoad







