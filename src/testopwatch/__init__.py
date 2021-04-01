r"""

 _____  _____  _____  _____                             _         _
|_   _||  ___|/  ___||_   _|                           | |       | |
  | |  | |__  \ `--.   | |  ___   _ __ __      __ __ _ | |_  ___ | |__
  | |  |  __|  `--. \  | | / _ \ | '_ \\ \ /\ / // _` || __|/ __|| '_ \
  | |  | |___ /\__/ /  | || (_) || |_) |\ V  V /| (_| || |_| (__ | | | |
  \_/  \____/ \____/   \_/ \___/ | .__/  \_/\_/  \__,_| \__|\___||_| |_|
                                 | |
                                 |_|
"""
from testopwatch._result import TimeLoggingTestResult
from testopwatch._runner import DjangoTimeRunner, TimeRunner

__version__ = "0.1.0"

__title__ = "testopwatch"
__description__ = "Timing your tests "
__uri__ = "https://github.com/programeri-tech/testopwatch"

__author__ = "Nikola Smiljanic / Andrija Zivkovic"
__email__ = "nikolassmiljanic5@gmail.com"

__license__ = "MIT"
__copyright__ = "Copyright (c) 2021 " + __author__

__all__ = ["TimeLoggingTestResult", "TimeRunner", "DjangoTimeRunner"]
