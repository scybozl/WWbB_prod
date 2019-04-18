## Initialise Herwig7 for LHEF showering
include("MC15JobOptions/Herwig7_LHEF.py")

## Provide config information
evgenConfig.generators += ["Powheg","Herwig7"] 
evgenConfig.tune        = "MMHT2014"
evgenConfig.description = "Sherpa/Herwig7 LHEF WWbb"
evgenConfig.keywords    = ["SM","ttbar"]
evgenConfig.contact     = ["Ludovic Scyboz (scyboz@mpp.mpg.de)"]

## Configure Herwig7
Herwig7Config.me_pdf_commands(order="NLO", name="PDF4LHC15_nlo_30")
Herwig7Config.tune_commands()
Herwig7Config.lhef_powhegbox_commands(lhe_filename=runArgs.inputGeneratorFile, me_pdf_order="NLO")

Herwig7Config.add_commands("""
#set /Herwig/Generators/EventGenerator:NumberOfEvents 10000000
""")

## run generator
Herwig7Config.run()
