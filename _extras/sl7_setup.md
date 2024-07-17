---
title: Example SL7 setup for a new session
permalink: sl7_setup
keypoints:
- getting basic applications on SL7
- getting authentication set ip
--- 

## launch the Apptainer

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

~~~
# use ups to find programs

export UPS_OVERRIDE="-H Linux64bit+3.10-2.17"
source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
setup metacat
setup rucio


# do some data access setup
export IFDH_CP_MAXRETRIES=0\0\0\0\0  # no retries
export DATA_DISPATCHER_URL=https://metacat.fnal.gov:9443/dune/dd/data
export DATA_DISPATCHER_AUTH_URL=https://metacat.fnal.gov:8143/auth/dune
export METACAT_SERVER_URL=https://metacat.fnal.gov:9443/dune_meta_prod/app
export METACAT_AUTH_SERVER_URL=https://metacat.fnal.gov:8143/auth/dune
export RUCIO_ACCOUNT=$USER

# access some disks
export DUNEDATA=/exp/dune/data/users/$USER
export DUNEAPP=/exp/dune/app/users/$USER
export PERSISTENT=/pnfs/dune/persistent/users/$USER
export SCRATCH=/pnfs/dune/scratch/users/$USER

# do some authentication

voms-proxy-destroy
kx509
export EXPERIMENT=dune
export ROLE=Analysis
voms-proxy-init -rfc -noregen -voms dune:/dune/Role=$ROLE -valid 24:00
export X509_USER_PROXY=/tmp/x509up_u`id -u`

htgettoken -i dune --vaultserver htvaultprod.fnal.gov

export BEARER_TOKEN_FILE=/run/user/`id -u`/bt_u`id -u`

## you need to change these to match current versions

export DUNESW_VERSION=v09_90_01d00
export DUNESW_QUALIFIER=e26:prof

setup -B dunesw ${DUNESW_VERSION} -q ${DUNESW_QUALIFIER}
~~~
{: .language-bash}
