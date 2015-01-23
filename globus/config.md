# Config Steps


## Create authentication key for ssh to globus
On midway generate public/private key pair
    Note: the user submitting the cron-like file transfer script should generate this key pair.

    ssh-keygen -t rsa -b 1024 -C "$(whoami)@$(hostname)-$(date -I)"

Save as ...

    /home/kazutaka/.ssh/id_hostkeyname

Go to public key file and copy key to clipboard

Go to Globus.org and sign in
Go to Manage Identities
	add linked identity
	add ssh public key
	paste public key and submit

## Download Globus Connect Personal
On Globus.org go to Manage Endpoints	
Select add Globus Connect Personal
Enter Endpoint name for PC
Download and install Windows version

## Installation
During installation select folder(s) to be accessible by Globus
Select option to make directory sharable
Select option to have Globus start up when Windows starts

## Sharing
On Globus.org go to Manage Endpoints
Expand menu for the new endpoint and click the Sharing tab
Create shared endpoint
Enter in path of folder to share (ex. /C/Data)
Select Globus users/groups to share the endpoint with

## Permissions
On Midway execute the following on the top-level destination directory 
so that all files transferred to it inherit read and write permissions for the pi-rossc group

    setfacl -Rdm g:pi-rossc:rw /project/rossc/Orofacial/BiteForce/Data
	
## Submit sbatch script

Submit sbatch script to run as a cron job, which will then execute the nightly transfers.

Modify [`cron-template.sbatch`](cron-template.sbatch) with correct keys and paths. 

Change the last line of the script to include the name of the modified script (ie):

    sbatch --quiet --begin=$(next-cron-time "$SCHEDULE") cron-template.sbatch
    =>
    sbatch --quiet --begin=$(next-cron-time "$SCHEDULE") xromm-cron.sbatch

Rename:

    mv cron-template.sbatch xromm-cron.sbatch

Submit the resulting cron job with `sbatch`:

    sbatch xromm-cron.sbatch


