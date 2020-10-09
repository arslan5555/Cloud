from collections import Counter
from flask import jsonify
from tasks import file_function
import os
from flask import Flask
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'],)
def counter():
	total_count = Counter({'han':0, 'hon':0, 'den':0, 'det':0, 'denna':0, 'denne':0,'hen':0})
	unique_tweet_count=0
	my_list=[]
	path = "/home/ubuntu/data"
	dir_list = os.listdir(path)
	start_time=time.time()
	for name in dir_list:
		my_list.append(file_function.delay(name))
	for x in my_list:
		res=x.get()
		m=Counter(res[0])
		unique_tweet_count=res[1]+unique_tweet_count
		total_count=m + total_count
	print(total_count)
	print("Unique tweet count: ",unique_tweet_count)
	end_time=time.time()
	print("time is %s seconds" % (time.time() - start_time))
	return total_count
if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0', port=5000)
