# -*- coding: utf-8 -*-
"""
==========================================================
Program : Quantum_Device_Profiler/InstrumentServer.py
==========================================================
To Do:

- handle connection errors
- implement all methods

"""
__author__ =  "Sadman Ahmed Shanto"
__date__ = "02/13/2023"
__email__ = "shanto@usc.edu"

from utilities import *
import Labber

class InstrumentServer:

    """Docstring for InstrumentServer. """

    def __init__(self, instruments_list):
        """TODO: to be defined. """
        self.instruments = parse_json(instruments_list)
        self.client = self.connectToServer
        self.activeInstruments = None

    def connectToServer(self):
        return Labber.connectToServer(timeout=None) # establish connection to Labber

    def startAllInstruments(self):
        create_header("INSTRUMENT SERVER")
        labber_instrs = []
        for instr in self.instruments:
            instr_uid = instr["instr_uid"]
            print(f"{instr["instr_name"]} has started successfully!")
            activ_instr = self.client.connectToInstrument(get_labber_settings(instr))
            labber_instrs.append({"instr_uid":instr_uid, "instr":activ_instr})
        self.activeInstruments = labber_instrs


    def stopAllInstruments(self):
        raise NotImplementedError()

    def getActiveInstruments(self):
        return self.activeInstruments
