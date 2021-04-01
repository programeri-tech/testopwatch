from collections import defaultdict
from time import monotonic_ns
from unittest import TextTestResult


class TimeLoggingTestResult(TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_started_at = {}
        self.function_name_total_time = defaultdict(int)

    def getDescription(self, test):
        return str(test)

    def startTest(self, test):
        name = self.getDescription(test)
        self._test_started_at[name] = monotonic_ns()
        super().startTest(test)

    def addSuccess(self, test):
        name = self.getDescription(test)
        _, function_name = name.split()
        elapsed = monotonic_ns() - self._test_started_at[name]
        self.function_name_total_time[function_name] += elapsed
        self.stream.writeln(f"time_exec: {elapsed / 10 ** 9:.7f}s test_name: {name} OK")
