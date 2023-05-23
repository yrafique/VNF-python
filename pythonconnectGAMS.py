import os

# set the path to your GAMS installation

import sys
sys.path.append(r"C:\GAMS\win64\24.9\apifiles\Python\api\api_36")
sys.path.append(r"C:\GAMS\win64\24.9\apifiles\Python\api\gams")
sys.path.append(r"C:\Program Files\Python36")



# import the GAMS API
import gams

# initialize the GAMS workspace
ws = gams.GamsWorkspace()

# specify the GAMS model file
gams_model = "your_model.gms"

# create a GAMS job
job = ws.add_job_from_file("optimization_wFlow_varsplit.gms")

# run the GAMS job
job.run()

# retrieve the GAMS database
db = job.out_db()