#!/usr/bin/env python
import os
os.system("export ENAME")
os.system("export EPASS")
USERNAME = os.environ["ENAME"]  # just the part before the @ sign, add yours here
PASSWORD = os.environ["EPASS"]

print USERNAME
print PASSWORD