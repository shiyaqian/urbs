import os
import pyomo.environ
import shutil
import urbs
from datetime import datetime
from pyomo.opt.base import SolverFactory

# SCENARIO GENERATORS

# Commodity prices

def scenario_generator_CO2price(scenario_name, value):
    # e.g. data[commodity].loc[('Campus', 'CO2', 'Env'), 'price']
    
    def scenario(data):
        data['commodity'].loc[('Campus', 'CO2', 'Env'), 'price'] = value
        return data
        
    scenario.__name__ = 'scenario_CO2-prize' + scenario_name  # used for result filenames
    return scenario


def scenario_generator_Elecprice(scenario_name, value):
    # e.g. data[commodity].loc[('Campus', 'Elec', 'price'), 'price']
    
    def scenario(data):
        data['commodity'].loc[('Grid', 'Gridelec', 'Stock'), 'price'] = value
        return data
        
    scenario.__name__ = 'scenario_Elec-prize' + scenario_name  # used for result filenames
    return scenario


# Global quantities

def scenario_generator_wacc(scenario_name, value):
    # e.g. data[commodity].loc[('Campus', 'CO2', 'Env'), 'price']
    
    def scenario(data):
        data['process'].loc[:,'wacc'] = value
        data['transmission'].loc[:,'wacc'] = value
        data['storage'].loc[:,'wacc'] = value
        return data
        
    scenario.__name__ = 'scenario_wacc-' + scenario_name  # used for result filenames
    return scenario