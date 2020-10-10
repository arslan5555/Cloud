import json
import re
import os
import operator
from collections import Counter
from celery import Celery

app = Celery('tasks', backend='rpc://', broker='amqp://a_ham:asdfgh123@192.168.2.221:5672/myvhost')
@app.task
def file_function(file_name):
	count_han=0,count_hon=0,count_den=0,count_det=0,count_denna=0,unique_tweets=0,count_denne=0,count_hen=0,counter=0
	with open('/home/ubuntu/data/'+ file_name) as f:
		for line in f:
			if line.strip():
				data=json.loads(line)
				if 'retweeted_status' not in data:
					unique_tweets +=1
					string=data['text'].lower()
					if sum(1 for match in re.finditer(r"\bhan\b",string)) >0:
						count_han  += 1
					if sum(1 for match in re.finditer(r"\bhon\b",string)) >0:
						count_hon += 1
					if sum(1 for match in re.finditer(r"\bden\b",string)) >0:
						count_den +=1
					if sum(1 for match in re.finditer(r"\bdet\b",string)) >0:
						count_det +=1
					if sum(1 for match in re.finditer(r"\bdenna\b",string)) >0:
						count_denna +=1
					if sum(1 for match in re.finditer(r"\bdenne\b",string)) >0:
						count_denne +=1
					if sum(1 for match in re.finditer(r"\bhen\b",string)) >0:
						count_hen +=1
	D = Counter({'han' : count_han, 'hon' : count_hon, 'den' : count_den, 'det' : count_det, 'denna' : count_denna, 'denne':count_denne, 'hen': count_hen})
	return D,unique_tweets
