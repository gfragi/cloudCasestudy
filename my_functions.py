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
    def nginx(users: int) -> dict:
        users = users
        vms: int = math.ceil(users / 1024)
        ram: int = vms * (8 + 1)
        cores: int = vms * (8 + 1)
        disk = vms * (255 + 2.5)
        technology = 'iaas'
        return vms, ram, cores, disk, technology

    @property
    def framework(users: int) -> dict:
        users = users
        vms: int = math.ceil(users / 65535)
        ram: int = vms * (32 + 1)
        cores: int = vms * (8 + 1)
        disk = vms * (600 + 2.5)
        technology = 'iaas'
        return vms, ram, cores, disk, technology

    @property
    def rel_db(users: int) -> dict:
        users = users
        vms: int = math.ceil(users / 5000)
        ram: int = vms * (24 + 1)
        cores: int = vms * (8 + 1)
        disk = vms * (100 + 2.5)
        technology = 'iaas'
        return vms, ram, cores, disk, technology

    @property
    def memory_db(users: int) -> dict:
        users = users
        vms: int = math.ceil(users / 10000)
        ram: int = vms * (8 + 1)
        cores: int = vms * (4 + 1)
        disk = vms * (10 + 2.5)
        technology = 'iaas'
        return vms, ram, cores, disk, technology

    def iaas_total(users: int):
        users = users
        ram = math.ceil(users / 1024) * 9 + math.ceil(users / 65535) * 33 + math.ceil(users / 5000) * 25 \
              + math.ceil(users / 10000) * 9 + 32
        cores = math.ceil(users / 1024) * 9 + math.ceil(users / 65535) * 9 + math.ceil(users / 5000) * 5 \
                + math.ceil(users / 10000) * 5 + 16
        disk = math.ceil(users / 1024) * 257.5 + math.ceil(users / 65535) * 602.5 \
               + math.ceil(users / 5000) * 102.5 + math.ceil(users / 10000) * 12.5 + 100

        return ram, cores, disk


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
        return instances, ram, cores, disk, technology

    def framework(users: int) -> dict:
        users = users
        instances: int = math.ceil(users / 65535)
        ram: int = instances * 32
        cores: int = instances * 8
        disk = instances * 600
        technology = 'caas'
        return instances, ram, cores, disk, technology

    def rel_db(users: int) -> dict:
        users = users
        instances: int = math.ceil(users / 5000)
        ram: int = instances * 24
        cores: int = instances * 8
        disk = instances * 100
        technology = 'caas'
        return instances, ram, cores, disk, technology

    def memory_db(users: int) -> dict:
        users = users
        instances: int = math.ceil(users / 10000)
        ram: int = instances * 8 + 1
        cores: int = instances * 4
        disk = instances * 10
        technology = 'caas'
        return instances, ram, cores, disk, technology

    def caas_total(users: int):
        users = users
        ram = math.ceil(users / 1024) * 8 + math.ceil(users / 65535) * 32 + math.ceil(users / 5000) * 24 \
              + math.ceil(users / 10000) * 8 + 32.5
        cores = math.ceil(users / 1024) * 8 + math.ceil(users / 65535) * 8 + math.ceil(users / 5000) * 8 \
                + math.ceil(users / 10000) * 8 + 1.5
        disk = math.ceil(users / 1024) * 255 + math.ceil(users / 65535) * 600 \
               + math.ceil(users / 5000) * 100 + math.ceil(users / 10000) * 10
        return ram, cores, disk
