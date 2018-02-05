# Ritesh Tandon
# Spring 2018 - i524
# Eve/REST

from eve import Eve
import psutil
import platform
from datetime import datetime
import json

app = Eve()



# Returns everything outlined below
@app.route('/mysystemdetails/alldetails', methods=['GET'])
def alldetails():
  
    # create a dictionary z ; call ram(), mydisk(), processorinfo() method and merge the dictionary data
    # returned by the methods. Returned all the system details using json.dumps method
    z=ram().copy()
    z.update(mydisk())
    z.update(processorinfo())
    return json.dumps(z)


# write a function that returns dictionary with RAM values
def ram():
    ram = {
            "RAM Size": str(psutil.virtual_memory().total/(1024*1024)) + " MB",
            "RAM available": str(psutil.virtual_memory().available/(1024*1024)) + " MB",
            "Used RAM": str(psutil.virtual_memory().used/(1024*1024)) + " MB",
            "Free": str(psutil.virtual_memory().free/(1024*1024)) + " MB"
            }

    return ram
 

# write a function that returns hard disk values in dictionary
def mydisk():
    diskusage = {
            "Disk Size": str(psutil.disk_usage('/').total/(1024*1024)) + " MB",
            "Used Disk": str(psutil.disk_usage('/').used/(1024*1024)) + " MB",
            "Free Disk": str(psutil.disk_usage('/').free/(1024*1024)) + " MB",
            }

    return diskusage

# write a function that returns processor info in dictionary
def processorinfo():
    pinfo = {
              "CPU - Cores": psutil.cpu_count(),
              "CPU - Usage": str(psutil.cpu_percent()) + "%",
          
            }
 
    return pinfo

if __name__ == '__main__':
	app.run()
