import requests
import pandas as pd

# 1.0 Call
endpoint="https://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search?resource_id=e96bf614-467b-40ab-91b9-e48a616ea775"
response=requests.get(url=endpoint)

# 2.0 Deal with response
body=response.json()

listFields=body.get("result")["fields"]
columnsList=[i["id"] for i in listFields]

listResults=body.get("result")["records"]
corpusList=[]
for idx, item in enumerate(listResults):
    corpusList.append([])
    for head in columnsList:
        corpusList[idx].append(item[head])

frame=pd.DataFrame(corpusList,columns=columnsList)
print(frame.head())







