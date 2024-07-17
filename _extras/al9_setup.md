---
title: Example AL9 setup for a new session
permalink: al9_setup
keypoints:
- getting basic applications on Alma9
- getting authentication set ip
--- 

You can store the code below as 
 `myal9.sh` and run it every time you log in. 

> ##Note - the full LArSoft suite doesn't work yet with spack
> Use the [Apptainer/sl7 method]({{ site.baseurl }}al9_setup.html) until we get that working if you want to use the full DUNE software suite. 
{: .callout}

~~~

# use spack to get applications
source /cvmfs/larsoft.opensciencegrid.org/spack-v0.22.0-fermi/setup-env.sh
spack load gcc@12.2.0 arch=linux-almalinux9-x86_64_v3
spack load root@6.28.12 arch=linux-almalinux9-x86_64_v3
spack load fife-utils@3.7.0

spack load sam-web-client@3.4%gcc@12.2.0    
export SAM_EXPERIMENT=dune
# this loads rucio and metacat
spack load r-m-dd-config@1.0 experiment=dune
export IFDH_CP_MAXRETRIES=0\0\0\0\0  # no retries
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

~~~
{: .language-bash}
