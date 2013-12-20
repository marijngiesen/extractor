import sys
from subprocess import call
from extractor import registry


def extract(filename):
    if registry.DEBUG:
        sys.stdout.write(" + extracting " + str(filename) + "...")
        if registry.DRYRUN: sys.stdout.write(registry.UNRAR_BINARY + " e -y " + filename + " > /dev/null")
        sys.stdout.flush()

    if not registry.DRYRUN:
        status = call(registry.UNRAR_BINARY + " e -y " + filename + " > /dev/null", shell=True)
    else:
        status = 0

    if status != 0:
        if registry.DEBUG: print " failed"
        return False

    if registry.DEBUG: print " done"

    return True

