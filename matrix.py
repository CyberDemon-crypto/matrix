#!/usr/bin/python3
"""made by https://github.com/CyberDemon-crypto"""
import sys, time, random, os
os.system('clear')
sys.stdout.write('\u001b[32m')
lines = 20   # Height
width = 150  # Width
sys.stdout.write('\n' * lines)


def gen():
    a = ''
    for i in range(width):
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
        sys.stdout.write(f'\u001b[2D\u001b[31m{" "*(width//2-17)}Hacker detected!\u001b[0m\n')
        break

