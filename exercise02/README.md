# Exercise_Project
### Author: Jasper

[![standard-readme compliant](https://img.shields.io/badge/Exercise-02-green)](https://github.com/asd01248967/workspace)

This exercise_project is used to construct LNMP enviroament to show up the website,  just only sample phpinfo(), maybe someone nave interesting to edit more stronger and more function, I will appreciate you

This repository contains:

1. [ansible.cfg](ansible.cfg) - ansible configuration file, keep with default, but can edit parameter you want to, mentioning you! if you not very familiar with these parameter, check offical Doc. or get wrong! 
2. [hosts](hosts) - For Ansbile used to  pattern mode, context is list you wanna be  ansbile managered node mechine's IP / FQDN / Hostname,can taking these mechine as group as well, then will flexible execute some particually jobs with order  requirements
3. [playbook.yml](playbook.yml) - Ansible playbook, This file is major dirver ansible to execute every role's main.yml, have four role: common、db、webserver、php, every role contain main.yml file and as the case may be append template file
4. [README.md](README.md) - Explain how this repositry's file used to what enviroment construct and how to usage
5. [role](roles) - deppend particular purpose create mapping direction to finish job, and then by file in subdirecton to driver behave is 
## Table of Contents

- [Background](#background)
- [Requirements](#Requirements.txt)
- [Quick Start](#Quick Start)
- [Maintainers](#maintainers)

## Background

I wanna to try and learn use ansible to construct a LNMP enviroment automatic,and can flexible modifity behave or order as well

This exercise_project is used to construct LNMP enviroament to show up the website, just only sample phpinfo(), maybe someone nave interesting to edit more stronger and more function, I will appreciate you

Attitude Is Everything, keep goin, keep moving, fall forward

The exercise00.py goals for this repository are:

> once done ansilbe requirement(ansible, git, ssh key pass to node, test ssh, host file),keep workdir in the path same with playbook.yml, then you can through command to construct a LNMP enviroment

## Requirements.txt

Used module for exercise02:
```sh
1.yum install ansilbe git
2.git clone https://github.com/asd01248967/exercise_project.git
3.cd exercise_project
4.edit host file (adjust to your enviroment match-list for managed node)
5.ansible controller generator public key and pass to node mechine 
 > ssh_keygen
 > cat ~/.ssh/id_rsa.pub & copy (in ansible controller)
 > vim ~/.ssh/authorized_keys & paste(in ansible node)
6.test ssh connection : ssh node_IP, if sucessfly will present change and node_IP
7.test ansilbe : ansible all -m shell -a "echo hello"
8.workdir same as playbook.yml, command line : ansible-playbook playbook.yml
```

## Quick Start

```sh
1.ansible-playbook playbook.yml
```
## Maintainers

[@Jasper](https://github.com/asd01248967)