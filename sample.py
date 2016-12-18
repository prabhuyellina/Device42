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
            self.password =  config.get('Device42', 'password')
            self.url = config.get('Device42', 'url')
            self.auth = (self.user_id, self.password)
        except:
            print "File doesn't exist"
            return

    '''
    To Get the Buildings List
    '''
    def get_buildings(self):

        url=self.url+'buildings/'
        print url
        r=requests.request(method='GET', url=url, auth=self.auth, verify=False)
        print r.status_code
        return r.text

    '''
    To Get the Rooms List
    '''
    def get_rooms(self):

        url = self.url+'rooms/'
        r = requests.request(method='GET', url=url, auth=self.auth, verify=False)
        print r.text
        return r.text

    '''
    To Get the racks List
    '''
    def get_racks(self):

        url = self.url+'racks/'
        r = requests.request(method='GET', url=url, auth=self.auth, verify=False)
        print r.text
        return r.text

    '''
    To Get the Devices List
    '''
    def get_devices(self):

        url = self.url+'devices/'
        r = requests.request(method='GET', url=url, auth=self.auth, verify=False)
        print r.text
        return r.text


    def post_building(self, payload):

        url = self.url + 'buildings/'
        r=requests.request(method='POST', url=url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    def post_room(self, payload):

        url = self.url + 'rooms/'
        r=requests.request(method='POST', url=url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    def post_rack(self, payload):

        url = self.url + 'racks/'
        r=requests.request(method='POST', url=url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    def post_devices(self, payload):

        url = self.url + 'devices/'
        r=requests.request(method='POST', url=url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    def post_hardwares(self, payload):

        url = self.url + 'hardwares/'
        r=requests.request(method='POST', url=url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code




def main():

    obj=Device(raw_input('Enter the Config File name \n'))
    #obj.get_buildings()
    #obj.get_rooms()
    #obj.get_racks()
    #obj.get_devices()
    payload = {'name': 'Rack2_Building2', 'size': '1', 'building':'Building2', 'room':'Building2_Room2'}
    payload={'name': 'Device1', 'hardware': 'Physical_1', 'type': 'physical'}
    #obj.post_building(payload)
    #obj.post_room(payload)
    #obj.post_rack(payload)
    #obj.post_hardwares(payload)
    #obj.post_devices(payload)

main()

