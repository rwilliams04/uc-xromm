# Config Steps


## Create authentication key for ssh to globus
On midway generate public/private key pair
    Note: the user submitting the cron-like file transfer script should generate these key pairs.

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

## Submit sbatch script

Submit sbatch script to run as a cron job, which will then execute the nightly transfers.

Modify [`cron_globustemplate.sbatch`](cron_globustemplate.sbatch) with correct keys and paths.

Rename:

    mv cron_globustemplate.sbatch xromm-cron.sbatch

Submit the resulting cron job with `sbatch`:

    sbatch xromm-cron.sbatch


