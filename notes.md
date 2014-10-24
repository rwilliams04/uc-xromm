# Notes

The RCC will be hosting a testbed instance of the XMA Portal at `xromm.rcc.uchicago.edu`.  Kia will be accessing the testbed via `ssh` from IP address range `128.148.*` (`*.brown.edu`).

The XMA Portal source files are currently available in `xromm.rcc.uchicago.edu:/home/jvoigt/xma-portal-source`, which should be accessible to all RCC staff. That’s actually a clone of Kia's bitbucket repo, so we can pull/update the source if Kia makes any changes.

The source is also available via [a private repo](https://github.com/rcc-uchicago/xma-portal).  Contact [@joyrexus](https://github.com/joyrexus) for access.


## Storing XROMM experiments

A few thoughts on the file organization for XROMM experiments on Midway
(`project/rossc/lab/experiments`).

The basic units of organization in the XMA Portal are **studies** and **trials**.  A
study (i.e., experiment) consists of one or more trials (i.e., series of
recorded observations).  A trial can be thought of as a particular "session" in the experiment.  Any given trial can consist of one or more files.

The directory layout for the Lab's dedicated project space for storing
experimental files should reflect this hierarchy by having uniquely named
subdirectories for each study, each containing uniquely named subdirectories
for each trial.
