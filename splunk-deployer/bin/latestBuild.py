## Elias Haddad ehaddad@splunk.com
import os
import sys
import urllib2
import re




def getLatestSPL(TA_HOME, ta):
        #endpoint=TA_HOME + str(ta) + '/builds/develop/latest'
        endpoint=TA_HOME + str(ta) + '/demo/latest'
        try:
                response = urllib2.urlopen(endpoint)
                html = response.read()
                RList= re.findall(r">([0-9a-zA-Z\-_\.]+\.[a-zA-Z]{3})</", html)
                #get latest 
                for s in RList:
                        package_name=s

                return package_name

        except Exception, e:
                print "Error - Coud not get SPL. Error=" + str(e) + " TA=" + str(ta) + " endpoint=" + endpoint
                return -1

def downloadLatestSPL(SPLUNK_HOME, TA_HOME, ta, spl):
        #endpoint= TA_HOME + str(ta) + '/builds/develop/latest/'  + str(spl)
        endpoint= TA_HOME + str(ta) + '/demo/latest/'  + str(spl)
        try:
                response = urllib2.urlopen(endpoint)
                spl_file = response.read()
                file_name= re.sub(r"\.spl|\.tgz", "", str(spl))
                path_file=SPLUNK_HOME + "/etc/apps/" + file_name
                file = open(path_file, "w")
                file.write(spl_file)
                file.close()
                return endpoint

        except Exception, e:
                print "Error - Coud not save and download spl file. Error=" + str(e) + " TA=" + str(ta) + " endpoint=" + endpoint
                return -1

def downloadLatestBuilderSPL(SPLUNK_HOME, TA_HOME, ta, spl):
        #endpoint= TA_HOME + str(ta) + '/builds/develop/latest/'  + str(spl)
        endpoint= TA_HOME + str(ta) + '/demo/latest/'  + str(spl)
        try:
                response = urllib2.urlopen(endpoint)
                spl_file = response.read()
                file_name= re.sub(r"\.spl|\.tgz", "", str(spl))
                path_file=SPLUNK_HOME + "/etc/apps/" + file_name
                file = open(path_file, "w")
                file.write(spl_file)
                file.close()
                return endpoint

        except Exception, e:
                print "Error - Coud not save and download spl file. Error=" + str(e) + " TA=" + str(ta) + " endpoint=" + endpoint
                return -1