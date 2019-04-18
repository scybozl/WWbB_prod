#! /bin/bash

export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/
source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh
#asetup 19.2.5.17.1,MCProd,here
#asetup 20.7.8.19,AtlasDerivation,here
#asetup 20.7.8.31,AtlasDerivation,here
#asetup 19.2.5.32
#asetup 20.7.9.9.7,MCProd
asetup 21.2,latest,AthDerivation,slc6

#localSetupPandaClient
#localSetupRucioClients
#voms-proxy-init --voms=atlas
