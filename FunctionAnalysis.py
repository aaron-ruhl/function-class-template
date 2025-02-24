# FunctionAnalysis.py

import matplotlib.pyplot as _plt
import numpy as _np
            
if __name__ == '__main__': #run as an executable to get __name__ == '__main__'   
    def f(x: float) -> 'f(x)':
        '''This function was initialized by FunctionAnalysis'''
        return _np.tan(_np.sqrt(x**2+1)) 
    
    def df(x: float) -> "f'(x)":
        '''This function was initialized by FunctionAnalysis'''
        return _np.tan(_np.sqrt(x**2+1))




class Function():
    '''_Analysis object generator. Seperate multiple numerical functions with a comma.
            Ex: Function(f,g,h) or Function(f)'''
    
    def __new__(cls,*args):
        if len(args) == 1: #if only one function
            return cls._fromfunction(*args)
        else:
            return cls._fromlist(*args)
            
    @classmethod
    def _fromfunction(cls, function) -> '_Analysis(function)':
        '''Returns a _Analysis object'''
        return _Analysis(function)
    
    @classmethod
    def _fromlist(cls, *args) -> '[f,g,]':
        '''Returns an iterable list of _Analysis(function) objects'''
        functionlist = []
        for func in args: 
            functionlist.append(_Analysis(func)) 
        return functionlist

   
class _Analysis():
    '''Function Analysis Tools'''
    def __init__(self, possible_function):
        if isinstance(possible_function, int | float | str | list | dict | tuple | None ):
            raise ValueError(f"Unsupported Function Detected: {possible_function}={type(possible_function)}")
        self._function = possible_function
    
    def __repr__(self):
        return f'Function({self._function})'
    
    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, possible_function):
        if isinstance(possible_function, int | float | str | list | dict | tuple | None ):
            raise ValueError(f"unsupported function format: {type(possible_function)=}")        
        self._function = possible_function
        
    def calc(self, *args) -> list: 
        '''Returns values of the instantiated function 
        **Seperate multiple inputs with commas**
            Ex: calc(2,3,4,5)'''   
        results = _np.array(args, float)
        func_vector = _np.vectorize(self._function)
        results = func_vector(results)
        '''for x in args:
            results.append(self._function(x))
        '''
        return results
        
    '''Analysis Methods Go Here'''
