# btalignment
This computes the 3d pose of cameras and calibration boards.

## Installation
```
pip install git+https://github.com/SheffieldMLtracking/btalignment.git
```


## Usage Examples
```
btalignment ~/beephotos/2024-06-20/CalibTest200624
```
This
- runs the algorithm on the first 6 (bug: why does this only use 5?) photos from each greyscale camera.
- adds points to the images (can check them using btqviewer)
- adds an alignment.json file to each of the btalignment folders (one for each camera).

```
btalignment ~/beephotos/2024-06-20/CalibTest200624 --xval
```
This,
- leaves one observation out of each camera, and does the alignment with the remaining images, and does this once for each greyscale camera (in my case this is 4 times). The output looks like:

The putput shows (1) how many images were accessed, (2) the top table shows how many calibration boards were decoded in each time point for each camera. (3) The bottow table shows the maximum pixel distance error across the code corners, for each camera.

```
$ btalignment ~/Documents/Research/rsync_bee/test/beephotos/2024-06-20/CalibTest200624 --xval
Removing colour cameras from set
In cal/12/02G14695547 found 58 files, used 6 of them.
In cal/14/02G06394393 found 58 files, used 6 of them.
In cal/10/02D49670796 found 58 files, used 6 of them.
In cal/13/02G14695548 found 58 files, used 6 of them.
 
Loading images, and searching for Matrix Code Boards in each.

Number of cameras:      4
Number of time indices: 5
       12-02G1 14-02G0 10-02D4 13-02G1  
    0     1       1       1       1     
    1     1       1       1       1     
    2     1       1       1       1     
    3     1       1       1       1     
    4     1       1       1       1     
          5       5       5       5   

Running Cross-validation

20 observations // 4 Nfolds => 6 step size
Split 1/4.
Split 2/4.
Split 3/4.
Split 4/4.
 Camera     Errors
12-02G146  3.1
14-02G063  3.0
10-02D496  2.0
13-02G146  1.5
```

## Usage
```
usage: btalignment [-h] [--calset CALSET] [--xval] [--after AFTER] [--before BEFORE] [--maxnum MAXNUM] [--keepnoflashpair] [--keepcolour]
                   [--xvalfoldspercamera XVALFOLDSPERCAMERA] [--xvalheldoutcount XVALHELDOUTCOUNT] [--refreshcache] [--threshold THRESHOLD]
                   [--sourcename SOURCENAME]
                   imgpath

Runs the alignment algorithm for the bee-track project. This can either run a cross validation check, or can generate an alignment configuration.

positional arguments:
  imgpath               Path to images (this needs to be to the session folder, e.g. 2024-06-20/CalibTest200624

options:
  -h, --help            show this help message and exit
  --calset CALSET       Name of the calibration set (default = 'cal')
  --xval                Setting this means the algorithm will just do a cross-validation check (and won't write to the config file.
  --after AFTER         Only process images that were created after this time HH:MM:SS
  --before BEFORE       Only process images that were created before this time HH:MM:SS
  --maxnum MAXNUM       Maximum number of photos to include per camera (default = 6)
  --keepnoflashpair     Tool ignores second photo in flash/no-flash pair. This option makes the tool use both.
  --keepcolour          Tool tries to identify the cameras as colour/greyscale and only keeps greyscale. Setting this uses all the cameras
  --xvalfoldspercamera XVALFOLDSPERCAMERA
                        Number of cross-validation folds. Default: set to leave out one item from each camera in turn.
  --xvalheldoutcount XVALHELDOUTCOUNT
                        How many items to hold out each time (default = 1)
  --refreshcache        Whether to refresh the decoding cache
  --threshold THRESHOLD
                        Threshold of score before adding to data
  --sourcename SOURCENAME
                        The name to give this source of labels (default:btretrodetect)
```
