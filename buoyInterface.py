print "Starting...\n"

knownIPs = ["172.17.52.75"]

while True:
    ip = knownIPs[int(raw_input("Enter ID: ")]
    command = raw_input("Enter command: ")
    value = 0    
    try:
        value = raw_input("Enter value: ")
    except:
        value = 0
    print ip, command, value,"\n"