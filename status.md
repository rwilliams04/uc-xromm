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
