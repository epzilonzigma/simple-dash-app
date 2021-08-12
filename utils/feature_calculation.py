import numpy as np
import pandas as pd

def sin_trans(x):
    return np.sin((x-1)*(2.*np.pi/12))

def cos_trans(x):
    return np.cos((x-1)*(2.*np.pi/12))

def construct_input_dataframe(year, month, product_type, price, product_characteristics, umbrella_characteristics):
    df_month_sin = sin_trans(int(month))
    df_month_cos = cos_trans(int(month))
    kids = 0
    dots = 0
    umbrella = 0
    folding = 0
    ruffled = 0
    hat = 0
    poncho = 0


    if 'child' in product_characteristics:
        kids = 1
    if 'dots' in product_characteristics:
        dots = 1
    if product_type == 'umbrella':
        umbrella = 1
    if product_type == 'hat':
        hat = 1
    if product_type == 'poncho':
        poncho = 1
    if 'ruffled' in umbrella_characteristics:
        ruffled = 1
    if 'folding' in umbrella_characteristics:
        folding = 1
        

    df = pd.DataFrame({'Price': price, 'umbrella': umbrella, 'folding': folding, 'poncho': poncho, 'hat': hat, 'dots': dots, 'kids': kids, 'ruffled': ruffled, 'order_month_sin': df_month_sin,'order_month_cos': df_month_cos}, index = [0])

    return df

def predict_order_volume(input, model):
    forecast = model.predict(input).iloc[0]
    return forecast.round()