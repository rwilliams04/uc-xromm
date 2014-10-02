#!/bin/bash

#specify the time limit for the cron job
#SBATCH --time=5:0:0

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
rsync -vz -e "ssh -i /home/kazutaka/.ssh/id_Ripple_PC" labadmin@128.135.180.217:/cygdrive/c/Data  <path to Midway destination directory>

#Transferring data with compression
rsync -avz -e "ssh -i /home/kazutaka/.ssh/id_Ripple_PC" labadmin@128.135.180.217:/cygdrive/c/Data  <path to Midway destination directory>

#Transferring data without compression
rsync -vz -e "ssh -i /home/kazutaka/.ssh/id_RT_Matlab_PC" labadmin@128.135.180.236:/cygdrive/c/Models  <path to Midway destination directory>

#Transferring data with compression
rsync -avz -e "ssh -i /home/kazutaka/.ssh/id_RT_Matlab_PC" labadmin@128.135.180.236:/cygdrive/c/Models  <path to Midway destination directory>

#Transferring data without compression
rsync -vz -e "ssh -i /home/kazutaka/.ssh/id_Procapture_PC" labadmin@128.135.180.159:/cygdrive/c/Data :/cygdrive/d/Data :/cygdrive/e/Data :/cygdrive/f/Data  <path to Midway destination directory>

#Transferring data with compression
rsync -avz -e "ssh -i /home/kazutaka/.ssh/id_Procapture_PC" labadmin@128.135.180.159:/cygdrive/c/Data :/cygdrive/d/Data :/cygdrive/e/Data :/cygdrive/f/Data  <path to Midway destination directory>


# resubmit this script with --begin set to the next scheduled cron time
# next-cron-time is a script that parses a cron schedule string and returns
# the next execution time
sbatch --quiet --begin=$(next-cron-time "$SCHEDULE") cron_templatersync.sbatch
