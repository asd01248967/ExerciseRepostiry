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
- [QuickStart](#QuickStart)
- [Maintainers](#maintainers)

## Background

## Requirements.txt

## QuickStart

## Maintainers

[@Jasper](https://github.com/asd01248967)