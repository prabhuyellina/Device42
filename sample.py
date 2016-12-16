import requests
import csv
import ConfigParser
import os


class Device:

    def __init__(self, file_name):
        print "Hello Welcome to Device 42\n"
        try:
            #os.path.isfile(file_name)
            config = ConfigParser.ConfigParser()
            config.read(file_name)
            self.user_id = config.get('Device42', 'user_id')
            self.password = config.get('Device42', 'password')
            self.url = config.get('Device42', 'url')
            self.auth = (self.user_id, self.password)
        except:
            print "File doesn't exist"


#To Get the Buildings List
    def get_buildings(self):

        url=self.url + 'buildings/'
        r=requests.get(url, auth=self.auth, verify=False)
        print r.text

# To Get the Rooms List
    def get_rooms(self):

        url=self.url+'rooms/'
        r=requests.get(url, auth=self.auth, verify=False)
        print r.text

# To Get the Devices List
    def get_devices(self):

        url=self.url+'devices/'
        r=requests.get(url, auth=self.auth, verify=False)
        print r.text

    def get_method(self, url):
        r=requests.get(url, auth=self.auth, verify=False)
        print r.text

    #'To Insert the data'
    def post_method(self,url, item_name, payload):

        url = url + str(item_name)
        data=csv.DictReader(open('deviceHard.csv', 'r'))
        for line in data:
            r=requests.post(url, auth=self.auth, verify=False, data=line)
            print r.status_code

    def update_method(self, item_name, payload):

        url = self.url + str(item_name)
        r = requests.put(url, auth=self.auth, verify=False, data=payload)
        print r.status_code

    #'To delete the data'
    def delete_method(self, url, device_id):

        url=url + 'devices/'+str(device_id)
        r = requests.delete(url, verify=False, auth=self.auth)
        print r.status_code


def main():

    file_name= raw_input('Enter the File name to add the data\n')
    obj=Device(file_name)

main()

