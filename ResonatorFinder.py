# -*- coding: utf-8 -*-
"""
=========================================================
Program : Quantum_Device_Profiler/ResonatorFinder.py
=========================================================
To Do:

- implement methods

"""
__author__ =  "Sadman Ahmed Shanto"
__date__ = "02/13/2023"
__email__ = "shanto@usc.edu"

#libraries used
from utilities import *
import numpy as np
import os, sys
import Labber


class ResonatorVNA:

    """Docstring for ResonatorVNA:. """

    def __init__(self, vna_obj, user_inputs):
        """TODO: to be defined. """
        self.vna = vna_obj
        self.config = parse_json(user_inputs)
        self.resonances_exp = self.config["expected_resonances"]
        self.num_resonances = len(self.resonances_exp)
        self.res_types = self.config["res_type"]
        self.resonances_found = None

    def set_VNA_state(self,averages=10,if_bandwidth=1000,e_delay=102):
        raise NotImplementedError()


    def adjust_e_delay(self):
        """
        algorithm:
            - span long freq
            - phase grad test -> make it flat or sloping down
        """
        raise NotImplementedError()

    def find_resonators(self):
        resonances_found = []
        for i, res_f in enumerate(self.resonances_exp):
            res_found = self.find_resonator(res_f, self.res_types[i])
            resonances_found.append(res_found)

    def find_resonator(self, res_f, res_type):
        """
        algorithm:
            - go to res_f + big boundary
            - 

        returns: found_resonant_freq (float) #GHz
        TO DO:
        - handle finding resonator by resonator type
            - changing VNA mode and etc
        """
        raise NotImplementedError()




