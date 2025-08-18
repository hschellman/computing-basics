

Make certain you have [al9 set up]({{ site.baseurl }}/al9_setup)

Get rucio:

~~~
spack load r-m-dd-config experiment=dune lab=fnal.gov # r stands for rucio
export RUCIO_ACCOUNT=justinreadonly
~~~
{: .language-bash}

Then use htgettoken to get a token so you can read the files you find. 

~~~
htgettoken -i dune --vaultserver htvaultprod.fnal.gov #:8200
export BEARER_TOKEN_FILE=/run/user/`id -u`/bt_u`id -u`
~~~
{: .language-bash}


The first time you do it it will ask you to authenticate using a web browser.

<!-- ~~~
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
{: .bash} -->

You should be able to read files at remote sites now. 
You may need to repeat the `htgettoken` as the interactive tokens are pretty short-lived.  Batch jobs do their own tokens. 

