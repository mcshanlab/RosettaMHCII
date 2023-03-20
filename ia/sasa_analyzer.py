#!/usr/bin/python

#       Sgourakis Lab
#   Author: Andrew McShan

'''

INTERFACE class contains all the necessary functionalities required to calculate
interface energies between two chains in a pose.

'''

# Load the Rosetta commands for use in the Python shell
from pyrosetta import *
from pyrosetta.rosetta.protocols.analysis import InterfaceAnalyzerMover
from pyrosetta.rosetta.protocols.analysis import PerResidueInterfaceData

class SASA:

    # class members
    pose = None # pose for which we want to calculte binding energies
    ia_sasa = None # InterfaceAnalyzerMover object that provides all the interface related interfaces

    # constructor
    def __init__(self, pose):
        self.ia_sasa = None
        self.pose = pose

    # method to apply the mover and populate necessary interface energies
    def analyze(self):
        self.ia_sasa = InterfaceAnalyzerMover()
        # we could have used self.ia.apply(self.pose), but the apply() function in turn calls
        # apply_const(), so we just call that directly
        self.ia_sasa.apply_const(self.pose)

    # getter method
    def get_regional_avg_per_residue_SASA_int(self):
        # return the interface score (or binding energy)
        return self.ia_sasa.get_interface_regional_avg_per_residue_SASA_int()
