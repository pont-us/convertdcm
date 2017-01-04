convert-dcm: collect and convert DCM files
==========================================

`convert-dcm` trawls through a hierarchy of folders looking for files
with the suffix DCM (case insensitive). When it finds one, it converts
it to a JPEG files, gives it a name based on the parent folder, and
puts the JPEG in a specified output folder. Example:

`/some/random/file/path/PID234_banana/1.dcm` ->  
`output_folder/banana.JPG`

If a folder contains more than one DCM file, a suffix based on the
name of the DCM file itself is added. Example:

`/some/random/file/path/PID234_banana/1.dcm` ->  
`output_folder/banana-1.JPG`

`/some/random/file/path/PID234_banana/2.dcm` ->  
`output_folder/banana-2.JPG`

Requirements
------------

convert-dcm requires an installation of Python 3, and the ImageMagick
suite (specifically, the `convert` program from this suite). Both
Python and ImageMagick are widely and freely available for multiple
platforms.

Running `convert-dcm`
---------------------

`convert-dcm` is run from the command line.

`convert-dcm -h` displays help about the program.

`convert-dcm input_folder output_folder` will search `input_folder` for
DCMs and deposit the resulting JPEGs in `output_folder`. It will not
overwrite existing, identically named JPEGs in `output_folder`.

`convert-dcm --overwrite input_folder output_folder` will search
`input_folder` for DCMs and deposit the resulting JPEGs in
`output_folder`. It will overwrite any existing, identically named JPEGs
in `output_folder`.

