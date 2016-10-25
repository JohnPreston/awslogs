#!/usr/bin/env python
import os, re
import json
import boto3
import requests
import argparse

def get_client():
    """
    creates the client
    """

    client = boto3.client('ec2')
    return client


def get_ec2_instances_tags(client, instance_id, filters=[]):
    """

    describe instances

    """
    instances_list = []
    instances_list.append(instance_id)

    res = client.describe_instances(InstanceIds=instances_list, Filters=filters)
    reservations = res['Reservations']
    for resa in reservations:
        for instance in resa['Instances']:
            return instance['Tags']


def whoami():
    """
    Function to get some info about the VM from meta-data
    """
    r_instance_id = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
    return r_instance_id.text

def get_tag_value(tags, name):
    """
    Returns the value of the given tag name
    """

    for tag in tags:
        if name == tag['Key']:
            return tag['Value']

    return None

def parser():
    parser = argparse.ArgumentParser(description='Get Tag Value')
    parser.add_argument("--name", required=False)
    parser.add_argument("--all", action='store_true', required=False)

    args = parser.parse_args()
    return args
def main():

    args = parser()
    instance_id = whoami()
    filters = []
    client = get_client()
    tags = get_ec2_instances_tags(client, instance_id, filters=filters)

    name = args.name
    all = args.all
    if name:
        print get_tag_value(tags, name)
    elif all:
        dict_tags = {}
        for tag in tags:
            dict_tags[tag['Key']] = tag['Value']
        print json.dumps(dict_tags)


if __name__ == '__main__':
    main()
