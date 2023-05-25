from tuyapy import TuyaApi
import sys
from ai_config import *

def LightOn():
    api = TuyaApi()
    api.init(USERNAME, PASSWORD, COUNTRY_CODE)
    light_id = str()
    api.get_device_by_id(light_id).turn_on()
    sys.exit()
