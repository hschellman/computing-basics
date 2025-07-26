---
title: 2025 Example AL9 setup for a new session
permalink: al9_setup
keypoints:
- getting basic applications on Alma9
- getting authentication set up
--- 

You can store the code below as 
 `myal9.sh` and run it every time you log in. 

> ## Note - the full LArSoft suite doesn't work yet with spack
> Use the [Apptainer/sl7 method]({{ site.baseurl }}al9_setup.html) until we get larsoft working if you want to use the full DUNE software suite. 
{: .callout}

~~~
# setup spack version 1.0 - generic env
. /cvmfs/dune.opensciencegrid.org/dune-spack/spack-develop-fermi/setup-env.sh
spack env activate dune-tutorial
export RUCIO_ACCOUNT=${USER}
~~~
{: .language-bash}

You can ignore the warning messages - this is still under development


