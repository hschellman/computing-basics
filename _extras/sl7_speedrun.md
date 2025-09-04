---
title: 2025 Speedrun of SL7 setup and test
permalink: sl7_speedrun
keypoints:
- all in one place
--- 
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


{% include sl7_setup_2025.md %}
{% include sl7_token.md %}

## check root

~~~
{% include examplerootfile.md}
.q
~~~
{: .language-bash} 

## check rucio

