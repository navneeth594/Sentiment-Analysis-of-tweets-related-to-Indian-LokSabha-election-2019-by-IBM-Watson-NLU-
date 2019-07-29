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
f=open('mix.txt','r')

l=f.readlines()
d=l[:1000]
csv_data=[]
csv_data1=[]
mass=[]
lass=[]

for i in d:
    s=[]
    sh=[]
    mm=[]
    cd=[]
    try:
        response = natural_language_understanding.analyze(
            text=i,
            features=Features(
                sentiment=SentimentOptions(targets=['narendra','modi','amit','shah','yedyurappa','vajpayee','nirmala','sitharaman','seetha','advani','arun','jaitley','piyush','goyal','sushma','swaraj','yogi','adithyanath','smriti','irani','nithin','nitin','gadkari','chouhan','maneka','varun','sinha','shatrughan','anurag','thakur','rss','namo','chowkidar','balakot','pulwama','bjp','bharatiya','janata','varnasi','gst','demonitization','surgical','strike','sarkar','tejaswi','surya','nda','rahul','congress','priyanka','sonia','indira','gandhi','manmohan','singh','siddramaiah','dk','shivkumar','muslim','amethi','wynad','sashi','tharoor','chor','pappu','rafale','inc','upa','chidambaram','karge','kamal','nath','ahmed','patel','amarinder']),
                entities=EntitiesOptions(emotion=True, sentiment=True, 
                                        limit=4))).get_result()

        a=json.dumps(response, indent=2)
        b=json.loads(a)
        for j in b['entities']:
        	if j['type']=='Organization':
        		if j['text']=='bjp':
        			s.append(i)
        			s.append(j['sentiment']['label'])
        		if j['text']=='congress':
        			sh.append(i)
        			sh.append(j['sentiment']['label'])

        	if j['type']=='Person':

                if j['text']=='modi' or j['text']=='narendra' or j['text']=='modiji' or j['text']=='namo':
                    mm.append(j['emotion']['sadness'])
                    mm.append(j['emotion']['joy'])
                    mm.append(j['emotion']['fear'])
                    mm.append(j['emotion']['disgust'])
                    mm.append(j['emotion']['anger'])

                if j['text']=='rahul' or j['text']=='pappu' or j['text']=='gandhi':
                    cd.append(j['emotion']['sadness'])
                    cd.append(j['emotion']['joy'])
                    cd.append(j['emotion']['fear'])
                    cd.append(j['emotion']['disgust'])
                    cd.append(j['emotion']['anger'])
    except:
    	pass
    if len(s)>1:
    	csv_data.append(s)
    if len(sh)>1:

    	csv_data1.append(sh)
    if len(mm)>1:
    	mass.append(mm)

    if len(cd)>1:
    	lass.append(cd)


with open('congress.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csv_data1)

csvFile.close()

with open('bjp.csv', 'a') as csvFile1:
    writer = csv.writer(csvFile1)
    writer.writerows(csv_data)

csvFile1.close()	


with open('namo.csv', 'a') as csvFile2:
    writer = csv.writer(csvFile2)
    writer.writerows(mass)

csvFile2.close()

with open('rahul.csv', 'a') as csvFile3:
    writer = csv.writer(csvFile3)
    writer.writerows(lass)

csvFile3.close()