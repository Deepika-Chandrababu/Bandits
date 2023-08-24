from environments.gaussian_jun import linear_means,linear_bandit,polynomial_means,polynomial_bandit
from environments.captions_jun import captions_means,captions_bandit
from environments.poisson_olivier import poisson_oli_means,poisson_oli_bandit
from environments.poisson_exp import poisson_exp_means,poisson_exp_bandit
from environments.scaled_gaussian import scaled_gaussian_means,scaled_gaussian_bandit
import environments.gaussian_jun_lin_var as gj_linvar
from environments.agri_crop import agri_bandit
import numpy as np 
import ast

def parse_args(s):
    args_str = s[s.find("{"):s.find("}")+1]
    return ast.literal_eval(args_str)

def select(name):
    if name.startswith("linear{"):
        args = parse_args(name)
        n = args["n"] 
        variance = args["var"] 
        real_means = linear_means(n)
        bandit = linear_bandit(n, variance)
        return (real_means, bandit)
    elif name.startswith( "agri{"):
        args = parse_args(name)
        real_means = [32.54180977803026,768.0174635463128,84.85967726183506,3.3254387145815225,782.6908605684513,
                      168.04063570750495,90.49841647837853,326.52997868419953,19.09290083330714,234.93081563523785,
                      274.95080955707044,1051.3406627810841,39.62677518336869,478.73592004844875,62.429126626909664,
                      34.836258721620986,90.14560447381182,16.769891986055104,11.49314723943683]
        bandit = agri_bandit( )
        return (real_means, bandit)
    elif name.startswith( "polynomial{"):
        args = parse_args(name)
        n = args["n"]
        variance = args["var"]
        real_means = polynomial_means(n)
        bandit = polynomial_bandit(n, variance)
        return (real_means, bandit)
    elif name.startswith("linear-linvar{"):
        args = parse_args(name)
        n = args["n"]
        max_variance = args["max_var"]
        min_variance = args["min_var"]
        real_means = linear_means(n)
        bandit = gj_linvar.linear_bandit(n, max_variance, min_variance)
        return (real_means, bandit)
    elif name.startswith( "polynomial-linvar{"):
        args = parse_args(name)
        n = args["n"]
        max_variance = args["max_var"]
        min_variance = args["min_var"]
        real_means = polynomial_means()
        bandit = gj_linvar.polynomial_bandit(n, max_variance, min_variance)
        return (real_means, bandit)
    elif name.startswith( "captions{"):
        args = parse_args(name)
        n = args["n"]
        real_means = captions_means(n)
        bandit =captions_bandit(n)
        return (real_means, bandit)
    elif name.startswith( "poisson_olivier{"):
        args = parse_args(name)
        n = args["n"]
        real_means = poisson_oli_means(n)
        bandit = poisson_oli_bandit(n)
        return (real_means, bandit)
    elif name.startswith( "poisson-exp{"):
        real_means = poisson_exp_means()
        bandit = poisson_exp_bandit()
        return (real_means, bandit)
    elif name.startswith( "scaled_gaussian{"):
        args = parse_args(name)
        n = args["n"]
        real_means = scaled_gaussian_means()[:n]
        bandit = scaled_gaussian_bandit(n)
        return (real_means, bandit)
    else:
       choices = \
            ["linear{n,var}", "polynomial{n,var}", \
             "captions{n}", "poisson-olivier{n}", "scaled_gaussian{n}"]
       raise ValueError("Invalid environment \"" + name + "\", " + \
            "choose from " + \
            "[" + ", ".join(choices) + "]") 
