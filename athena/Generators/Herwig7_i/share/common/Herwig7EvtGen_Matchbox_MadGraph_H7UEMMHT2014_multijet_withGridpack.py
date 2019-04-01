from Herwig7_i.Herwig7_iConf import Herwig7
from Herwig7_i.Herwig7ConfigMatchbox import Hw7ConfigMatchbox

name = runArgs.jobConfig[0]
dsid = int(name.split(".")[1])

genSeq += Herwig7()

## Provide config information
evgenConfig.generators += ["Herwig7"]
evgenConfig.tune        = "MMHT2014"

## initialize generator configuration object
generator = Hw7ConfigMatchbox(genSeq, runArgs, run_name="HerwigMatchbox", beams="pp")

## configure generator
generator.me_pdf_commands(order="NLO", name="MMHT2014nlo68cl")
generator.tune_commands()

# HT slice boundaries
pTDict = {0:0,1:0,2:15,3:50,4:150,5:350,6:600,7:950,8:1500,9:2200,10:2800,11:3500,12:4200}
multDict = {0:1.1,1:1.2,2:2.2,3:4.0,4:5.0,5:6.0,6:7.0,7:8.0,8:9.0,9:10.0,10:10.0,11:10.0,12:10.0}

#Herwig7EvtGen_Matchbox_MadGraph_H7UEMMHT2014_multijet.py 
name_info = name.split("_JZ")[1].split(".py")[0]
slice = int(name_info)
mergingscale = 30

evt_multiplier = multDict[slice]

if runArgs.maxEvents > 0:
    nevents=runArgs.maxEvents*evt_multiplier
else:
    nevents=5000*evt_multiplier
 
generator.add_commands("""
read Matchbox/StandardModelLike.in
read Matchbox/DiagonalCKM.in

## Set the order of the couplings
cd /Herwig/MatrixElements/Matchbox
set Factory:OrderInAlphaS 2
set Factory:OrderInAlphaEW 0

## Select the process
## You may use identifiers such as p, pbar, j, l, mu+, h0 etc.
do Factory:Process p p -> j j

##################################################
## Matrix element library selection
##################################################

## Select a generic tree/loop combination or a
## specialized NLO package

# read Matchbox/MadGraph-GoSam.in
# read Matchbox/MadGraph-MadGraph.in
# read Matchbox/MadGraph-NJet.in

read Matchbox/MadGraph-OpenLoops.in

# read Matchbox/HJets.in
# read Matchbox/VBFNLO.in

##################################################
## Cut selection
## See the documentation for more options
##################################################
cd /Herwig/Cuts/

## cuts on additional jets

read Matchbox/DefaultPPJets.in

insert JetCuts:JetRegions 0 FirstJet
"""
+ "set FirstJet:PtMin "+str(pTDict[slice])+"*GeV"
"""
##################################################
## Scale choice
## See the documentation for more options
##################################################

cd /Herwig/MatrixElements/Matchbox
set Factory:ScaleChoice /Herwig/MatrixElements/Matchbox/Scales/MaxJetPtScale

##################################################
## Matching and shower selection
## Please also see flavour scheme settings
## towards the end of the input file.
##################################################

read Matchbox/MCatNLO-DefaultShower.in
# read Matchbox/Powheg-DefaultShower.in
## use for strict LO/NLO comparisons
# read Matchbox/MCatLO-DefaultShower.in
## use for improved LO showering
# read Matchbox/LO-DefaultShower.in
 
read Matchbox/FiveFlavourScheme.in
## required for dipole shower and fixed order in five flavour scheme
# read Matchbox/FiveFlavourNoBMassScheme.in

""")

# Using author's default
generator.sampler_commands("MonacoSampler", 20000, 4, 50000, 1, 100)

if runArgs.generatorRunMode == 'build':
  generator.do_build(10)

elif runArgs.generatorRunMode == 'integrate':
  generator.do_integrate(runArgs.generatorJobNumber)

elif runArgs.generatorRunMode == 'mergegrids':
  generator.do_mergegrids(10,gridpack="Herwig7_gridpack.tar.gz")

elif runArgs.generatorRunMode == 'run':
    if runArgs.runNumber == 364922: generator.do_run(gridpack="group.phys-gener.Herwig7_Matchbox_MG_H7UEMMHT2014.364922.multijet_angular_JZ2.TXT.mc15_v2._00001.tar.gz")
    elif runArgs.runNumber == 364923: generator.do_run(gridpack="group.phys-gener.Herwig7_Matchbox_MG_H7UEMMHT2014.364923.multijet_angular_JZ3.TXT.mc15_v2._00001.tar.gz")
    elif runArgs.runNumber == 364924: generator.do_run(gridpack="group.phys-gener.Herwig7_Matchbox_MG_H7UEMMHT2014.364924.multijet_angular_JZ4.TXT.mc15_v2._00001.tar.gz")
    elif runArgs.runNumber == 364925: generator.do_run(gridpack="group.phys-gener.Herwig7_Matchbox_MG_H7UEMMHT2014.364925.multijet_angular_JZ5.TXT.mc15_v2._00001.tar.gz")
    elif runArgs.runNumber == 364926: generator.do_run(gridpack="group.phys-gener.Herwig7_Matchbox_MG_H7UEMMHT2014.364926.multijet_angular_JZ6.TXT.mc15_v2._00001.tar.gz")
    elif runArgs.runNumber == 364927: generator.do_run(gridpack="group.phys-gener.Herwig7_Matchbox_MG_H7UEMMHT2014.364927.multijet_angular_JZ7.TXT.mc15_v2._00001.tar.gz")
    elif runArgs.runNumber == 364928: generator.do_run(gridpack="group.phys-gener.Herwig7_Matchbox_MG_H7UEMMHT2014.364928.multijet_angular_JZ8.TXT.mc15_v2._00001.tar.gz")
    elif runArgs.runNumber == 364929: generator.do_run(gridpack="group.phys-gener.Herwig7_Matchbox_MG_H7UEMMHT2014.364929.multijet_angular_JZ9.TXT.mc15_v2._00001.tar.gz")
    elif runArgs.runNumber == 364930: generator.do_run(gridpack="group.phys-gener.Herwig7_Matchbox_MG_H7UEMMHT2014.364930.multijet_angular_JZ10.TXT.mc15_v2._00001.tar.gz")
    elif runArgs.runNumber == 364931: generator.do_run(gridpack="group.phys-gener.Herwig7_Matchbox_MG_H7UEMMHT2014.364931.multijet_angular_JZ11.TXT.mc15_v2._00001.tar.gz")
    elif runArgs.runNumber == 364932: generator.do_run(gridpack="group.phys-gener.Herwig7_Matchbox_MG_H7UEMMHT2014.364932.multijet_angular_JZ12.TXT.mc15_v2._00001.tar.gz")
