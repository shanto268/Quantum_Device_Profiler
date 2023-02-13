# -*- coding: utf-8 -*-
"""
===================================================
Program : Quantum_Device_Profiler/utilities.py
===================================================
To Do:

- implement `get_labber_settings` method

"""
__author__ =  "Sadman Ahmed Shanto"
__date__ = "02/13/2023"
__email__ = "shanto@usc.edu"

#libraries used
import numpy as np
import os, sys
import json

def parse_json(json_file):
    with open(json_file) as json_file_obj:
        data = json.load(json_file_obj)
    return data

def get_labber_settings(instr):
    """
    TO DO: 
        - have conditionals based on the type of instrument to generate the correct dict object for Labber
    returns instr_name <string>, instr_config<dict>
    """
    raise NotImplementedError

def create_header(hstring):
    return "\n\n"+"="*15+f"\t{hstring}\t"+"="*15+"\n\n"
