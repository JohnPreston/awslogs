AWSLogs
=========

Simple role to install and configure AWS CloudWatch log agent

Requirements
------------

Run on Amazon Linux only - 2016-10-25

Role Variables
--------------

| Name | Type | Required | Default | Description
|--- |--- |--- |--- |---
| for_real | boolean | False | False | Allows to run in a dry-run way to /var/tmp to verify all variables are sound
| tmp_dir | string | True | /var/tmp/ | Default "test" directory
| aws_logs_conf_dir | string | True | /etc/awslogs | Default loction of the aws logs configuration files
| aws_cli_conf_file | string | True | awscli.conf | Default configuration for aws logs cli parameters
| aws_logs_conf_file | string | True | awslogs.conf | Default configuration file for aws logs
| use_time_separator | boolean | True | True | For streams, separate each depending on the time of the execution


Dependencies
------------

N/A

Example Playbook
----------------

```

- hosts: localhost
  roles:
  - JohnPreston.awslogs
  vars:
  - app_name: myapp
  - log_streams:
    - file_dir: "/var/www/{{ app_name }}/rest/log"
      file_name: fatal.log
      log_group_name: "{{ tags['aws:cloudformation:stack-name'] }}"
      log_stream_name: "{{ tags['ApplicationName'] }}-fatal"
      date_format: '%Y-%m-%d-%H-%M-%S'
    - log_group_name: "{{ tags['aws:cloudformation:stack-name'] }}"
      file_name: error.log
      log_stream_name: "{{ tags['ApplicationName'] }}-error"
      file_dir: "/var/www/{{ app_name }}/rest/log"
      date_format: '%Y-%m-%d-%H-%M-%S'
```


License
-------

GPLv3

Author Information
------------------

John Mille [JohnPreston]
