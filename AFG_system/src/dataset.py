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
    def separate_tc(cls, tcs:list):
        for i in range(len(tcs)):
            cls.testcases.append(
                {
                    'testcase_no' : i+1,
                    'input_tc': tcs[i]['input'],
                    'output_tc': tcs[i]['output']
                }
            )
        
    @classmethod
    def run(cls, des:str, wp:str, tcs:list):
        cls.description = des
        cls.wrong_prog = wp
        cls.separate_tc(tcs)