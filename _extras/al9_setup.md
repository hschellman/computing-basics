---
title: Example AL9 setup for a new session
permalink: al9_setup
keypoints:
- getting basic applications on Alma9
- getting authentication set up
--- 

You can store the code below as 
 `myal9.sh` and run it every time you log in. 

> ## Note - the full LArSoft suite doesn't work yet with spack
> Use the [Aptainer/SL7]({{ site.baseurl }}/sl7_setup.html) until we get that working if you want to use the full DUNE software suite. 
{: .callout}

~~~

# access some disks
export DUNEDATA=/exp/dune/data/users/$USER
export DUNEAPP=/exp/dune/app/users/$USER
export PERSISTENT=/pnfs/dune/persistent/users/$USER
export SCRATCH=/pnfs/dune/scratch/users/$USER

# do some authentication

htgettoken -i dune --vaultserver htvaultprod.fnal.gov

export BEARER_TOKEN_FILE=/run/user/`id -u`/bt_u`id -u`

~~~
{: .language-bash}

------------------------

## setup specific versions of code here

~~~
# find a spack environment and set it up
# setup spack

source /cvmfs/larsoft.opensciencegrid.org/spack-v0.22.0-fermi/setup-env.sh
export CVSROOT=minervacvs@cdcvs.fnal.gov:/cvs/mnvsoft

# get the packages you need to run this - this is a total hack of guesswork
echo "ROOT"
spack load root@6.28.12%gcc@12.2.0 arch=linux-almalinux9-x86_64_v3

echo "CMAKE"
spack load cmake@3.27.9%gcc@11.4.1 arch=linux-almalinux9-x86_64_v3

echo "GCC"
spack load gcc@12.2.0

echo "Rucio and metacat"
spack load r-m-dd-config experiment=dune lab=fnal.gov
export RUCIO_ACCOUNT=${USER}
export SAM_EXPERIMENT=dune

echo "IFDHC"
spack load ifdhc@2.8.0%gcc@12.2.0 arch=linux-almalinux9-x86_64_v3
spack load ifdhc-config@2.6.20%gcc@11.4.1 arch=linux-almalinux9-x86_64_v3

echo "PY-PIP"                       
spack load py-pip@23.1.2%gcc@11.4.1 arch=linux-almalinux9-x86_64_v3

echo "Justin"
spack load justin

~~~
{: .language-bash}
