import os
import sys
from extractor import files, registry


def usage():
    print "Usage: " + sys.argv[0] + " <directory>"
    sys.exit(1)


def main():
    if len(sys.argv) != 2:
        usage()

    if os.environ.get("EXTRACTOR_DEBUG") == "1":
        print "DEBUG"
        registry.DEBUG = 1

    if os.environ.get("EXTRACTOR_DRYRUN") == "1":
        print "DRYRUN"
        registry.DRYRUN = 1
        registry.DEBUG = 1

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print "Error: Directory " + directory + " does not exist"
        sys.exit(1)

    if not os.path.isfile(registry.UNRAR_BINARY) or not os.access(registry.UNRAR_BINARY, os.X_OK):
        print "Error: Unrar binary " + registry.UNRAR_BINARY + " does not exist or is not executable"
        sys.exit(1)

    files.process(directory)
