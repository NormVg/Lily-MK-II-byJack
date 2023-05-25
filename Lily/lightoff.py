from tuyapy import TuyaApi
import sys
from ai_config import *

def LightOff():
    api = TuyaApi()
    api.init(USERNAME, PASSWORD, COUNTRY_CODE)
    api.get_device_by_id(light_id).turn_off()
    sys.exit()
