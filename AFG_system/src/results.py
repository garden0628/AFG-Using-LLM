class Results:
    loc = 0
    exec_traces = []
    status = None
    timeout = 1
    test_code = ''
    input_tc = ''
    output_tc = ''
    output = None
    
    @classmethod
    def init_global_vars(cls):
        cls.loc = 0
        cls.exec_traces = []
        cls.status = None
        cls.timeout = 1
        cls.test_code = ''
        cls.input_tc = ''
        cls.output_tc = ''
        cls.output = None