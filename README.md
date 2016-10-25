AWSLogs
=========

Simple role to install and configure AWS CloudWatch log agent

Requirements
------------

Run on Amazon Linux only - 2016-10-25

Role Variables
--------------



Dependencies
------------

N/A

Example Playbook
----------------

```

- hosts:
  - ec2_instances
  - localhost
  roles:
  - awscli
  vars:
  - log_streams:
    - app_1_stdout:
      log_stream_name: '{instance_id}'
      log_group_name: myapp: myapp1_stdout
      file: /var/log/myapp.stdout.log

```


License
-------

GPLv3

Author Information
------------------

John Mille [JohnPreston]
