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


SSH_PREFIX="ssh -i /home/$(whoami)/.ssh"       # prefix to globus ssh key
ROSS_EXP=/project/rossc/Orofacial/BiteForce/Data     # top-level destination directory
GLOBUS_USERNAME=kazutaka         #Globus account username

#Use endpoint-activate to refresh credentials for all endpoints
$SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org endpoint-activate kazutaka#Ripple_dataFiles
$SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org endpoint-activate kazutaka#procapture_Captures
$SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org endpoint-activate kazutaka#procapture_E
$SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org endpoint-activate kazutaka#procapture_F
$SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org endpoint-activate kazutaka#procapture_G
$SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org endpoint-activate kazutaka#procapture_H


#Initiate transfers for each endpoint.  A check of the source and destination directories is made (checksum) 
#and only files that are not identical to the source directory are transferred to the destination directory

echo "kazutaka#Ripple_dataFiles/ ucrcc#midway${ROSS_EXP}/<...>/ -r" | $SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org transfer -s 3

echo "kazutaka#procapture_Captures/ ucrcc#midway${ROSS_EXP}/<...>/ -r" | $SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org transfer -s 3

echo "kazutaka#procapture_E/ ucrcc#midway${ROSS_EXP}/<...>/ -r" | $SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org transfer -s 3

echo "kazutaka#procapture_F/ ucrcc#midway${ROSS_EXP}/<...>/ -r" | $SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org transfer -s 3

echo "kazutaka#procapture_G/ ucrcc#midway${ROSS_EXP}/<...>/ -r" | $SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org transfer -s 3

echo "kazutaka#procapture_H/ ucrcc#midway${ROSS_EXP}/<...>/ -r" | $SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org transfer -s 3

# resubmit this script with --begin set to the next scheduled cron time
# next-cron-time is a script that parses a cron schedule string and returns
# the next execution time
sbatch --quiet --begin=$(next-cron-time "$SCHEDULE") cron-template.sbatch
