import random

# Rhel questions found on the internet

rhelQuestions = [
"1) How to interrupt the boot process and reset the root password.\n",

"2) How to add repos.\n", #http://repo.eight.example.com/BaseOS and http://repo.eight.example.com/AppStream
"3) How to disable repos.\n",
"4) How to enable repos.\n",
"""5) How to create a repo.(Consider createrepo package already installed and 
you have already copied the packages you want to /root/local_repo)\n""",

"6) How to change the system time to your (or nearest to you) timezone and ensure NTP sync is configured.\n",

"""7) How to add a secondary IP addresses statically to your current running interface. 
Do this in a way that doesn’t compromise your existing settings: IPV4 - 10.0.0.5/24 IPV6\n""", 
"""8) How to add a secondary IP addresses statically to your current running interface. 
Do this in a way that doesn’t compromise your existing settings: IPV6 - fd01::100/64\n""",

"9) Enable packet forwarding on system1. This should persist after reboot.\n",

"10) System should boot into the multiuser target by default\n", 
"11) Boot messages should be present (not silenced).\n", # Check

"12) Create a new 2GB volume group named 'vgprac' in /dev/sdb1.\n",

"13) Create a 500MB logical volume named 'lvprac' inside the 'vgprac' volume group.\n",

"14) The 'lvprac' logical volume should be formatted with the xfs filesystem.\n",
"15) The 'lvprac' logical volume should be mounted persistently on the /mnt/lvprac directory.UUID is Q1w2e3r4t5y6u7i8o9p0\n",

"16) Extend the xfs filesystem on 'lvprac' by 500MB.\n",

"17) Use the appropriate utility to create a 5TiB thin provisioned volume.\n",

"""18) Configure a basic web server that displays “Welcome to the web server” once connected to it.
Assume that httpd is installed and started.\n""",

"19) Ensure the firewall allows the http/https services.\n",

"20) Find all files that are larger than 5MB in the /etc directory and copy them to /find/largefiles\n",

"""21) Write a script named awesome.sh in the root directory on system. 
- If 'me' is given as an argument, then the script should output 'Yes, I’m awesome.'
- If 'them' is given as an argument, then the script should output 'Okay, they are awesome.'
- If the argument is empty or anything else is given, the script should output 'Usage ./awesome.sh me|them'\n""",

"22) Create users phil, laura, stewart, and kevin.\n",
"23) - All new users should have a file named 'Welcome' in their home folder after account creation.\n",
"24) - All user passwords should expire after 60 days and be atleast 8 characters in length.\n",
"25) - phil and laura should be part of the 'accounting' group. If the group doesn’t already exist, create it.\n",
"26) - stewart and kevin should be part of the 'marketing' group. If the group doesn’t already exist, create it.\n",
"27) - Only members of the accounting group should have access to the '/accounting' directory.\n",
"28) - Make laura the owner of this directory. Make the accounting group the group owner of the '/accounting' directory.\n",
"29) - Only members of the marketing group should have access to the '/marketing' directory.\n",
"30) - Make stewart the owner of this directory. Make the marketing group the group owner of the '/marketing' directory.\n",
"31) - New files should be owned by the group owner and only the file creator should have the permissions to delete their own files.\n",

"32) Create a cron job that writes 'This practice exam was easy and I’m ready to ace my RHCSA' to /var/log/messages at 12pm only on weekdays.\n",

"33) Configure your installation disk as the default repository. Make sure to disable all other repositories.\n",

"34) Configure your system to clean up /tmp files every hour.\n",

"""35)  Consider you have 2 10G hard drives in your virtual machine. Configure one Stratis volume
with the name myvol on top of these hard drives and make sure the volume is
mounted persistently and automatically while booting.\n""",

"36) Find all files that have the SUID permission set and write the result to the file /tmp/suid.txt.\n",

"37) Create the user lisa.\n",
"38) Ensure that lisa needs to reset her password every 30 days.\n",
"39) Ensure that lisa is able to manage passwords for all users, but not the user root.\n",

"40) Ensure that user lisa has permissions to modify all files in the /etc directory, without changing user or group ownership.\n",

"""41) On the primary hard disk, use all the remaining disk space for an LVM volume group.
In this volume group, create a 2GiB logical volume to be used as swap space.\n""",

"42) On your primary network interface, configure a secondary IP address of 10.0.0.10/24.\n",

"43) Secure the SSH service, such that only user lisa is allowed to log in.\n",

"""44) Make sure that after a system restart, the system by default boots a graphical
environment. (Even if it is doing this already by default, type the command again so
that it is in your Bash history.)\n""",

"45) Configure Bash history such that the last 2500 commands used are written to the history file.\n",

"46) Install the vsftpd service.\n",
"47) Ensure that vsftpd service is started automatically after a reboot\n",
"48) Configure vsftpd service such that anonymous users are able to upload files.\n",

"49) Configure your system to use PHP version 7.1 as the default version.\n",

"50) Create a VDO volume with a virtual size of 1TiB.\n",

"""51) Create a detached apache http web server container with the name, 
(site1) and with the tag '1-112' from registry.redhat.io/rhel8/httpd-24:1-112 image.\n""",

"""52) Port 8080 on the container should be mapped to port 8080 on the host.
Declare the environment variables, HTTPD_USER and HTTPD_PASSWORD and use admin as their values.\n""",

"52) Create and mount the ~/storage/html/ directory as a persistent storage to the container as /var/www/.\n",

"""54) Configure the container as a service using systemd and make the web server/container persistent across reboot.
(You have to be logged in as the user to do this)\n""",

"""55) Add 3 users: harry, natasha, tom. The requirements: 
The Additional group of the two users: harry, Natasha is the admin group. 
The user: tom’s login shell should be non-interactive.\n""",
"""56) Configure your Host Name, IP Address, Gateway and DNS.
Host name: station.domain40.example.com
IP Address: 172.24.40.40/24
Gateway: 172.24.40.1
DNS/nameserver: 172.24.40.1 \n""",
"""57) Create a shared directory, “/home/admins”.
Make it have the following characteristics:
(1) “/home/admins” belongs to the group, “adminuser” and this directory can be read and written by members of group “adminuser”
(2) Any files created in “/home/admins” should permit the group members to be able to read and write on the files.\n""",
"""58) Install a FTP server, and request to anonymous download from /var/ftp/pub catalog.
 (It needs you to configure yum direct to the already existing file server.)\n""",]

#Rhel answers, hopefully all correct

rhelAnswers= [
"""rd.break enforcing=0 then
mount remount,rw /sysroot/ chroot /sysroot/ passwd exit exit and when logged in
restorecon -Rv /etc/shadow && setenforce 1""", # Reset root password commands
"dnf config-manager --add-repo='repository_url'",
"dnf config-manager --disablerepo 'repository'",
"dnf config-manager --enablerepo 'repository'",
"""createrepo --database /root/local_repo 
dnf config-manager --add-repo file:///root/local_repo/""",
"""timedatectl set-timezone Continent/City
timedatectl set-ntp yes""",
"nmcli connection add con-name eth0 ifname enp0s3 type ethernet ip4 10.0.0.5/24 gw4 10.0.2.2",
"nmcli connection add con-name eth0 ifname enp0s3 type ethernet ipv6 fd01::100/64",
"vim /etc/sysctl.conf and type net.ipv4.ip_forward = 1 then sysctl -w",
"systemctl set-default multi-user.target", 
"vim /etc/default/grub and remove 'rhgb quiet' then grub2-mkconfig -o /boot/grub2/grub.cfg",
"vgcreate vgprac /dev/sbd1",
"lvcreate --size 500M --name lvprac vgprac",
"mkfs.xfs -K /dev/mapper/vgprac-lvprac",
"""vim /etc/fstab then type 
UUID=Q1w2e3r4t5y6u7i8o9p0 /mnt/lvprac xfs default 0 0
and then systemctl daemon-reload""",
"lvextend -r -L +500M /dev/vgprac/lvprac",
"vdo create --name=vdoasync --device=/dev/sdc --vdoLogicalSize=5T --writePolicy=auto",
"""vim /var/www/html/index.html and type 'Welcome to the web server'
then curl localhost/index.html to check if it's working.If not systemctl enable httpd systemctl start httpd""",
"firewall-cmd --add-service=http firewall-cmd --add-service=https",
"find /etc/ -type f -size +5M > /find/largefiles",
"""touch /awesome.sh
 #!/bin/bash 
 if [[ $1 == 'me' ]]
 then
    echo 'Yes, I’m awesome.'
  elif [[ $1 == 'them' ]]
  then
    echo 'Okay, they are awesome.'
  else
    echo 'Usage ./awesome.sh me|them'
  fi""",
"useradd phil && useradd laura && useradd kevin && useradd stewart",
"touch /etc/skel/Welcome",
"chage -M 60 'username' and vim /etc/security/pwquality.conf",
"groupadd accounting then usermod -aG accounting 'username'",
"groupadd marketing then usermod -aG marketing 'username'",
"setfacl -R -m g:accounting:rwx /accounting/ and chmod o-rwx /accounting", # Not sure about this answer 
"chown laura:accounting /accounting",
"setfacl -R -m g:marketing:rwx /marketing and chmod o-rwx /marketing",
"chown stewart:marketing /marketing",
"chmod g+s /marketing && chmod o+t /marketing and chmod g+s /accounting && chmod o+t /accounting",
"crontab -e 00 12 * * 1-5 echo 'This practice exam was easy and I’m ready to ace my RHCSA' >> /var/log/messages",
"""dnf config-manager --add-repo=file:///run/media/root/RHEL*
dnf config-manager --disablerepo *""",
"crontab -e 00 * * * * rm -rf /tmp/*",
"""stratis pool create myvol /dev/sdb /dev/sdc 
stratis fs create myvol myfs
blkid -s UUID -o value /dev/mapper/stratis/* >> /etc/fstab
in fstab type UUID='stratis-uuid' /mountpoint xfs default,x-systemd.requires=stratisd.service 0 0
systemctl daemon-reload mount -a""",
"find / -perm /4000 >> /tmp/suid.txt",
"useradd lisa",
"chage -M 30 lisa",
"visudo lisa ALL= /usr/bin/passwd [A-Za-z]*, !/usr/bin/passwd *root*",
"setfacl -R -m u:lisa:rwx /etc",
"vgcreate vg1 /dev/sdb lvcreate -L 2G -n swap1 vg1 mkswap /dev/mapper/vg1-swap1 swapon /dev/mapper/vg1-swap1",
"nmcli connection modify eth0 +ip4 10.0.0.10/24",
"vim /etc/ssh/sshd.conf and add AllowUsers lisa",
"systemctl set-default graphical-target",
"vim /etc/skel/.bashrc and type HISTORY=2500 for all users and vim .bashrc HISTORY=2500 for your user",
"dnf install vsftpd",
"systemctl enable vsftpd",
"vim /etc/vsftpd/vsftpd.conf and uncomment anon_upload_enable=YES write_enable=YES and comment anonynous_enable=NO",
"dnf module list php dnf module remove php:'unwanted version' dnf module install php:7.1",
"vdo create --name=vdoasync --device=/dev/sdc --vdoLogicalSize=1T --writePolicy=auto",
"""skopeo inspect docker://registry.redhat.io/rhel8/httpd-24, podman pull registry.redhat.io/rhel8/httpd-24:1-112, 
podman run -d --name site1 registry.redhat.io/rhel8/httpd-24:1-112""",
"podman run -d --name site1 -p 8080:8080/tcp -e HTTPD_USER=admin -e HTTPD_PASSWORD=admin registry.redhat.io/rhel8/httpd-24:1-112",
"""podman run -d --name site1 -p 8080:8080/tcp -e HTTPD_USER=admin -e HTTPD_PASSWORD=admin
 -v /home/student/storage:/var/www registry.redhat.io/rhel8/httpd-24:1-112""",
"""mkdir .config/systemd/user/, cd .config/systemd/user/, podman generate systemd --name site1 --files -new,
loginctl enable-linger student, stop and remove container, systemctl --user daemon-reload, 
systemctl --user enable --now container-site1.service""",
"groupadd admin, useradd -G admin harry, useradd -G admin natasha, useradd -s /sbin/nologin tom",
"""vim /etc/sysconfig/network-scripts/ifcfg-'name of network', add lines 
IPADDR=172.24.40.40,PREFIX=24,GATEWAY=172.24.40.1,DNS1=172.24.40.1
nmcli conn down 'name of network';nmcli conn up 'name of network',
vim /etc/hostname, add line station.domain40.example.com, systemctl restart systemd-hostnamed.service""",
"mkdir -p /home/admins,groupadd adminuser, chown :adminuser /home/admins, chmod g+w /home/admins, chmod g+s /home/admins",
"""You can do this 2 ways, manually or with createrepo.
Manually : vim /etc/yum.repos.d/local.repo, [name],baseurl=file:///mnt/AppStream (if you get files from cd),
baseurl=http://GIVEN LINK(if link was given),gpgcheck=0,name='name of your choice',enable=1,
Createrepo : mkdir -p /home/local_repo, createrepo -d /home/local_repo, dnf config-manager --add-repo file:///mnt/AppStream (if you get files from cd),
dnf config-manager --add-repo http://GIVEN LINK(if link was given),
dnf install vsftpd, vim /etc/vsftpd/vsftpd.conf, uncomment anonymous_enable=YES, systemctl restart vsftpd.service, dnf install lftp, lftp localhost""" # Na to dokimasw molis ftiaksw enan ftp server,
]

# NEED TO ADD MORE CONTAINER QUESTIONS

# Questions/Answer class
class QA:
  def __init__(self, question, correctAnswer, falseAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.falseAnsw = falseAnswers

# Add the '\n' on every answer for reading easier
for i in range(0,len(rhelAnswers)):
  rhelAnswers[i] = rhelAnswers[i] + '\n'

# List stores all QA objects
ItemsList = []

# Adds a question , the right answer and 3 more random answers
def QAList():
  for question, answer in zip(rhelQuestions, rhelAnswers):
    QA.question = question
    QA.corrAnsw = answer
    ItemsList.append(QA(QA.question, QA.corrAnsw, [rhelAnswers[random.randint(0,48)],
    rhelAnswers[random.randint(0,48)],rhelAnswers[random.randint(0,48)],]))
  return ItemsList