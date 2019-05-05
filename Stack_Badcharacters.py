#!/usr/bin/python
from subprocess import call



try:
	script = "cat stack_copy.txt | awk '{print $2}' | tr '\n' ' ' | sed 's/ //g' | sed 's/.\{2\}/& /g' | tr ' ' '\n'"
        out = call(script, shell=True)
        print out
except:
        print "stack_Copy.txt not found.."
