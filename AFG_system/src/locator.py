from AFG_system.src.tester import Tester
from AFG_system.src.utils import regularize, get_stmt_list
from AFG_system.src.unittests import Tracing
from AFG_system.src.results import Results

class Locator:
    def __init__(self, tester:Tester, success:str='Success'):
        self.tester = tester
        self.__success = success
        
    def __tarantula(self, code:str, test_hist:dict, trace_hist:dict) -> dict:
        total_pass, total_fail= 0, 0
        pass_cnt_dict, fail_cnt_dict = {}, {}
        
        code = regularize(code)
        for lineno in range(len(get_stmt_list(code))):
            pass_cnt_dict[lineno] = 0
            fail_cnt_dict[lineno] = 0
            
        for testcase_no, status in test_hist.items():
            for lineno in set(trace_hist[testcase_no]):
                if status != self.__success:
                    total_fail += 1
                    fail_cnt_dict[lineno] += 1
                else:
                    total_pass += 1
                    pass_cnt_dict[lineno] += 1
                    
        suspiciousness = {}
        for lineno in range(len(get_stmt_list(code))):
            pass_cnt = pass_cnt_dict[lineno]
            fail_cnt = fail_cnt_dict[lineno]
            score = 0
            try:
                score = round((fail_cnt / total_fail) / ((fail_cnt / total_fail) + (pass_cnt / total_pass)), 1)
            except ZeroDivisionError:
                if fail_cnt > 0 and pass_cnt == 0:
                    score = 1
            suspiciousness[lineno] = score
            
        return suspiciousness
    
    def run(self, code) -> dict:
        test_hist, trace_hist = {}, {}
        failed_tcs = []

        code = regularize(code)
        for testcase in self.tester.testsuite:
            self.tester.run(code, testcase, Tracing)
            testcase_no = testcase['testcase_no']
            test_hist[testcase_no] = Results.status
            trace_hist[testcase_no] = Results.exec_traces

            if Results.status != self.__success:
                failed_tcs.append(testcase)

        stmt_list = get_stmt_list(code)
        suspiciousness = self.__tarantula(code, test_hist, trace_hist)
        rankings = dict(sorted(suspiciousness.items(), key=lambda x:x[1], reverse=True))
        top_rank_lineno = list(rankings.keys())[0]
        susp_stmt = stmt_list[top_rank_lineno]
        
        return failed_tcs, susp_stmt