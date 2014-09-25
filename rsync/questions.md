# Transfer setup questions


## What are the source systems?

The various hosts containing files to be transferred:

* Ripple PC (`128.135.180.217`)
* RT Matlab PC (`128.135.180.236`)
* Procapture PC (`128.135.180.159`)


## What are the different media types being transferred?

#### Ripple

* `.nev` - event files
* `.ns5` - neural recording file sampled at 30kHz
* `.stim` - stimulation parameter files (optional)
* `.xfg` - configuration file

#### Procapture 

* `<Data>_<Time>_Evtxx` - project directory containing ...
  * `.mpj` - project files
  * `Evt#` -  sub dir for each camera (will be most likely only 2 or 3 depending on whether we use simple C arm or XROMM) containing ...
    * `.avi` - video files
    * `.cfg` - configuration files
    * `.au2` - data files

#### RT Matlab

* `.mat` - mat files containing behavioral variables
* `.slx` - Simulink model used to run to control multiple devices and behaviors for animals
* `.txt` - some analog signal readout from DAQ (optional)


## What are the file sizes and approximate size of the total nightly transfer?

> We are expecting somewhere between 500GB to 1TB


## What is the network capacity?

> Will be 3 or 4 1GB ethernet 


## Should the files be transferred with compression?

> We will discuss this, but depending on the transfer speed. Prefer not to.


## Where are the files to be transferred located?

Source paths on each system:

#### Ripple

    C:/Data/Date 

#### Procapture

    C:/Data/<Data>_<Time>_Evtxx
    D:/Data/<Data>_<Time>_Evtxx
    E:/Data/<Data>_<Time>_Evtxx
    F:/Data/<Data>_<Time>_Evtxx

#### RT Matlab 

    C:/Models/


## Where are they being transferred to?

`midway.rcc.uchicago.edu:/project/rossc/lab/experiments/`


## What should the resulting directory layout look like on the target system?

> We would like to maintain the directory structure from each source 


## How frequently should transfers occur?

> We're assuming nightly on weekdays 


## Should the files be deleted after a transfer?

We're assuming that they shouldn't be deleted after a transfer.

> I think we need to delete once batch processes start on Midway, especially image data (as we only have 2 TB disks on the machine), so we might need to have a script to flag the completion of file transfers and parsing of necessary information for meta data and initial batch processes to each PC to delete files. 


## Under what username should the transfer occur?

> Rsync transfers will occur through cron-like sbatch jobs submitted under the username kazutaka.


## Are there any log files or manifests containing meta-data to be parsed?

> Yes, but not all the details are determined. Most likely all go into .txt or .mat files and .cfg and .xfg files. 


## Can we add the `ws` user to the `rossc` group in order to have read/write permissions?

We need to ensure that a restricted but generic user has at least read access
to the relevant files post-transfer.

> Yes 


## Would it be easier to do a push or a pull transfer?

We're assuming a pull transfer triggered from Midway would be easier.

> Definitely. 


## Where are the config files located?

Useful to know if they need to be revised.

* rsync scripts?
* cron config?
* ssh public keys?

> We can create those files at a convenient location for each machine. 
