import shutil 
import datetime


now=datetime.datetime.now()
date=str(now)[:10]

# define the name of the directory to be deleted
path = '/tmp/'+date

try:  
  shutil.rmtree(path)
except OSError:  
  print ("Deletion of the directory %s failed" % path)
else:  
  print ("Successfully deleted the directory %s" % path)
