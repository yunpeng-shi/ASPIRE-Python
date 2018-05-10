import  numpy as np
import em_classavg.data_utils as data_utils
import em_classavg.em_main_gpu as em_main_gpu

images = data_utils.mat_to_npy('images')
images = np.transpose(images, axes=(2, 0, 1))  # move to python convention
init_avg_image = data_utils.mat_to_npy('init_avg_image')

is_load_params_from_mat = True

if is_load_params_from_mat:
    trunc_param, beta, ang_jump, max_shift, shift_jump, n_scales, \
    is_remove_outliers, outliers_precent_removal = em_main_gpu.load_matlab_params()

    im_avg_est, im_avg_est_orig, log_lik, opt_latent, outlier_ims_inds = \
        em_main_gpu.run(images, init_avg_image, trunc_param, beta, ang_jump, max_shift, shift_jump,
                    n_scales, is_remove_outliers, outliers_precent_removal)
else:
    im_avg_est, im_avg_est_orig, log_lik, opt_latent, outlier_ims_inds = em_main_gpu.run(images, init_avg_image)
