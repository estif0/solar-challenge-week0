"""
Analysis package for statistical tests and solar-specific calculations.

This package provides:
- Statistical tests (statistical_tests)
- Solar metrics calculations (solar_metrics)
"""

from .statistical_tests import (
    StatisticalAnalyzer,
    compare_groups,
    quick_correlation_test,
    summary_statistics
)

__all__ = [
    'StatisticalAnalyzer',
    'compare_groups',
    'quick_correlation_test',
    'summary_statistics',
]
