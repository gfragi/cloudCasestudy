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
class iaas_b:
    def nginx(users: int) -> dict: # nginx & redis db
        users = users
        vms: int = math.ceil(users / 1024)
        ram: int = vms * 17
        cores: int = vms * 13
        disk : int = vms * 267.5
        technology = 'iaas_b'
        return vms, ram, cores, disk, technology

    def framework(users: int) -> dict:
        users = users
        vms: int= math.ceil(users / 65535)
        ram: int = vms * 33
        cores: int = vms * 9
        disk : int = vms * (600 + 2.5)
        technology = 'iaas_b'
        return vms, ram, cores, disk, technology
 
    def rel_db(users: int) -> dict:
        users = users
        vms: int = math.ceil(users / 5000)
        ram: int = vms * 25
        cores: int = vms * 9
        disk : int = vms * (100 + 2.5)
        technology = 'iaas_b'
        return vms, ram, cores, disk, technology

    def iaas_total(users: int) -> list:
        users = users
        ram = math.ceil(users / 1024) * 18 + math.ceil(users / 65535) * 33 +  math.ceil(users / 5000) * 25
        cores =  math.ceil(users / 1024) * 14 + math.ceil(users / 65535) * 9 + math.ceil(users / 5000) * 9
        disk = math.ceil(users / 1024) * 288 + math.ceil(users / 65535) * 602.5 \
               + math.ceil(users / 5000) * 102.5 + math.ceil(users / 10000) * 12.5
        nginx: int = math.ceil(users / 1024)
        framework: int= math.ceil(users / 65535)
        rel_db: int = math.ceil(users / 5000)
        instances = nginx + framework + rel_db

        return instances, ram, cores, disk
    
    def total_inst (users: int) -> dict:
        users = users
        nginx: int = math.ceil(users / 1024)
        framework: int= math.ceil(users / 65535)
        rel_db: int = math.ceil(users / 5000)
        instances = nginx + framework + rel_db
        disk = math.ceil(users / 1024) * 288 + math.ceil(users / 65535) * 602.5 \
               + math.ceil(users / 5000) * 102.5 + math.ceil(users / 10000) * 12.5
        return instances, disk

#======================================================================================================================================================


class iaas_a:
    def nginx(users: int) -> dict:
        users = users
        vms: int = math.ceil(users / 1024)
        ram: int = vms * 9
        cores: int = vms * 9
        disk = vms * 257.5
        technology = 'iaas_a'
        return vms, ram, cores, disk, technology

    def framework(users: int) -> dict:
        users = users
        vms: int = math.ceil(users / 65535)
        ram: int = vms * 33
        cores: int = vms * 9
        disk = vms * (600 + 2.5)
        technology = 'iaas_a'
        return vms, ram, cores, disk, technology

    def rel_db(users: int) -> dict:
        users = users
        vms: int = math.ceil(users / 5000)
        ram: int = vms * 25
        cores: int = vms * 9
        disk = vms * (100 + 2.5)
        technology = 'iaas_a'
        return vms, ram, cores, disk, technology

    def memory_db(users: int) -> dict:
        users = users
        vms: int = math.ceil(users / 10000)
        ram: int = vms * 9
        cores: int = vms * 5
        disk = vms * (10 + 2.5)
        technology = 'iaas_a'
        return vms, ram, cores, disk, technology
    

    def iaas_total(users: int) -> list:
        users = users
        ram = math.ceil(users / 1024) * 9 + math.ceil(users / 65535) * 33 + math.ceil(users / 5000) * 25 \
              + math.ceil(users / 10000) * 9
        cores = math.ceil(users / 1024) * 9 + math.ceil(users / 65535) * 9 + math.ceil(users / 5000) * 9 \
                + math.ceil(users / 10000) * 9
        disk = math.ceil(users / 1024) * 257.5 + math.ceil(users / 65535) * 602.5 \
               + math.ceil(users / 5000) * 102.5 + math.ceil(users / 10000) * 12.5
        nginx: int = math.ceil(users / 1024)
        framework: int= math.ceil(users / 65535)
        rel_db: int = math.ceil(users / 5000)
        memory_db: int = math.ceil(users / 10000)
        instances = nginx + framework + rel_db + memory_db
        return instances, ram, cores, disk



    def total_inst (users: int) -> dict:
        users = users
        nginx: int = math.ceil(users / 1024)
        framework: int= math.ceil(users / 65535)
        rel_db: int = math.ceil(users / 5000)
        memory_db: int = math.ceil(users / 10000)
        instances = nginx + framework + rel_db + memory_db
        disk = math.ceil(users / 1024) * 257.5 + math.ceil(users / 65535) * 602.5 \
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
        technology = 'caas'
        return instances, ram, cores, disk,  technology

    def framework(users: int) -> dict:
        users = users
        instances: int = math.ceil(users / 65535)
        ram: int = instances * 32
        cores: int = instances * 8
        disk = instances * 600
        technology = 'caas'
        return instances, ram, cores, disk,  technology

    def rel_db(users: int) -> dict:
        users = users
        instances: int = math.ceil(users / 5000)
        ram: int = instances * 24
        cores: int = instances * 8
        disk = instances * 100
        technology = 'caas'
        return instances, ram, cores, disk,  technology

    def memory_db(users: int) -> dict:
        users = users
        instances: int = math.ceil(users / 10000)
        ram: int = instances * 8
        cores: int = instances * 4
        disk = instances * 10
        technology = 'caas'
        return instances, ram, cores, disk, technology

    def caas_total(users: int):
        users = users
        ram = math.ceil(users / 1024) * 8 + math.ceil(users / 65535) * 32 + math.ceil(users / 5000) * 24 \
              + math.ceil(users / 10000) * 8
        cores = math.ceil(users / 1024) * 8 + math.ceil(users / 65535) * 8 + math.ceil(users / 5000) * 8 \
                + math.ceil(users / 10000) * 8
        disk = math.ceil(users / 1024) * 255 + math.ceil(users / 65535) * 600 \
               + math.ceil(users / 5000) * 100 + math.ceil(users / 10000) * 10
        nginx: int = math.ceil(users / 1024)
        framework: int= math.ceil(users / 65535)
        rel_db: int = math.ceil(users / 5000)
        memory_db: int = math.ceil(users / 10000)
        instances = nginx + framework + rel_db + memory_db
        return instances, ram, cores, disk

    def total_inst (users: int) -> dict:
        users = users
        nginx: int = math.ceil(users / 1024)
        framework: int= math.ceil(users / 65535)
        rel_db: int = math.ceil(users / 5000)
        memory_db: int = math.ceil(users / 10000)
        instances = nginx + framework + rel_db
        disk = math.ceil(users / 1024) * 255 + math.ceil(users / 65535) * 600 \
               + math.ceil(users / 5000) * 100 + math.ceil(users / 10000) * 10
        return instances, disk