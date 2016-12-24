import sample
import logging
import unittest
import ConfigParser


class TestDevice42(unittest.TestCase):

    def setUp(self):
        """
        Testing Device42 API's in sample module
        """
        print 'Welcome To Device42 Testing'
        config = ConfigParser.ConfigParser()
        config.read(raw_input('Enter Config file Name'))
        device42_cfg = config.get('Credentials', 'Device42_cfg')
        test_log_file = config.get('Credentials', 'test_log')
        self.d42_obj = sample.Device(device42_cfg)
        logging.basicConfig(format='%(asctime)s %(message)s', filename=test_log_file, level=logging.DEBUG)

    def test_get_buildings(self):

        try:
            response = self.d42_obj.get_buildings()
            self.assertEqual(response.status_code, 200)
            info = 'get_buildings API is working and returned with: %s' % response
            logging.info(info)
        except AttributeError as e:
            logging.error('Error Occurred while testing get_building module', e)

    def test_get_rooms(self):

        try:
            response = self.d42_obj.get_rooms()
            self.assertEqual(response.status_code, 200)
            info = 'get_rooms API is working and returned with: %s' %response
            logging.info(info)
        except AttributeError as e:
            logging.error('Error Occurred while testing get_rooms module', e)

    def test_get_hardwares(self):

        try:
            response = self.d42_obj.get_hardwares()
            self.assertEqual(response.status_code, 200)
            info = 'get_hardwares API is working and returned with: %s' %response
            logging.info(info)
        except AttributeError as e:
            logging.error('Error Occurred while testing get_hardwares module', e)

    def test_get_racks(self):

        try:
            response = self.d42_obj.get_racks()
            self.assertEqual(response.status_code, 200)
            info = 'get_racks API is working and returned with: %s' % response
            logging.info(info)
        except AttributeError as e:
            logging.error('Error Occurred while testing get_racks module', e)

    def test_get_devices(self):

        try:
            response = self.d42_obj.get_racks()
            self.assertEqual(response.status_code, 200)
            info = 'get_devices API is working and returned with: %s' % response
            logging.info(info)
        except AttributeError as e:
            logging.error('Error Occurred while testing get_devices module', e)

    def test_post_building(self):

            try:
                payload = {'name': 'Building_testing'}
                response = self.d42_obj.post_building(payload)
                self.assertEqual(response.status_code, 200)
                info = 'post_buildings API is working and returned with: %s' % response
                logging.info(info)
            except AttributeError as e:
                logging.error('Error Occurred while testing post_building module', e)

    def test_post_room(self):

        try:
            payload = {'name': 'Room_testing', 'building': 'Building_testing'}
            response = self.d42_obj.post_room(payload)
            self.assertEqual(response.status_code, 200)
            info = 'post_room API is working and returned with: %s' % response
            logging.info(info)
        except AttributeError as e:
            logging.error('Error Occurred while testing post_room module', e)

    def test_post_hardwares(self):

        try:
            payload = {'name': 'hardware_testing', 'type': 'physical_testing'}
            response = self.d42_obj.post_hardwares(payload)
            self.assertEqual(response.status_code, 200)
            info = 'post_hardwares API is working and returned with: %s' % response
            logging.info(info)
        except AttributeError as e:
            logging.error('Error Occurred while testing post_hardwares module', e)

    def test_post_rack(self):

        try:
            payload = {'name': 'rack_testing', 'room': 'Room_testing', 'size': '42'}
            response = self.d42_obj.post_rack(payload)
            self.assertEqual(response.status_code, 200)
            info = 'post_rack API is working and returned with: %s' % response
            logging.info(info)
        except AttributeError as e:
            logging.error('Error Occurred while testing post_rack module', e)

    def test_post_devices(self):

        try:
            payload = {'name': 'Device_Testing', 'type': 'physical_testing', 'hardware': 'hardware_testing',
                       'customer': 'ABC', 'serial_no': '132',
                       'asset_no': '123', 'uuid': '264'}
            response = self.d42_obj.post_devices(payload)
            self.assertEqual(response.status_code, 200)
            info = 'post_devices API is working and returned with: %s' % response
            logging.info(info)
        except AttributeError as e:
            logging.error('Error Occurred while testing post_devices module', e)


if __name__ == '__main__':
    unittest.main()

