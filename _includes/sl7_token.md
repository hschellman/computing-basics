
To get a token that allows you to access files interactively in SL7

~~~
htgettoken -i dune --vaultserver htvaultprod.fnal.gov -r interactive 
export BEARER_TOKEN_FILE=/run/user/`id -u`/bt_u`id -u`
export X509_CERT_DIR=/cvmfs/oasis.opensciencegrid.org/mis/certificates
~~~
{: ..language-bash}

put this in a file called `dune_token.sh`  

The first time you do this you will see:
~~~
Attempting kerberos auth with https://htvaultprod.fnal.gov:8200 ... succeeded
Attempting to get token from https://htvaultprod.fnal.gov:8200 ... failed
Attempting OIDC authentication with https://htvaultprod.fnal.gov:8200

Complete the authentication at:
    https://cilogon.org/device/?user_code=XXXX
No web open command defined, please copy/paste the above to any web browser
Waiting for response in web browser
~~~
{: ..output}

Go to that web site and authenticate

~~~
Storing vault token in /tmp/vt_uXXX
Saving credkey to /nashome/s/USER/.config/htgettoken/credkey-dune-interactive
Saving refresh token ... done
Attempting to get token from https://htvaultprod.fnal.gov:8200 ... succeeded
Storing bearer token in /run/user/XXXX/bt_XXXX
~~~
{: ..output}



## Accessing `rucio` and `justin` require a bit more

in SL7 - put this in a file called `dune_data_sl7.sh` so you can use it again.

~~~
setup metacat
setup rucio
export RUCIO_ACCOUNT=justinreadonly
setup justin
justin time # this just tells justin that you exist and want to authenticate
justin get-token # this actually gets a token and associated proxy for access to rucio and the batch system
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

Once again go to the website that appears and authenticate.  After the first authentication to justIn you need to do a second justin call

~~~
justin get-token
~~~
{: ..language-bash}

You will need to do this sequence weekly as your justin access expires. 

> ## Note: 
> Despite the name of this command it gets you both a token and a special X.509 proxy and it is the latter you are actually using to talk to rucio in these SL7 examples
{: .callout}