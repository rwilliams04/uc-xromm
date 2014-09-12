## 1. Generate public/private key pair

    ssh-keygen -t rsa -b 1024 -C "$(whoami)@$(hostname)-$(date -I)"

Save as ...

    ~/.ssh/id_hostkeyname


## 2. Copy public key to local machine

    ssh-copy-id -i ~/.ssh/id_hostkeyname.pub username@hostname


## 3. Test rsync

    rsync -avz -e "ssh -i /home/user/.ssh/id_hostkeyname" \
      username@hostname:<path to files> <path to destination directory>


## 4. Submit cron-like job nightly transfers

Modify [`cron_template.sbatch`](cron_template.sbatch) with correct keys and paths.

Rename:

    mv cron_template.sbatch xromm-cron.sbatch

Submit the resulting cron job with `sbatch`:

    sbatch xromm-cron.sbatch

