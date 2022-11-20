import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

with open("README.md", "a") as myfile:
    myfile.write("\n appended " % id_generator())
