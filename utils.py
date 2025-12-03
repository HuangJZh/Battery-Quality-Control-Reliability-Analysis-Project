# utils.py
import numpy as np
import pandas as pd
import scipy.io
import matplotlib.pyplot as plt
from scipy.stats import weibull_min, norm, binom, beta
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings('ignore')

class BatteryDataLoader:
    """NASA电池数据加载器"""
    
    @staticmethod
    def load_battery_data(file_path):
        """加载单个电池数据"""
        data = scipy.io.loadmat(file_path)
        
        # 提取关键字段
        cycles = data['cycle'][:, 0]
        capacity = data['capacity'][:, 0]
        
        # 检查是否有阻抗数据
        if 'impedance' in data:
            impedance = data['impedance'][:, 0]
        else:
            impedance = np.zeros_like(capacity)
            
        return {
            'cycle': cycles,
            'capacity': capacity,
            'impedance': impedance
        }
    
    @staticmethod
    def calculate_lifetime(capacity, threshold=0.8):
        """计算电池寿命（容量衰减到阈值时的循环次数）"""
        initial_capacity = capacity[0]
        target_capacity = threshold * initial_capacity
        
        # 找到第一个低于阈值的点
        below_threshold = np.where(capacity < target_capacity)[0]
        if len(below_threshold) > 0:
            return below_threshold[0]  # 返回循环次数
        else:
            return len(capacity) - 1  # 如果没失效，返回总循环数
    
    @staticmethod
    def extract_lifetimes_from_folder(folder_path, num_batteries=10):
        """从文件夹中提取多个电池的寿命数据"""
        lifetimes = []
        initial_capacities = []
        
        for i in range(1, num_batteries + 1):
            try:
                file_name = f"B{str(i).zfill(4)}.mat"
                file_path = f"{folder_path}/{file_name}"
                
                data = BatteryDataLoader.load_battery_data(file_path)
                lifetime = BatteryDataLoader.calculate_lifetime(data['capacity'])
                lifetimes.append(lifetime)
                initial_capacities.append(data['capacity'][0])
                
            except FileNotFoundError:
                continue
        
        return np.array(lifetimes), np.array(initial_capacities)

class StatisticalAnalyzer:
    """统计分析工具类"""
    
    @staticmethod
    def fit_weibull_distribution(data):
        """拟合威布尔分布"""
        params = weibull_min.fit(data, floc=0)
        k, loc, scale = params
        return {'k': k, 'lambda': scale}
    
    @staticmethod
    def bayesian_update(prior_alpha, prior_beta, successes, trials):
        """贝叶斯更新（Beta-Binomial共轭）"""
        posterior_alpha = prior_alpha + successes
        posterior_beta = prior_beta + trials - successes
        return posterior_alpha, posterior_beta
    
    @staticmethod
    def confidence_interval_proportion(successes, trials, confidence=0.95):
        """比例参数的置信区间（正态近似）"""
        p_hat = successes / trials
        z_alpha = norm.ppf(1 - (1 - confidence) / 2)
        se = np.sqrt(p_hat * (1 - p_hat) / trials)
        lower = p_hat - z_alpha * se
        upper = p_hat + z_alpha * se
        return lower, upper
    
    @staticmethod
    def hypothesis_test_proportion(successes, trials, p0, alpha=0.05, alternative='greater'):
        """比例假设检验"""
        p_hat = successes / trials
        se = np.sqrt(p0 * (1 - p0) / trials)
        z_stat = (p_hat - p0) / se
        
        if alternative == 'greater':
            p_value = 1 - norm.cdf(z_stat)
            reject = p_value < alpha
        elif alternative == 'less':
            p_value = norm.cdf(z_stat)
            reject = p_value < alpha
        else:
            p_value = 2 * (1 - norm.cdf(abs(z_stat)))
            reject = p_value < alpha
            
        return {
            'z_statistic': z_stat,
            'p_value': p_value,
            'reject_H0': reject
        }