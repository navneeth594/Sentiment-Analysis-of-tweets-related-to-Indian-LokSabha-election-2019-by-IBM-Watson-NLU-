import pandas as pd
import csv
a=open('bjp.txt','w')
b=open('congress.txt','w')
c=open('mix.txt','w')
d=open('others.txt','w')

data = pd.read_csv('sentpnn.csv', header=0)

col_a = list(data.text)
m=['narendra','modi','amit','shah','yedyurappa','vajpayee','nirmala','sitharaman','seetha','advani','arun','jaitley','piyush','goyal','sushma','swaraj','yogi','adithyanath','smriti','irani','nithin','nitin','gadkari','chouhan','maneka','varun','sinha','shatrughan','anurag','thakur','rss','namo','chowkidar','balakot','pulwama','bjp','bharatiya','janata','varnasi','gst','demonitization','surgical','strike','sarkar','tejaswi','surya','nda']
n=['rahul','congress','priyanka','sonia','indira','gandhi','manmohan','singh','siddramaiah','dk','shivkumar','muslim','amethi','wynad','sashi','tharoor','chor','pappu','rafale','inc','upa','chidambaram','karge','kamal','nath','ahmed','patel','amarinder']
back=[]
for i in col_a:
	if 'narendra' in i or 'modi'in i or 'amit' in i or 'shah'in i or'yedyurappa' in i or 'vajpayee'in i or 'nirmala' in i or 'sitharaman'in i or 'seetha' in i or 'advani' in i or 'arun' in i or 'jaitley' in i or 'piyush'in i or 'goyal' in i or 'sushma'in i or 'swaraj' in i or 'yogi' in i or 'adithyanath' in i or 'smriti' in i or 'irani' in i or 'nithin' in i or 'nitin' in i or 'gadkari' in i or 'chouhan' in i or 'maneka' in i or 'varun' in i or 'sinha' in i or 'shatrughan' in i or 'anurag' in i or 'thakur' in i or 'rss' in i or 'namo' in i or 'chowkidar' in i or 'balakot' in i or 'pulwama' in i or 'bjp' in i or 'bharatiya' in i or 'janata' in i or 'varnasi' in i or 'gst' in i or 'demonitization' in i or 'surgical' in i or 'strike' in i or 'sarkar' in i or 'tejaswi' in i or 'surya' in i or 'nda' in i:
			if 'rahul' in i or 'congress' in i or 'priyanka' in i or 'sonia' in i or 'indira' in i or 'gandhi' in i or 'manmohan' in i or 'singh' in i or 'siddramaiah' in i or 'dk' in i or 'shivkumar' in i or 'muslim' in i or 'amethi' in i or 'wynad' in i or 'sashi' in i or 'tharoor' in i or 'chor' in i or 'pappu' in i or 'rafale' in i or 'inc' in i or 'upa' in i or 'chidambaram' in i or 'karge' in i or 'kamal' in i or 'nath' in i or 'ahmed' in i or 'patel' in i or 'amarinder' in i:
				
				c.write(i+'\n')
					 
			else:

				a.write(i+'\n')
				
	else:
		back.append(i)

for i in back:
	if 'rahul' in i or 'congress' in i or 'priyanka' in i or 'sonia' in i or 'indira' in i or 'gandhi' in i or 'manmohan' in i or 'singh' in i or 'siddramaiah' in i or 'dk' in i or 'shivkumar' in i or 'muslim' in i or 'amethi' in i or 'wynad' in i or 'sashi' in i or 'tharoor' in i or 'chor' in i or 'pappu' in i or 'rafale' in i or 'inc' in i or 'upa' in i or 'chidambaram' in i or 'karge' in i or 'kamal' in i or 'nath' in i or 'ahmed' in i or 'patel' in i or 'amarinder' in i:
		
		b.write(i+'\n')
			
	else:
		d.write(i+'\n')

a.close()
b.close()
c.close()
d.close()



