import pyvisa
import time
import binascii

#if you don't know the resource, try
#print(rm.list_resources())

#USB resource of Device
#signal_generator = 'USB0::0xF4EC::0x1103::SDG1PA0D801185::INSTR'
oscilloscope = 'USB0::0x2A8D::0x1776::MY59242900::INSTR'

if __name__ == '__main__':
    """"""
    rm = pyvisa.ResourceManager()
    #gen = rm.open_resource(signal_generator, timeout=50000, chunk_size = 24*1024*1024)
    scope = rm.open_resource(oscilloscope, timeout=50000, chunk_size = 24*1024*1024)

    scope.write("*IDN?")
    print(scope.read())
    scope.write(":CHAN1:SCAL?")
    print(scope.read())
    # scope.write("PACU PKPK,C1")
    # time.sleep(4)
    # scope.write("STOP")
    # scope.write("C1:PAVA? PKPK")
    # print(scope.read())
    # time.sleep(3)
    # scope.write("ARM")

