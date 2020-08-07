from ctypes import c_int

import logging
import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
import pycuda.gpuarray as gpuarray
from cufinufft import cufinufft

from aspire.nfft import Plan
from aspire.utils import ensure

logger = logging.getLogger(__name__)

class cuFINufftPlan(Plan):
    def __init__(self, sz, fourier_pts, epsilon=1e-15, many=0, **kwargs):
        """
        A plan for non-uniform FFT in 2D or 3D.

        :param sz: A tuple indicating the geometry of the signal
        :param fourier_pts: The points in Fourier space where the Fourier transform is to be calculated,
            arranged as a dimension-by-K array. These need to be in the range [-pi, pi] in each dimension.
        :param epsilon: The desired precision of the NUFFT
        :param many: Optional integer indicating if you would like to compute a batch of `many`
        transforms.  Implies vol_f.shape is (..., `many`). Defaults to 0 which disables batching.
        """

        # Passing "many" expects one large higher dimensional array.
        #   Set some housekeeping variables so we can discern how to handle the dims later.
        self.many = False
        self.ntransforms = 1
        if many != 0:
            self.many = True
            self.ntransforms = many

        # Basic dtype passthough.
        dtype = fourier_pts.dtype
        if dtype == np.float64 or dtype == np.complex128:
            self.dtype = np.float64
            self.complex_dtype = np.complex128
        elif dtype == np.float32 or dtype == np.complex64:
            self.dtype = np.float32
            self.complex_dtype = np.complex64
        else:
            raise RuntimeError("Unsupported dtype encountered")

        self.sz = sz
        self.dim = len(sz)
        # TODO: Following the row major conversion, this should no longer happen.
        if fourier_pts.flags.f_contiguous:
            logger.warning('cufinufft has caught an F_CONTIGUOUS array,'
                           ' `fourier_pts` will be copied to C_CONTIGUOUS.')
        self.fourier_pts = np.asarray(np.mod(fourier_pts + np.pi, 2 * np.pi) - np.pi, order='C', dtype=self.dtype)
        self.num_pts = fourier_pts.shape[1]
        self.epsilon = max(epsilon, np.finfo(self.dtype).eps)

        self._transform_plan = cufinufft(2, self.sz, -1, self.epsilon, ntransforms=self.ntransforms,
                                         dtype=self.dtype)

        self._adjoint_plan = cufinufft(1, self.sz, 1, self.epsilon, ntransforms=self.ntransforms,
                                       dtype=self.dtype)

    def transform(self, signal):
        """
        Compute the NUFFT transform using this plan instance.

        :param signal: Signal to be transformed. For a single transform,
        this should be a a 1, 2, or 3D array matching the plan `sz`.
        For a batch, signal should have shape `(*sz, many)`.

        :returns: Transformed signal of shape `num_pts` or
        `(many, num_pts)`.
        """

        assert signal.dtype == self.dtype or signal.dtype == self.complex_dtype

        sig_shape = signal.shape
        if self.many:
            sig_shape = signal.shape[:-1]         # order...
        ensure(sig_shape == self.sz, f'Signal to be transformed must have shape {self.sz}')

        # Note that it would be nice to address this ordering enforcement after the C major conversions.
        signal_gpu = gpuarray.to_gpu(signal.astype(self.complex_dtype, copy=False, order='F'))

        # This ordering situation is a little strange, but it works.
        result_gpu = gpuarray.GPUArray((self.ntransforms, self.num_pts), dtype=self.complex_dtype, order='C')

        fourier_pts_gpu = gpuarray.to_gpu(self.fourier_pts.astype(self.dtype))
        self._transform_plan.set_pts(self.num_pts, *fourier_pts_gpu)

        self._transform_plan.execute(result_gpu, signal_gpu)

        result = result_gpu.get()

        if not self.many:
            result = result[0]

        return result

    def adjoint(self, signal):
        """
        Compute the NUFFT adjoint using this plan instance.

        :param signal: Signal to be transformed. For a single transform,
        this should be a a 1D array of len `num_pts`.
        For a batch, signal should have shape `(many, num_pts)`.

        :returns: Transformed signal `(sz)` or `(sz, many)`.
        """

        assert signal.dtype == self.complex_dtype or signal.dtype == self.dtype
        if self.dim == 3 and self.dtype == np.float64:
            raise TypeError('Currently the 3d1 sub-problem method is singles only.')

        signal_gpu = gpuarray.to_gpu(signal.astype(self.complex_dtype, copy=False, order='C'))

        # Note that it would be nice to address this ordering enforcement after the C major conversions.
        result_gpu = gpuarray.GPUArray((*self.sz, self.ntransforms), dtype=self.complex_dtype, order='F')

        fourier_pts_gpu = gpuarray.to_gpu(self.fourier_pts)

        self._adjoint_plan.set_pts(self.num_pts, *fourier_pts_gpu)

        self._adjoint_plan.execute(signal_gpu, result_gpu)

        result = result_gpu.get()

        if not self.many:
            result = result[...,0]

        return result
