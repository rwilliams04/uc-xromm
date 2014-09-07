# rsync checklist


## What are the source systems?

Specify the various hosts containing files to be transferred.

* `hostname.uchicago.edu`
* `hostname.uchicago.edu`
* `hostname.uchicago.edu`


## What are the different media types being transferred?


## What are the file sizes and approximate size of the total nightly transfer?


## What is the network capacity?


## Should the files be transferred with compression?


## Where are the files to be transferred located?

Specify the source paths on each system.


## Where are they being transferred to?


## What should the resulting directory layout look like on the target system?


## How frequently should transfers occur?

We're assuming nightly.


## Should the files be deleted after a transfer?

We're assuming that they shouldn't be deleted after a transfer.


## Under what username should the transfer occur?


## Are there any log files or manifests containing meta-data to be parsed?


## Can we add the `ws` user to the `rossc` group in order to have read/write permissions?


## Would it be easier to do a push or a pull transfer?

We're assuming a pull transfer triggered from Midway would be easier.
