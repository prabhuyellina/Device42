import sample
import logging

class test:
    def __init__(self):
        print 'Welcome To Device42 Testing'
        self.d42_obj = sample.Device('Device42.cfg')
        logging.basicConfig(format='%(asctime)s %(message)s', filename='test_log.txt', level=logging.DEBUG)

    def test_get_buildings(self):

        try:
            status_code = self.d42_obj.get_buildings()
            if status_code == 200:
                info = 'get_buildings if working and the status code is: %s' %(status_code)
                logging.info(info)
            else:
                info = 'get_buildings if not working and return with the status code: %s' %(status_code)
                logging.info(info)
        except:
            logging.error('Error Occured while testing get_building module')

    def test_get_rooms(self):

        try:
            status_code = self.d42_obj.get_rooms()
            if status_code == 200:
                info = 'get_rooms if working and the status code is: %s' %(status_code)
                logging.info(info)
            else:
                info = 'get_rooms if not working and return with the status code: %s' %(status_code)
                logging.info(info)
        except:
            logging.error('Error Occured while testing get_rooms module')

    def test_get_hardwares(self):

        try:
            status_code = self.d42_obj.get_hardwares()
            if status_code == 200:
                info = 'get_hardwares if working and the status code is: %s' % (status_code)
                logging.info(info)
            else:
                info = 'get_hardwares if not working and return with the status code: %s' % (status_code)
                logging.info(info)
        except:
            logging.error('Error Occured while testing get_hardwares module')


    def test_get_racks(self):

        try:
            status_code = self.d42_obj.get_racks()
            if status_code == 200:
                info = 'get_racks if working and the status code is: %s' % (status_code)
                logging.info(info)
            else:
                info = 'get_racks if not working and return with the status code: %s' % (status_code)
                logging.info(info)
        except:
            logging.error('Error Occured while testing get_racks module')

    def test_get_devices(self):

        try:
            status_code = self.d42_obj.get_racks()
            if status_code == 200:
                info = 'get_devices if working and the status code is: %s' % (status_code)
                logging.info(info)
            else:
                info = 'get_devices if not working and return with the status code: %s' % (status_code)
                logging.info(info)
        except:
            logging.error('Error Occured while testing get_devices module')

