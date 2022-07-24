# %%============== Import libraries =========
import math

import numpy as np
import pandas as pd
import warnings
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import stats
from scipy import stats


# %% ================ Create a class for each technology ==================
# Class for IaaS
# noinspection PyMethodParameters
class iaas:
    def nginx(users: int) -> dict: # nginx & redis db
        users = users
        vms: int = math.ceil(users / 1024)
        ram: int = vms * 17
        cores: int = vms * 13
        disk : int = vms * 267.5
        d_type = 'SSD'
        technology = 'iaas'
        
        return vms, ram, cores, disk, d_type, technology

    def framework(users: int) -> dict:
        users = users
        vms: int= math.ceil(users / 65535)
        ram: int = vms * 33
        cores: int = vms * 9
        disk : int = vms * (600 + 2.5)
        d_type = 'HDD'
        technology = 'iaas'
        return vms, ram, cores, disk, d_type, technology
 
    def rel_db(users: int) -> dict:
        users = users
        vms: int = math.ceil(users / 5000)
        ram: int = vms * 25
        cores: int = vms * 9
        disk : int = vms * (100 + 2.5)
        technology = 'iaas'
        d_type = 'SSD'
        return vms, ram, cores, disk, d_type, technology

    def iaas_total(users: int, vm_type: str) -> list:
        vm_types = ['xsmall', 'small', 'medium', 'large'] 
        users = users
        ram = math.ceil(users / 1024) * 18 + math.ceil(users / 65535) * 33 +  math.ceil(users / 5000) * 25
        cores =  math.ceil(users / 1024) * 14 + math.ceil(users / 65535) * 9 + math.ceil(users / 5000) * 9
        disk = math.ceil(users / 1024) * 288 + math.ceil(users / 65535) * 602.5 \
               + math.ceil(users / 5000) * 102.5 + math.ceil(users / 10000) * 12.5

        if vm_type =='xsmall':
            vms = math.ceil(cores/8)
        if vm_type == 'small':
            vms = math.ceil(cores/20)
        if vm_type == 'medium':
            vms = math.ceil(cores/32)
        elif vm_type == 'large':
            vms = math.ceil(cores/64)

        return vms, ram, cores, disk
    
    def total_inst (users: int) -> dict:
        users = users
        nginx: int = math.ceil(users / 1024)
        framework: int= math.ceil(users / 65535)
        rel_db: int = math.ceil(users / 5000)
        instances = nginx + framework + rel_db
        disk = math.ceil(users / 1024) * 288 + math.ceil(users / 65535) * 602.5 \
               + math.ceil(users / 5000) * 102.5 + math.ceil(users / 10000) * 12.5
        return instances, disk
    
    
# Class for CaaS
# noinspection PyMethodParameters
class caas:
    def nginx(users: int) -> dict:
        users = users
        instances: int = math.ceil(users / 1024)
        ram: int = instances * 8
        cores: int = instances * 8
        disk = instances * 255
        d_type = 'SSD'
        technology = 'caas'
        return instances, ram, cores, disk, d_type, technology

    def framework(users: int) -> dict:
        users = users
        instances: int = math.ceil(users / 65535)
        ram: int = instances * 32
        cores: int = instances * 8
        disk = instances * 600
        d_type = 'HDD'
        technology = 'caas'
        return instances, ram, cores, disk, d_type, technology

    def rel_db(users: int) -> dict:
        users = users
        instances: int = math.ceil(users / 5000)
        ram: int = instances * 24
        cores: int = instances * 8
        disk = instances * 100
        d_type = 'SSD'
        technology = 'caas'
        return instances, ram, cores, disk, d_type, technology

    def memory_db(users: int) -> dict:
        users = users
        instances: int = math.ceil(users / 10000)
        ram: int = instances * 8
        cores: int = instances * 4
        disk = instances * 10
        d_type = 'HDD'
        technology = 'caas'
        return instances, ram, cores, disk, d_type, technology

    def caas_total(users: int, inst_type: str):
        users = users
        inst_types = ['xsmall', 'small', 'medium', 'large']
        ram = math.ceil(users / 1024) * 8 + math.ceil(users / 65535) * 32 + math.ceil(users / 5000) * 24 \
              + math.ceil(users / 10000) * 8
        cores = math.ceil(users / 1024) * 8 + math.ceil(users / 65535) * 8 + math.ceil(users / 5000) * 8 \
                + math.ceil(users / 10000) * 8
        disk = math.ceil(users / 1024) * 255 + math.ceil(users / 65535) * 600 \
               + math.ceil(users / 5000) * 100 + math.ceil(users / 10000) * 10
        if inst_type =='xsmall':
            vms = math.ceil(cores/8)
        if inst_type == 'small':
            vms = math.ceil(cores/20)
        if inst_type == 'medium':
            vms = math.ceil(cores/32)
        elif inst_type == 'large':
            vms = math.ceil(cores/64) 
        return vms, ram, cores, disk

    def total_inst (users: int) -> dict:
        users = users
        nginx: int = math.ceil(users / 1024)
        framework: int= math.ceil(users / 65535)
        rel_db: int = math.ceil(users / 5000)
        instances = nginx + framework + rel_db
        disk = math.ceil(users / 1024) * 255 + math.ceil(users / 65535) * 600 \
               + math.ceil(users / 5000) * 100 + math.ceil(users / 10000) * 10
        return instances, disk
    
