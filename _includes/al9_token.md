

Make certain you have [al9 set up]({{ site.baseurl }}/al9_setup)

Get rucio:

~~~
spack load r-m-dd-config experiment=dune lab=fnal.gov # r stands for rucio
export RUCIO_ACCOUNT=$USER
~~~
{: .language-bash}

First ask it to tell you about a file

~~~
rucio replica list file fardet-vd:prodmarley_nue_es_flat_radiological_decay0_dunevd10kt_1x8x14_3view_30deg_20250217T033222Z_gen_004122_supernova_g4stage1_g4stage2_detsim_reco.root  --pfns --protocols=root
~~~
{: .language-bash}

The first time you do it it will ask you to authenticate. 

~~~
Please use your internet browser, go to:

    https://dune-rucio.fnal.gov/auth/oidc_redirect?uXGMjOvvdH7pV9hSf6qF9bq    

and authenticate with your Identity Provider.
Copy paste the code from the browser to the terminal and press enter:
~~~
{: .output}

I entered the string from the website
~~~
YgZTGDqHQg6NOO77NsCY5J88uyIkkoZ1tRb6iTXK0j5RsX0AjA
~~~
{: .bash}

and then got 3 locations. 

