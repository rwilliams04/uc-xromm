# Install Notes

Config notes and recommendations for installing an XMA Portal instance on CentOS or Scientific Linux.

---

A VM with at least 4GB memory is recommended.  The `ffmpeg` processing of media files is much faster with 6GB or more of available RAM.

Disk space is dependent on how many studies we need to host/archive in the portal and the size of the data files going comprising each trial.
The portal uses `/tmp` as a "staging area" for many processes.  Kia has 150GB available on her test server, 500GB in deployment.  Apparently `/tmp` cannot be NFS mounted.

Kia recommends allocating 300GB or more for data storage (i.e., movie and data files).  This can be an NFS mounted partition.

## Steps

* install CentOS 6.5 (or Scientific Linux)
* disable SELinux and ipv6
* add [EPEL yum repository](https://fedoraproject.org/wiki/EPEL)
* install [portal dependencies](rpms.md)
* install additional `ffmpeg` dependencies (described below)
* configure mysql and repository storage directory (described below)


## FFMPEG

Kia suggests installing a specific version of [`ffmpeg`](https://brownbox.brown.edu/download.php?hash=7fbbba96).

   FFMPEG=/usr/local/bin/ffmpeg_20130909
   mkdir $FFMPEG
   tar xfz ffmpeg.static.64bit.2013-09-09.tar.gz -C $FFMPEG

The [`ffmpeg2theora`](http://v2v.cc/~j/ffmpeg2theora/download.html) binary is also needed:

    chmod +x ffmpeg2theora-0.29.linux64.bin
    sudo install -m 755 ffmpeg2theora-0.29.linux64.bin /usr/local/bin/ffmpeg2theora


## MySQL

In `/etc/my.cnf` add:

    skip-networking
    local-infile=0
    query_cache_size = 32M
    query_cache_type = 1

As MySQL root, create database `UCHICAGO`:

    create database UCHICAGO;

Give access to `admin`:

    grant all privileges on UCHICAGO.\* to 'admin'@'%';


## File Storage

Data and movie files associated with XROMM studies will be persisted in `/repo/uchicago` (or anywhere not under apache document root).

Give user `apache.apache` ownership to `/repo/uchicago`:

    chown -R apache.apache /repo/uchicago

