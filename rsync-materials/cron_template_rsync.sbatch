#!/bin/bash

#specify the time limit for the cron job
#SBATCH --time=1:0:0

# use cron.log and append to it
#SBATCH --output=cron.log
#SBATCH --open-mode=append

# the account, partition, and qos should not be changed
#SBATCH --account=cron-account
#SBATCH --partition=cron
#SBATCH --qos=cron

# Specify a valid cron string for the schedule
# this is to be submitted everyday at 11:59 PM

SCHEDULE='59 23 * * *'

#Some data are to be transferred with compression, others without.

#Transferring data without compression
rsync -vz -e "ssh -i /home/username/.ssh/id_hostkey1" username@hostname:"path to source files"  "path to destination directory"

#Transferring data with compression
rsync -avz -e "ssh -i /home/username/.ssh/id_hostkey1" username@hostname:"path to source files"  "path to destination directory"

#Transferring data without compression
rsync -vz -e "ssh -i /home/username/.ssh/id_hostkey2" username@hostname:"path to source files"  "path to destination directory"

#Transferring data with compression
rsync -avz -e "ssh -i /home/username/.ssh/id_hostkey2" username@hostname:"path to source files"  "path to destination directory"

#Transferring data without compression
rsync -vz -e "ssh -i /home/username/.ssh/id_hostkey3" username@hostname:"path to source files"  "path to destination directory"

#Transferring data with compression
rsync -avz -e "ssh -i /home/username/.ssh/id_hostkey3" username@hostname:"path to source files"  "path to destination directory"


# resubmit this script with --begin set to the next scheduled cron time
# next-cron-time is a script that parses a cron schedule string and returns
# the next execution time
sbatch --quiet --begin=$(next-cron-time "$SCHEDULE") cron_templatersync.sbatch
