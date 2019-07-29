import json
import csv
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 \
    import Features, SentimentOptions, EntitiesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='ErzCAc2jcc3qVEq3NZsyjPKqjygC-ERaLHAjUXAInyn8',
    url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api'
)
f=open('bjp.txt','r')

l=f.readlines()
d=l[:1000]
csv_data=[['text','sentiment']]
modi=[['sadness','joy','fear','disgust','anger']]
for i in d:
    s=[]
    sh=[]
    try:
        response = natural_language_understanding.analyze(
            text=i,
            features=Features(
                sentiment=SentimentOptions(targets=['narendra','modi','amit','shah','yedyurappa','vajpayee','nirmala','sitharaman','seetha','advani','arun','jaitley','piyush','goyal','sushma','swaraj','yogi','adithyanath','smriti','irani','nithin','nitin','gadkari','chouhan','maneka','varun','sinha','shatrughan','anurag','thakur','rss','namo','chowkidar','balakot','pulwama','bjp','bharatiya','janata','varnasi','gst','demonitization','surgical','strike','sarkar','tejaswi','surya','nda','rahul','congress','priyanka','sonia','indira','gandhi','manmohan','singh','siddramaiah','dk','shivkumar','muslim','amethi','wynad','sashi','tharoor','chor','pappu','rafale','inc','upa','chidambaram','karge','kamal','nath','ahmed','patel','amarinder']),
                entities=EntitiesOptions(emotion=True, sentiment=True, 
                                        limit=4))).get_result()

        a=json.dumps(response, indent=2)
        b=json.loads(a)
        s.append(i)
        s.append(b['sentiment']['document']['label'])

        for j in b['entities']:
            if j['type']=='Person':
                if j['text']=='modi' or j['text']=='narendra' or j['text']=='modiji' or j['text']=='namo':
                    sh.append(j['emotion']['sadness'])
                    sh.append(j['emotion']['joy'])
                    sh.append(j['emotion']['fear'])
                    sh.append(j['emotion']['disgust'])
                    sh.append(j['emotion']['anger'])
        
    except:
        pass
    csv_data.append(s)
    modi.append(sh)

with open('bjp.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csv_data)

csvFile.close()

with open('namo.csv', 'w') as csvFile1:
    writer = csv.writer(csvFile1)
    writer.writerows(modi)

csvFile1.close()