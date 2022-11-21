import string
import random
from datetime import datetime

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

dt = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

with open("README.md", "a") as myfile:
    myfile.write("  \n- appended python %s (random string %s)" % (dt, id_generator()))
