light = input('What is the status of the traffic light?(red/yellow/green)')

if light:
    if light == 'red':
        print('Stop')
    elif light == 'yellow':
        print('Ready to go')
    elif light == 'green':
        print('start')
    else:
        print('error')
else:
    print('error')