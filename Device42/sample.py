import requests
import csv

class device:
    def __init__(self):
        print "Hello Welcome\n"



    #To Get the data
    def get_method(self,url,user_id,password):
        r=requests.get(url, auth=(user_id,password), verify=False)
        print r.text
    #To Insert the data
    def post_method(self,url,user_id,password,payload):
        data=csv.DictReader(open('deviceHard.csv', 'r'))
        for line in data:
            r=requests.post(url,auth=(user_id,password), verify=False,data=line)
            print r.status_code

obj=device()
#obj.get_method('https://192.168.2.128/api/1.0/buildings/','admin','adm!nd42')
payload={'name':'Building2','address':'2nd Street','contact_name':'prabhu1','contact_phone':'1234567890'}
obj.post_method('https://192.168.2.128/api/1.0/device/','admin','adm!nd42',payload)