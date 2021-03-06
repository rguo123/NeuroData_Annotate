.. NeuroData Annotation documentation master file, created by
   sphinx-quickstart on Sun Oct 15 23:15:51 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to NeuroData Annotate's documentation!
================================================

1. Clone annotation repo. In Terminal type:
    ``git clone https://github.com/rguo123/NeuroData_Annotate.git``

2. Install dependences by typing: ``pip3 install -r requirements.txt``

3. Get BOSS API token by logging in to https://api.boss.neurodata.io/. Note: You need resource manager permissions to upload data to the BOSS.

4. Create ``neurodata.cfg`` file and insert BOSS token as shown below:

  .. code-block:: bash
     :emphasize-lines: 4

     [Default]
     protocol = https
     host = api.boss.neurodata.io
     token = INSERT TOKEN HERE

  .. toctree::
     :maxdepth: 2
     :caption: Contents:

5. Pull data from BOSS by typing ``python3 NeuroDataResource.py`` in terminal and following the input prompt.

.. figure::  images/ndr_input.png
   :align:   center

   a. This saves your data in a specific directory structure. In this example, we would see:

.. figure:: images/directories.png
   :align: center

6. Annotate with FIJI:

  a. Install onto your system using https://imagej.net/Fiji/Downloads/.

  b. Open FJII, and start a new blank TrakEM2.

  .. figure:: images/new_blank.png
     :align:  center

  c. Navigate to the folder of your image volume and select "open".

  d. This should have changed your ImageJ canvas. Now, drag your volume (helloworld.tif) from your folder into the canvas.

  e. In the popup window, make sure that "Resize canvas to fit stack" is checked. After clicking OK, your canvas should snap to your image.

  f. In your TrakEM2 properties, right click on "anything" in the template column and add a new "area_list".

  .. figure:: images/new_area_list.png
     :align: center

  g. Drag the entire "anything" folder into "Unitled 0" in the middle column.

  h. Right click the nested "anything" folder inside "Untitled 0" and add a "new area list".

  .. figure:: images/final_area_list.png
     :align: center

  i. Annotate Your Data by drawing all over it. You can scroll to annotate different slices in your tif.

  j. When done, right click your canvas and select "Export" -> "Arealists as labels (tif)".

  NOTE: At any point, you can export your annotations as an xml by the same method listed above. Opening the xml file will start you where you left off.

  k. A black screen will appear - these are your annotations, don't worry if you can't see them.

  l. Save your annotations in the correct directory *with the same name*, an example given below.

  .. figure:: images/annotation_file.png
      :align: center

7. To push annotations to the BOSS, run ``gen_commands.py``.

8. Paste command line output into terminal. If this doesn't work, you will probably have to change some parameters in ``gen_commands.py``. Below is a list of all parameters:

Parameters
~~~~~~~~~~
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameters       | Description                             | Required    | Tips and Examples                                                                                                                                       |
+==================+=========================================+=============+=========================================================================================================================================================+
| script           |  Path to ingest_large_vol.py script     |  Yes        |  Should not have to change.                                                                                                                             |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| source_type      |  Where the data is being ingested from  |  Yes        |  Either ``s3`` or ``local``.                                                                                                                            |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| s3_bucket_name   |  AWS S3 Bucket name                     |  No         |  Only specify if source_type is ``s3``                                                                                                                  |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| aws_profile      |  AWS Profile                            |  No         |  Only specify if source_type is ``s3``. `AWS Profile Help <http://docs.aws.amazon.com/cli/latest/userguide/cli-multiple-profiles.html>`_                |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| boss_config_file |  Path and filename of BOSS API token    |  Yes        |  Should not have to change.                                                                                                                             |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| slack_token      |  Slack API token                        |  No         |  Use if you want slack notifiction once ingest is finished.                                                                                             |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| slack_username   |  Slack username                         |  No         |  Use if you want slack notification once ingest is finished.                                                                                            |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| collection       |  BOSS collection name                   |  Yes        |  You need permission for existing BOSS collections. Specifying a collection not in the BOSS will create a new collection (again, need permissions).     |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| experiment       |  BOSS experiment name                   |  Yes        |  See ``collection`` input.                                                                                                                              |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| channel          |  BOSS channel name                      |  Yes        |  See ``collection`` input.                                                                                                                              |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| data_directory   |  Directory data is stored in            |  Yes        |  Format: ``Path/To/Data/``                                                                                                                              |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| file_name        |  Filename of data without file extension|  Yes        |  Can specify which z slices you want for tif files. Example: TODO.                                                                                      |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| file_format      |  Extension of data file                 |  Yes        |  Example: ``tif``, ``png``.                                                                                                                             |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| z_step           |  Increment of filename numbering        |  Yes        |  Typically keep at 1.                                                                                                                                   |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| voxel_size       |  Physical dimensions of each voxel      |  Yes        |  Typically keep at ``1 1 1``. This just determines some BOSS metadata mostly.                                                                           |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| voxel_unit       |  Physical unit for voxel size           |  Yes        |  Options: nanometers, micrometers, millimeters, centimeters.                                                                                            |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| data_type        |  Data type of image                     |  Yes        |  ``uint8`` or ``uint16`` for data, ``uint64`` for annotations. Bug: Have to specify in ``ingest_large_vol.py`` the datatype as well.                    |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| data_dimensions  |  X, Y, Z, dimensions of data            |  Yes        |  Format: X Y Z (e.g. ``1280 720 5``).                                                                                                                   |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| z_range          |  List of z slices to ingest             |  Yes        |  First inclusive, last exclusive (e.g. ``[0, 5]``).                                                                                                     |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| workers          |  Number of workers to use               |  Yes        |  Potential memory errors.                                                                                                                               |
+------------------+-----------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+


Dockered Approach!
================================================
1. Install Docker by following instructions here: `Docker Installation <https://docs.docker.com/engine/installation/>`_

2. In terminal, type the following command:
``docker pull rguo123/nddannotate``

3. Start NeuroData_Annotate Container by typing in terminal
``docker run -it rguo123/annotate``.

4. You should now be in the docker container's bash shell.

5. Use the above instructions to pull data with NeuroData Resource.

6. To copy data out of the container, use the following command:
``docker cp CONTAINER:SRC_Path DEST_Path``.
Use this to copy your BOSS data onto your computer.

7. Annotate the data following the Fiji instructions above.

8. Copy annotations back into docker container when you are ready with the command
``docker cp SOURCE_PATH CONTAINER:Dest_Path``

9. Reenter your container with the command
``docker exec -it container_id /bin/bash"``

10. Run ingest_large_vol commands to successfully push your data to the BOSS.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
