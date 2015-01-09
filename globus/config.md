# Config Steps


## Install cygwin and globus

On source PCs, install [Cygwin](http://cygwin.com/install.html) with the Openssh and globus packages

During installation select the following two packages on the package selection screen:

    Net -
      **openssh**
      **rsync**
        
After selecting packages, select the option to resolve all dependencies.

    
## Configure `sshd`
    
On source PCs, configure `sshd` for `ssh` usage without an active Cygwin session (these steps assume the `labadmin` account has administrator privileges on each machine):

* Open a Cygwin session

* Enter the command: `ssh-host-config`

* Enter the following responses to the subsequent queries

		"Should privilege separation be used?" : yes
		"Overwrite existing /etc/sshd_config file?" : yes
		"Overwrite existing /etc/sshd_config file?" : yes
		"Should this script attempt to create a new local account 'sshd'?" : yes
		"Do you want to install sshd as a service?" : yes
		"Enter the value of CYGWIN for the daemon" : ntsec

* Start the sshd service with the command : net start sshd
	
A tutorial that includes steps one and two can be found [here](http://www.howtogeek.com/howto/41560/how-to-get-ssh-command-line-access-to-windows-7-using-cygwin)

    
## Setup key pairs
    
On Midway, generate public/private key pair for each source system

Note: the user submitting the cron-like file transfer script should generate these key pairs.

    ssh-keygen -t rsa -b 1024 -C "$(whoami)@$(hostname)-$(date -I)"

Save as ...

    /home/kazutaka/.ssh/id_hostkeyname

Copy each public key to its respective source machine

    ssh-copy-id -i ~/.ssh/id_hostkeyname.pub labadmin@hostname


## Test globus transfer commands

Note: all paths on the PC are written as referenced from `/cygdrive` (ex. `C:\Data` would be `/cygdrive/c/Data`).

> PROVIDE SAMPLE OF GLOBUS COMMAND FOR TESTING


## Submit cron-like job nightly transfers

Modify [`cron_template.sbatch`](cron_template.sbatch) with correct keys and paths.

Rename:

    mv cron_template.sbatch xromm-cron.sbatch

Submit the resulting cron job with `sbatch`:

    sbatch xromm-cron.sbatch

