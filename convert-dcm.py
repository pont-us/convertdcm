#!/usr/bin/env python3

"""
Walk a directory tree, converting any DCM files to JPEGs and collecting
them in a single output directory. Each output file is named according
to the name of the parent directory of the input file.

Requires the "convert" utility from the ImageMagick software
suite to perform the conversion.

By Pontus Lurcock, 2016 (pont -at- talvi.net).
Released into the public domain.
"""

import os
import os.path
import argparse
import subprocess
import re

def main():
    parser = argparse.ArgumentParser(description="Convert and collect DCM files")
    parser.add_argument("--overwrite", "-o", help="overwrite existing files",
                        action="store_true", default=False)
    parser.add_argument("source_dir", metavar="source-dir", type=str, nargs=1,
                      help="Directory to search for DCM files")
    parser.add_argument("dest_dir", metavar="dest-dir", type=str, nargs=1,
                      help="Output directory (must exist)")
    args = parser.parse_args()

    for x in os.walk(args.source_dir[0]):
        dirpath, dirnames, filenames = x
        dcim_files = [f for f in filenames if f.lower().endswith(".dcm")]
        use_suffix = ( len(dcim_files) > 1 )
        for filename in filenames:
            lcase = filename.lower()
            if lcase.endswith(".dcm"):
                dcim = os.path.join(dirpath, filename)
                dcim_parent = os.path.basename(dirpath)
                core_id = re.sub(r"PID..._", "", dcim_parent)
                outfile = os.path.join(args.dest_dir[0], core_id)
                if (use_suffix):
                    outfile += "-" + filename[:-4]
                outfile += ".JPG"
                print(dcim_parent+"/"+filename + " -> " + outfile)
                if (not os.path.exists(outfile)) or args.overwrite:
                    subprocess.call(["convert", dcim, "-quality", "95", outfile])
                else:
                    print("Not overwriting "+outfile)

if __name__ == "__main__":
    main()
