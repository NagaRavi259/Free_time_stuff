previous_status ='0'
while True:
    status = input('')
    if status == previous_status:
        pass
    else:
        previous_status=status
        if '0'==previous_status:
            print('server was down')
        else:
            print('server was running')