from .base_predicates import Expression
from typing import List

class PredicateWrapper(Expression):
    """
    A wrapper for predicates that allows them to be used as expressions.
    This class is used to wrap predicates so they can be used in the expression
    system of the environment.
    """

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        raise NotImplementedError("PredicateWrapper should not be called directly. Use a specific predicate class instead.")

    def expected_arg_types(self) -> List[type]:
        raise NotImplementedError
    
    def __str__(self):
        return f"{self.__class__.__name__}()"
    

class Constraint(PredicateWrapper):
    def __init__(self):
        super().__init__()
        if not hasattr(self, 'constraint_satisfied'):
            raise NotImplementedError("Subclasses must define 'constraint_satisfied' attribute.")
        
    def __call__(self, arg):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def expected_arg_types(self):
        return [bool]


class ConstraintAlways(Constraint):
    def __init__(self):
        self.constraint_satisfied = True
        super().__init__()
    
    def __call__(self, arg):
        self.constraint_satisfied = arg and self.constraint_satisfied
        return self.constraint_satisfied


class ConstraintNever(Constraint):
    def __init__(self):
        self.constraint_satisfied = True
        super().__init__()
    
    def __call__(self, arg):
        self.constraint_satisfied = not arg and self.constraint_satisfied
        return self.constraint_satisfied


class ConstraintOnce(Constraint):
    def __init__(self):
        self.constraint_satisfied = False
        super().__init__()
    
    def __call__(self, arg):
        self.constraint_satisfied = arg or self.constraint_satisfied
        return self.constraint_satisfied