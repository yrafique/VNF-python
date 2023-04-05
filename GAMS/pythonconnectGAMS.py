import os

# set the path to your GAMS installation
gams_path = "C://GAMS/win64/"
print(gams_path)
os.environ["PATH"] += os.pathsep + gams_path

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