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
        Device42_cfg = config.get('Credentials', 'Device42_cfg')
        test_log_file = config.get('Credentials', 'test_log')
        self.d42_obj = sample.Device(Device42_cfg)
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


if __name__ == '__main__':
    unittest.main()

