from tank import Tank
from simatic import Plc

import time

tk101 = Tank()
plc01 = Plc()

while(True):
    tank_state = tk101.process()
    plc01.write_input(0, 0, tank_state['hi_level'])
    plc01.write_input(0, 1, tank_state['lo_level'])
    tk101.invalve = plc01.read_output(0, 0)
    tk101.outvalve = plc01.read_output(0, 1)
    time.sleep(1)