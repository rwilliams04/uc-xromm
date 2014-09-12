## Step 1. (Generate public/private key pair)

A)
```
ssh-keygen -t rsa -b 1024 -C "$(whoami)@$(hostname)-$(date -I)"
```

B)
save as key as
~/.ssh/id_hostkeyname

## Step 2. (Copy public key to local machine)

ex.
```
ssh-copy-id -i ~/.ssh/id_hostkeyname.pub username@hostname
```

## Step 3. (Test rsync) 

ex.
```
rsync -avz -e "ssh -i /home/user/.ssh/id_hostkeyname" username@hostname:"path to files" "path to destination directory"
```

## Step 4. (Submit cron-like job nightly transfers)
A)
Modify cron_template_rsync.sbatch file for correct keys and paths

B)
Submit cron_template_rsync.sbatch:

```
sbatch cron_template.sbatch
```


