command = ""
while command != "quit":
    command = input(">").lower()
    if command == "start":
        print("car started")
    elif command == "stop":
        print("car stopped")
    elif command == "quit":
        print('quit')
    elif command == "help":
        print(""" start - to start 
        stop - to stop
        quit - to quit """)
    else:
        print("sorry, i don't get it")