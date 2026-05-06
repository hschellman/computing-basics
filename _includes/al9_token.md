### Interactive file access

Make certain you have [al9 set up]({{ site.baseurl }}/al9_setup)

Then use `htgettoken` to get a token so you can read the files you find. 

~~~
htgettoken -i dune --vaultserver htvaultprod.fnal.gov -r interactive #:8200
export BEARER_TOKEN_FILE=/run/user/`id -u`/bt_u`id -u`
export X509_CERT_DIR=/cvmfs/oasis.opensciencegrid.org/mis/certificates
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

### Accessing rucio and justIn resources requires a bit more

You should already be set up above.  Now you can use `justIn` to get you a token.  

1. First tell `justIn` knows about you

~~~
justin time
~~~
{: ..language-bash}

The first time you do this you will get asked (after the `justin time` command)

~~~
To authorize this computer to run the justin command, visit this page with your
usual web browser and follow the instructions within the next 10 minutes:
https://dunejustin.fnal.gov/authorize/XXXXX

Check that the Session ID displayed on that page is BfhVBmQ

Once you've followed the instructions on that web page, please run the command
you tried again. You won't need to authorize this computer again for 7 days.
~~~
{: ..output}

Once again go to the website that appears and authenticate.  

2. After the first authentication to justIn you need to do a second justin call

~~~
justin get-token
~~~
{: ..language-bash}

You will need to do this sequence weekly as your justin access expires. 

> ## Note: 
> Despite the name of this command it gets you both a token and a special X.509 proxy and it is the latter you are actually using to talk to rucio in these SL7 examples
{: .callout}