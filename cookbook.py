import os
import pyomo.environ
import shutil
import numpy as np
import urbs
from datetime import datetime
from pyomo.opt.base import SolverFactory

# SCENARIO GENERATORS

# Commodity prices


def scen_co2price(site, value):
    # scenario_name_suffix, site = string, value = float

    def scenario(data):
        data['commodity'].loc[(site, 'CO2', 'Env'), 'price'] = value
        return data

    scenario.__name__ = 'scenario_CO2-price-' + '{:04}'.format(value)
    # used for result filenames
    return scenario


def scen_gasprice(site, value):
    # scenario_name_suffix, site = string, value = float

    def scenario(data):
        data['commodity'].loc[(site, 'Gas', 'Stock'), 'price'] = value
        return data

    scenario.__name__ = 'scenario_Gas-price-' + '{:04}'.format(value)
    # used for result filenames
    return scenario


def scen_elecprice(site, value):
    # scenario_name_suffix, site = string, value = float

    def scenario(data):
        data['commodity'].loc[(site, 'Gridelec', 'Stock'), 'price'] = value
        return data

    scenario.__name__ = 'scenario_Elec-price-' + '{:04}'.format(value)
    # used for result filenames
    return scenario


def scen_geothprice(site, value):
    # scenario_name_suffix, site = string, value = float

    def scenario(data):
        data['commodity'].loc[(site, 'Geothermal', 'Stock'), 'price'] = value
        return data

    scenario.__name__ = 'scenario_GT-price-' + '{:04}'.format(value)
    # used for result filenames
    return scenario


# Global quantities

def scen_wacc(value):
    # scenario_name_suffix, site = string, value = float

    def scenario(data):
        data['process'].loc[:, 'wacc'] = value
        data['transmission'].loc[:, 'wacc'] = value
        data['storage'].loc[:, 'wacc'] = value
        return data

    scenario.__name__ = 'scenario_wacc-' + '{:03}'.format(value)
    # used for result filenames
    return scenario


# Scenario lists

def scen_1d_paramvar(scen_param, site, min, max, steps):
    scenario_list = []

    for index in np.linspace(min, max, steps):
        scenario_list.append(scen_param(site, index))
    
    return scenario_list
    

# def scen_2d_paramvar(scen_param1, site1, min1, max1, steps1,
        # scen_param2, site2, min2, max2, steps2):
    # scenario_list = []

    # for index1 in np.linspace(min1, max1, steps1):
        # scenario_list.append(
            # scen(
            # '{:06}'.format(index),
            # site1,
            # index1))
    
    # return scenario_list
