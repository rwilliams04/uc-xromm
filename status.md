# Status

See list of [open issues](https://github.com/rcc-uchicago/uc-xromm/issues) for status on particular issues.


---


## 2014-09-25 

The [UChicago instance](http://xromm.rcc.uchicago.edu) of the XMA Portal is now up and running.  File downloads from a provisional data directory are currently being tested.


## 2014-09-20 

After testing rsync config, Taka is going to create some sample data that will be similar to a normal recording day, then check the file sizes, speed, and etc. 


## 2014-09-14 

Taka (`kazutaka`) was added to the `cron-account` group in order to submit
"cron-like" jobs via slurm, viz. to run the nightly rsync transfers.

Daily transfers may sometimes take > 1 hour to complete, so the cron qos was
upped to allow for jobs running up to 5 hours.


## 2014-09-11 

Richard met with Ross Lab to consult on initial rsync setup.  Details
[here](https://github.com/rcc-uchicago/uc-xromm/issues/3).

Note that Taka is currently unable to test the rsync config because all of the XROMM-related systems are now offline. Taka writes ...

> We had to move all the devices that will be in XROMM setup to a room
without any internet connection, and we don't know when we can bring them
back to a room with at least 3 ethernet connections, so most likely I won't
be able to test the rsync in the upcoming week.


## 2014-08-13 

In meeting with the Ross Lab yesterday, we confirmed that there will be
multiple source systems on which experimental data will be generated.  Instead of consolidating the various data files on a system within the Lab, we'll work
towards automating transfers to a dedicated directory in `/project/rossc`.  (Note that Andy now has `/project/rossc` mounted on the VM.) The overall file layout has yet to be determined, but Taka seems to have a rough idea of how it should look.

We [made plans](https://github.com/rcc-uchicago/uc-xromm/issues/3) with Taka to meet after Labor day to work on setting up the transfer scripts.  The current plan is to use cron-triggered rsync jobs.  Then, post-transfer we'll need to parse [a manifest file](https://github.com/rcc-uchicago/uc-xromm/blob/master/packaging.md#studyjson) (included with each package of trial data getting transferred) and use that to automagically add new records to the portal's backend database.  

As we learned in prior meetings, when submitting to Brown’s existing XMA portal, they currently have to go through a cumbersome one-by-one file upload process and manually input the meta-data associated with each file.  They’d of course like to avoid that altogether.

There was also mention of the need for a database dedicated to logging
experimental runs in a manner similar to the XMA Portal, but with additional
Lab-specific details.  This would be for internal use only.  Taka indicated
that he could provide schema details in the coming weeks.

Lastly, earlier today Kia provided access to the portal source files and backend database schema.  Kia's CNet account is now active, so she can login to the VM and assist with initial setup and configuration.


## 2014-08-05 

We have a dedicated VM for hosting the XMA Portal at `xromm.rcc.uchicago.edu`.

Kia provided a list of dependencies for the portal and some have been installed
on the VM, but our SysAdmin wants to review the portal's source files before
proceeding (to see if all of the listed dependencies are needed?).

Kia informed us that she needs to add copyright and legalese to the source files before she can make them available.


## 2014-07-24

The RCC team met with Kia via Skype on 2014-07-24.  Kia provided an overview of the Portal's trial creation and file upload workflow via the web interface.  

We decided it would be easiest to host a local copy of the XMA Portal for
experimentation and potentially customize for the particular needs of the Ross Lab. The plan is to setup a dedicated VM for the portal.

The XMA portal is built on a basic LAMP stack.  Kia is going to provide Robin with specific dependencies and Robin is going to talk to Andy about setting up the VM.

Kia is going to send Jason the database schema so we can understand the basic
table structure and overall organization of the portal's backend storage
layer.

Having local control over the environment will allow us to experiment with
alternative methods for submitting trial data.


## 2014-07-22 

Kia created accounts for Robin and Jason in the [sandbox portal](http://xmaportal.org/sandbox) (a clone of the XMA portal used for testing purposes).  Robin and Jason were both made members of the `ross` group and Jason was anointed **LabAdmin** for this group.

Note that LabAdmins have the same privileges as the PI, entitling them to
create new studies and modify permissions.

Kia created a new study named [`UChicago Test Study`](http://xmaportal.org/sandbox/larequest.php?request=exploreStudy&StudyID=45&instit=SANDBOX1) for us, with Jason listed as **Study Leader**.  Robin has view access.
