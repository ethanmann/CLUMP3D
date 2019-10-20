import os
from file_readers import *
import cluster_config
import preliminaries

###########################################################################
# markov chain monte carlo variables (ML)
# rescale number of iterations if desired (JS)
nMCMCTimes = 2
nMCMCTimesXSZ = 1
nMCMCTimesGL = 1
nBFTimesXSZ = 1
nSeedsTimes = 5*nMCMCTimes
###########################################################################

###########################################################################
# i'll put the 2D later (ML)
# do we want to run initial 2D fits to provide starting parameter values? (JS)
Run2DXSZ = True
Run2DGL = True
Run3D = True
Run3DExtension = False
RunPictures = True
###########################################################################

###########################################################################
# chi-square weight variables (ML)
# do we want to change weighting of different datasets in fit? (JS)
ChiSquareWeightXSZ = 1
ChiSquareWeightGL = 1
ChiSquareWeightSB1D = 1
ChiSquareWeightSB2D = 1
ChiSquareWeightT = 1
ChiSquareWeightSZ = 1
###########################################################################

###########################################################################
# what type of priors to use, and set some file extensions (JS)
SBMapString = "2D" # x-ray?
qPriorString = "flat" # matter shape priors, apparently the acceptable values are "flat";"nbody";"nbodyJS02";"flatICM";"spherical"
qICMPriorString = "none" # gas shape priors, values are "none","T"(TICM=TMat),"HE"(qICMi=qiphi),"HE+T"(TICM=TMat and qICM1=q1phi),"LS03"(approximated LS03)

# strings (ML)
GLProjStringToAddTmp1 = "example_v1.0"
XSZProjStringToAddTmp1 = "_example_v1.0" # "_v2017"
GLXSZ3DStringToAddTmp1 = "example_v1.0" # "";"_SaWLens";"_nPlanck";"_v01"

# additional sharp priors
SharpPriorsToAddString = "none" # defaults include "PUniv" "TUniv" and "none"

if qPriorString == "spherical":
    qPriorString = "sph"
else:
    qPriorString = "ell"

if XSZProjStringToAddTmp1 != "" and XSZProjStringToAddTmp1[0] != "_":
    XSZProjStringToAddTmp1 = "_" + XSZProjStringToAddTmp1

if GLXSZ3DStringToAddTmp1 != "" and GLXSZ3DStringToAddTmp1[0] != "_":
    GLXSZ3DStringToAddTmp1 = "_" + GLXSZ3DStringToAddTmp1
###########################################################################

###########################################################################
# cosmological parameters and units (JS)

# SEE preliminaries.py
# omegaM0v, hv, pull from astropy
# omegaLambda0v = 1 - omegaM0v

MUnits = 10**15 * preliminaries.MSunMKS / preliminaries.hv
rUnits = preliminaries.MpcMKS / preliminaries.hv
PUnits = preliminaries.G * MUnits**2 / rUnits**2   # G M^2 / (R * R^3)
###########################################################################

import_cluster_info()
import_gl_info()
import_sz_info()
