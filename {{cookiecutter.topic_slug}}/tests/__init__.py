import sys
import pytest

__all__ = ['py2_only', 'py3_later']

py2_only = pytest.mark.skipif(sys.version_info[0] >= 3, reason='Python 2')
py3_later = pytest.mark.skipif(sys.version_info[0] <= 2, reason='Python 3+')
