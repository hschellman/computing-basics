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
> Use the [Apptainer/sl7 method]({{ site.baseurl }}/sl7_setup.html) until we get larsoft working if you want to use the full DUNE software suite. 
{: .callout}

~~~
# setup spack version 1.0 - generic env
. /cvmfs/dune.opensciencegrid.org/dune-spack/spack-develop-fermi/setup-env.sh
spack env activate dune-tutorial
export RUCIO_ACCOUNT=${USER}
~~~
{: .language-bash}

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
