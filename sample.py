import pdb
pdb.set_trace()
import requests
import csv
import ConfigParser
import os
import json


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
            self.input_file_name=config.get('Device42','file_name')
        except:
            print "File doesn't exist"

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

    '''
    To post the building
    '''

    def post_building(self, payload):

        url = self.url + 'buildings/'
        r=requests.request(method='POST', url=url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    '''
    To post the room
    '''
    def post_room(self, payload):

        url = self.url + 'rooms/'
        r=requests.request(method='POST', url=url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    '''
    To post the rack
    '''
    def post_rack(self, payload):

        url = self.url + 'racks/'
        r=requests.request(method='POST', url=url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    '''
    To post the device
    '''
    def post_devices(self, payload):

        url = self.url + 'devices/'
        r=requests.request(method='POST', url=url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    '''
    To post the hardwares
    '''
    def post_hardwares(self, payload):

        url = self.url + 'hardwares/'
        r=requests.request(method='POST', url=url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    def post_data(self):

        '''
        To post the data from csv file
        '''

        if (self.input_file_name.lower().endswith('.csv')):
            data=csv.DictReader(open(self.input_file_name, 'r'))
            building_list = self.get_buildings()
            #room_list = self.get_rooms()
            #device_list = self.get_devices()
            for column in data:
                '''
                Checking the Building Data
                '''

                if column['building'] != 'None':
                    print eval(building_list)['buildings']
                    for each_building_data in eval(building_list)['buildings']:
                        print each_building_data.values()
                        if column['building'] in each_building_data.values():
                            print 'Building Exists'
                        else:
                            '''
                            Creating a new building
                            '''
                            payload = {'name': column['building']}
                            return_code = self.post_building(payload)
                            if return_code == 200:
                                print 'Building Added Successfuly'
                            else:
                                print 'Unable to add the Building'
                else:
                    print 'No Building Name is Given for %s' %(column['name'])

        else:
            print "Set the proper csv file name in config file"
            return



def main():

    obj=Device('Device42.cfg')

    #raw_input('Enter the Config File name \n'))
    #obj.get_buildings()
    #obj.get_rooms()
    #obj.get_racks()
    #obj.get_devices()
    #payload = {'name': 'Rack2_Building2', 'size': '1', 'building':'Building2', 'room':'Building2_Room2'}
    #payload={'name': 'Device1', 'hardware': 'Physical_1', 'type': 'physical'}
    #obj.post_building(payload)
    #obj.post_room(payload)
    #obj.post_rack(payload)
    #obj.post_hardwares(payload)
    #obj.post_devices(payload)
    obj.post_data()

main()

