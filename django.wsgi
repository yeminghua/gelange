import os, sys
#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project) 

#
sys.stdout = sys.stderr
sys.path.append(workspace)
print workspace,"(----------------------------------------------------------)"
sys.path.append(workspace + "/mysite/gelange/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler() 
