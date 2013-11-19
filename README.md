vagrant-osb-federated
=====================

Release 1.0

Vagrant OSB Installation - Total Install time on a 5400RPM Mac Mini about 14 minutes.

I highly suggest, I think this is more of a requirement, that you do this install while online.  Preparing the operating system does require yum calls that the script will need to perform as well as modifications are made to Centos 6.4 box. 

Remember, your first download of the box (512mb) might take a couple of extra minutes.  However, once you have the box, you have it for as long as you want or until VirtualBox Guest Additions change with the next release.  You have been warned.

You will need the following files to sucessfully install OSB.  You will need to download them from Oracle and accept their licensing agreement.

Files are current a/o 11/19/2013

- jdk-7u45-linux-x64.tar.gz
- ofm_osb_generic_11.1.1.7_disk1_of_1.zip
- p17071663_1036_Generic.zip (This is patchset 6 from Oracle for WebLogic 10.3.6) 
- wls1036_generic.jar

For OracleXE

- oracle-xe-11.2.0-1.0.x86_64.rpm

Place these files in the root of the project:

<your path>/vagrant-osb-federated/[your files go here]

You don't necessarily need the patch file, put it is easily obtained:

http://support.oracle.com and then login with your OTN Account.  Here is how you download this patch if you have an OTN account

- http://mbaldwin.clarify-it.com/d/de29wr

If you are not downloading the patchset, then these are the lines you need to comment out in site.pp

- http://mbaldwin.clarify-it.com/d/hy77xa

If you do not download Patchset 6, then you will need to modify the site.pp in the manifests directory so that the Bsu is not run.It will fail...obviously without the file.

Notes about the install:

vagrant up entbus - starts the enteprise bus
vagrant up erpbus - starts the erpbus
vagrant up xe11g - starts the XE11g database.

vagrant up - starts the whole enchilada (not recommended)


Once it runs, you will have a running AdminServer and nodemanager for each VM that you start.. There is an osb_server1 which is shutdown.  You can start the osb_server1 if you want from Fusion Middleware Control or from the wls console.  If you are developing proxies, I don't see any reason to start that server until you need it.

Username and passwords are weblogic/welcome1

- http://localhost:7001/console - WLS Console
- http://localhost:7001/sbconsole - OSB Console 
- http://localhost:7001/em - Fusion Middleware Control for the osbDomain

Testing:

This has been tested on MacOS up to Mavericks.  Installing on Windows 7/8 should be the same as long as you have the latest VirtualBox from Oracle.

I am currently using VirtualBox 4.3.2 r90405

Questions:

If you have questions, please open an issue on the repo in git.  I will try my best to help as soon as possible.

My Blog is vbatik.wordpress.com

http://vbatik.wordpress.com/2013/11/07/install-oracle-service-bus-with-vagrant/

Acknowledgements:

Edwin Biemond was, as always, a great help.


- Company: Amis, Netherlands
- Email: biemond__AT__gmail.com
- Blog: http://biemond.blogspot.com
- LinkedIn: http://www.linkedin.com/in/biemond
- Twitter: http://twitter.com/biemond
- Git: https://github.com/biemond

