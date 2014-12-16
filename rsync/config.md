## 1. On source PCs, install [Cygwin](http://cygwin.com/install.html) with the Openssh and rsync packages

    A) During installation select the following two packages on the package selection screen:

        Net -
            **openssh**
            **rsync**
            
    B) After selecting packages, select the option to resolve all dependencies
    
## 2.  On source PCs, configure sshd for ssh usage without an active Cygwin session (these steps assume the labadmin account has administrator privileges on each machine):

	A) From the desktop, right click Cygwin and select "Run as administrator" to open a Cygwin session

	B) Enter the command: ssh-host-config

	C) Enter the following responses to the subsequent queries
		"Should privilege separation be used?" : yes
		"Overwrite existing /etc/sshd_config file?" : yes
		"Overwrite existing /etc/sshd_config file?" : yes
		"Should this script attempt to create a new local account 'sshd'?" : yes
		"Do you want to install sshd as a service?" : yes
		"Enter the value of CYGWIN for the daemon" : ntsec
		"Do you want to use a different name?" : no
		"Create new privileged user account 'cyg_server'?" : yes
		"Please enter the password" : <labadmin password>

	D) Start the sshd service with the command : net start sshd
	
	E) Alter sshd_config to prevent premature ssh session timeouts: 
		sed -i 's/#ClientAliveCountMax 3/ClientAliveCountMax 999999999/' /etc/sshd_config 
	
A tutorial that includes steps one and two can be found [here](http://www.howtogeek.com/howto/41560/how-to-get-ssh-command-line-access-to-windows-7-using-cygwin)

    
## 3. On source machines, recursively change permissions on directories that will be transferred

    chmod -R 666 <Data directory>
    
    
## 4. On Midway, generate public/private key pair for each source system

    Note: the user submitting the cron-like file transfer script should generate these key pairs.

    ssh-keygen -t rsa -b 1024 -C "$(whoami)@$(hostname)-$(date -I)"

Save as ...

    /home/kazutaka/.ssh/id_hostkeyname


## 5. Copy each public key to its respective source machine

    ssh-copy-id -i ~/.ssh/id_hostkeyname.pub labadmin@hostname

    
## 6. Test rsync 

    Note: all paths on the PC are written as referenced from /cygdrive 
    ex. C:\Data  ==>  /cygdrive/c/Data

    sample rsync.
    rsync -avz -e "ssh -i /home/kazutaka/.ssh/id_hostkeyname" \
      labadmin@hostname:/cygdrive/c/Data <path to Midway destination directory>


## 7. Submit cron-like job nightly transfers

Modify [`cron_template.sbatch`](cron_template.sbatch) with correct keys and paths.

Rename:

    mv cron_template.sbatch xromm-cron.sbatch

Submit the resulting cron job with `sbatch`:

    sbatch xromm-cron.sbatch

