import requests
import csv
import ConfigParser
import logging
import pdb
pdb.set_trace()


class Device:

    def __init__(self, file_name):
        print "Hello Welcome to Device 42\n"
        try:
            #os.path.isfile(file_name)
            config = ConfigParser.ConfigParser()
            config.read(file_name)
            self.user_id = config.get('Device42', 'user_id')
            self.password =  config.get('Device42', 'password')
            self.input_file_name = config.get('Device42', 'file_name')
            self.log_file_name = config.get('Device42', 'log_file_name')
            self.building_url = config.get('Url', 'building_url')
            self.room_url = config.get('Url', 'room_url')
            self.hardware_url = config.get('Url', 'hardware_url')
            self.racks_url = config.get('Url', 'racks_url')
            self.device_url = config.get('Url', 'device_url')
            self.auth = (self.user_id, self.password)

            """
            Logging Info
            """
            logging.basicConfig(format='%(asctime)s %(message)s', filename=self.log_file_name, level=logging.DEBUG)

        except:
            print "File doesn't exist"

    def get_buildings(self):
        """
        To Get the Buildings List
        """

        r=requests.request(method='GET', url=self.building_url, auth=self.auth, verify=False)
        print r.status_code
        return r.text

    def get_rooms(self):
        """
        To Get the Rooms List
        """

        r = requests.request(method='GET', url=self.room_url, auth=self.auth, verify=False)
        print r.text
        return r.text

    def get_hardwares(self):
        """
        To Get the hardware List
        """

        r = requests.request(method='GET', url=self.hardware_url, auth=self.auth, verify=False)
        print r.text
        return r.text

    def get_racks(self):
        """
        To Get the racks List
        """

        r = requests.request(method='GET', url=self.racks_url, auth=self.auth, verify=False)
        print r.text
        return r.text

    def get_devices(self):
        """
        To Get the Devices List
        """

        r = requests.request(method='GET', url=self.device_url, auth=self.auth, verify=False)
        print r.text
        return r.text

    def post_building(self, payload):
        """
        To post the building
        """

        r=requests.request(method='POST', url=self.building_url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    def post_room(self, payload):
        """
        To post the room
        """

        r=requests.request(method='POST', url=self.room_url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    def post_rack(self, payload):
        """
        To post the rack
        """

        r=requests.request(method='POST', url=self.racks_url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    def post_devices(self, payload):
        """
        To post the device
        """

        r=requests.request(method='POST', url=self.device_url, data=payload, auth=self.auth, verify=False)
        print r.status_code
        return r.status_code

    def post_hardwares(self, payload):
        """
        To post the hardware
        """

        r=requests.request(method='POST', url=self.hardware_url, data=payload, auth=self.auth, verify=False)
        logging.info(r.status_code)
        return r.status_code

    def post_data(self):

        '''
        To post the data from csv file
        '''

        if (self.input_file_name.lower().endswith('.csv')):
            data=csv.DictReader(open(self.input_file_name, 'r'))
            building_list = self.get_buildings()
            room_list = self.get_rooms()
            hardware_list = self.get_hardwares()
            rack_list = self.get_racks()
            device_list = self.get_devices()
            for column in data:
                '''
                Checking the Building Data
                '''

                if column['building'] != 'None':
                    check_match= next((entity for entity in eval(building_list)['buildings'] if column['building'] in entity.values()), None)
                    if check_match:
                        info = '%s Building Exists' %(column['building'])
                        logging.debug(info)
                    else:
                        '''
                        Creating a new building
                        '''
                        payload = {'name': column['building']}
                        return_code = self.post_building(payload)
                        if return_code == 200:
                            info = '%s Building Added Successfuly' %(column['building'])
                            logging.debug(info)
                        else:
                            info = 'Unable to add the %s Building' %(column['building'])
                            logging.debug(info)
                else:
                    info = 'No Building Name is Given for device %s' %(column['name'])
                    logging.debug(info)

                '''
                Checking the Room Data
                '''

                if column['room'] != 'None':
                    check_match = next((entity for entity in eval(room_list)['rooms'] if column['room'] in entity.values()), None)
                    if check_match:
                        info = '%s Room Exists' %(column['room'])
                        logging.debug(info)
                    else:
                        '''
                        Creating a new room
                        '''
                        payload = {'name': column['room'],'building':column['building']}
                        return_code = self.post_room(payload)
                        if return_code == 200:
                            info = '%s room Added Successfuly' %(column['room'])
                            logging.debug(info)
                        else:
                            info = 'Unable to add the room'
                            logging.debug(info)
                else:
                    info = 'No Room Name is Given for the device %s' % (column['name'])
                    logging.debug(info)

                '''
                Checking the hardware Data
                '''
                if column['hardware'] != 'unknown':
                    null = None
                    check_match = next((entity for entity in eval(hardware_list)['models'] if column['hardware'] in entity['name']), None)
                    if check_match:
                        info = '%s Hardware Exists' %(column['hardware'])
                        logging.debug(info)
                    else:
                        '''
                        Creating a new hardware
                        '''
                        payload = {'name': column['hardware'],'type':column['type']}
                        return_code = self.post_hardwares(payload)
                        if return_code == 200:
                            info = '%s hardware Added Successfuly' %(column['hardware'])
                            logging.debug(info)
                        else:
                            info = 'Unable to add the %s hardware' %(column['hardware'])
                            logging.debug(info)
                else:
                    info = 'No hardware Name is Given for the device %s' % (column['name'])
                    logging.debug(info)

                '''
                Checking the Racks Data
                '''

                if column['rack'] != 'None':
                    true='True'
                    check_match = next((entity for entity in eval(rack_list)['racks'] if column['room'] in entity.values()), None)
                    if check_match:
                        info = '%s Rack Exists' % (column['rack'])
                        logging.debug(info)
                    else:
                        '''
                        Creating a new rack
                        '''
                        if column.has_key('size'):
                            rack_size = column['size']
                        else:
                            rack_size = 42
                        payload = {'name': column['rack'], 'room': column['room'], 'size': rack_size}
                        return_code = self.post_rack(payload)
                        if return_code == 200:
                            info = '%s rack Added Successfuly' % (column['rack'])
                            logging.debug(info)
                        else:
                            info = 'Unable to add the %s rack' %(column['rack'])
                            logging.debug(info)
                else:
                    info = 'No rack Name is Given for the device %s' % (column['name'])
                    logging.debug(info)

                '''
                Checking the Device Data
                '''

                if column['name'] != 'None':
                    check_match = next((entity for entity in eval(device_list)['Devices'] if column['name'] in entity.values()), None)
                    print check_match
                    if check_match:
                        info = '%s Device Exists' % (column['name'])
                        logging.debug(info)
                        payload = {'name': column['name'], 'type': column['type'], 'hardware': column['hardware'],
                                   'customer': column['customer'], 'serial_no': column['serial_no'],
                                   'asset_no': column['asset_no'], 'uuid': column['uuid']}
                        return_code = self.post_devices(payload)
                        if return_code == 200:
                            info = '%s device Updated Successfuly' % (column['name'])
                            logging.debug(info)

                    else:
                        '''
                        Creating a new Device
                        '''
                        payload = {'name': column['name'], 'type': column['type'], 'hardware': column['hardware'],
                                   'customer': column['customer'], 'serial_no': column['serial_no'],
                                   'asset_no': column['asset_no'], 'uuid': column['uuid']}
                        return_code = self.post_devices(payload)
                        if return_code == 200:
                            info = '%s device Added Successfuly' % (column['name'])
                            logging.debug(info)
                            print info
                        else:
                            info = 'Unable to add the %s device' %(column['name'])
                            logging.debug(info)
                else:
                    info = 'No Device Name is Given for the device %s' % (column['name'])
                    logging.debug(info)

        else:
            info = "Set the proper csv file name in config file"
            logging.debug(info)
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

