

OK_OPS_100 = [
    ('HCTSA_CO_AutoCorr', 0.455836),
    ('HCTSA_CO_CompareMinAMI', 0.812098),
    ('HCTSA_CO_Embed2', 0.485682),
    ('HCTSA_CO_Embed2_AngleTau', 0.618405),
    ('HCTSA_CO_Embed2_Basic', 0.45301),
    ('HCTSA_CO_FirstMin', 0.468537),
    ('HCTSA_CO_FirstZero', 0.454108),
    ('HCTSA_CO_HistogramAMI', 0.429133),
    ('HCTSA_CO_NonlinearAutocorr', 0.452267),
    ('HCTSA_CO_RM_AMInformation', 0.454285),
    ('HCTSA_CO_TranslateShape', 0.388259),
    ('HCTSA_CO_f1ecac', 0.509994),
    ('HCTSA_CO_fzcglscf', 0.448804),
    ('HCTSA_CO_glscf', 0.452579),
    ('HCTSA_CO_tc3', 0.447589),
    ('HCTSA_CO_trev', 0.466574),
    ('HCTSA_CP_ML_StepDetect', 0.434192),
    ('HCTSA_DN_Burstiness', 0.458042),
    ('HCTSA_DN_Cumulants', 0.450433),
    ('HCTSA_DN_CustomSkewness', 0.452511),
    ('HCTSA_DN_HighLowMu', 0.446394),
    ('HCTSA_DN_HistogramMode', 0.448977),
    ('HCTSA_DN_Mean', 0.448335),
    ('HCTSA_DN_MinMax', 0.448189),
    ('HCTSA_DN_Moments', 0.450407),
    ('HCTSA_DN_OutlierTest', 0.460275),
    ('HCTSA_DN_ProportionValues', 0.455138),
    ('HCTSA_DN_Quantile', 0.452477),
    ('HCTSA_DN_RemovePoints', 0.501206),
    ('HCTSA_DN_Spread', 0.45608),
    ('HCTSA_DN_TrimmedMean', 0.45544),
    ('HCTSA_DN_Withinp', 0.447668),
    ('HCTSA_DN_cv', 0.452507),
    ('HCTSA_DN_pleft', 0.456524),
    ('HCTSA_EN_ApEn', 0.475962),
    ('HCTSA_EN_DistributionEntropy', 0.440973),
    ('HCTSA_EN_PermEn', 0.472049),
    ('HCTSA_EN_RM_entropy', 0.45098),
    ('HCTSA_EN_SampEn', 0.573267),
    ('HCTSA_EN_Shannonpdf', 0.451591),
    ('HCTSA_EN_TSentropy', 0.455837),
    ('HCTSA_EX_MovingThreshold', 0.448276),
    ('HCTSA_HT_HypothesisTest', 0.460972),
    ('HCTSA_MD_pNN', 0.446215),
    ('HCTSA_MD_polvar', 0.453528),
    ('HCTSA_MD_rawHRVmeas', 0.43417),
    ('HCTSA_MF_arfit', 0.527739),
    ('HCTSA_NL_MS_LZcomplexity', 0.442058),
    ('HCTSA_NL_MS_fnn', 0.493602),
    ('HCTSA_NL_TSTL_PoincareSection', 0.532851),
    ('HCTSA_PH_ForcePotential', 0.365595),
    ('HCTSA_RN_Gaussian', 0.387117),
    ('HCTSA_SB_BinaryStretch', 0.399313),
    ('HCTSA_SB_MotifTwo', 0.357184),
    ('HCTSA_SC_HurstExponent', 0.329066),
    ('HCTSA_SC_fastdfa', 0.442697),
    ('HCTSA_ST_Length', 0.378771),
    ('HCTSA_ST_LocalExtrema', 0.361439),
    ('HCTSA_ST_SimpleStats', 0.45575),
    ('HCTSA_SY_DynWin', 1.1968),
    ('HCTSA_SY_LinearTrend', 0.461867),
    ('HCTSA_SY_LocalGlobal', 0.601483),
    ('HCTSA_SY_RangeEvolve', 0.468541),
    ('HCTSA_SY_SpreadRandomLocal', 1.64848),
    ('HCTSA_SY_StatAv', 0.453558),
    ('HCTSA_SY_StdNthDer', 0.463994),
]


FAILED_OPS_100 = [
    ("HCTSA_CO_AddNoise", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_CO_AutoCorrShape", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_CO_Embed2_Dist", "'h' undefined near line 71 column 6"),
    ("HCTSA_CO_Embed2_Shapes", "'poissfit' undefined near line 132 column 5"),
    ("HCTSA_CO_StickAngles", "This function requires Matlab's Signal Processing Toolbox"),
    ("HCTSA_CO_TSTL_AutoCorrMethod", "help: 'acf' not found"),
    ("HCTSA_CO_TSTL_amutual", "Input signal must be a scalar time series"),
    ("HCTSA_CO_TSTL_amutual2", "help: 'amutual2' not found"),
    ("HCTSA_CP_l1pwc_sweep_lambda", "warning: operator -: automatic broadcasting operation applied\nwarning: division by zero\nA(I) = X: X must have the same size as I"),
    ("HCTSA_CP_wavelet_varchg", "This function requires Matlab's Wavelet Toolbox"),
    ("HCTSA_DN_CompareKSFit", "'normfit' undefined near line 55 column 16"),
    ("HCTSA_DN_Compare_zscore", "'ksdensity' undefined near line 38 column 9"),
    ("HCTSA_DN_FitKernelSmooth", "'ksdensity' undefined near line 60 column 9"),
    ("HCTSA_DN_Fit_mle", "'mle' undefined near line 57 column 11"),
    ("HCTSA_DN_OutlierInclude", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_DN_SimpleFit", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_DN_nlogL_norm", "'normfit' undefined near line 38 column 19"),
    ("HCTSA_DT_IsSeasonal", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_EN_MS_shannon", "invalid index to scalar variable."),
    ("HCTSA_EN_Randomize", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_EN_wentropy", "'wentropy' undefined near line 62 column 15"),
    ("HCTSA_FC_LocalSimple", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_FC_LoopLocalSimple", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_FC_Surprise", "All values in the sequence were not assigned to a group"),
    ("HCTSA_HT_DistributionTest", "'betafit' undefined near line 71 column 13"),
    ("HCTSA_MD_hrv_classic", "vertical dimensions mismatch (1x1 vs 1x127)"),
    ("HCTSA_MF_ARMA_orders", "Enters Oct2Py interact mode"),
    ("HCTSA_MF_AR_arcov", "'arcov' undefined near line 49 column 8"),
    ("HCTSA_MF_CompareAR", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_CompareTestSets", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_ExpSmoothing", "Training set size below minimum of 100 -- increasing to this.\nwarning: operator -: automatic broadcasting operation applied\nA(I) = X: X must have the same size as I"),
    ("HCTSA_MF_FitSubsegments", "warning: iddata: more outputs than samples - matrice 'y' should probably be transposed\nThis function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_GARCHcompare", "This function requires Matlab's Econometrics Toolbox"),
    ("HCTSA_MF_GARCHfit", "This function requires Matlab's Econometrics Toolbox"),
    ("HCTSA_MF_GP_FitAcross", "sq_string cannot be indexed with {"),
    ("HCTSA_MF_GP_LearnHyperp", "matrix cannot be indexed with {"),
    ("HCTSA_MF_GP_LocalPrediction", "sq_string cannot be indexed with {"),
    ("HCTSA_MF_GP_hyperparameters", "warning: The input time series is not, but should be z-scored\nsq_string cannot be indexed with {"),
    ("HCTSA_MF_ResidualAnalysis", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_StateSpaceCompOrder", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_StateSpace_n4sid", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_armax", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_hmm_CompareNStates", "Data matrix length must be multiple of sequence length T"),
    ("HCTSA_MF_hmm_fit", "Data matrix length must be multiple of sequence length T"),
    ("HCTSA_MF_steps_ahead", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_NL_BoxCorrDim", "Embedding dimension, m, incorrectly specified."),
    ("HCTSA_NL_CaosMethod", "'cao' is a script from the file /home/santi/Proyectos/pyopy/pyopy/externals/toolboxes/hctsa/Toolboxes/OpenTSTOOL/tstoolbox/mex/cao.m\n\ntstoolbox/mex/cao\n   This mex-file applies Cao's method to the input data set. If the data\n   set contains points of dimension D, it computes E and E* for a data\n   set of dimension 1 (taken from the first column of the input data\n   set), then for a data set of dimension 2 (taken from the first two\n   columns) up to a dimension of D. Optionally, this algorithm extends\n   Cao's method in a straightforward manner to use more than one nearest\n   neighbors.\n\n   Syntax:\n\n     * [E, E*] = cao(pointset, query_indices, k)\n\n   Input arguments:\n\n     * pointset - a N by D double matrix containing the coordinates of\n       the point set, organized as N points of dimension D\n     * query_indices - query points are taken out of the pointset,\n       query_indices is a vector of length R which contains the indices\n       of the query points (indices may vary from 1 to N)\n     * k - number of nearest neighbors to compute. Cao's method can be\n       extended to use more than only the first nearest neighbor (k=1).\n\n   Output arguments:\n\n     * E and E* are vectors of size D. Please refer the Cao's article for\n       a precise description of their meaning.\n\n Copyright 1997-2001 DPI Goettingen, License http://www.physik3.gwdg.de/tstool/gpl.txt\n\nAdditional help for built-in functions and operators is\navailable in the online version of the manual.  Use the command\n'doc <topic>' to search the manual index.\n\nHelp and information about Octave is also available on the WWW\nat http://www.octave.org and via the help@octave.org\nmailing list.\nwarning: cao: some elements in list of return values are undefined\n'data' undefined near line 136 column 9"),
    ("HCTSA_NL_MS_nlpe", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_NL_TISEAN_c1", "Just written temporary data file tisean_temp_c1_20140513_185809_370.dat for TISEAN\nsh: c1: command not found\nCall to TISEAN method 'c1' failed"),
    ("HCTSA_NL_TISEAN_d2", "Just wrote the input time series (N = 100) to the temporary file tisean_temp_d2_20140513_185809_877.dat for TISEAN\nsh: d2: command not found\nCall to TISEAN function 'd2' failed."),
    ("HCTSA_NL_TSTL_FractalDimensions", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_NL_TSTL_GPCorrSum", "'cao' is a script from the file /home/santi/Proyectos/pyopy/pyopy/externals/toolboxes/hctsa/Toolboxes/OpenTSTOOL/tstoolbox/mex/cao.m\n\ntstoolbox/mex/cao\n   This mex-file applies Cao's method to the input data set. If the data\n   set contains points of dimension D, it computes E and E* for a data\n   set of dimension 1 (taken from the first column of the input data\n   set), then for a data set of dimension 2 (taken from the first two\n   columns) up to a dimension of D. Optionally, this algorithm extends\n   Cao's method in a straightforward manner to use more than one nearest\n   neighbors.\n\n   Syntax:\n\n     * [E, E*] = cao(pointset, query_indices, k)\n\n   Input arguments:\n\n     * pointset - a N by D double matrix containing the coordinates of\n       the point set, organized as N points of dimension D\n     * query_indices - query points are taken out of the pointset,\n       query_indices is a vector of length R which contains the indices\n       of the query points (indices may vary from 1 to N)\n     * k - number of nearest neighbors to compute. Cao's method can be\n       extended to use more than only the first nearest neighbor (k=1).\n\n   Output arguments:\n\n     * E and E* are vectors of size D. Please refer the Cao's article for\n       a precise description of their meaning.\n\n Copyright 1997-2001 DPI Goettingen, License http://www.physik3.gwdg.de/tstool/gpl.txt\n\nAdditional help for built-in functions and operators is\navailable in the online version of the manual.  Use the command\n'doc <topic>' to search the manual index.\n\nHelp and information about Octave is also available on the WWW\nat http://www.octave.org and via the help@octave.org\nmailing list.\nwarning: cao: some elements in list of return values are undefined\nCall to TSTOOL function 'cao' failedEmbedding of the 100-sample time series failed"),
    ("HCTSA_NL_TSTL_LargestLyap", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_NL_TSTL_ReturnTime", "int64 matrix cannot be indexed with {"),
    ("HCTSA_NL_TSTL_TakensEstimator", "Embedding dimension, m, incorrectly specified."),
    ("HCTSA_NL_TSTL_acp", "binary operator '>' not implemented for 'cell' by 'scalar' operations"),
    ("HCTSA_NL_TSTL_dimensions", "'cao' is a script from the file /home/santi/Proyectos/pyopy/pyopy/externals/toolboxes/hctsa/Toolboxes/OpenTSTOOL/tstoolbox/mex/cao.m\n\ntstoolbox/mex/cao\n   This mex-file applies Cao's method to the input data set. If the data\n   set contains points of dimension D, it computes E and E* for a data\n   set of dimension 1 (taken from the first column of the input data\n   set), then for a data set of dimension 2 (taken from the first two\n   columns) up to a dimension of D. Optionally, this algorithm extends\n   Cao's method in a straightforward manner to use more than one nearest\n   neighbors.\n\n   Syntax:\n\n     * [E, E*] = cao(pointset, query_indices, k)\n\n   Input arguments:\n\n     * pointset - a N by D double matrix containing the coordinates of\n       the point set, organized as N points of dimension D\n     * query_indices - query points are taken out of the pointset,\n       query_indices is a vector of length R which contains the indices\n       of the query points (indices may vary from 1 to N)\n     * k - number of nearest neighbors to compute. Cao's method can be\n       extended to use more than only the first nearest neighbor (k=1).\n\n   Output arguments:\n\n     * E and E* are vectors of size D. Please refer the Cao's article for\n       a precise description of their meaning.\n\n Copyright 1997-2001 DPI Goettingen, License http://www.physik3.gwdg.de/tstool/gpl.txt\n\nAdditional help for built-in functions and operators is\navailable in the online version of the manual.  Use the command\n'doc <topic>' to search the manual index.\n\nHelp and information about Octave is also available on the WWW\nat http://www.octave.org and via the help@octave.org\nmailing list.\nwarning: cao: some elements in list of return values are undefined\nCall to TSTOOL function 'cao' failedTime-delay embedding for TSTOOL failed"),
    ("HCTSA_NL_crptool_fnn", "A(I): index out of bounds; value 5 out of bound 4"),
    ("HCTSA_NL_embed_PCA", "Embedding time series using TSTOOL function 'embed' failed"),
    ("HCTSA_NW_VisibilityGraph", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_PD_PeriodicityWang", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_PH_Walker", "'ansaribradley' undefined near line 221 column 17"),
    ("HCTSA_PP_Compare", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_PP_Iterate", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_PP_ModelFit", "polyfit: X and Y must be vectors of the same size"),
    ("HCTSA_PP_PreProcess", "polyfit: X and Y must be vectors of the same size"),
    ("HCTSA_SB_BinaryStats", "vertical dimensions mismatch (1x1 vs 1x99)"),
    ("HCTSA_SB_CoarseGrain", "'ng' undefined near line 84 column 38"),
    ("HCTSA_SB_MotifThree", "All values in the sequence were not assigned to a group"),
    ("HCTSA_SB_TransitionMatrix", "Some time-series values not assigned to a group"),
    ("HCTSA_SB_TransitionpAlphabet", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_SC_FluctAnal", "'robustfit' undefined near line 246 column 21"),
    ("HCTSA_SD_MakeSurrogates", "'surrmethod' undefined near line 73 column 8"),
    ("HCTSA_SD_SurrogateTest", "horizontal dimensions mismatch (51x1 vs 49x1)"),
    ("HCTSA_SD_TSTL_surrogates", "Index start exceeds matrix dimensions"),
    ("HCTSA_SP_Summaries", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_ST_FitPolynomial", "polyfit: X and Y must be vectors of the same size"),
    ("HCTSA_ST_MomentCorr", "A(I,J): row index out of bounds; value 2 out of bound 1"),
    ("HCTSA_SY_DriftingMean", "Has a bug (l is not defined) and enters Oct2Py interact mode"),
    ("HCTSA_SY_KPSStest", "This function requires Matlab's Econometrics Toolbox"),
    ("HCTSA_SY_LocalDistributions", "'ksdensity' undefined near line 87 column 16"),
    ("HCTSA_SY_PPtest", "This function requires Matlab's Econometrics Toolbox"),
    ("HCTSA_SY_SlidingWindow", "'ksdensity' undefined near line 60 column 9"),
    ("HCTSA_SY_StdNthDerChange", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_SY_TISEAN_nstat_z", "int64 matrix cannot be indexed with {"),
    ("HCTSA_SY_VarRatioTest", "This function requires Matlab's Econometrics Toolbox"),
    ("HCTSA_TSTL_delaytime", "help: 'delaytime' not found"),
    ("HCTSA_TSTL_localdensity", "'cao' is a script from the file /home/santi/Proyectos/pyopy/pyopy/externals/toolboxes/hctsa/Toolboxes/OpenTSTOOL/tstoolbox/mex/cao.m\n\ntstoolbox/mex/cao\n   This mex-file applies Cao's method to the input data set. If the data\n   set contains points of dimension D, it computes E and E* for a data\n   set of dimension 1 (taken from the first column of the input data\n   set), then for a data set of dimension 2 (taken from the first two\n   columns) up to a dimension of D. Optionally, this algorithm extends\n   Cao's method in a straightforward manner to use more than one nearest\n   neighbors.\n\n   Syntax:\n\n     * [E, E*] = cao(pointset, query_indices, k)\n\n   Input arguments:\n\n     * pointset - a N by D double matrix containing the coordinates of\n       the point set, organized as N points of dimension D\n     * query_indices - query points are taken out of the pointset,\n       query_indices is a vector of length R which contains the indices\n       of the query points (indices may vary from 1 to N)\n     * k - number of nearest neighbors to compute. Cao's method can be\n       extended to use more than only the first nearest neighbor (k=1).\n\n   Output arguments:\n\n     * E and E* are vectors of size D. Please refer the Cao's article for\n       a precise description of their meaning.\n\n Copyright 1997-2001 DPI Goettingen, License http://www.physik3.gwdg.de/tstool/gpl.txt\n\nAdditional help for built-in functions and operators is\navailable in the online version of the manual.  Use the command\n'doc <topic>' to search the manual index.\n\nHelp and information about Octave is also available on the WWW\nat http://www.octave.org and via the help@octave.org\nmailing list.\nCall to TSTOOL function 'cao' failedEmbedding failed."),
    ("HCTSA_TSTL_predict", "Takes too long?"),
    ("HCTSA_WL_DetailCoeffs", "This function requires Matlab's Wavelet Toolbox"),
    ("HCTSA_WL_coeffs", "This function requires Matlab's Wavelet Toolbox"),
    ("HCTSA_WL_cwt", "This function requires Matlab's Wavelet Toolbox"),
    ("HCTSA_WL_dwtcoeff", "This function requires Matlab's Wavelet Toolbox"),
    ("HCTSA_WL_fBM", "This function requires Matlab's Wavelet Toolbox"),
    ("HCTSA_WL_scal2frq", "This function requires Matlab's Wavelet Toolbox"),
]

OK_OPS_1000 = [
    ('HCTSA_CO_AutoCorr', 0.453194),
    ('HCTSA_CO_CompareMinAMI', 0.881044),
    ('HCTSA_CO_Embed2', 0.488851),
    ('HCTSA_CO_Embed2_AngleTau', 0.628033),
    ('HCTSA_CO_Embed2_Basic', 0.454406),
    ('HCTSA_CO_FirstMin', 0.553029),
    ('HCTSA_CO_FirstZero', 0.451441),
    ('HCTSA_CO_HistogramAMI', 0.455775),
    ('HCTSA_CO_NonlinearAutocorr', 0.454304),
    ('HCTSA_CO_RM_AMInformation', 0.478684),
    ('HCTSA_CO_TranslateShape', 0.544556),
    ('HCTSA_CO_f1ecac', 1.44473),
    ('HCTSA_CO_fzcglscf', 0.467605),
    ('HCTSA_CO_glscf', 0.459298),
    ('HCTSA_CO_tc3', 0.45946),
    ('HCTSA_CO_trev', 0.456515),
    ('HCTSA_CP_ML_StepDetect', 0.472378),
    ('HCTSA_DN_Burstiness', 0.4535),
    ('HCTSA_DN_Cumulants', 0.455108),
    ('HCTSA_DN_CustomSkewness', 0.455038),
    ('HCTSA_DN_HighLowMu', 0.451633),
    ('HCTSA_DN_HistogramMode', 0.456351),
    ('HCTSA_DN_Mean', 0.453989),
    ('HCTSA_DN_MinMax', 0.458204),
    ('HCTSA_DN_Moments', 0.455286),
    ('HCTSA_DN_OutlierTest', 0.465299),
    ('HCTSA_DN_ProportionValues', 0.456434),
    ('HCTSA_DN_Quantile', 0.455972),
    ('HCTSA_DN_RemovePoints', 0.50125),
    ('HCTSA_DN_Spread', 0.455003),
    ('HCTSA_DN_TrimmedMean', 0.455403),
    ('HCTSA_DN_Withinp', 0.454873),
    ('HCTSA_DN_cv', 0.457673),
    ('HCTSA_DN_pleft', 0.4556),
    ('HCTSA_EN_ApEn', 0.602411),
    ('HCTSA_EN_DistributionEntropy', 0.463206),
    ('HCTSA_EN_PermEn', 0.593681),
    ('HCTSA_EN_RM_entropy', 0.472317),
    ('HCTSA_EN_SampEn', 9.27101),
    ('HCTSA_EN_Shannonpdf', 0.448249),
    ('HCTSA_EN_TSentropy', 0.457206),
    ('HCTSA_EX_MovingThreshold', 0.484508),
    ('HCTSA_HT_HypothesisTest', 0.460673),
    ('HCTSA_MD_pNN', 0.458185),
    ('HCTSA_MD_polvar', 0.498099),
    ('HCTSA_MD_rawHRVmeas', 0.465364),
    ('HCTSA_MF_arfit', 0.529519),
    ('HCTSA_NL_MS_LZcomplexity', 0.453656),
    ('HCTSA_NL_MS_fnn', 0.624692),
    ('HCTSA_NL_TSTL_PoincareSection', 0.533112),
    ('HCTSA_PH_ForcePotential', 0.916312),
    ('HCTSA_RN_Gaussian', 0.4509),
    ('HCTSA_SB_BinaryStretch', 0.449936),
    ('HCTSA_SB_MotifTwo', 0.464988),
    ('HCTSA_SC_HurstExponent', 0.434928),
    ('HCTSA_SC_fastdfa', 0.456161),
    ('HCTSA_ST_Length', 0.453327),
    ('HCTSA_ST_LocalExtrema', 0.470905),
    ('HCTSA_ST_SimpleStats', 0.454591),
    ('HCTSA_SY_DynWin', 20.3514),
    ('HCTSA_SY_LinearTrend', 0.452683),
    ('HCTSA_SY_LocalGlobal', 9.41106),
    ('HCTSA_SY_RangeEvolve', 0.526317),
    ('HCTSA_SY_SpreadRandomLocal', 1.15736),
    ('HCTSA_SY_StatAv', 0.456492),
    ('HCTSA_SY_StdNthDer', 0.455388),
]


FAILED_OPS_1000 = [
    ("HCTSA_CO_AddNoise", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_CO_AutoCorrShape", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_CO_Embed2_Dist", "'h' undefined near line 71 column 6"),
    ("HCTSA_CO_Embed2_Shapes", "'poissfit' undefined near line 132 column 5"),
    ("HCTSA_CO_StickAngles", "This function requires Matlab's Signal Processing Toolbox"),
    ("HCTSA_CO_TSTL_AutoCorrMethod", "help: 'acf' not found"),
    ("HCTSA_CO_TSTL_amutual", "Input signal must be a scalar time series"),
    ("HCTSA_CO_TSTL_amutual2", "help: 'amutual2' not found"),
    ("HCTSA_CP_l1pwc_sweep_lambda", "warning: operator -: automatic broadcasting operation applied\nwarning: division by zero\nA(I) = X: X must have the same size as I"),
    ("HCTSA_CP_wavelet_varchg", "This function requires Matlab's Wavelet Toolbox"),
    ("HCTSA_DN_CompareKSFit", "'normfit' undefined near line 55 column 16"),
    ("HCTSA_DN_Compare_zscore", "'ksdensity' undefined near line 38 column 9"),
    ("HCTSA_DN_FitKernelSmooth", "'ksdensity' undefined near line 60 column 9"),
    ("HCTSA_DN_Fit_mle", "'mle' undefined near line 57 column 11"),
    ("HCTSA_DN_OutlierInclude", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_DN_SimpleFit", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_DN_nlogL_norm", "'normfit' undefined near line 38 column 19"),
    ("HCTSA_DT_IsSeasonal", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_EN_MS_shannon", "invalid index to scalar variable."),
    ("HCTSA_EN_Randomize", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_EN_wentropy", "'wentropy' undefined near line 62 column 15"),
    ("HCTSA_FC_LocalSimple", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_FC_LoopLocalSimple", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_FC_Surprise", "All values in the sequence were not assigned to a group"),
    ("HCTSA_HT_DistributionTest", "'betafit' undefined near line 71 column 13"),
    ("HCTSA_MD_hrv_classic", "vertical dimensions mismatch (1x1 vs 1x511)"),
    ("HCTSA_MF_ARMA_orders", "Enters Oct2Py interact mode"),
    ("HCTSA_MF_AR_arcov", "'arcov' undefined near line 49 column 8"),
    ("HCTSA_MF_CompareAR", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_CompareTestSets", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_ExpSmoothing", "warning: operator -: automatic broadcasting operation applied\nA(I) = X: X must have the same size as I"),
    ("HCTSA_MF_FitSubsegments", "warning: iddata: more outputs than samples - matrice 'y' should probably be transposed\nThis function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_GARCHcompare", "This function requires Matlab's Econometrics Toolbox"),
    ("HCTSA_MF_GARCHfit", "This function requires Matlab's Econometrics Toolbox"),
    ("HCTSA_MF_GP_FitAcross", "sq_string cannot be indexed with {"),
    ("HCTSA_MF_GP_LearnHyperp", "matrix cannot be indexed with {"),
    ("HCTSA_MF_GP_LocalPrediction", "sq_string cannot be indexed with {"),
    ("HCTSA_MF_GP_hyperparameters", "warning: The input time series is not, but should be z-scored\nsq_string cannot be indexed with {"),
    ("HCTSA_MF_ResidualAnalysis", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_StateSpaceCompOrder", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_StateSpace_n4sid", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_armax", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_MF_hmm_CompareNStates", "Data matrix length must be multiple of sequence length T"),
    ("HCTSA_MF_hmm_fit", "Data matrix length must be multiple of sequence length T"),
    ("HCTSA_MF_steps_ahead", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_NL_BoxCorrDim", "Embedding dimension, m, incorrectly specified."),
    ("HCTSA_NL_CaosMethod", "'cao' is a script from the file /home/santi/Proyectos/pyopy/pyopy/externals/toolboxes/hctsa/Toolboxes/OpenTSTOOL/tstoolbox/mex/cao.m\n\ntstoolbox/mex/cao\n   This mex-file applies Cao's method to the input data set. If the data\n   set contains points of dimension D, it computes E and E* for a data\n   set of dimension 1 (taken from the first column of the input data\n   set), then for a data set of dimension 2 (taken from the first two\n   columns) up to a dimension of D. Optionally, this algorithm extends\n   Cao's method in a straightforward manner to use more than one nearest\n   neighbors.\n\n   Syntax:\n\n     * [E, E*] = cao(pointset, query_indices, k)\n\n   Input arguments:\n\n     * pointset - a N by D double matrix containing the coordinates of\n       the point set, organized as N points of dimension D\n     * query_indices - query points are taken out of the pointset,\n       query_indices is a vector of length R which contains the indices\n       of the query points (indices may vary from 1 to N)\n     * k - number of nearest neighbors to compute. Cao's method can be\n       extended to use more than only the first nearest neighbor (k=1).\n\n   Output arguments:\n\n     * E and E* are vectors of size D. Please refer the Cao's article for\n       a precise description of their meaning.\n\n Copyright 1997-2001 DPI Goettingen, License http://www.physik3.gwdg.de/tstool/gpl.txt\n\nAdditional help for built-in functions and operators is\navailable in the online version of the manual.  Use the command\n'doc <topic>' to search the manual index.\n\nHelp and information about Octave is also available on the WWW\nat http://www.octave.org and via the help@octave.org\nmailing list.\nwarning: cao: some elements in list of return values are undefined\n'data' undefined near line 136 column 9"),
    ("HCTSA_NL_MS_nlpe", "This function requires Matlab's System Identification Toolbox"),
    ("HCTSA_NL_TISEAN_c1", "Just written temporary data file tisean_temp_c1_20140513_190148_264.dat for TISEAN\nsh: c1: command not found\nCall to TISEAN method 'c1' failed"),
    ("HCTSA_NL_TISEAN_d2", "Just wrote the input time series (N = 1000) to the temporary file tisean_temp_d2_20140513_190148_771.dat for TISEAN\nsh: d2: command not found\nCall to TISEAN function 'd2' failed."),
    ("HCTSA_NL_TSTL_FractalDimensions", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_NL_TSTL_GPCorrSum", "'cao' is a script from the file /home/santi/Proyectos/pyopy/pyopy/externals/toolboxes/hctsa/Toolboxes/OpenTSTOOL/tstoolbox/mex/cao.m\n\ntstoolbox/mex/cao\n   This mex-file applies Cao's method to the input data set. If the data\n   set contains points of dimension D, it computes E and E* for a data\n   set of dimension 1 (taken from the first column of the input data\n   set), then for a data set of dimension 2 (taken from the first two\n   columns) up to a dimension of D. Optionally, this algorithm extends\n   Cao's method in a straightforward manner to use more than one nearest\n   neighbors.\n\n   Syntax:\n\n     * [E, E*] = cao(pointset, query_indices, k)\n\n   Input arguments:\n\n     * pointset - a N by D double matrix containing the coordinates of\n       the point set, organized as N points of dimension D\n     * query_indices - query points are taken out of the pointset,\n       query_indices is a vector of length R which contains the indices\n       of the query points (indices may vary from 1 to N)\n     * k - number of nearest neighbors to compute. Cao's method can be\n       extended to use more than only the first nearest neighbor (k=1).\n\n   Output arguments:\n\n     * E and E* are vectors of size D. Please refer the Cao's article for\n       a precise description of their meaning.\n\n Copyright 1997-2001 DPI Goettingen, License http://www.physik3.gwdg.de/tstool/gpl.txt\n\nAdditional help for built-in functions and operators is\navailable in the online version of the manual.  Use the command\n'doc <topic>' to search the manual index.\n\nHelp and information about Octave is also available on the WWW\nat http://www.octave.org and via the help@octave.org\nmailing list.\nwarning: cao: some elements in list of return values are undefined\nCall to TSTOOL function 'cao' failedEmbedding of the 1000-sample time series failed"),
    ("HCTSA_NL_TSTL_LargestLyap", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_NL_TSTL_ReturnTime", "int64 matrix cannot be indexed with {"),
    ("HCTSA_NL_TSTL_TakensEstimator", "Embedding dimension, m, incorrectly specified."),
    ("HCTSA_NL_TSTL_acp", "binary operator '>' not implemented for 'cell' by 'scalar' operations"),
    ("HCTSA_NL_TSTL_dimensions", "'cao' is a script from the file /home/santi/Proyectos/pyopy/pyopy/externals/toolboxes/hctsa/Toolboxes/OpenTSTOOL/tstoolbox/mex/cao.m\n\ntstoolbox/mex/cao\n   This mex-file applies Cao's method to the input data set. If the data\n   set contains points of dimension D, it computes E and E* for a data\n   set of dimension 1 (taken from the first column of the input data\n   set), then for a data set of dimension 2 (taken from the first two\n   columns) up to a dimension of D. Optionally, this algorithm extends\n   Cao's method in a straightforward manner to use more than one nearest\n   neighbors.\n\n   Syntax:\n\n     * [E, E*] = cao(pointset, query_indices, k)\n\n   Input arguments:\n\n     * pointset - a N by D double matrix containing the coordinates of\n       the point set, organized as N points of dimension D\n     * query_indices - query points are taken out of the pointset,\n       query_indices is a vector of length R which contains the indices\n       of the query points (indices may vary from 1 to N)\n     * k - number of nearest neighbors to compute. Cao's method can be\n       extended to use more than only the first nearest neighbor (k=1).\n\n   Output arguments:\n\n     * E and E* are vectors of size D. Please refer the Cao's article for\n       a precise description of their meaning.\n\n Copyright 1997-2001 DPI Goettingen, License http://www.physik3.gwdg.de/tstool/gpl.txt\n\nAdditional help for built-in functions and operators is\navailable in the online version of the manual.  Use the command\n'doc <topic>' to search the manual index.\n\nHelp and information about Octave is also available on the WWW\nat http://www.octave.org and via the help@octave.org\nmailing list.\nwarning: cao: some elements in list of return values are undefined\nCall to TSTOOL function 'cao' failedTime-delay embedding for TSTOOL failed"),
    ("HCTSA_NL_crptool_fnn", "A(I): index out of bounds; value 3 out of bound 2"),
    ("HCTSA_NL_embed_PCA", "Embedding time series using TSTOOL function 'embed' failed"),
    ("HCTSA_NW_VisibilityGraph", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_PD_PeriodicityWang", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_PH_Walker", "'ansaribradley' undefined near line 221 column 17"),
    ("HCTSA_PP_Compare", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_PP_Iterate", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_PP_ModelFit", "polyfit: X and Y must be vectors of the same size"),
    ("HCTSA_PP_PreProcess", "polyfit: X and Y must be vectors of the same size"),
    ("HCTSA_SB_BinaryStats", "vertical dimensions mismatch (1x1 vs 1x999)"),
    ("HCTSA_SB_CoarseGrain", "'ng' undefined near line 84 column 38"),
    ("HCTSA_SB_MotifThree", "All values in the sequence were not assigned to a group"),
    ("HCTSA_SB_TransitionMatrix", "Some time-series values not assigned to a group"),
    ("HCTSA_SB_TransitionpAlphabet", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_SC_FluctAnal", "'robustfit' undefined near line 246 column 21"),
    ("HCTSA_SD_MakeSurrogates", "'surrmethod' undefined near line 73 column 8"),
    ("HCTSA_SD_SurrogateTest", "horizontal dimensions mismatch (501x1 vs 499x1)"),
    ("HCTSA_SD_TSTL_surrogates", "Index start exceeds matrix dimensions"),
    ("HCTSA_SP_Summaries", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_ST_FitPolynomial", "polyfit: X and Y must be vectors of the same size"),
    ("HCTSA_ST_MomentCorr", "A(I,J): row index out of bounds; value 2 out of bound 1"),
    ("HCTSA_SY_DriftingMean", "Has a bug (l is not defined) and enters Oct2Py interact mode"),
    ("HCTSA_SY_KPSStest", "This function requires Matlab's Econometrics Toolbox"),
    ("HCTSA_SY_LocalDistributions", "'ksdensity' undefined near line 87 column 16"),
    ("HCTSA_SY_PPtest", "This function requires Matlab's Econometrics Toolbox"),
    ("HCTSA_SY_SlidingWindow", "'ksdensity' undefined near line 60 column 9"),
    ("HCTSA_SY_StdNthDerChange", "This function requires Matlab's Curve Fitting Toolbox"),
    ("HCTSA_SY_TISEAN_nstat_z", "int64 matrix cannot be indexed with {"),
    ("HCTSA_SY_VarRatioTest", "This function requires Matlab's Econometrics Toolbox"),
    ("HCTSA_TSTL_delaytime", "help: 'delaytime' not found"),
    ("HCTSA_TSTL_localdensity", "'cao' is a script from the file /home/santi/Proyectos/pyopy/pyopy/externals/toolboxes/hctsa/Toolboxes/OpenTSTOOL/tstoolbox/mex/cao.m\n\ntstoolbox/mex/cao\n   This mex-file applies Cao's method to the input data set. If the data\n   set contains points of dimension D, it computes E and E* for a data\n   set of dimension 1 (taken from the first column of the input data\n   set), then for a data set of dimension 2 (taken from the first two\n   columns) up to a dimension of D. Optionally, this algorithm extends\n   Cao's method in a straightforward manner to use more than one nearest\n   neighbors.\n\n   Syntax:\n\n     * [E, E*] = cao(pointset, query_indices, k)\n\n   Input arguments:\n\n     * pointset - a N by D double matrix containing the coordinates of\n       the point set, organized as N points of dimension D\n     * query_indices - query points are taken out of the pointset,\n       query_indices is a vector of length R which contains the indices\n       of the query points (indices may vary from 1 to N)\n     * k - number of nearest neighbors to compute. Cao's method can be\n       extended to use more than only the first nearest neighbor (k=1).\n\n   Output arguments:\n\n     * E and E* are vectors of size D. Please refer the Cao's article for\n       a precise description of their meaning.\n\n Copyright 1997-2001 DPI Goettingen, License http://www.physik3.gwdg.de/tstool/gpl.txt\n\nAdditional help for built-in functions and operators is\navailable in the online version of the manual.  Use the command\n'doc <topic>' to search the manual index.\n\nHelp and information about Octave is also available on the WWW\nat http://www.octave.org and via the help@octave.org\nmailing list.\nCall to TSTOOL function 'cao' failedEmbedding failed."),
    ("HCTSA_TSTL_predict", "Takes too long?"),
    ("HCTSA_WL_DetailCoeffs", "This function requires Matlab's Wavelet Toolbox"),
    ("HCTSA_WL_coeffs", "This function requires Matlab's Wavelet Toolbox"),
    ("HCTSA_WL_cwt", "This function requires Matlab's Wavelet Toolbox"),
    ("HCTSA_WL_dwtcoeff", "This function requires Matlab's Wavelet Toolbox"),
    ("HCTSA_WL_fBM", "This function requires Matlab's Wavelet Toolbox"),
    ("HCTSA_WL_scal2frq", "This function requires Matlab's Wavelet Toolbox"),
]