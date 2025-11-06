import os
import numpy as np
import scipy.io as sio
from self_py_fun.HW8Fun import produce_trun_mean_cov, plot_trunc_mean, plot_trunc_cov

os.chdir(r'C:\Users\swyy1\OneDrive - Emory\GitHub\BIOS584\BIOS-584')

eeg_trunc_obj = sio.loadmat('data/K114_001_BCI_TRN_Truncated_Data_0.5_6.mat')

bp_low = 0.5
bp_upp = 6
electrode_num = 16
electrode_name_ls = ['F3', 'Fz', 'F4', 'T7', 'C3', 'Cz', 'C4', 'T8', 'CP3', 'CP4', 'P3', 'Pz', 'P4', 'PO7', 'PO8', 'Oz']

parent_dir = r'C:\Users\swyy1\OneDrive - Emory\GitHub\BIOS584\BIOS-584'
parent_data_dir = '{}/data'.format(parent_dir)
time_index = np.linspace(0, 800, 25) # This is a hypothetic time range up to 800 ms after each stimulus.

subject_name = 'K114'
session_name = '001_BCI_TRN'

eeg_trunc_signal = eeg_trunc_obj['Signal']
eeg_trunc_type = eeg_trunc_obj['Type']
eeg_trunc_type = np.squeeze(eeg_trunc_type, axis = 1)

K114_trun_mean_cov = produce_trun_mean_cov(eeg_trunc_signal, eeg_trunc_type, electrode_num)
signal_tar_mean, signal_ntar_mean, signal_tar_cov, signal_ntar_cov, signal_all_cov = K114_trun_mean_cov

signal_tar_mean, signal_ntar_mean, signal_tar_cov, signal_ntar_cov, signal_all_cov = K114_trun_mean_cov
plot_trunc_mean(signal_tar_mean, signal_ntar_mean, subject_name, time_index, electrode_num, electrode_name_ls)

plot_trunc_cov(signal_ntar_cov, "Target", time_index, subject_name, electrode_num, electrode_name_ls)
plot_trunc_cov(signal_ntar_cov, "Non-Target", time_index, subject_name, electrode_num, electrode_name_ls)
plot_trunc_cov(signal_ntar_cov, "All", time_index, subject_name, electrode_num, electrode_name_ls)
