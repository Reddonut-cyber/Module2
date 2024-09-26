import json
import os



n = "asdf.odi"
if os.path.exists(n):
        with open(n, 'r') as file:
                     json.load(file)
   