"""Write all the commands needed for every task.Leave a space after every command.
------------------------------------------------------------------------------------

  You wake up in a strange room you've never been before.
As you look around you see that the room is completely empty.
There is only a half-open door and there is a light coming out from the next room.

  As you enter the room you see a PC in front of you.You turn it on and it asks you for 
a password.Of cource you don't know it so you know that you have to change it.

You reboot the PC and you press 'e'.You delete the 'quiet' and 'rhgb' words and you start typing.


===============================================================
 Interrupt the boot process in order to gain access to a system
===============================================================

Mission : CHANGE THE ROOT PASSWORD!
------------------------------------\n"""

input 

rd.break enforcing=0

"You press ctrl+x to get forward.Type the rest of commands."

input

mount remount,rw /sysroot/ chroot /sysroot/ passwd exit exit

"""As you press the last 'exit' command the system continue to boot.
You put the new password and you log in the system. You know that you have to make the 
changes permanent.
You open the terminal and you start typing the needed commands."""

input

restorecon -Rv /etc/shadow && setenforce 1

