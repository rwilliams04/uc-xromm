# XMA Portal

Kia Huffman is the admin for the [XMA Portal](http://xmaportal.org/) at Brown.
The portal allows users to "publish" and share their x-ray motion analysis data
(i.e., the trial data generated in the course of experimental studies).

The XMA Portal at Brown is one instance of an XROMM data **repository**.

Each repository contains a number of **studies**. Each study is associated with one or more PIs (Principal Investigator) and a **Study Leader** (usually a grad student or postdoc coordinating the experiments).  Each study is in turn comprised of a number of **trials**.  A trial contains references to the uploaded raw data files (calibration and video files) associated with the given trial and other relevant metadata.

At least the initial incarnation of the portal was hosted at Brown's Brainerd
research lab.  They had 24TB available for file storage.  The portal was backed
by a MySQL database.  PHP was used to develop the web frontend.  The portal frontend enables users to create studies, upload trial data, and associate metadata with the uploaded files.


## Questions

* What metadata is needed when creating a new ...
  * study?
  * trial?

* What raw data is typically included as part of a trial?

* Can we devise an API for programmatically ...
  * submitting study and/or trial metdata?
  * transferring the raw data files?


## Known Issues

Kia noted ...

> Right now the biggest issue is (from what I gathered talking to Callum), that **his data collection workflow will not work smoothly with our current portal file upload mechanism.** So we need to find a solution that fits his data collection workflow better, right now I do not have any good solution.  

> The XMA Portal solves many fundamental problems by integrating essential
calibration files and metadata linked to the raw video data, however **accessing XROMM data for analysis remains a bottleneck in the workflow.** The XMA Portal could potentially take over these preparation tasks (on a local server), delivering a package of video data, metadata, and calibration images to the analysis platform, and then receiving processed data and information about the analysis process (i.e. provenance) and cataloging them back into the database. 
