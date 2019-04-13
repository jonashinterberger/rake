import filecmp
import time
import sys, os


sleeptime = 1
path_to_a = './hash1.txt'
path_to_b = './hashold.txt'

while True:
  os.system("./get.sh")
  if filecmp.cmp(path_to_a, path_to_b):
    print("No change detected")
    time.sleep(20)
  else:
    print("New RSS detected, printing now")
    os.system("./print.sh")
