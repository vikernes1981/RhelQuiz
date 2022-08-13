storyList = [
"""Write all the commands needed for every task.Leave a space after every command.
------------------------------------------------------------------------------------

  ===============================================================
  Interrupt the boot process in order to gain access to a system
  ===============================================================

  You wake up in a strange room you've never been before.
As you look around you see that the room is completely empty.
There is only a half-open door and there is a light coming out from the next room.

  As you enter the room you see a PC in front of you.You turn it on and it asks you for 
a password.Of cource you don't know it so you know that you have to change it.

Mission : CHANGE THE ROOT PASSWORD!
------------------------------------\n""",

 """ Well done,you managed to login but you know that your solution 
ain't permanent and you have to make your changes permanent.

Mission : MAKE YOUR CHANGES PERMANENT
--------------------------------------\n""",

"""You got it.Now you have permanent access to this PC!

Suddenly a message pops on the screen :

  =========================================================
  IF YOU WANT TO PROCEED YOU HAVE 
  TO ADD AN IPV4 TO INTERFACE NAMED ENP0S3 , NAMED ETH0!
  IP : 10.0.2.20/24
  GW : 10.0.2.2
  ==========================================================

Mission : ADD A NEW IP
------------------------

( Order : connection name, interface name, type, IPv4, gateway ) """,
"""You press enter and you check to see if the IP is working but nothing is there.
You remember that you have restart the connection for changes to kick in.\n""",

"""Perfect, you got a ping!

Yet another message pops :

  ====================================
  WELL DONE, NOW ADD A SECONDARY IP
  TO MOVE FORWARD!
  IP : 10.0.2.19
  ====================================


Mission : ADD SECONDARY IP\n""",

"""As you press enter a new message pops : 

  =========================================
  OH! YOU ARE GOOD, LET'S SEE HOW YOU'LL
  COPE LATER!
  =========================================

  The message disappears and the PC turns off and 
at the same time you hear a 'click' and you see a secret
door opening right where there was a wall before.

  You walk through the door and you see another PC looking as
if it's waiting for you with a message again.

  ==================================================
  YOU MANAGED TO GET HERE, LET'S SEE HOW YOU CAN 
  GO FURTHER.
  THIS PC DOES NOT HAVE ENOUGH MEMORY TO PROCCESS 
  WHAT'S NEEDED TO BE DONE.
  DEAL WITH IT!
  ==================================================

  From the context of this message you understand that you have to 
make some SWAP space.You guess that 2G will suffice.


Mission : ADD 2G SWAP SPACE FROM /DEV/SDB AND MAKE IT PERSISTENT AFTER REBOOT
------------------------------------------------------------------------------

(Since there are multiple ways to do this I used VG,LV commands
VG name : vg1 , lv name : swap1. Don't forget to MOUNT )

Now make changes permanent.
  
  UUID=q1w2e3r4t5

  Now give a LABEL to the swap space just for the heck of it.
    I used e2label command
    
    LABEL=SWAP1\n""",

""" Once you press Enter and you mount the swap you hear another click.
You look around for another door opening but you see nothing.
You start looking around and see a small drawer underneath the table where
the PC is sitting.

Inside the drawer there is a small note :
    
    -------------------------------------------------
    | Find a file named secret.txt with a size of 5M.|
    | Don't let any errors on the screen!            |
    -------------------------------------------------
    
  You look around to see if you can find any hint of who 
might be helping you.
You find no clues and you decide to search for the file in the pc.

Mission : FIND SAID FILE
--------------------------\n""",

""" You find the file and you start to feel excited.
You open it and you see that it is full of gibberish. As you scroll down you
you notice some readable text in caps :

  =================================
  | CHANGE THE HOSTNAME TO 'JASON'|
  | REBOOT AFTER                  |
  =================================\n""",

  """ After the reboot took place you notice that, even though you 
fixed network, you now have no access. Then you remember that you haven't 
configure the services to start automaticaly at boot. Let's do that now.

Mission : CONFIGURE NETWORK MANAGER TO START AUTOMATICALLY AT BOOT
THEN START IT.\n""",

"""Perfect! Now, just to make sure, you check to see the firewall
access.

Mission : CHECK THE FIREWALL ENABLED SERVICES AND ALLOW ACCESS TO 
HTTP. MAKE CHANGES PERMANENT.\n""",
]

storyAnswers = [
"rd.break enforcing=0 mount -o remount,rw /sysroot chroot /sysroot passwd exit exit",
"restorecon -Rv /etc/shadow setenforce 1"
"nmcli connection add con-name eth0 ifname enp0s3 type ethernet ip4 10.0.2.20/24 gw4 10.0.2.2",
"nmcli connection down eth0 nmcli connection up eth0",
"nmcli connection modify eth0 ip4 10.0.2.19/24",
"vgcreate vg1 /dev/sdb lvcreate -L 2G -n swap1 vg1 mkswap /dev/mapper/vg1-swap1 swapon /dev/mapper/vg1-swap1",
"vim /etc/fstab UUID=q1w2e3r4t5 swap swap defaults 0 0 mount -a",
"e2label /dev/mapper/vg1-swap1 SWAP1",
"find / -type f -name 'secret.txt' -size 5M 2>/dev/null",
"vim /etc/hostname JASON hostnamectl reboot",
"systemctl enable NetworkManager systemctl start NetworkManager",
"firewall-cmd --list-services firewall-cmd --add-service=http --permanent firewall-cmd --reload",
]