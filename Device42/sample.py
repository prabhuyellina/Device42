import requests
import csv


class Device:

    def __init__(self, user_id, password):
        print "Hello Welcome\n"
        self.auth=(user_id, password)

    #To Get the data
    def get_method(self, url):
        r=requests.get(url, auth=self.auth, verify=False)
        print r.text

    #'To Insert the data'
    def post_method(self,url, payload):

        data=csv.DictReader(open('deviceHard.csv', 'r'))
        for line in data:
            r=requests.post(url, auth=self.auth, verify=False, data=line)
            print r.status_code

    def update_method(self, url, item_name, payload):

        url = url + str(item_name)
        r = requests.put(url, auth=self.auth, verify=False, data=payload)
        print r.status_code

    #'To delete the data'
    def delete_method(self, url, device_id):

        url=url + 'devices/'+str(device_id)
        r = requests.delete(url, verify=False, auth=self.auth)
        print r.status_code

url='https://192.168.2.128/api/1.0/'
obj=Device('admin','adm!nd42')
#obj.get_method('https://192.168.2.128/api/1.0/devices/','admin','adm!nd42')
payload={'name':'TXARL1-MSA1','serial_no':'SN4150198005U','customer':'prabhu1','hardware':'Physical_Hardware1'}
#obj.post_method('https://192.168.2.128/api/1.0/device/','admin','adm!nd42',payload)
#obj.delete_method(url,'admin','adm!nd42',2)
obj.update_method(url ,'devices/', payload)

