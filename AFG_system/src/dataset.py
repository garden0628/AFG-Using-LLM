class Dataset:
    testcases = []
    wrong_prog = ''
    description = ''
    
    @classmethod
    def init_glob_vars(cls):
        cls.testcases = []
        cls.wrong_prog = ''
        cls.description = ''
        
    @classmethod
    def separate_tc(cls, tcs:str):
        tcs_list = list(tcs.split(','))
        tcs_num = (len(tcs_list) + 1) // 2
        for i in range(1, tcs_num + 1):
            idx = (i - 1) * 2
            cls.testcases.append(
                {
                    'testcase_no' : i,
                    'input_tc': tcs_list[idx],
                    'output_tc': tcs_list[idx + 1] 
                }
            )
        
    @classmethod
    def run(cls, des:str, wp:str, tcs:str):
        cls.description = des
        cls.wrong_prog = wp
        cls.separate_tc(tcs)