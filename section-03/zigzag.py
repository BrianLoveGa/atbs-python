import time, sys

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('******###_-_###******')
        time.sleep(0.1)

        if indentIncreasing:
            indent = indent +1
            if indent == 40:
                indentIncreasing = False
        else:
            indent = indent -1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
    
