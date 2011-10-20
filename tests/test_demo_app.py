import nose
import unittest
from test_framework.fixtures import login_manager

app_url = 'https://app.hubspotqa.com/market/53/canvas/testapp/'

class MarketplaceContainerWeb(unittest.TestCase):

    def setUp(self):
        self.application_name = 'AppMarketplace'
        self.unique_id = 53
        
        login_manager.login(self.driver, 53, 'qa', 'selenium@hubspot.com', 'U!feM!kO')
        self.driver.implicitly_wait(5)

    def __search_leads(self, search_string='Maxey', api_key='demo'):
        """use the demo app to search for the given string with the given api key"""
        self.driver.get(app_url)
        search_field = self.driver.find_element_by_name("search_field")
        api_key_field = self.driver.find_element_by_name("api_key")
        submit_button = self.driver.find_element_by_css_selector("button[type=submit]")
        
        search_field.send_keys(search_string)
        api_key_field.send_keys(api_key)
        submit_button.click()

    def test_search_leads(self):
        """try to search the demo app and make sure we get results"""
        self.__search_leads()
        
        #get the results
        result_div = self.driver.find_element_by_css_selector("div#remoteContents")
        results = result_div.text
        #make sure this isn't an error/timeout
        self.assertTrue('DeadlineExceededError' not in results, "The leads search timed out.")
        self.assertTrue('Traceback (most recent call last):' not in results, "An exception occurred on the page.")
        
        #check the params that were passed through
        param_values = {
            "caller": "HubSpot Marketplace",
            "userid": "7600",
            "portalid": "53",
            "appname": "[TEST APP] - Leads Search",
            "callbackurl": "https://leads-search.appspot.com/",
            "pageurl": "https://leads-search.appspot.com/result",
            "canvasurl": "https://app.hubspotqa.com/market/53/canvas/testapp/",
            "requestsignature": "kAQ0_7i0-64PUL_4LwANI-qxWP4.cGF5bG9hZA"
        }
        param_fields = self.driver.find_elements_by_css_selector('p.param > span')
        for field in param_fields:
            self.assertTrue(field.text == param_values[field.get_attribute('name')], "Expected: %s, Got: %s, for param named: %s"%
                                                                    param_values[field.get_attribute('name')],
                                                                    field.text,
                                                                    field.name)

    def __test_invalid_api_key(self):
        """try to search the demo app with a nonexistent and make sure we get an error"""
        self.__search_leads(api_key="thisisafakekey")
        
        result_div = self.driver.find_element_by_css_selector("div.app > div.header")
        results = result_div.text
        self.assertTrue('Canvas App Error' in results, "The leads search accepted a fake api key.")