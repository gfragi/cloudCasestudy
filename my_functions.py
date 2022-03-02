# %%============== Import libraries =========
import numpy as np
import pandas as pd
import warnings
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import stats
from scipy import stats


#%% ================ Create a class for each technology ==================
# Class for IaaS
class iaas:
    def nginx(users: int) -> dict:
        users = users
        vms: int = users // 1024
        ram: int = vms * (8 + 1)
        cores: int = vms * (8 + 1)
        disk = vms * (255 + 2.5)
        return {'vms': vms, 'ram': ram, 'cores': cores, 'disk': disk}

    def framework(users: int) -> dict:
        users = users
        vms: int = users // 65535
        ram: int = vms * (32 + 1)
        cores: int = vms * (8 + 1)
        disk = vms * (600 + 2.5)
        return {'vms': vms, 'ram': ram, 'cores': cores, 'disk': disk}

    def rel_db(users: int) -> dict:
        users = users
        vms: int = users // 5000
        ram: int = vms * (24 + 1)
        cores: int = vms * (8 + 1)
        disk = vms * (100 + 2.5)
        return {'vms': vms, 'ram': ram, 'cores': cores, 'disk': disk}

    def memory_db(users: int) -> dict:
        users = users
        vms: int = users // 10000
        ram: int = vms * (8 + 1)
        cores: int = vms * (4 + 1)
        disk = vms * (10 + 2.5)
        return {'vms': vms, 'ram': ram, 'cores': cores, 'disk': disk}

# Class for CaaS
class caas:
    def nginx(users: int) -> dict:
        users = users
        instances: int = users // 1024
        ram: int = instances * 8
        cores: int = instances * 8
        disk = instances * 255
        return {'instances': instances, 'ram': ram, 'cores': cores, 'disk': disk}

    def framework(users: int) -> dict:
        users = users
        instances: int = users // 65535
        ram: int = instances * 32
        cores: int = instances * 8
        disk = instances * 600
        return {'instances': instances, 'ram': ram, 'cores': cores, 'disk': disk}

    def rel_db(users: int) -> dict:
        users = users
        instances: int = users // 5000
        ram: int = instances * 24
        cores: int = instances * 8
        disk = instances * 100
        return {'instances': instances, 'ram': ram, 'cores': cores, 'disk': disk}

    def memory_db(users: int) -> dict:
        users = users
        instances: int = users // 10000
        ram: int = instances * 8 + 1
        cores: int = instances * 4
        disk = instances * 10
        return {'instances': instances, 'ram': ram, 'cores': cores, 'disk': disk}
