class TestSuite:
    def __init__(self, testcases:list):
        self.testcases = testcases
        self.current_index = 0
        
    def __iter__(self):
        self.current_index = 0
        return self
    
    def __next__(self):
        if self.current_index < len(self.testcases):
            testcase = self.testcases[self.current_index]
            self.current_index += 1
            return testcase
        raise StopIteration
    
    def __str__(self):
        prints = ''
        for testcase in self.testcases:
            prints += f"Testcase No: {testcase['testcase_no']}\n"
            prints += f"Input: {testcase['input_tc']}\n"
            prints += f"Output: {testcase['output_tc']}\n"
        return prints
    
    def __len__(self):
        return len(self.testcases)

    def get_tc_no_list(self):
        return [tc['testcase_no'] for tc in self.testcases]