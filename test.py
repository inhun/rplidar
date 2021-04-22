import time


for i in range(10):
    now = time.strftime('%H%M%S', time.localtime(time.time()))
    with open(f'data/distance/{now}.txt', 'w') as f:
        f.write(str(i))
