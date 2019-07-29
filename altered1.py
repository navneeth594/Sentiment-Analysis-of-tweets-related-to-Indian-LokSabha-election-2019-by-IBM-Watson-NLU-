import pandas as pd
import csv

data = pd.read_csv('apr20.csv', header=0)
col_a = list(data.full_text)

def remove_nan(l):
    for i in range(len(l)):
        try:
            if str(l[i])=='nan' or str(l[i])=='NaN' or str(l[i])=='nAn' or str(l[i])=='NAN':
                del l[i]
        except:
            pass
    return len(l)

prev=[]
pres=remove_nan(col_a)
while pres!=prev:
    prev=pres
    pres=remove_nan(col_a)

v=[]

x=[]
y=[]

for i in range(len(col_a)):
	tc=col_b[i]
	if 'narendra' in tc or 'modi'in tc or 'amit' in tc or 'shah'in tc or'yedyurappa' in tc or 'vajpayee'in tc or 'nirmala' in tc or 'sitharaman'in tc or 'seetha' in tc or 'advani' in tc or 'arun' in tc or 'jaitley' in tc or 'piyush'in tc or 'goyal' in tc or 'sushma'in tc or 'swaraj' in tc or 'yogi' in tc or 'lok' in tc or 'sabha' in tc or 'adithyanath' in tc or 'smriti' in tc or 'irani' in tc or 'nithin' in tc or 'nitin' in tc or 'gadkari' in tc or 'chouhan' in tc or 'maneka' in tc or 'varun' in tc or 'sinha' in tc or 'shatrughan' in tc or 'anurag' in tc or 'thakur' in tc or 'rss' in tc or 'namo' in tc or 'chowkidar' in tc or 'balakot' in tc or 'pulwama' in tc or 'bjp' in tc or 'bharatiya' in tc or 'janata' in tc or 'varnasi' in tc or 'gst' in tc or 'demonitization' in tc or 'surgical' in tc or 'strike' in tc or 'sarkar' in tc or 'tejaswi' in tc or 'surya' in tc or 'nda' in tc or 'elections' in tc or 'result' in tc or 'inc' in tc or 'upa' in tc or "nikhil ellidyappa" in tc or 'chor' in tc or 'pm' in tc or 'minister' in tc or 'rahul' in tc or 'congress' in tc or 'priyanka' in tc or 'sonia' in tc or 'indira' in tc or 'gandhi' in tc or 'manmohan' in tc or 'singh' in tc or 'siddramaiah' in tc or 'dk' in tc or 'shivkumar' in tc or 'muslim' in tc or 'amethi' in tc or 'wynad' in tc or 'sashi' in tc or 'tharoor' in tc or 'chor' in tc or 'pappu' in tc or 'rafale' in tc or 'chidambaram' in tc or 'karge' in tc or 'kamal' in tc or 'nath' in tc or 'ahmed' in tc or 'patel' in tc or 'amarinder' in tc:
		v.append(tc)

for i in v:
    if 'trump'  in i or 'Trump'  in i or 'Bernie' in i or 'sanders' in i or 'clinton'in i or 'obama' in i or 'donald' in i or 'elizabeth' in i or 'warren' in i or 'kamala' in i or 'harris' in i or 'usa' in i or '2020' in i or 'us' in i or 'america' in i or 'mueller' in i or 'joyann' in i or 'senatorromney' in i:
        x.append(i)
for i in v:
    if i not in x:
        y.append(i)
csv_data=[['text']]
for i in y:
    s=[]
    s.append(i)
    csv_data.append(s)

with open('sentpnn.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csv_data)

csvFile.close()