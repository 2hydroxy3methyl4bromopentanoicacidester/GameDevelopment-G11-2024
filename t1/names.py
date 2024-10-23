import os

for x in os.listdir():
    if os.path.isfile(x) and x.startswith("t"):
        print(f"\"{x}\",")#.replace("-burns", ""))
    if os.path.isfile(x) and x.startswith("x-"):
        print(f"\"{x}\",")#.replace("-burns", ""))