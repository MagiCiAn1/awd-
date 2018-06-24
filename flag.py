#coding:utf-8
import requests
import time
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning


def submit_flag(flag):

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    url='https://172.16.4.1/Common/awd_sub_answer'
    token=''
    for i in flag:
    	print i
    	data={'answer':i,'token':''}
    	r=requests.post(url,verify=False,data=data)
    	time.sleep(3) #sleep 3 second
    	#print json.loads(r.content)['msg']
def main():
	flag=[]
	#获取flag


	#
	submit_flag(flag)
	return len(flag)
i=0
while True:
	i+=1
	print '[+]执行第%d轮攻击...'%i
	num=main()
	print "[+]第%d轮攻击完毕，获得%d个flag"%(i,num)
	time.sleep(60) #sleep 1min