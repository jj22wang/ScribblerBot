import subprocess

proc = subprocess.Popen("php /getNextCommand.php", shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#script_response = proc.communicate()[0]
script_response = proc.stdout.read()
print script_response
#subprocess.call("php /Users/Jack/Downloads/move test (fifth_updates)/newTestCommand.php")

print "hi"
#p = subprocess.Popen(['echo ', '"Hello World"'], shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  
#print p.communicate()
