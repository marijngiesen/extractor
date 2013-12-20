import os
import re
from extractor import registry, archive


def process(directory):
    for root, dirs, files in os.walk(directory):
        if registry.DEBUG: print "Scanning " + root

        filenames = [filename for filename in files if re.search("\.(rar|r\d{2})$", filename) is not None]

        if len(filenames) < 1:
            continue

        files_to_process = remove_archive_span(filenames) + find_unlinked_archive_span_start(filenames)

        current_dir = os.getcwd()
        os.chdir(root)

        status = []
        for filename in files_to_process:
            status.append(archive.extract(filename))

        if not False in status:
            remove(filenames)

        os.chdir(current_dir)


def remove(filenames):
    if registry.DEBUG: print " + removing archive files...",

    for filename in filenames:
        if not registry.DRYRUN:
            os.unlink(filename)
        else:
            print " " * 4 + filename

    if registry.DEBUG: print "done"


def filter_archive_span(filenames):
    return [filename for filename in filenames if re.search("\.(part\d*\d+\.rar|r\d{2})$", filename) is not None]


def find_unlinked_archive_span_start(filenames):
    return [filename for filename in filenames if re.search("\.part0*1\.rar$", filename) is not None]


def remove_archive_span(filenames):
    return [filename for filename in filenames if filename not in filter_archive_span(filenames)]

