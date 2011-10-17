from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.command import Command
from service import Service

class WebDriver(RemoteWebDriver):

    def __init__(self,deviceID=None):
        self.service = Service(deviceID)
        self.service.start()
        RemoteWebDriver.__init__(self,
            command_executor=self.service.service_url,
            desired_capabilities=DesiredCapabilities.ANDROID)

    def quit(self):
        """ Close AndroidDriver application on device"""
        try:
            RemoteWebDriver.quit(self)
        except httplib.BadStatusLine:
            pass
        finally:
            self.service.stop()
if __name__ == '__main__':
    #driver= WebDriver('emulator-5554')
    driver= WebDriver()
    driver.get("http://www.symbio.com")
    driver.quit()