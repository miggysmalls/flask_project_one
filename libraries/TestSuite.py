import subprocess


class TestSuite(object):

    def __init__(self):
        self.suite_name = None
        self.test_count = None
        self.test_names = []

    def collect_tests_from_suites(self):
        result = subprocess.run(['python', '-m', 'pytest', 'tests/project_one/scenario_one.py', '--collect-only', '-s'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # print(f'\n\nEXECUTION RESULT {result.stdout}')
        # output =
        # print(f'\n\nEXECUTION RESULT \n{output}')
        # lines = result.stdout.decode("utf-8").splitlines()
        print('\n\n')
        tests = []
        for line in result.stdout.decode("utf-8").splitlines():
            if line.startswith('<Module '):
                self.suite_name = line.strip('<Module >', )
            if line.startswith('  <Function '):
                self.test_names.append(line)
        self.test_count = len(self.test_names)
        print(f'Suite Name: {self.suite_name}')
        for test in tests:
            print(f'Test file name: {(test.split("  <Function ")[1]).split(">")[0]}')
        print(f'\n\nERRORS: {result.stderr}')