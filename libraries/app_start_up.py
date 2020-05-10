import subprocess


def collect_tests_from_suites(path):
    result = subprocess.run(['python', '-m', 'pytest', 'tests/project_one/scenario_one.py', '--collect-only'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('\n')
    test_names = []
    for line in result.stdout.decode("utf-8").splitlines():
        if line.startswith('<Module '):
            module_name = line.strip('<Module >',)
        if line.startswith('  <Function '):
            test_names.append((line.split("  <Function ")[1]).split(">")[0])

    print(f'Suite Name: {module_name}')
    for test in test_names:
        print(f'Test file name: {test}')
    print(f'ERRORS: {result.stderr}')