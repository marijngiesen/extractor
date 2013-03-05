#!/usr/bin/python

import os
import sys
from subprocess import call

UNRAR_BINARY = "/usr/bin/unrar"


def usage():
    print "Usage: " + os.path.basename(__file__) + " <directory>"
    sys.exit(1)


def processDirectory(directory):
    for root, dirs, files in os.walk(directory):
        print "Scanning " + root

        filename = [filename for filename in files if ".rar" in filename]
        if len(filename) < 1:
            continue

        sys.stdout.write(" + extracting " + str(filename[0]) + "...")
        sys.stdout.flush()

        currentDir = os.getcwd()
        os.chdir(root)

        status = call(UNRAR_BINARY + " e -y " + filename[0] + " > /dev/null", shell=True)
        if status != 0:
            print " failed"
            continue

        print " done"

        # TODO: remove archive files
        print " + removing archive files...",
        print "done"

        os.chdir(currentDir)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print "Error: Directory " + directory + " does not exist"
        sys.exit(1)

    processDirectory(directory)
