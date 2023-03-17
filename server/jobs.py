def create_job(command):
    print("creating job: ",command)
    return 0

def test_job(command):
    check = True
    while check == True:
      check = False
      for i in range(0, len(command)-1):
        if command[i] > command[i+1]:
          check = True
          temp = command[i]
          command[i] = command[i+1]
          command[i+1] = temp
    print("command sorted: ", command)