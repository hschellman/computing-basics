---
title: Mission Setup
teaching: 60
exercises: 20
questions:
- How do I prepare for the DUNE computing tutorial?
objectives:  
- Get ready to do the tutorial
- Understand the authentication process
- Set up your computing environment for DUNE
- Set up grid access and job submission
keypoints:
- Kerberos is FNAL’s method for ensuring strong authentication to its computing resources
- Computing resources at FNAL are accessed using the Secure SHell protocol
- Specific computer nodes are accessed by DUNE users
- Access is streamlined using configuration files
- CERN users configure and access CERN resources instead
---
## Objectives

- Get ready to do the tutorial
- Understand the authentication procedures
- Set up your environment for DUNE
- Do an exercise to help us check if all is good
- Get streaming and grid access

## Requirements


You must be on the DUNE Collaboration member list and have a valid FNAL or CERN account. <!-- See the old [Indico Requirement page][indico-event-requirements] for more information.-->

You should join the DUNE Slack instance and look in #computing-training-basics (see Mission Setup below)  for help with this tutorial

Windows users are invited to review the [Windows Setup page]({{ site.baseurl }}/Windows.html).

## Step 1: DUNE membership

To follow most of this training, you must be on the DUNE Collaboration member list. If you are not, talk to your supervisor or representative to get on it.

>### Note: Other experiments may find the setup and first few modules useful.
> The first few modules on access and disk spaces should work for other Fermilab experiments if you substitute `dune --> other`. 
{: .callout}

## Step 2: Getting accounts

### With FNAL
If you have a valid FNAL computing account with DUNE, go to step 3.

If you have a valid FNAL computing account but not on DUNE yet (say you have access to another experiment's resources), you can ask for a DUNE-specific account using the Service Now [Update my Affiliation/Experiment/Collaboration membership Request](https://fermi.servicenowservices.com/nav_to.do?uri=%2Fcom.glideapp.servicecatalog_cat_item_view.do%3Fv%3D1%26sysparm_id%3D9a35be8d1b42a550746aa82fe54bcb6f%26sysparm_link_parent%3Da5a8218af15014008638c2db58a72314%26sysparm_catalog%3De0d08b13c3330100c8b837659bba8fb4%26sysparm_catalog_view%3Dcatalog_default%26sysparm_view%3Dcatalog_default) form. 

If you do not have any FNAL accounts yet, you need to contact  your supervisor and/or Institutional Board representative to obtain a Fermilab User Account. More info: [https://get-connected.fnal.gov/users/access/](https://get-connected.fnal.gov/users/access/).  This can take several weeks the first time. 

### With CERN
If you have a valid CERN account and access to CERN machines, you will be able to do many of the exercises as some data is available at CERN. The LArSoft tutorial has been designed to work from CERN. We strongly advise pursuing the FNAL computing account though.

If you have trouble getting access, please reach out to the training team several days ahead of time.  Some issues take some time to resolve.  Please do not put this off.  We cannot help you the day of the tutorial as we are busy doing the tutorial.  

## Step 3: Mission setup (rest of this page)

We ask that you have completed the setup work to verify your access to the DUNE servers. It is not complicated, and should take 10 - 20 min.

If you are not familiar with Unix shell commands, here is a tutorial you can do on your own to be ready: [The Unix Shell](https://swcarpentry.github.io/shell-novice/)

If you have any questions, contact us at `dune-computing-training@fnal.gov` or on DUNE Slack `#computing_training_basics`.


You should join the DUNE Slack instance and look in [#computing-training-basics](https://dunescience.slack.com/archives/C02TJDHUQPR) for help with this tutorial

go to [https://atwork.dunescience.org/tools/](https://atwork.dunescience.org/tools/) scroll down to Slack and request an invite.  Please do not do this if you are already in DUNE Slack.

Also check out our [Computing FAQ](https://github.com/orgs/DUNE/projects/19/views/1) for help with connection and account issues. 



## 0. Basic setup on your computer. 

[Computer Setup]({{ site.baseurl }}/ComputerSetup.html) goes through how to find a terminal and set up xwindows on MacOS and Windows.  You can skip this if already familiar with doing that. 

> ## Note
> The instructions directly below are for FNAL accounts. If you do not have a valid FNAL account but a CERN one, go at the bottom of this page to the [Setup on CERN machines](#setup_CERN).
{: .challenge}

## 1. Kerberos business

<!--**STEP 1**: DUNE Membership
To follow the tutorial, you must be on the DUNE Collaboration member list. You can check if you are on it [here][dune-collaboration]. If you are not, talk to your Institutional Board representative to get on it.

**STEP 2**: FNAL account
If you have a valid FNAL account with DUNE, go to the next step.

If you have a valid FNAL account but not on DUNE yet (say you have access to another experiment's resources), you can ask for a DUNE-specific account using the [Service Now Computing Account Request form][computing-account-request-form].

If you do not have any FNAL accounts yet, go through this form: [https://get-connected.fnal.gov/users/access/][get-connected-user-access]

**STEP 3**: Kerberos business -->
If you already are a Kerberos aficionado, go to the next section. If not, we give you a little tour of it below.

**What is it?** Kerberos is a computer-network authentication protocol that works on the basis of tickets.

**Why does FNAL use Kerberos?** Fermilab uses Kerberos to implement strong authentication, so that no passwords go over the internet (if a hacker steals a ticket, it is only valid for a day).

**How does it work?** Kerberos uses tickets to authenticate users. Tickets are made by the kinit command, which asks for your kerberos password (info on kerberos password [here][kerberos-password]). The kinit command reads the password, encrypts it and sends it to the Key Distribution Centre (KDC) at FNAL. The Kerberos configuration file, which lists the KDCs, is stored in a file named krb5.conf. On Linux and Mac, it is located here:

~~~
/etc/krb5.conf
~~~
{: .source}

If you do not have it, create it. A FNAL template is available [here][kerberos-template] for each OS (Linux, Mac, Windows). More explanations on this config file are available [here][kerberos-config] if you're curious.

To log in to a machine, you need to have a valid kerberos ticket. You don't need to do this every time you login, only when your ticket is expired. Kerberos tickets last for 26 hours. To create your ticket:

~~~
kinit -f username@FNAL.GOV
~~~
{: .language-bash}

The -f option means your ticket is forwardable. A forwardable ticket is one that originated on computer A, but can be forwarded to computer B and will remain valid on computer B. Careful: you need to write FNAL.GOV in uppercase.

To know if you have a valid ticket, type:

~~~
klist
~~~
{: .source}

Typical output of klist on macOS looks like this:

~~~
Mac-124243:~ trj$ klist
Ticket cache: FILE:/tmp/krb5cc_10143_xSCwboGiuY
Default principal: trj@FNAL.GOV

Valid starting     Expires            Service principal
05/18/23 12:43:23  05/19/23 11:41:42  krbtgt/FNAL.GOV@FNAL.GOV
	renew until 05/25/23 12:41:42
05/18/23 15:13:22  05/19/23 11:41:42  nfs/homesrv01.fnal.gov@FNAL.GOV
~~~
{: .output}

Tickets are stored in /tmp and have file permissions so that only you can read and write them.
If your ticket has not expired yet but will soon, you can refresh it for another 26 hours by typing:

~~~
kinit -R
~~~
{: .language-bash}

Refreshing a ticket can be done for up to one week after it was initially issued.

Running into issues? Users logging in from outside the Fermilab network may be behind Network Address Translation (NAT) routers. If so, you may need an "addressless" ticket. For this, add the option -A:

~~~
kinit -A -f username@FNAL.GOV
~~~
{: .language-bash}

Some users have reported problems with the Kerberos utilities provided by Macports and Anaconda. Macintosh users should use the system-provided Kerberos utilities -- such as /usr/bin/kinit.  Use the command

~~~
which kinit
~~~
{: .language-bash}

to report the path of the kinit that's first in your $PATH search list. If you have another, non-working one, a suggestion is to make an alias like this one:

~~~
alias mykinit="/usr/bin/kinit -A -f myusername@FNAL.GOV"
~~~
{: .language-bash}

Then you can simply use:

~~~
mykinit
~~~
{: .language-bash}

If you need to remove a ticket (for example, you are logged in at CERN with one Kerberos account but want to log in to a Fermilab machine with your Fermilab account), you can use the command

~~~
kdestroy
~~~
{: .language-bash}

After executing this command, you will have to use kinit again to get a new ticket.  If you have tickets from a non-working kinit, be sure to use the corresponding kdestroy to remove them.  klist should return an empty list to make sure you have a clean setup before running the system-provided kinit.

Some users have reported that an installation of Anaconda interferes with the use of the system kinit.  If you must use the kinit supplied with Anaconda, see these [instructions][anaconda-faq-kinit].

Check out the DUNE FAQ for a long list of possible error messages and suggested solutions. 

[DUNE FAQ][DUNE FAQ]

## 2. ssh-in
**What is it?** SSH stands for Secure SHell. It uses an encrypted protocol used for connecting to remote machines and it works with Kerberos tickets when configured to do so. The configuration is done in your local file in your home directory:

~~~
cat ~/.ssh/config
~~~
{: .language-bash}

If it does not exist, create it. A minimum working example to connect to FNAL machines is as follows:

~~~
Host *.fnal.gov
ForwardAgent yes
ForwardX11 yes
ForwardX11Trusted yes
GSSAPIAuthentication yes
GSSAPIDelegateCredentials yes
~~~
{: .output}

Now you can try to log into a machine at Fermilab. There are now 15 different machines you can login to: from dunegpvm01 to dunegpvm15 (gpvm stands for 'general purpose virtual machine' because these servers run on virtual machines and not dedicated hardware, others nodes which are indented for building code run on dedicated hardware). The dunegpvm machines run Scientific Linux Fermi 7 (SLF7). To know the load on the machines, use this monitoring link: dunegpvm status.

**How to connect?** The ssh command does the job. The -Y option turns on the xwindow protocol so that you can have graphical display and keyboard/mouse handling (quite useful). But if you have the line "ForwardX11Trusted yes" in your ssh config file, this will do the -Y option. For connecting to e.g. dunegpvm07, the command is:

~~~
ssh username@dunegpvmXX.fnal.gov
~~~
{: .language-bash}

where XX is a number from 01 to 15. 
If you experience long delays in loading programs or graphical output, you can try connecting with VNC. More info: [Using VNC Connections on the dunegpvms][dunegpvm-vnc].

## 3. Get a clean shell
To run DUNE software, it is necessary to have a 'clean login'. What is meant by clean here? If you work on other experiment(s), you may have some environment variables defined (for NOvA, MINERvA, MicroBooNE). Theses may conflict with the DUNE environment ones.

Two ways to clean your shell once on a DUNE machine:

**Cleanup option 1:** Manual check and cleanup of your custom environment variables
To list all of your environment variables:

~~~
env
~~~
{: .language-bash}

The list may be long. If you want to know what is already setup (potentially conflicting later with DUNE), you can grep the environment variables for a specific experiment (here the -i option is 'case insensitive'). Here is an example to list all NOvA-specific variables:

~~~
env | grep -i nova 
~~~
{: .language-bash}

Another useful command that will detect UPS products that have been set up is

~~~
ups active
~~~
{: .language-bash}

A "clean" response to the above command is:  

~~~
bash: ups: command not found...
~~~
{: .output}

and if your environment has UPS products set up, the above command will list the ones you have.

Once you identify environment variables that might conflict with your DUNE work, you can tweak your login scripts, like .bashrc, .profile, .shrc, .login etc., to temporarily comment out those (the "export" commands that are setting custom environment variables, or UPS's setup command).  Note:  files with names that begin with `.` are "hidden" in that they do not show up with a simple `ls` command.  To see them, type `ls -a` which lists **a**ll files.

**Cleanup option 2:** Back up your login scripts and go minimal at login (recommended)

A simpler solution would be to rename your login scripts (for instance .bashrc as .bashrc_save and/or .profile as .profile_bkp) so that your setup at login will be minimal and you will get the cleanest shell. For this to take into effect, you will need to exit and reconnect through ssh.

> ## Note: Avoid putting experiment specific setups in `.bashrc` or `.profile`
> You are going to be doing some setup for dune, which you will also need to  do when you submit batch jobs.  It is much easier to make a script `setup_dune.sh` which you execute every time you log in.  Then you can duplicate the contents of that script in the script you use to run batch jobs on remote machines.  It also makes it much easier for people to help you debug your setup. 
{: .callout}

## 4.1 Setting up DUNE software - Scientific Linux 7 version <a name="SL7_setup"></a>

See [SL7_to_Alma9][SL7_to_Alma9] for more information 

To set up your environment in SL7, the commands are:

Log into a DUNE machine running Alma9

Launch an SL7 container

~~~
/cvmfs/oasis.opensciencegrid.org/mis/apptainer/current/bin/apptainer shell --shell=/bin/bash \
-B /cvmfs,/exp,/nashome,/pnfs/dune,/opt,/run/user,/etc/hostname,/etc/hosts,/etc/krb5.conf --ipc --pid \
/cvmfs/singularity.opensciencegrid.org/fermilab/fnal-dev-sl7:latest
~~~
{: .language-bash}

You will then be in a container which looks like:

~~~
Apptainer>
~~~
{: .output}

You can then set up DUNE's code 

~~~
export UPS_OVERRIDE="-H Linux64bit+3.10-2.17" # makes certain you get the right UPS
source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
~~~
{: .language-bash}

You should see in your terminal the following output:
~~~
Setting up larsoft UPS area... /cvmfs/larsoft.opensciencegrid.org/products/
Setting up DUNE UPS area... /cvmfs/dune.opensciencegrid.org/products/dune/
~~~
{: .output}



> ## Optional
> > ## See how you can make an alias so you don't have to type everything
> > You can store this in your (minimal) .bashrc or .profile if you want this alias to be available in all sessions. The alias will be defined but not executed. Only if you type the command `dune_setup` yourself.> Not familiar with aliases? Read below.
> > 
> > To create unix custom commands for yourself, we use 'aliases':
> > ~~~
> > alias my_custom_commmand='the_long_command_you_want_to_alias_in_a_shorter_custom_name'
> > ~~~
> > {: .source}
> > For DUNE setup, you can type for instance:
> > ~~~
> > alias dune_setup='source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh'
> > ~~~
> > {: .language-bash}
> > 
> > So next time you type:
> > ~~~
> > dune_setup
> > ~~~
> > {: .source}
> > Your terminal will execute the long command. This will work for your current session (if you disconnect, the alias won't exist anymore). 
> {: .solution}
{: .callout}

> ## Optional
> > ## See if ROOT works
> > Try testing ROOT to make certain things are working
> >
> > ~~~
> > setup root v6_28_12 -q e26:p3915:prof # sets up root for you  
> > root -l -q $ROOTSYS/tutorials/dataframe/df013_InspectAnalysis.C
> > ~~~
> > {: .language-bash}
> > You should see a plot that updates and then terminates.  You may need to `export DISPLAY=0:0`.
> {: .solution}
{: .callout}


### Caveats for later

> ## Note: You cannot submit jobs from the Container
> You cannot submit jobs from the Container - you need to open a separate window. In that window do the minimal [Alma9](#AL9_setup) setup below and submit your jobs from that window. 
>
>You may need to print your submit command to the screen or a file to do so if your submission is done from a script that uses ups. 
{: .callout}

## 4.2 Setting up DUNE software - Alma9 version <a name="AL9_setup"></a>
=======
Try testing ROOT to make certain things are working

~~~
setup root -v v6_28_12 -q e26:p3915:prof # sets up root for you  

#  right now setup seems to spew out 1000's of lines of verbose output just doing its job. 

root -l -q $ROOTSYS/tutorials/dataframe/df013_InspectAnalysis.C
~~~
{: .language-bash}

You should see a plot that updates and then terminates.   You may need to `export DISPLAY=0:0` .

### Caveats for later

You cannot submit jobs from the Container - you need to open a separate window, not do the apptainer and submit your jobs from that window. 


## 4.2 Setting up DUNE software - Alma9 version


We are moving to the Alma9 version of unix.  Not all DUNE code has been ported yet but if you are doing basic analysis work, try it out. 

Here is how you set up basic DUNE software on Alma 9. We are now using the super-computer packaging system [Spack][Spack documentation] to give versioned access to code.

1. login into a unix machine at FNAL or CERN

2. Log into a gpvm or lxplus

~~~
source /cvmfs/larsoft.opensciencegrid.org/spack-packages/setup-env.sh 
~~~
{: .language-bash}

~~~
# get some basic things - 
# use the command spack find to find packages you might want
# If you just type spack load ... you may be presented with a choice and will need to choose. 
#
spack load root@6.28.12
spack load cmake@3.27.7
spack load gcc@12.2.0
spack load fife-utils@3.7.0
spack load metacat@4.0.0
spack load rucio-clients@33.3.0
spack load sam-web-client@3.4%gcc@12.2.0 
spack load kx509

# config for dune
spack load r-m-dd-config experiment=dune
export SAM_EXPERIMENT=dune
~~~
{: .language-bash}

> ## Optional
> > ## See if ROOT works
> > Try testing ROOT to make certain things are working
> >
> > ~~~ 
> > root -l -q $ROOTSYS/tutorials/dataframe/df013_InspectAnalysis.C
> > ~~~
> > {: .language-bash}
> > You should see a plot that updates and then terminates.   
> {: .solution}
{: .callout}
{: .language-bash}

### Caveats

We don't have a full ability to rebuild DUNE Software packages yet.  We will be adding more functionality here.  Unless you are doing simple ROOT based analysis you will need to use the [SL7 Container](#SL7_setup) method for now. 



## 5. Exercise! (it's easy)
This exercise will help organizers see if you reached this step or need help.

1) Start in your home area `cd ~` on the DUNE machine (normally CERN or FNAL) and create the file ```dune_presetup_2024.sh```.  


Launch the *Apptainer* as described above in the [SL7 version](#SL7_setup) 

Write in it the following:
~~~
export DUNELAR_VERSION=v09_90_01d00
export DUNELAR_QUALIFIER=e26:prof

export UPS_OVERRIDE="-H Linux64bit+3.10-2.17"
setup dunesw $DUNELAR_VERSION -q $DUNELAR_QUALIFIER

alias dune_setup='source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh'
~~~
{: .source}
When you start the training, you will have to source this file:
~~~
source ~/dune_presetup_2024.sh
~~~
{: .language-bash}
Then, to setup DUNE, use the created alias:
~~~
dune_setup
~~~
{: .language-bash}

2) Create working directories in the `dune/app` and `pnfs/dune` areas (these will be explained during the training):
~~~
mkdir -p /exp/dune/app/users/${USER}
mkdir -p /pnfs/dune/scratch/users/${USER}
mkdir -p /pnfs/dune/persistent/users/${USER}
~~~
{: .language-bash}

3) Print the date and add the output to a file named `my_first_login.txt`:
~~~
date >& /exp/dune/app/users/${USER}/my_first_login.txt
~~~
{: .language-bash}
4) With the above, we will check if you reach this point. However we want to tailor this tutorial to your preferences as much as possible. We will let you decide which animals you would like to see in future material, between: "puppy", "cat", "squirrel", "sloth", "unicorn pegasus llama" (or "prefer not to say" of course). Write your desired option on the second line of the file you just created above.

> ## Note

> If you experience difficulties, please ask for help in the Slack channel [#computing-training-basics](https://dunescience.slack.com/archives/C02TJDHUQPR).  Please mention in your message this is about the Setup step 5. Thanks!

{: .challenge}

## 6. Getting setup for streaming and grid access
In addition to your kerberos access, you need to be in the DUNE VO (Virtual Organization) to access to global DUNE resources. This is necessary in particular to stream data and submit jobs to the grid. If you are on the DUNE collaboration list and have a Fermilab ID you should have been added automatically to the DUNE VO.

To check if you are on the VO, two commands. The kx509 gets a certificate from your kerberos ticket. On a DUNE machine, type:
~~~
kx509
~~~
{: .language-bash}

~~~
Authorizing ...... authorized
Fetching certificate ..... fetched
Storing certificate in /tmp/x509up_u55793

Your certificate is valid until: Wed Jan 27 18:03:55 2021
~~~
{: .output}

To access the grid resources, you will need either need a proxy or a token. More information on proxy is available [here][proxy-info].



## How to authorize with the KX509/Proxy method <a name="proxy"></a>

On Alma9 you may need to do this first 

~~~
spack load kx509
~~~

This is to be done once every 24 hours per login machine you’re using to identify yourself:

~~~
kx509
export ROLE=Analysis
export X509_USER_PROXY=/tmp/x509up_dune_Analysis_`id -u`
voms-proxy-init -rfc -noregen -voms=dune:/dune/Role=$ROLE -valid 120:00
~~~
{: .language-bash}

~~~
Your identity: /DC=org/DC=cilogon/C=US/O=Fermi National Accelerator Laboratory/ OU=People/CN=Claire David/CN=UID:cdavid
Contacting  voms1.fnal.gov:15042 [/DC=org/DC=incommon/C=US/ST=Illinois/L=Batavia/O=Fermi Research Alliance/OU=Fermilab/CN=voms1.fnal.gov] "dune" Done
Creating proxy .................................... Done

Your proxy is valid until Mon Jan 25 18:09:25 2021
~~~
{: .output}

You should be able to access files now

> {: .solution}
{: .callout}

Report this by appending the output of `voms-proxy-info` to your first login file:
~~~
voms-proxy-info >> /exp/dune/app/users/${USER}/my_first_login.txt
~~~
{: .language-bash}

With this done, you should be able to submit jobs and access remote DUNE storage systems via xroot. 



### Tokens method <a name="tokens"></a>

We are moving from proxies to tokens - these are a bit different.  

#### 1. Get your token

~~~
 htgettoken -i dune --vaultserver htvaultprod.fnal.gov
~~~
{: .language-bash}

the first time you do this (and once a month thereafter), it will ask you to open a web browser and 

~~~
Attempting OIDC authentication with https://htvaultprod.fnal.gov:8200

Complete the authentication at:
    https://cilogon.org/device/?user_code=ABC-D1E-FGH
No web open command defined, please copy/paste the above to any web browser
Waiting for response in web browser
~~~
{: .output}

You will need to follow the instructions and copy and paste that link into your browser (can be any browser). There is a time limit on it so its best to do it right away. Choose Fermilab as the identity provider in the menu, even if your home institution is listed. After you hit log on with your service credentials, you'll get a message saying you approved the access request, and then after a short delay (may be several seconds) in the terminal you will see.


~~~
Saving credkey to /nashome/u/username/.config/htgettoken/credkey-dune-default
Saving refresh token ... done
Attempting to get token from https://htvaultprod.fnal.gov:8200 ... succeeded
Storing bearer token in /tmp/bt_token_dune_Analysis_somenumber.othernumber
Storing condor credentials for dune
~~~
{: .output}

you only have to do the web thing once/month.

#### 2. Tell the system where your token is


~~~
export BEARER_TOKEN_FILE=/run/user/`id -u`/bt_u`id -u`
~~~
{: .language-bash}

the `id -u` just returns your numerical user ID 

With this done, you should be able to submit jobs and access remote DUNE storage systems via xroot. 



> ## Issues

> If you have issues here, please ask [#computing-training-basics](https://dunescience.slack.com/archives/C02TJDHUQPR) in Slack to get support. Please mention in your message it is the Step 6 of the setup. Thanks!
{: .challenge}

> ## Success
> If you obtain the message starting with `Your proxy is valid until`... Congratulations! You are ready to go!
{: .keypoints}


## Set up on CERN machines <a name="setup_CERN"></a>

<!-- Caution: the following instructions are for those of you who do not have a valid FNAL account but have access to CERN machines. -->

> # Warning Some data access operations here still require a fermilab account. We are working on a solution.  
{: .callout}

See [https://github.com/DUNE/data-mgmt-ops/wiki/Using-Rucio-to-find-Protodune-files-at-CERN](https://github.com/DUNE/data-mgmt-ops/wiki/Using-Rucio-to-find-Protodune-files-at-CERN) for instructions on getting full access to DUNE data via metacat/rucio from lxplus. 

### 1. Source the DUNE environment setup script
CERN access is mainly for ProtoDUNE collaborators. If you have a valid CERN ID and access to lxplus via ssh, you can setup your environment for this tutorial as follow:

log into `lxplus.cern.ch`

fire up the Apptainer as explained in [SL7 Setup](#SL7_setup) but with a slightly different version as mounts are different.

~~~
/cvmfs/oasis.opensciencegrid.org/mis/apptainer/current/bin/apptainer shell --shell=/bin/bash\
-B /cvmfs,/afs,/opt,/run/user,/etc/hostname --ipc --pid \
/cvmfs/singularity.opensciencegrid.org/fermilab/fnal-dev-sl7:latest
~~~
{: .language-bash}

You may have to add some mounts - here I added `/afs/` but removed `/nashome/`, `/exp/`, `/etc/krb5.conf` and `/pnfs/`.

You should then be able to proceed with much of the tutorial thanks to the wonder that is [`/cvmfs/`]({{ site.baseurl }}/03.3-cvmfs.html).

Set up the DUNE software 

~~~
export UPS_OVERRIDE="-H Linux64bit+3.10-2.17" # makes certain you get the right UPS
source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
setup kx509
~~~
{: .language-bash}

~~~
Setting up larsoft UPS area... /cvmfs/larsoft.opensciencegrid.org/products/
Setting up DUNE UPS area... /cvmfs/dune.opensciencegrid.org/products/dune/
~~~
{: .output}

If you have a Fermilab account already do this to get access the data catalog worldwide

~~~
kdestroy
kinit -f <fnalaccount>@FNAL.GOV
kx509
export ROLE=Analysis
voms-proxy-init -rfc -noregen -voms=dune:/dune/Role=$ROLE -valid 120:00
~~~
{: .language-bash}

~~~
Checking if /tmp/x509up_u79129 can be reused ... yes
Your identity: /DC=org/DC=cilogon/C=US/O=Fermi National Accelerator Laboratory/OU=People/CN=Heidi <fnalusername>n/CN=UID:<fnalusername>
Contacting  voms1.fnal.gov:15042 [/DC=org/DC=incommon/C=US/ST=Illinois/O=Fermi Research Alliance/CN=voms1.fnal.gov] "dune" Done
Creating proxy .......................................................................................... Done

Your proxy is valid until Sat Aug 24 17:11:41 2024
~~~
{: .output}



### 2. Access tutorial datasets
Normally, the datasets are accessible through the grid resource. But with your CERN account, you may not be part of the DUNE VO yet (more on this during the tutorial). We found a workaround: some datasets have been copied locally for you. You can check them here:
~~~
ls /afs/cern.ch/work/t/tjunk/public/may2023tutorialfiles/
~~~
{: .language-bash}
~~~
np04_raw_run005387_0019_dl5_reco_12900894_0_20181102T023521.root
PDSPProd4_protoDUNE_sp_reco_stage1_p1GeV_35ms_sce_datadriven_41094796_0_20210121T214555Z.root
~~~
{: .output}

### 3. Notify us
You should be good to go, and you might revisit [Indico event page][indico-event-page].
If however you are experiencing issues, please contact us as soon as possible. Be sure to mention "Setup on CERN machines" if that is the case, and we will do our best to assist you.

> ## Success
> If you can list the files above, you should be able to do most of the tutorial on LArSoft.
{: .keypoints}

> ## Warning
> Connecting to CERN machines will not give you the best experience to understand storage spaces and data management. If you obtain a FNAL account in the future, you can however do the training through the recorded videos that will be made available after the event.
{: .checklist}

> ## Issues
> If you have issues here, please go to the [#computing-training-basics](https://dunescience.slack.com/archives/C02TJDHUQPR)Slack channel to get support. Please note that you are on a CERN machine in your message. Thanks!
{: .discussion}

### Useful Links
   
The [DUNE FAQ][DUNE FAQ] on GitHub.

[Wiki page][dune-wiki-interactive-resources] on DUNE's interactive computing resources, including tips on using Kerberos and VNC.

{%include links.md%} 

[SL7_to_Alma9]: https://wiki.dunescience.org/wiki/SL7_to_Alma9_conversion#SL7_to_Alma_9_conversion

[Spack documentation]: https://fifewiki.fnal.gov/wiki/Spack
[indico-event-page]: https://indico.fnal.gov/event/59762/
[indico-event-requirements]: https://indico.fnal.gov/event/59762/page/3229-requirements
[dune-collaboration]: http://collaboration.dunescience.org/
[computing-account-request-form]: https://fermi.servicenowservices.com/com.glideapp.servicecatalog_cat_item_view.do?v=1&sysparm_id=d361073881218500bea3634b5c987c4c&sysparm_link_parent=a5a8218af15014008638c2db58a72314&sysparm_catalog=e0d08b13c3330100c8b837659bba8fb4&sysparm_catalog_view=catalog_Service_Catalog 
[get-connected-user-access]: https://get-connected.fnal.gov/users/access/ 
[kerberos-password]: https://fermi.servicenowservices.com/kb_view.do?sysparm_article=KB0011294 
[kerberos-template]: https://authentication.fnal.gov/krb5conf/ 
[kerberos-config]: https://fermi.servicenowservices.com/kb_view.do?sysparm_article=KB0011315 
[dunegpvm-status]: https://fifemon.fnal.gov/monitor/d/000000004/experiment-overview?orgId=1&var-experiment=dune&from=now-6h&to=now-5m&panelId=30&fullscreen
[dunegpvm-vnc]: https://wiki.dunescience.org/wiki/DUNE_Computing/Using_VNC_Connections_on_the_dunegpvms
[proxy-info]: https://cdcvs.fnal.gov/redmine/projects/sbndcode/wiki/Get_a_certificate_proxy 
[dune-setup-jan2021]: https://wiki.dunescience.org/wiki/DUNE_Computing/Setup_Jan2021
[dune-training-may2021]: https://dune.github.io/computing-training-202105/
[dune-wiki-interactive-resources]: https://wiki.dunescience.org/wiki/DUNE_Computing/DUNE_Interactive_Computing_Resources
[anaconda-faq-kinit]: https://github.com/DUNE/FAQ/issues/22
[dunefaq]: https://github.com/DUNE/FAQ
[DUNE FAQ]: https://github.com/orgs/DUNE/projects/19/views/1
s

