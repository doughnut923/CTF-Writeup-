from hashlib import sha256

with open('rockyou.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        print(line.strip())
        print(sha256(line.strip().encode()).hexdigest())
        if(sha256(line.strip().encode()).hexdigest() == 'cd0894152aa5eec36ec79eb2bcb90ca40f056804530f40732b4957a496b23dc8'):
            print(line.strip(), 'is a passwrod')
            exit()
