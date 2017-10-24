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

.. figure::  images/ndr_show.png
   :align:   center

6. Annotate with FIJI:

  a. Install onto your system using https://imagej.net/Fiji/Downloads/.

  b. Open FJII, and start a new blank TrakEM2.

  .. figure:: images/new_blank.png
     :align:  center

  c. Navigate to the folder of you image volume, and select "open".

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

  k. A black screen will appear - these are your annotations, don't worry if you can't see them. Save the annotations with cmd+s.

  l. Your annotations are now saved in your "DATA" folder under the name you gave them.

7. To push annotations to the BOSS, edit ``gen_commands.py`` file and input annotation file parameters.

8. Once all inputs are filled out, type ``python3 gen_commands.py`` in terminal.

9. Paste command line output into terminal.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
