---
title: Example SL7 setup for a new session
permalink: sl7_setup
keypoints:
- getting basic applications on SL7
- getting authentication set ip
--- 

## launch the Apptainer

( I put this command in a file called apptainer.sh so I don't have to retype all the time.)

Start the Apptainer


> ## Choose your apptainer
> 
> > ## gpvm apptainer
> > ~~~
> > {% include apptainer_gpvm.md %}
> > ~~~
> > {: .language-bash}
> {: .solution}
> > ## cern apptainer
> > ~~~
> > {% include apptainer_cern.md %}
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}


## then do the following 

you can store this as

`mysl7.sh` and run it every time you log in.  

{% include sl7_setup_2025.md %}
