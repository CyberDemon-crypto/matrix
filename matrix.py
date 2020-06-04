"""made by https://github.com/CyberDemon-crypto"""
import sys, time, random
sys.stdout.write('\u001b[32m')
lines = 20  # Height
sys.stdout.write('\n' * lines)


def gen():
    a = ''
    for i in range(40):    # Width
        a += str(random.randint(0, 1))
    print(a)


while True:
    try:
        time.sleep(0.1)     # Refresh interval
        sys.stdout.write('\u001b[1000D')
        sys.stdout.write(f'\u001b[{lines}A')
        for i in range(lines):
            gen()
    except KeyboardInterrupt:
        break
