---
title: Example SL7 setup for a new session
permalink: sl7_setup
keypoints:
- getting basic applications on SL7
- getting authentication set ip
--- 

## launch the Apptainer

( I put this command in a file called apptainer.sh so I don't have to retype all the time.)

###  FNAL

~~~
/cvmfs/oasis.opensciencegrid.org/mis/apptainer/current/bin/apptainer shell --shell=/bin/bash \
-B /cvmfs,/exp,/nashome,/pnfs/dune,/opt,/run/user,/etc/hostname,/etc/hosts,/etc/krb5.conf --ipc --pid \
/cvmfs/singularity.opensciencegrid.org/fermilab/fnal-dev-sl7:latest
~~~
{: .language-bash}
 
### CERN 

~~~
/cvmfs/oasis.opensciencegrid.org/mis/apptainer/current/bin/apptainer shell --shell=/bin/bash\
-B /cvmfs,/afs,/opt,/run/user,/etc/hostname,/etc/krb5.conf --ipc --pid \
/cvmfs/singularity.opensciencegrid.org/fermilab/fnal-dev-sl7:latest
~~~
{: .language-bash}


## then do the following 

you can store this as

`mysl7.sh` and run it every time you log in.  

{% include sl7_setup_2025.md %}