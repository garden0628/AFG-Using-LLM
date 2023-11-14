from AFG_system.src.tester import Tester
from AFG_system.src.utils import regularize
from AFG_system.src.unittests import Validating
from AFG_system.src.results import Results

import re

class Validator:
    def __init__(self, tester:Tester):
        self.tester = tester
        
    def extract_code(self, code:str) -> str:
        code = re.findall(r"```(.*?)```", code, re.DOTALL)
        if code:
            lines = code[0].split('\n')
            lines.pop(0)
            code = '\n'.join(lines)
        return code
    
    def run(self, code:str) -> bool:
        test_hist = {}

        extracted = self.extract_code(code)
        if extracted:
            code = regularize(extracted)
        for testcase in self.tester.testsuite:
            self.tester.run(code, testcase, Validating)
            testcase_no = testcase['testcase_no']
            test_hist[testcase_no] = Results.status
        
        return all(result == 'Success' for result in test_hist.values()), extracted