import os

for x in os.listdir():
    if os.path.isfile(x) and x.startswith("t"):
        print(x.replace("-burns", ""))