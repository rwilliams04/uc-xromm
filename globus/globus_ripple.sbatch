#!/bin/bash
# use globus_ripple.log and append to it
#SBATCH --output=globus_ripple.log
#SBATCH --open-mode=append

#account=pi-rossc

SSH_PREFIX="ssh -i /home/$(whoami)/.ssh"       # prefix to globus ssh key
ROSS_EXP=/project/rcc/rwilliams/XROMM/globustest0216     # top-level destination directory
GLOBUS_USERNAME=rwilliams
HOST_ENDPOINT=kazutaka#Ripple_dataFiles #name of globus endpoint
HOST_IP="128.135.180.217"
LOGFILE=globus_ripple.log

#Use endpoint-activate to refresh credentials for all endpoints
$SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org endpoint-activate ucrcc#midway
wait
$SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org endpoint-activate ${HOST_ENDPOINT}

#Initiate transfers for endpoint.  
#A check of the source and destination directories is made (checksum) 
#and only files that are not identical to the source directory 
#are transferred to the destination directory
taskline=$(echo "${HOST_ENDPOINT}/ ucrcc#midway${ROSS_EXP}/Neural/ -r" | $SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org transfer -s 3 | tee -a $LOGFILE)
taskID=$(echo $taskline | awk '{print $3}')


#########
#Uncomment the following code to enable deletion of source files after successful transfer
#########

##Ping host machine. If ping is successful (status = 0), wait for the transfer to finish,
##then get the status of the transfer.
##If the status of the transfer is 'SUCCEEDED', then delete contents of source directory
#ping $HOST_IP -w 3
#if [ $? -eq 0 ]
#  then $SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org wait -q $taskID
#  transfer_status=$($SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org status $taskID -f status | awk '{print $2}')
#  if [ $transfer_status == 'SUCCEEDED' ]
#    then echo "${HOST_ENDPOINT}/*" | $SSH_PREFIX/id_globus $GLOBUS_USERNAME@cli.globusonline.org delete -r
#  fi
#fi
