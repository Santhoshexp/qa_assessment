# 1) Backup Directory to Remote Location

This repository contains a Python script named backup.py for copying a tar file from the source location to a remote server.

## Modules Used

- **logging**: For logging all the activites done while executing the script.
- **tarfile**: For converting the source directory to a tar file -compressing.
- **Paramiko**: For transfering the files to a remote machine using the scp module.

## Steps to execute

- python backup.py

## Note

- Change the variable values accordingly based on the scenario.
- Some of the variable names used are usernmae, password , source_location ,remote_location etc.


# 2) Health Check Monitor

This repository contains a Python script named health_monitoring.py, which monitors the health of the system and records in a log file for every 2 minutes.

## Modules Used

- **logging**: For logging all the activites done while executing the script.
- **psutil**: For fteching the health metrics like cpu , memory utilization etc.

  
## Steps to execute

- python health_monitoring.py

## Note

- Change the variable values accordingly based on the scenario.
- Some of the variable names used are Cpu , Memory threshold , sleep interval etc.


# 3) Selenium and Request module solution for Problem 1

The 2 different solutions are given in a seperate folder with a seperate readme.md file containg additional information.



