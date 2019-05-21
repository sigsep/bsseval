# bsseval

[![Build Status](https://travis-ci.org/sigsep/bsseval.svg?branch=master)](https://travis-ci.org/sigsep/bsseval)
[![Latest Version](https://img.shields.io/pypi/v/bsseval.svg)](https://pypi.python.org/pypi/bsseval)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/bsseval.svg)](https://pypi.python.org/pypi/bsseval)

## Metrics

### BSSEval v3

* Source / Images

### BSSEval v4

The BSSEval metrics, as implemented in the [MATLAB toolboxes](http://bass-db.gforge.inria.fr/bss_eval/) and their re-implementation in [mir_eval](http://craffel.github.io/mir_eval/#module-mir_eval.separation) are widely used in the audio separation literature. One particularity of BSSEval is to compute the metrics after optimally matching the estimates to the true sources through linear distortion filters. This allows the criteria to be robust to some linear mismatches. Apart from the optional evaluation for all possible permutations of the sources, this matching is the reason for most of the computation cost of BSSEval, especially considering it is done for each evaluation window when the metrics are computed on a framewise basis.

For this package, we enabled the option of having _time invariant_ distortion filters, instead of necessarily taking them as varying over time as done in the previous versions of BSS eval. First, enabling this option _significantly reduces_ the computational cost for evaluation because matching needs to be done only once for the whole signal. Second, it introduces much more dynamics in the evaluation, because time-varying matching filters turn out to over-estimate performance. Third, this makes matching more robust, because true sources are not silent throughout the whole recording, while they often were for short windows.

### SI-SDR

## Installation

### Package installation

You can install the `bsseval` parsing package using pip:

```bash
pip install bsseval
```

## Usage

## Submission

## References

