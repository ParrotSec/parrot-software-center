#
# Regular cron jobs for the parrot-software-center package
#
0 4	* * *	root	[ -x /usr/bin/parrot-software-center_maintenance ] && /usr/bin/parrot-software-center_maintenance
