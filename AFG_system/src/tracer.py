import sys, trace, threading
from AFG_system.src.results import Results

class Tracer(trace.Trace):
    """
    기존 Trace 라이브러리 수정
    :variable 'self.loc': 타겟 코드의 라인 수(line of code)
    """
    def __init__(self, count=1, trace=0, countfuncs=0, countcallers=0,
                        ignoremods=(), ignoredirs=[sys.prefix, sys.exec_prefix], infile=None, outfile=None,
                        timing=False):
        super().__init__(count, trace, countfuncs, countcallers,
                        ignoremods, ignoredirs, infile, outfile,
                        timing)
        self.loc = Results.loc
    
    def execution_trace(self, lineno:int):
        """
        실행된 라인만을 추출해서 Results.exec_traces에 추가
        :param 'lineno': 현재 실행중인 라인넘버
        """
        if lineno < self.loc:
            Results.exec_traces.append(lineno)
    
    def localtrace_count(self, frame, why, arg):
        if why == "line":
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            key = filename, lineno
            self.counts[key] = self.counts.get(key, 0) + 1
            # append line numbers to traces list
            self.execution_trace(lineno-1)
        return self.localtrace
    
    def runctx(self, cmd:str, globals:dict=None, locals:dict=None):
        """
        Trace 라이브러리 실행하는 함수
        :param 'cmd': 실행될 코드
        :param 'globals': 전역 정보
        :param 'locals': 지역 정보
        """
        if globals is None: globals = {}
        if locals is None: locals = {}
        if not self.donothing:
            threading.settrace(self.globaltrace)
            sys.settrace(self.globaltrace)
        try:
            exec(cmd, globals)
        finally:
            if not self.donothing:
                sys.settrace(None)
                threading.settrace(None)