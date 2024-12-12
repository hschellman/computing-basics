---
title: Use Conda to install root
teaching: 30
exercises: 0
questions:  
- How do I get root and jupyter-lab for simple analysis
objectives:  
- get miniconda set up on your machine
- install root and jupyter-lab
keypoints:
- useful mainly for simple tuple analysis
---

##  Installing conda and root

This is derived from the excellent [https://iscinumpy.gitlab.io/post/root-conda/](https://iscinumpy.gitlab.io/post/root-conda/) by Henry Schreiner

Currently this has been tested on OSX and Linux distributions SL7 and AL9

## Download miniconda

1. Do you have wget on your system? If not, get it 

2. Download the miniconda installer

~~~
# Download the Linux installer
wget -nv http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
~~~
{: .language-bash}

~~~
# Or download the macOS installer
wget -nv https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O miniconda.sh
~~~
{: .language-bash}

## Install conda 

~~~
# Install Conda (same for macOS and Linux)
bash miniconda.sh -b -p $HOME/miniconda
~~~
{: .language-bash}

4. add this to your .bashrc or .profile to start it up when you log in

~~~
source $HOME/miniconda/etc/profile.d/conda.sh # Add to bashrc - similar files available for fish and csh
~~~
{: .language-bash}

## Making an environment with root in it

~~~
conda create -n my_root_env root -c conda-forge
~~~
{: .language-bash}

This will take a while. In the end you have an environment which contains root and a lot of other useful things

You can repeat step 1 to make different conda enviroments.

## Try out your new environment

To activate a particular environment you do:

~~~
conda activate my_root_env
~~~
{: .language-bash}

First time you use your environment you can do 

~~~
conda config --add --env channels conda-forge # only
~~~
{: .language-bash} 

the config command tells conda to use conda-forge as a default.   You should now have a conda environment with root in it. 

## Testing

~~~
(my_root_env) wngr405-mac3:utilities schellma$ root
   ------------------------------------------------------------------
  | Welcome to ROOT 6.28/00                        https://root.cern |
  | (c) 1995-2022, The ROOT Team; conception: R. Brun, F. Rademakers |
  | Built for macosx64 on Mar 21 2023, 08:18:00                      |
  | From tag , 3 February 2023                                       |
  | With                                                             |
  | Try '.help'/'.?', '.demo', '.license', '.credits', '.quit'/'.q'  |
   ------------------------------------------------------------------

root [1] .q
~~~
{: .output}

To get out of root type 

~~~
root> .q
~~~
{: .language-bash}



Try this

~~~
root -l -q $ROOTSYS/tutorials/dataframe/df013_InspectAnalysis.C
~~~
{: .language-bash}

You should see a plot that updates.  

 
