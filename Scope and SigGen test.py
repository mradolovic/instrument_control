#!/usr/bin/env python3.6.5
# -*- coding: utf-8 -*-
import pyvisa
import time
import binascii

#if you don't know the resource, try
#print(rm.list_resources())

#USB resource of Device
signal_generator = 'USB0::0xF4EC::0x1103::SDG1PA0D801185::INSTR'
oscilloscope = 'USB0::0xF4ED::0xEE3A::SDS1ECDX2R3058::INSTR'

if __name__ == '__main__':
    """"""
    rm = pyvisa.ResourceManager()
    #gen = rm.open_resource(signal_generator, timeout=50000, chunk_size = 24*1024*1024)
    scope = rm.open_resource(oscilloscope, timeout=50000, chunk_size = 24*1024*1024)
    # gen.write("*RST")
    # gen.write("C1:BSWV AMP,3")
    # gen.write("C1:BSWV FRQ,4000")
    # gen.write("*IDN?")
    # print(gen.read())
    # gen.write("C1:OUTP?")
    # print(gen.read())
    scope.write("*IDN?")
    print(scope.read())
    scope.write("*RST")
    scope.write("C1:ATTN 1")
    scope.write("C1:VDIV 500uV")
    scope.write("PACU PKPK,C1")
    time.sleep(4)
    scope.write("STOP")
    scope.write("C1:PAVA? PKPK")
    print(scope.read())
    time.sleep(3)
    scope.write("ARM")

