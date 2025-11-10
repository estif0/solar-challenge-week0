"""
Utility modules for data processing and analysis.

This package provides reusable utilities for:
- Data loading (data_loader)
- Data cleaning (data_cleaner)
- Visualization (visualization)
"""

from .data_loader import DataLoader, load_country, load_all
from .data_cleaner import (
    DataCleaner,
    detect_missing_summary,
    get_data_quality_report,
    quick_clean
)

__all__ = [
    'DataLoader',
    'load_country',
    'load_all',
    'DataCleaner',
    'detect_missing_summary',
    'get_data_quality_report',
    'quick_clean',
]
