---
title: The new Spack code management system
teaching: 15
exercises: 5
questions:
- How are different software versions handled? 
objectives:
- Understand the role of Spack
keypoints:
- Spack is a tool to deliver well defined software configurations
- CVMFS distributes software and related files without installing them on the target computer (using a VM, Virtual Machine).
---

{% include 04-Spack.toc.md %}
## What is Spack and why do we need it?

> ## Note 
> UPS is being replaced by a new [spack](https://fifewiki.fnal.gov/wiki/Spack) system for Alma9. 
> 
{: .callout}

An important requirement for making valid physics results is computational reproducibility. You need to be able to repeat the same calculations on the data and MC and get the same answers every time. You may be asked to produce a slightly different version of a plot for example, and the data that goes into it has to be the same every time you run the program. 

This requirement is in tension with a rapidly-developing software environment, where many collaborators are constantly improving software and adding new features. We therefore require strict version control; the workflows must be stable and not constantly changing due to updates. 

DUNE must provide installed binaries and associated files for every version of the software that anyone could be using. Users must then specify which version they want to run before they run it. All software dependencies must be set up with consistent versions in order for the whole stack to run and run reproducibly.

Spack is a tool to handle the software product setup operation. 

## Minimal spack for root analysis and file access

You can get spack going with our minimal implementation

~~~
. /cvmfs/dune.opensciencegrid.org/dune-spack/spack-develop-fermi/setup-env.sh
spack env activate dune-tutorial
~~~
{: .language-bash}

This sets up the file and job management packages (metacat, rucio, justin) and a version of root that can do streaming transfers.  It is useful for end stage tuple analysis. 

A full version with larsoft is in the works.

You can list what is available in that environment via

~~~
spack find
~~~
{: .language-bash}

Which lists packages like this:

~~~
-- linux-almalinux9-x86_64_v2 / %c,cxx=gcc@12.5.0 ---------------
cmake@3.31.8               libffi@3.4.8          openssl@3.3.3    root@6.28.12
davix@0.8.10               libjpeg-turbo@3.0.4   patchelf@0.17.2  rust@1.85.0
ftgl@2.4.0                 libpng@1.6.47         pcre@8.45        unuran@1.8.1
ifdhc@2.8.0                lz4@1.10.0            postgresql@15.8  vdt@0.4.6
ifdhc-config@2.8.0         ninja@1.13.0          python@3.9.15    xrootd@5.6.9
intel-tbb-oneapi@2021.9.0  nlohmann-json@3.11.3  re2c@3.1         xxhash@0.8.3
~~~
{: .output}

This particular environment loads only one version of the packages.

## A more flexible environment with more packages but you have to make choices of versions

An older instance with more packages and more flexibility is here: [AL9 setup]({{ site.baseurl }}/al9_setup)

Here if you execute the setup in [AL9 setup]({{ site.baseurl }}/al9_setup) and then try to do, for example

~~~
spack load geant4
~~~
{: .language-bash}

you have to make a choice

~~~
==> Error: geant4 matches multiple packages.
  Matching packages:
    r2dcnvb geant4@10.6.1%gcc@12.2.0 arch=linux-almalinux9-x86_64_v3
    5pqylh6 geant4@10.6.1%gcc@12.2.0 arch=linux-almalinux9-x86_64_v2
  Use a more specific spec (e.g., prepend '/' to the hash).
~~~
{: .output}

Now you have to choose. I would go with 'v3'.  You can either use the hash or the full string - I tend to use the full string as it has more information.

> ## You can do 
> ~~~
> spack load geant4@10.6.1%gcc@12.2.0 arch=linux-almalinux9-x86_64_v3 # pick v3
> ~~~
> {: .language-bash}
> or if you change your mind
> 
> ~~~
> spack unload geant4
> spack load geant4/5pqylh6. # changed my mind and used the hash for v2
> ~~~
> {: .language-bash}
{: .callout}

<!-- 
> ## Exercise 3
> * show all the versions of dunesw that are currently available by using the `ups list -aK+ dunesw` command
> * pick one version and substitute that for DUNELAR_VERSION and DUNELAR_QUALIFIER above and set up dunesw
{: .callout}

Many products modify the following search path variables, prepending their pieces when set up. These search paths are needed by _art_ jobs.

`PATH`: colon-separated list of directories the shell uses when searching for programs to execute when you type their names at the command line. The command `which` tells you which version of a program is found first in the PATH search list. Example:
~~~
which lar
~~~
{: .language-bash}

will tell you where the lar command you would execute is if you were to type `lar` at the command prompt. 
The other paths are needed by _art_ for finding plug-in libraries, fcl files, and other components, like gdml files.  
`CET_PLUGIN_PATH`  
`LD_LIBRARY_PATH`  
`FHICL_FILE_PATH`  
`FW_SEARCH_PATH`   -->

Also the PYTHONPATH describes where Python modules will be loaded from.

Try 

~~~
which root
~~~
{: .language-bash}
to see the version of root that spack sets up. Try it out!


### Spack basic commands

| Command                                        | Action                                                           |
|------------------------------------------------|------------------------------------------------------------------|
| `spack list`                         | List everything spack knows about |
| `spack find`                                   | Displays what is available in your environment                                  |
| `spack load`                         | Load a package |
| `spack unload`                         | Unload a package |



<!-- > ## Exercise 4
> * show all the dependencies of dunesw by using "ups depend dunesw $DUNELAR_VERSION -q $DUNELAR_QUALIFIER"
{: .challenge}
>## UPS Documentation Links
>
> * [UPS reference manual](http://www.fnal.gov/docs/products/ups/ReferenceManual/)
> * [UPS documentation](https://cdcvs.fnal.gov/redmine/projects/ups/wiki)
> * [UPS qualifiers](https://cdcvs.fnal.gov/redmine/projects/cet-is-public/wiki/AboutQualifiers)
{: .callout} -->
[Spack documention]: (https://fifewiki.fnal.gov/wiki/Spack) (requires FNAL SSO)

