#!/usr/bin/env python

import shlex

""" Script to generate ingest commands for ingest program """
""" Once generated, copy commands to terminal and run them """

""" Recommend copy this to a new location for editing """


script = "ingest_large_vol.py"

source_type = 'local'  # either 'local' or 's3'
s3_bucket_name = "BUCKET_NAME"  # not used for 'local' source_type
aws_profile = "default"  # not used for 'local' source_type

boss_config_file = "neurodata.cfg"  # location on local system for boss API key

# Slack messages (optional)
# sends a slack message when ingest is finished with a link to the see the data
# set to a blank string (e.g. '') to exclude from command output
slack_token = ""  # Slack token for sending Slack messages
slack_username = ""  # your slack username

# boss metadata
collection = 'Look_At_It'
experiment = 'EXP1'
channel = 'test'

# data_directory _with_ trailing slash (doesn't output correct paths on Windows)
data_directory = "DATA/"

# filename without extension (no '.tif')
# <p:4> indicates the z index of the tif file, with up to 4 leading zeros
file_name = "lookatit"

# extension name for images, supported image types are PNG and TIFF
# extension just needs to match the filename and can be any string (e.g.: ome, tif, png)
file_format = 'tif'

# increment of filename numbering (always increment in steps of 1 in the boss, typically will be '1')
z_step = '1'

# float or int supported
voxel_size = '1 1 1'

# nanometers/micrometers/millimeters/centimeters
voxel_unit = 'micrometers'

# uint8 or uint16 for image channels, uint64 for annotations
data_type = 'uint8'

# pixel extent for images in x, y and number of total z slices
data_dimensions = "1280 720 3"

# first inclusive, last _exclusive_ list of sections to ingest
# integers, typically the same as ZZZZ "data_dimensions"
zrange = [0, 3]

# Number of workers to use
# each worker loads additional 16 image files so watch out for out of memory errors
workers = 1


""" Code to generate the commands """


def gen_comm(zstart, zend):
    cmd = "python3 " + script + " "
    cmd += ' --base_path ' + shlex.quote(data_directory)
    cmd += ' --base_filename ' + shlex.quote(file_name)
    cmd += ' --extension ' + file_format
    cmd += ' --datasource ' + source_type
    cmd += ' --collection ' + collection
    cmd += ' --experiment ' + experiment
    cmd += ' --channel ' + channel
    cmd += ' --voxel_size ' + voxel_size
    cmd += ' --voxel_unit ' + voxel_unit
    cmd += ' --datatype ' + data_type
    cmd += ' --img_size ' + data_dimensions
    cmd += ' --z_range %d %d ' % (zstart, zend)
    cmd += ' --z_step ' + z_step
    cmd += ' --warn_missing_files'
    cmd += ' --boss_config_file ' + boss_config_file

    if slack_token != '' and slack_username != '':
        cmd += ' --slack_token_file ' + slack_token
        cmd += " --slack_usr " + slack_username

    if source_type == 's3':
        cmd += " --s3_bucket_name " + s3_bucket_name
        cmd += ' --aws_profile ' + aws_profile
    cmd += " &"

    return cmd


range_per_worker = (zrange[1] - zrange[0]) // workers

print("# Range per worker: ", range_per_worker)

if range_per_worker % 16:  # supercuboids are 16 z slices
    range_per_worker = ((range_per_worker // 16) + 1) * 16

print("# Range per worker (rounded up): ", range_per_worker)

# amount of memory per worker
ddim_xy = list(map(int, data_dimensions.split(' ')[0:2]))
if data_type == 'uint8':
    mult = 1
elif data_type == 'uint16':
    mult = 2
elif data_type == 'uint64':
    mult = 8
mem_per_w = ddim_xy[0] * ddim_xy[1] * mult * 16 / 1024 / 1024 / 1024
print('# Expected memory usage per worker {:.1f} GB'.format(mem_per_w))

# amount of memory total
mem_tot = mem_per_w * workers
print('# Expected total memory usage: {:.1f} GB'.format(mem_tot))


cmd = gen_comm(zrange[0], zrange[1])
cmd += ' --create_resources '
print('\n' + cmd + '\n')

for worker in range(workers):
    start_z = max((worker * range_per_worker +
                   zrange[0]) // 16 * 16, zrange[0])
    if start_z < zrange[0]:
        start_z = zrange[0]
    if start_z > zrange[1]:
        # No point start a useless thread
        continue

    next_z = ((worker + 1) * range_per_worker + zrange[0]) // 16 * 16
    end_z = min(zrange[1], next_z)

    cmd = gen_comm(start_z, end_z)
    print(cmd)
