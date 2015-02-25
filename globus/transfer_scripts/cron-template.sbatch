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

sbatch globus_ripple.sbatch
sbatch globus_procaptureCaptures.sbatch
sbatch globus_procaptureE.sbatch
sbatch globus_procaptureF.sbatch
sbatch globus_procaptureG.sbatch
sbatch globus_procaptureH.sbatch

# the next execution time
sbatch --quiet --begin=$(next-cron-time "$SCHEDULE") cron-template.sbatch
