import sys
import os
import  random
dirname = (r"C:\Users\Deepika Chandrababu\Desktop\Thesis\bfts-master")
file = (r"C:\Users\Deepika Chandrababu\Desktop\Thesis\bfts-master\bandit.py")
sys.path.append(os.path.dirname(file))

from bandit import Bandit
from datetime import datetime
import yaml
import pandas as pd
import numpy as np
import pcse
from pcse.fileinput import CABOFileReader
from pcse.models import Wofost72_WLP_FD
from pcse.base import ParameterProvider
from pcse.exceptions import WeatherDataProviderError
from pcse.util import WOFOST72SiteDataProvider
from pcse.fileinput import YAMLAgroManagementReader
from pcse.util import WOFOST72SiteDataProvider
from pcse.fileinput import ExcelWeatherDataProvider
from pcse.fileinput import YAMLCropDataProvider

data_dir = (r'C:\Users\Deepika Chandrababu\Desktop\bandits\bfts-master\agro')
soilfile = (r'C:\Users\Deepika Chandrababu\Desktop\bandits\bfts-master\soil\ec3.soil')
basedir = (r"C:\Users\Deepika Chandrababu\Desktop\bandits\bfts-master\samples")

# crop = YAMLCropDataProvider()
# crop.print_crops_varieties()


crops = ['barley', 'cassava', 'chickpea', 'cotton','cowpea',
            'fababean', 'groundnut', 'maize', 'millet', 'mungbean',
            'pigeonpea', 'potato', 'rapeseed', 'sorghum', 'soybean',
            'sugarbeet','sugarcane', 'sunflower', 'sweetpotato', 'wheat',
            'seed_onion']
varieties = ['Spring_barley_301', 'Cassava_VanHeemst_1988', 'Chickpea_VanHeemst_1988', 'Cotton_VanHeemst_1988','Cowpea_VanHeemst_1988',
            'Faba_bean_801', 'Groundnut_VanHeemst_1988', 'Maize_VanHeemst_1988', 'Millet_VanHeemst_1988', 'Mungbean_VanHeemst_1988',
            'Pigeonpea_VanHeemst_1988', 'Potato_701', 'Oilseed_rape_1001', 'Sorghum_VanHeemst_1988', 'Soybean_VanHeemst_1988',
            'Sugarbeet_601','Sugarcane_VanHeemst_1988', 'Sunflower_1101', 'Sweetpotato_VanHeemst_1988', 'Winter_wheat_101',
            'onion_agriadapt']

def variety_name(crop):
    return varieties[crops.index(crop)]

def agro_file(crop):
    return crop + ".agro" 

def n_arms():
    return len(crops)

def agri(crop):
    variety_name = variety_name(crop) 
    agro_cropname = agro_file(crop)
    cropd = YAMLCropDataProvider()
    cropd.set_active_crop(crop,variety_name)
    agromanagement_file= os.path.join(data_dir, agro_cropname)
    agromanagement = YAMLAgroManagementReader(agromanagement_file)
    # print(agromanagement)
    file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])
    print("Sampling file {}...".format(file))
    wdp = ExcelWeatherDataProvider(os.path.join(basedir, file))
    # print(wdp)
    soild = CABOFileReader(soilfile)
    sited = WOFOST72SiteDataProvider(WAV=10, CO2=360, CRAIRC=0.6)
    parameters = ParameterProvider(cropdata=cropd, soildata=soild, sitedata=sited)
    wofsim = Wofost72_WLP_FD(parameters, wdp, agromanagement)
    wofsim.run_till_terminate()
    wofsim.get_output()
    df_summary= pd.DataFrame(wofsim.get_summary_output())
    twso = df_summary["TWSO"].item()
    return twso

def agri_bandit():
    n = n_arms()
    def reward_fn(crop_):
        return lambda: agri(crop_)
    arms = list(map(reward_fn, crops))
    return Bandit(arms)
