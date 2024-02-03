# This is a first try of parsing

import edn_format

ednFile = open("input/arraymap.c.edn", "r")

print(edn_format.loads(ednFile.read()))

ednFile.close()
