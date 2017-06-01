import talon
from talon import quotations

talon.init()

text =  """Reply

-----Original Message-----

Quote"""

reply = quotations.extract_from(text, 'text/plain')
# reply = quotations.extract_from_plain(text)

print(reply)