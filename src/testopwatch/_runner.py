from unittest.runner import TextTestRunner

from django.test.runner import DiscoverRunner

from testopwatch._result import TimeLoggingTestResult


class TimeRunner(TextTestRunner):
    resultclass = TimeLoggingTestResult

    def __init__(self, *args, **kwargs):
        super(TimeRunner, self).__init__(*args, **kwargs)

    def run(self, test):
        result = super(TimeRunner, self).run(test)
        self.stream.writeln("----------- Total test class times -----------")
        all_times = result.function_name_total_time.items()
        sorted_times = sorted(all_times, key=lambda x: x[1], reverse=True)
        for name, total_time in sorted_times:
            self.stream.writeln(
                f"TestClass {name} finished in {total_time / 10 ** 9:.5f}s"
            )
        self.stream.writeln(result.separator2)
        return result


class DjangoTimeRunner(DiscoverRunner):
    test_runner = TimeRunner

    def get_resultclass(self):
        return TimeLoggingTestResult
