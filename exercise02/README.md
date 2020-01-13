# Exercise_Project
### Author: Jasper

[![standard-readme compliant](https://img.shields.io/badge/Exercise-02-green)](https://github.com/asd01248967/workspace)

This exercise_project is used to construct LNMP enviroament to show up the website,  just only sample phpinfo(), maybe someone nave interesting to edit more stronger and more function, I will appreciate you

This repository contains:

1. [ansible.cfg](ansible.cfg) - ansible configuration file, keep with default, but can edit parameter you want to, mentioning you! if you not very familiar with these parameter, check offical Doc. or get wrong! 
2. [hosts](hosts) - For Ansbile used to  pattern mode, context is list you wanna be  ansbile managered node mechine's IP / FQDN / Hostname,can taking these mechine as group as well, then will flexible execute some particually jobs with order  requirements
3. [playbook.yml](playbook.yml) - Ansible playbook, This file is major dirver ansible to execute every role's main.yml, have four role: common、db、webserver、php, every role contain main.yml file and as the case may be append template file
4. [README.md](README.md) - Explain how this repositry's file used to what enviroment construct and how to usage

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)

## Background

Attitude Is Everything, keep goin, keep moving, fall forward

This Exercise is used for increase personal coding skill that reach career destination

I will continue looking for something interesting project or little idea to practice

The exercise01.py goals for this repository are:

> For this exercise01 practice compute how many vocabularies exactly same as Attitude with one hundred points as well ,Suppose A is Point 1, B is point2, c is point 3, So on and so forth

## Requirements.txt

Used module for exercise01:
```sh
Regular expression
Openpyxl
```

## Quick Start

```sh

1. Create a Python Virtual Environment
2. git clone this_repo
3. cd this_repo
4. pip install re Openpyxl
5. python exercise01.py
6. Print result：
{'carpenter', 'Wednesday', 'delivery', 'pursue', 'whiskey', 'inflation', 'thirty', 'fountain', 'excellent', 'discipline', 'companion', 'socialism', 'elsewhere', 'eventual', 'hospital', 'corridor', 'personal', 'intellect', 'repress', 'clockwise', 'stress', ....etc}
It cost 1.433895 sec

```
## Maintainers

[@Jasper](https://github.com/asd01248967)