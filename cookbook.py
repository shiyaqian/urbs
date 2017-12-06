import os
import pyomo.environ
import shutil
import numpy as np
import urbs
from datetime import datetime
from pyomo.opt.base import SolverFactory

# SCENARIO GENERATORS
# In this script a variety of scenario generator functions are defined to
# facilitate scenario definitions.

# !IMPORTANT NOTE!
# All texts must be explicitely typed in as a string, e.g. 'Campus'.


def scenario_base(data):
    return data


# Global quantities

def sc_CO2limit(value):
    # Used to set global CO2 limit

    def scenario(data):
        data['global_prop'].loc['CO2 limit', 'value'] = value
        return data

    scenario.__name__ = 'scenario_CO2-limit-' + '{:04}'.format(value)
    return scenario


def sc_wacc(value):
    # Set wacc

    def scenario(data):
        data['process'].loc[:, 'wacc'] = value
        data['transmission'].loc[:, 'wacc'] = value
        data['storage'].loc[:, 'wacc'] = value
        return data

    scenario.__name__ = 'scenario_wacc-' + '{:03}'.format(value)
    return scenario


# Commodity

def sc_1comprop(site, com, type, property, value):
    # variation of 1 property of 1 given commodity

    def scenario(data):
        data['commodity'].loc[(site, com, type), property] = value
        return data

    scenario.__name__ = ('scenario_' + site + com + property +
                         '{:04}'.format(value)
                         )
    return scenario


def sc_2comprop(site1, site2, com1, com2, type1, type2, property1, property2,
                value1, value2):
    # variation of 2 properties of 2 given process

    def scenario(data):
        data['commodity'].loc[(site1, com1, type1), property1] = value1
        data['commodity'].loc[(site2, com2, type2), property2] = value2
        return data

    scenario.__name__ = ('scenario_' + site1 + com1 + property1 +
                         '{:04}'.format(value1) + site2 + com2 + property2 +
                         '{:04}'.format(value2)
                         )
    return scenario


# Process

def sc_1proprop(site, process, property, value):
    # variation of 1 property of 1 given process

    def scenario(data):
        data['process'].loc[(site, process), property] = value
        return data

    scenario.__name__ = ('scenario_' + site + process + property +
                         '{:04}'.format(value)
                         )
    return scenario


def sc_2proprop(site1, site2, process1, process2, property1, property2,
                value1, value2):
    # variation of 2 properties of 2 given process

    def scenario(data):
        data['process'].loc[(site1, process1), property1] = value1
        data['process'].loc[(site2, process2), property2] = value2
        return data

    scenario.__name__ = ('scenario_' + site1 + process1 + property1 +
                         '{:04}'.format(value1) + site2 + process2 +
                         property2 + '{:04}'.format(value2)
                         )
    return scenario


# Process commodities

def sc_1procomprop(process, com, dir, property, value):
    # variation of 1 property of 1 given process-commodity

    def scenario(data):
        data['process-commodity'].loc[(process, com, dir), property] = value
        return data

    scenario.__name__ = ('scenario_' + process + com + dir + property +
                         '{:04}'.format(value)
                         )
    return scenario


def sc_2procomprop(process1, process2, com1, com2, dir1, dir2, property1,
                   property2, value1, value2):
    # variation of 2 properties of 2 given process-commodity

    def scenario(data):
        data['process-commodity'].loc[(process1, com1, dir1), property1] = value1
        data['process-commodity'].loc[(process2, com2, dir2), property2] = value2
        return data

    scenario.__name__ = ('scenario_' + process1 + com1 + dir1 + property1 +
                         '{:04}'.format(value1) + process2 + com2 + dir2 +
                         property2 + '{:04}'.format(value2)
                         )
    return scenario


# Storage

def sc_1stoprop(site, sto, com, property, value):
    # variation of 1 property of 1 given storage

    def scenario(data):
        data['storage'].loc[(site, sto, com), property] = value
        return data

    scenario.__name__ = ('scenario_' + site + sto + com + property +
                         '{:04}'.format(value)
                         )
    return scenario


def sc_2stoprop(site1, site2, sto1, sto2, com1, com2, property1,
                property2, value1, value2):
    # variation of 2 properties of 2 given storages

    def scenario(data):
        data['process-commodity'].loc[(site1, sto1, com1), property1] = value1
        data['process-commodity'].loc[(site2, sto2, com2), property2] = value2
        return data

    scenario.__name__ = ('scenario_' + site1 + sto1 + com1 + property1 +
                         '{:04}'.format(value1) + site2 + sto2 + com2 +
                         property2 + '{:04}'.format(value2)
                         )
    return scenario

    # CO2_limits with Commodity Change
def sc_1comprop_co2Limit(site, com, type, property, value1, value2):
    # variation of 1 property of 1 given commodity

    def scenario(data):
        data['commodity'].loc[(site, com, type), property] = value1
        data['global_prop'].loc['CO2 limit', 'value'] = value2
        return data

    scenario.__name__ = ('scenario_' + site + com + property +
                         '{:04}'.format(value1) + 'scenario_CO2-limit-' + '{:04}'.format(value2)
                         )

    return scenario

def sc_1comprop_co2Limit_ohneW(site1, com1, type1, property1, value1,
                         site2, process2, property2, value2,
                         site3, process3, property3, value3,
                         site4, process4, property4, value4,
                         site5, process5, property5, value5,
                         site6, process6, property6, value6,
                         site7, process7, property7, value7,
                         site8, process8, property8, value8,
                         site9, process9, property9, value9,
                         site10, process10, property10, value10,
                         site11, process11, property11, value11,
                         site12, process12, property12, value12, value13):
    # variation of 1 property of 1 given commodity

    def scenario(data):
        data['commodity'].loc[(site1, com1, type1), property1] = value1
        data['process'].loc[(site2, process2), property2] = value2
        data['process'].loc[(site3, process3), property3] = value3
        data['process'].loc[(site4, process4), property4] = value4
        data['process'].loc[(site5, process5), property5] = value5
        data['process'].loc[(site6, process6), property6] = value6
        data['process'].loc[(site7, process7), property7] = value7
        data['process'].loc[(site8, process8), property8] = value8
        data['process'].loc[(site9, process9), property9] = value9
        data['process'].loc[(site10, process10), property10] = value10
        data['process'].loc[(site11, process11), property11] = value11
        data['process'].loc[(site12, process12), property12] = value12
        data['global_prop'].loc['CO2 limit', 'value'] = value13
        return data

    scenario.__name__ = ('scenario_' + site1 + com1 + property1 +
                         '{:04}'.format(value1) + 'scenario_CO2-limit-' + '{:04}'.format(value13)
                         )

    return scenario