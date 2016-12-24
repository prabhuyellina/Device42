import requests
import csv
import ConfigParser
import logging


class Device:

    def __init__(self, file_name):
        print "Hello Welcome to Device 42\n"
        try:
            config = ConfigParser.ConfigParser()
            config.read(file_name)
            self.user_id = config.get('Device42', 'user_id')
            self.password = config.get('Device42', 'password')
            self.input_file_name = config.get('Device42', 'file_name')
            self.log_file_name = config.get('Device42', 'log_file_name')
            self.building_url = config.get('Url', 'building_url')
            self.room_url = config.get('Url', 'room_url')
            self.hardware_url = config.get('Url', 'hardware_url')
            self.racks_url = config.get('Url', 'racks_url')
            self.device_url = config.get('Url', 'device_url')
            self.auth = (self.user_id, self.password)
            # Logging Info
            logging.basicConfig(format='%(asctime)s %(message)s', filename=self.log_file_name, level=logging.INFO)

        except IOError as e:
            info = "File doesn't exist"
            logging.error(info, e)

    def get_buildings(self):
        """
        To Get the Buildings List
        """

        try:
            response = requests.request(method='GET', url=self.building_url, auth=self.auth, verify=False)
            info = "Executed get_buildings API and returned with status code: %s" % response.status_code
            logging.info(info)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def get_rooms(self):
        """
        To Get the Rooms List
        """

        try:
            response = requests.request(method='GET', url=self.room_url, auth=self.auth, verify=False)
            info = "Executed get_rooms API and returned with status code: %s" % response.status_code
            logging.info(info)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def get_hardwares(self):
        """
        To Get the hardware List
        """

        try:
            response = requests.request(method='GET', url=self.hardware_url, auth=self.auth, verify=False)
            info = "Executed get_hardwares API and returned with status code: %s" % response.status_code
            logging.info(info)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def get_racks(self):
        """
        To Get the racks List
        """

        try:
            response = requests.request(method='GET', url=self.racks_url, auth=self.auth, verify=False)
            info = "Executed get_racks API and returned with status code: %s" % response.status_code
            logging.info(info)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def get_devices(self):
        """
        To Get the Devices List
        """
        try:
            response = requests.request(method='GET', url=self.device_url, auth=self.auth, verify=False)
            info = "Executed get_devices API and returned with status code: %s" % response.status_code
            logging.info(info)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def post_building(self, payload):
        """
        To post the building
        """

        try:
            response = requests.request(method='POST', url=self.building_url,\
                                        data=payload, auth=self.auth, verify=False)
            info = "Added Building %s and returned with status code: %s" % (payload['name'], response.status_code)
            logging.info(info)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def post_room(self, payload):
        """
        To post the room
        """

        try:
            response = requests.request(method='POST', url=self.room_url, data=payload, auth=self.auth, verify=False)
            info = "Added Room %s and returned with status code: %s" % (payload['name'], response.status_code)
            logging.info(info)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def post_rack(self, payload):
        """
        To post the rack
        """

        try:
            response = requests.request(method='POST', url=self.racks_url, data=payload, auth=self.auth, verify=False)
            info = "Added Rack %s and returned with status code: %s" % (payload['name'], response.status_code)
            logging.info(info)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def post_devices(self, payload):
        """
        To post the device
        """

        try:
            response = requests.request(method='POST', url=self.device_url, data=payload, auth=self.auth, verify=False)
            info = "Added Device %s and returned with status code: %s" % (payload['name'], response.status_code)
            logging.info(info)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def post_hardwares(self, payload):
        """
        To post the hardware
        """

        try:
            response = requests.request(method='POST', url=self.hardware_url,\
                                        data=payload, auth=self.auth, verify=False)
            info = "Added Hardware %s and returned with status code: %s" % (payload['name'], response.status_code)
            logging.info(info)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def delete_building(self, building_id):
        """
        Delete a building
        """
        try:
            url = self.building_url + str(building_id)
            print url
            response = requests.request(method='DELETE', url=url, auth=self.auth, verify=False)
            info = 'Building %d is deleted' % building_id
            logging.info(info)
            print response.status_code
            return response
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def delete_device(self, device_id):
        """
         Delete a Device
        """
        try:
            url = self.device_url + str(device_id)
            print url
            response = requests.request(method='DELETE', url=url, auth=self.auth, verify=False)
            logging.info(response)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def post_data(self):
        """
        To post the data from csv file
        """

        try:
            if self.input_file_name.lower().endswith('.csv'):
                data = csv.DictReader(open(self.input_file_name, 'r'))
                building_list = self.get_buildings().text
                room_list = self.get_rooms().text
                hardware_list = self.get_hardwares().text
                rack_list = self.get_racks().text
                device_list = self.get_devices().text
                # Checking the response of GET calls
                if building_list or room_list or hardware_list or rack_list\
                    or device_list is 'null':
                    info= 'Unable to get the desired data'
                    logging.info(info)
                    return 0
                for column in data:
                    '''
                    Checking the Building Data
                    '''

                    column = dict((k.lower(), v)for k, v in column.iteritems())
                    print column
                    if column['building'] != 'None' and column['building'] != '':
                        check_match = next((entity for entity in eval(building_list)['buildings']\
                                           if column['building'] in entity.values()), None)
                        if check_match:
                            info = '%s Building Exists' %(column['building'])
                            logging.info(info)
                        else:
                            '''
                            Creating a new building
                                '''
                            payload = {'name': column['building']}
                            response = self.post_building(payload)
                            if response.status_code == 200:
                                info = '%s Building Added Successfuly' %(column['building'])
                                logging.info(info)
                            else:
                                info = 'Unable to add the %s Building' %(column['building'])
                                logging.info(info)
                    else:
                        info = 'No Building Name is Given for device %s' %(column['name'])
                        logging.info(info)

                    '''
                    Checking the Room Data
                    '''

                    if column['room'] != 'None' and column['room'] != '':
                        check_match = next((entity for entity in eval(room_list)['rooms'] \
                                            if column['room'] in entity.values()), None)
                        if check_match:
                            info = '%s Room Exists' %(column['room'])
                            logging.info(info)
                        else:
                            '''
                            Creating a new room
                            '''
                            payload = {'name': column['room'], 'building':column['building']}
                            response = self.post_room(payload)
                            if response.status_code == 200:
                                info = '%s room Added Successfuly' %(column['room'])
                                logging.info(info)
                            else:
                                info = 'Unable to add the room'
                                logging.info(info)
                    else:
                        info = 'No Room Name is Given for the device %s' % (column['name'])
                        logging.info(info)

                    '''
                    Checking the hardware Data
                    '''
                    if column['hardware'] != 'unknown' and column['hardware'] != '':
                        null = None
                        check_match = next((entity for entity in eval(hardware_list)['models'] \
                                            if column['hardware'] in entity['name']), None)
                        if check_match:
                            info = '%s Hardware Exists' %(column['hardware'])
                            logging.info(info)
                        else:
                            '''
                            Creating a new hardware
                            '''
                            payload = {'name': column['hardware'],'type':column['type']}
                            response = self.post_hardwares(payload)
                            if response.status_code == 200:
                                info = '%s hardware Added Successfuly' %(column['hardware'])
                                logging.info(info)
                            else:
                                info = 'Unable to add the %s hardware' %(column['hardware'])
                                logging.info(info)
                    else:
                        info = 'No hardware Name is Given for the device %s' % (column['name'])
                        logging.info(info)

                    '''
                    Checking the Racks Data
                    '''

                    if column['rack'] != 'None' and column['rack'] != '':
                        true='True'
                        check_match = next((entity for entity in eval(rack_list)['racks']\
                                            if column['room'] in entity.values()), None)
                        if check_match:
                            info = '%s Rack Exists' % (column['rack'])
                            logging.info(info)
                        else:
                            '''
                            Creating a new rack
                            '''
                            if column.has_key('size'):
                                rack_size = column['size']
                            else:
                                rack_size = 42
                            payload = {'name': column['rack'], 'room': column['room'], 'size': rack_size}
                            response = self.post_rack(payload)
                            if response.status_code == 200:
                                info = '%s rack Added Successfuly' % (column['rack'])
                                logging.info(info)
                            else:
                                info = 'Unable to add the %s rack' %(column['rack'])
                                logging.info(info)
                    else:
                        info = 'No rack Name is Given for the device %s' % (column['name'])
                        logging.info(info)

                    '''
                    Checking the Device Data
                    '''

                    if column['name'] != 'None' and column['name'] != '':
                        check_match = next((entity for entity in eval(device_list)['Devices'] \
                                            if column['name'] in entity.values()), None)
                        if check_match:
                            info = '%s Device Exists' % (column['name'])
                            logging.info(info)
                            payload = {'name': column['name'], 'type': column['type'], 'hardware': column['hardware'],
                                   'customer': column['customer'], 'serial_no': column['serial_no'],
                                   'asset_no': column['asset_no'], 'uuid': column['uuid']}
                            response = self.post_devices(payload)
                            if response.status_code == 200:
                                info = '%s device Updated Successfuly' % (column['name'])
                                logging.info(info)

                        else:
                            '''
                            Creating a new Device
                            '''
                            payload = {'name': column['name'], 'type': column['type'], 'hardware': column['hardware'],
                                   'customer': column['customer'], 'serial_no': column['serial_no'],
                                   'asset_no': column['asset_no'], 'uuid': column['uuid']}
                            response = self.post_devices(payload)
                            if response.status_code == 200:
                                info = '%s device Added Successfuly' % (column['name'])
                                logging.info(info)
                                print info
                            else:
                                info = 'Unable to add the %s device' %(column['name'])
                                logging.info(info)
                    else:
                        info = 'No Device Name is Given for the device %s' % (column['name'])
                        logging.info(info)

            else:
                info = "Set the proper csv file name in config file"
                logging.info(info)
                return
        except:
            info = 'Error Occurred while posting Multiple Data'
            logging.error(info)


#def main():

    #obj=Device(raw_input('Enter the Config File name \n'))
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
    #obj.delete_device(2)
    #obj.delete_building(3)
    #obj.post_data()

#main()

