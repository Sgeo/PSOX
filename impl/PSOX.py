PSOX_MAJOR_VER = 0
PSOX_MINOR_VER_RANGE = (0, 0)

assert PSOX_MINOR_VER_RANGE[0] <= PSOX_MINOR_VER_RANGE[1]

from optparse import OptionParser
from subprocess import Popen, PIPE
import sys
from psox.errors import IllegalPSOXError, UnsupportedVersionError
from psox.utils import getlines, linelen, vn2vs

parser = OptionParser(usage="%prog [-s safety1,safety2] [-c \"fakecommandline\"] command", version="PSOX " + vn2vs(PSOX_MAJOR_VER, PSOX_MINOR_VER_RANGE) + " - %prog 0.0")
parser.add_option("-s", "--safety", dest="safety", help="Specifies safety options. e.g to allow full access to the filesystem, and no Internet access, use \"-s fullfileio,nonet\"")
parser.add_option("-c", "--command-line", dest="cline", help="Specifies the virtual command line for the client")

options, args = parser.parse_args()

client = Popen(args, stdin=PIPE, stdout=PIPE)

getline = client.stdout.readline

def send(msg):
    client.stdin.write(msg)
    client.stdin.flush()

curline = getlines(getline, linelen, 4)
if(curline[0:2]!="\x00\x07"):
    raise IllegalPSOXError
elif(curline[2] != chr(PSOX_MAJOR_VER)):
    raise UnsupportedVersionError

send("\x00")
curline = getlines(getline, linelen, 3)

cli_min_ver, cli_max_ver = ord(curline[0]), ord(curline[1])
print "Client's PSOX Ver: PSOX " + vn2vs(PSOX_MAJOR_VER, cli_min_ver, cli_max_ver)
if(cli_min_ver > cli_max_ver):
    raise IllegalPSOXError("Client's minimum version higher than its maximum?")
if(cli_max_ver < PSOX_MINOR_VER_RANGE[0]):
    raise UnsupportedVersionError("PSOX " + vn2vs(PSOX_MAJOR_VER, cli_max_ver) + " obsolete.")
if(cli_min_ver > PSOX_MINOR_VER_RANGE[1]):
    raise UnsupportedVersionError("PSOX " + vn2vs(PSOX_MAJOR_VER, cli_min_ver) + " not supported yet.")

cliver = min(cli_max_ver, PSOX_MINOR_VER_RANGE[1])

print "Running PSOX " + vn2vs(PSOX_MAJOR_VER, cliver)
