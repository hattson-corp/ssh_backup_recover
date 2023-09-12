# ssh_backup_recover
A simple tool for backingup and restoring users in linux ssh servers 

useage : 
1 : backup => 
  <code> python3 user_manager.py -b backup </code>
  Note : your backup file will be in the same directory and named backup.txt 
2 : recovery => 
  <code> python3 user_manager.py -r backup.txt -p password </code>
  Note: your users will created from backup.txt file and with your password 

  
