#It takes Build Number as argument
import shutil 
import datetime
import sys,argparse

#Get arguments from command line
parser = argparse.ArgumentParser(description='to delete directories created by bootstrapper-init')
parser.add_argument('-bn', '--build_number', help='Build number from Jenkins', required=True)
args = vars(parser.parse_args())
build_number=args['build_number']
now=datetime.datetime.now()
date=str(now)[:10]

# define the name of the directory to be deleted
path = '/tmp/'+date+'-'+build_number

try:  
  shutil.rmtree(path)
except OSError:  
  print ("Deletion of the directory %s failed" % path)
else:  
  print ("Successfully deleted the directory %s" % path)
