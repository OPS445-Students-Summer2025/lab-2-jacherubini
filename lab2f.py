#!/usr/bin/env python3

# Author: John  Cherubini
# ID: jacherubini
# Date Created 2025/05/22

import sys

if len(sys.argv) !=2:
	print(f"Usage: {sys.argv[0]} number")
	sys.exit(1)

timer =int(sys.argv[1])

while timer > 0:
	print(timer)
	timer -= 1

print("blast off!")
