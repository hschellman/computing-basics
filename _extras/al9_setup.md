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
> Use the [Apptainer/ method]({{ site.baseurl }}/sl7_setup.html) until we get larsoft working if you want to use the full DUNE software suite. 
{: .callout}

{% include al9_setup_2025a.md %}

<!-- ~~~
# find a spack environment and set it up
# setup spack  (pre spack 1.0 version)

source /cvmfs/larsoft.opensciencegrid.org/spack-v0.22.0-fermi/setup-env.sh
export CVSROOT=minervacvs@cdcvs.fnal.gov:/cvs/mnvsoft

# get the packages you need to run this - this will become simple in future
echo "ROOT"
spack load root@6.28.12%gcc@12.2.0 arch=linux-almalinux9-x86_64_v3

echo "CMAKE"
spack load cmake@3.27.9%gcc@11.4.1 arch=linux-almalinux9-x86_64_v3

echo "GCC"
spack load gcc@12.2.0

echo "Rucio and metacat"
spack load r-m-dd-config experiment=dune lab=fnal.gov
export RUCIO_ACCOUNT=justinreadonly
export SAM_EXPERIMENT=dune

echo "IFDHC"
spack load ifdhc@2.8.0%gcc@12.2.0 arch=linux-almalinux9-x86_64_v3
spack load ifdhc-config@2.6.20%gcc@11.4.1 arch=linux-almalinux9-x86_64_v3


echo "PY-PIP"                       
spack load py-pip@23.1.2%gcc@11.4.1 arch=linux-almalinux9-x86_64_v3

echo "justIN"
spack load justin
~~~
{: .language-bash} -->

You can ignore most warning messages - this is still under development - but pay attention to this one.

> ## Note
> > ## You may see a rucio config error message that looks like this
> > ~~~
> > ==> Warning: Your rucio config /nashome/X/XXXXX/.config/rucio/dune/etc/rucio.cfg does not list oidc authentication
> > If you remove it and spack load r-m-dd-config again it will get regenerated with oidc (Token) authentication
> > ~~~
> > {: .output}
> > This happens if you've run older versions of rucio that used kx509 authentication.  Remove `$HOME/.config/rucio/dune/etc/rucio.cfg` as it advises and rerun the `spack load r-m-dd-config` command to reset the config file.  You should not need to do this again.
> {: .solution}
{: .callout}
