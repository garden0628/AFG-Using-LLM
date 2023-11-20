import warnings
warnings.filterwarnings("ignore")

from AFG_system.src.testsuite import TestSuite
from AFG_system.src.utils import regularize, get_stmt_list
from AFG_system.src.results import Results
from AFG_system.src.unittests import RunUnitTest

class Tester:
    def __init__(self, testcases:list, timeout:int=1):
        self.testsuite = TestSuite(testcases)
        self.timeout = timeout
        
    def __gen_test_code(self, code:str, input_tc:str, key_input:bool=False) -> str:
        try:
            test_input = input_tc
            if 'print(' not in input_tc:
                test_input = 'print(' + input_tc + ')'
            regularize(input_tc)
            regularize(test_input)
        except:
            key_input = True
            
        test_code = code.strip()
        if not key_input:
            if 'print(' not in input_tc:
                input_tc = 'print(' + input_tc + ')'
            test_code = code + '\n\n' + input_tc
            
        return regularize(test_code)
    
    def run(self, code:str, testcase:dict[str, str], UnitTest) -> tuple[str, str]:
        code = regularize(code)
        Results.init_global_vars()
        Results.loc = len(get_stmt_list(code))
        Results.timeout = self.timeout
        Results.input_tc = testcase['input_tc']
        Results.output_tc = testcase['output_tc']
        Results.test_code = self.__gen_test_code(code, testcase['input_tc'])
        RunUnitTest.run(UnitTest)
        