#!/usr/bin/python
## YAML to JSON converter
import yaml as pyaml
import json
import sys

def convertToJSON(filename):
    print("Loading file...", end=" ")
    try:
        f=open(filename,"r")
        fbuf=f.read()
        f.close()
        print("%i bytes." % (len(fbuf)))
    except Exception as e:
        print(e)
        return

    try:
        print("Parsing YAML...", end=" ")
        yaml=pyaml.load(fbuf)
        print("%i entries." % (len(yaml)))
    except Exception as e:
        print(e)
        return
    
    jsonFilename=""
    for i in filename.split(".")[:-1]:
        jsonFilename+=i
    jsonFilename+=".json"
    
    try:
        print("Output filename is %s." % jsonFilename)
        f=open(jsonFilename,"w")
        f.write(json.dumps(yaml))
        print("JSON file written." % (jsonFilename))
    except Exception as e:
        print(e)
        return
    
for i in sys.argv[1:]:
    convertToJSON(i)
    
    
