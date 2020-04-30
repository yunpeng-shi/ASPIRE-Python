import numpy as np
from unittest import TestCase

from aspire.basis.polar_2d import PolarBasis2D

import os.path
DATA_DIR = os.path.join(os.path.dirname(__file__), 'saved_test_data')


class PolarBasis2DTestCase(TestCase):
    def setUp(self):
        self.basis = PolarBasis2D((8, 8), 4, 32)

    def tearDown(self):
        pass

    def testPolarBasis2DEvaluate_t(self):
        x = np.array([
            [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
             -1.08106869e-17,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
            [ 0.00000000e+00,  0.00000000e+00, -6.40456062e-03, -3.32961020e-03,
             -1.36887927e-02, -5.42770488e-03,  7.63680861e-03,  0.00000000e+00],
            [ 0.00000000e+00,  3.16377602e-03, -9.31273350e-03,  9.46128404e-03,
              1.93239220e-02,  3.79891953e-02,  1.06841173e-02, -2.36467925e-03],
            [ 0.00000000e+00,  1.72736955e-03, -1.00710814e-02,  4.93520304e-02,
              3.77702656e-02,  6.57365438e-02,  3.94739462e-03, -4.41228496e-03],
            [ 4.01551066e-18, -3.08071647e-03, -1.61670565e-02,  8.66886286e-02,
              5.09898409e-02,  7.19313349e-02,  1.68313715e-02,  5.19180892e-03],
            [ 0.00000000e+00,  2.87262215e-03, -3.37732956e-02,  4.51706505e-02,
              5.72215879e-02,  4.63553081e-02,  1.86552175e-03,  1.12608805e-02],
            [ 0.00000000e+00,  2.77905016e-03, -2.77499404e-02, -4.02645374e-02,
             -1.54969139e-02, -1.66229153e-02, -2.07389259e-02,  6.64060546e-03],
            [ 0.00000000e+00,  0.00000000e+00,  5.20080934e-03, -1.06788196e-02,
             -1.14761672e-02, -1.27443126e-02, -1.15563484e-02,  0.00000000e+00]
        ])
        pf = self.basis.evaluate_t(x)
        result = np.array([
            [ 0.38243133-1.00188796e-17j,  0.38243133-1.00188796e-17j,
              0.38243133-1.00188796e-17j,  0.38243133-1.00188796e-17j,
              0.38243133-1.00188796e-17j,  0.38243133-1.00188796e-17j,
              0.38243133-1.00188796e-17j,  0.38243133-1.00188796e-17j,
              0.38243133-1.00188796e-17j,  0.38243133-1.00188796e-17j,
              0.38243133-1.00188796e-17j,  0.38243133-1.00188796e-17j,
              0.38243133-1.00188796e-17j,  0.38243133-1.00188796e-17j,
              0.38243133-1.00188796e-17j,  0.38243133-1.00188796e-17j,
              0.38243133+1.00188796e-17j,  0.38243133+1.00188796e-17j,
              0.38243133+1.00188796e-17j,  0.38243133+1.00188796e-17j,
              0.38243133+1.00188796e-17j,  0.38243133+1.00188796e-17j,
              0.38243133+1.00188796e-17j,  0.38243133+1.00188796e-17j,
              0.38243133+1.00188796e-17j,  0.38243133+1.00188796e-17j,
              0.38243133+1.00188796e-17j,  0.38243133+1.00188796e-17j,
              0.38243133+1.00188796e-17j,  0.38243133+1.00188796e-17j,
              0.38243133+1.00188796e-17j,  0.38243133+1.00188796e-17j],
            [ 0.3249317 +1.47839074e-01j,  0.34595014+1.06355385e-01j,
              0.36957165+5.69575710e-02j,  0.39045046+2.17911953e-03j,
              0.4063995 -5.21354967e-02j,  0.41872477-9.98946906e-02j,
              0.43013599-1.38307796e-01j,  0.44144497-1.68826980e-01j,
              0.44960099-1.94794929e-01j,  0.44872328-2.17957567e-01j,
              0.43379428-2.36681249e-01j,  0.40485577-2.47073481e-01j,
              0.36865853-2.45913767e-01j,  0.33597018-2.32971425e-01j,
              0.31616666-2.10791785e-01j,  0.31313975-1.82190396e-01j,
              0.3249317 -1.47839074e-01j,  0.34595014-1.06355385e-01j,
              0.36957165-5.69575710e-02j,  0.39045046-2.17911953e-03j,
              0.4063995 +5.21354967e-02j,  0.41872477+9.98946906e-02j,
              0.43013599+1.38307796e-01j,  0.44144497+1.68826980e-01j,
              0.44960099+1.94794929e-01j,  0.44872328+2.17957567e-01j,
              0.43379428+2.36681249e-01j,  0.40485577+2.47073481e-01j,
              0.36865853+2.45913767e-01j,  0.33597018+2.32971425e-01j,
              0.31616666+2.10791785e-01j,  0.31313975+1.82190396e-01j],
            [ 0.14819172-3.78171176e-03j,  0.15519289+4.75602163e-02j,
              0.17389327+5.53498385e-02j,  0.18146449+1.37089189e-02j,
              0.15674204-3.85815662e-02j,  0.11862477-5.15231953e-02j,
              0.10075763-1.25689290e-02j,  0.11446016+4.53003874e-02j,
              0.15053714+8.11915306e-02j,  0.19116871+7.99536374e-02j,
              0.21025378+5.48466439e-02j,  0.18680217+3.31766117e-02j,
              0.13660805+3.68947359e-02j,  0.1072859 +6.24686168e-02j,
              0.11876919+7.93812474e-02j,  0.14075481+5.85637417e-02j,
              0.14819172+3.78171176e-03j,  0.15519289-4.75602163e-02j,
              0.17389327-5.53498385e-02j,  0.18146449-1.37089189e-02j,
              0.15674204+3.85815662e-02j,  0.11862477+5.15231953e-02j,
              0.10075763+1.25689290e-02j,  0.11446016-4.53003874e-02j,
              0.15053714-8.11915306e-02j,  0.19116871-7.99536374e-02j,
              0.21025378-5.48466439e-02j,  0.18680217-3.31766117e-02j,
              0.13660805-3.68947359e-02j,  0.1072859 -6.24686168e-02j,
              0.11876919-7.93812474e-02j,  0.14075481-5.85637417e-02j],
            [-0.22808599-5.29338933e-02j, -0.22401193-4.33128746e-03j,
             -0.11601473+1.35405676e-02j, -0.02110144-6.65071500e-03j,
             -0.02886296-3.91489616e-02j, -0.05298751-1.95319479e-02j,
             -0.04052728+5.66863498e-02j, -0.03546515+1.13544145e-01j,
             -0.04800556+1.15828804e-01j, -0.05683092+9.72225058e-02j,
             -0.05318826+8.54948014e-02j, -0.06674163+7.94216590e-02j,
             -0.11467046+8.49198927e-02j, -0.12932565+1.06139634e-01j,
             -0.1094488 +1.20159845e-01j, -0.15198775+1.02156797e-01j,
             -0.22808599+5.29338933e-02j, -0.22401193+4.33128746e-03j,
             -0.11601473-1.35405676e-02j, -0.02110144+6.65071500e-03j,
             -0.02886296+3.91489616e-02j, -0.05298751+1.95319479e-02j,
             -0.04052728-5.66863498e-02j, -0.03546515-1.13544145e-01j,
             -0.04800556-1.15828804e-01j, -0.05683092-9.72225058e-02j,
             -0.05318826-8.54948014e-02j, -0.06674163-7.94216590e-02j,
             -0.11467046-8.49198927e-02j, -0.12932565-1.06139634e-01j,
             -0.1094488 -1.20159845e-01j, -0.15198775-1.02156797e-01j]
        ])

        self.assertTrue(np.allclose(pf, result))
