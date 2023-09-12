# ssh_backup_recover
A simple tool for backingup and restoring users in linux ssh servers 

useage : <br>
1 : backup =><br> 
  <code> python3 user_manager.py -b backup </code><br>
  Note : your backup file will be in the same directory and named backup.txt <br><br>
2 : recovery => <br>
  <code> python3 user_manager.py -r backup.txt -p password </code><br>
  Note: your users will created from backup.txt file and with your password <br>

  
