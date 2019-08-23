from enum import Enum

class IPStatus(Enum):
    NotDefined = 1
    Success = 2
    Error = 3
    Timeout = 4
    Simulated = 5

    def toString(self):
        if self.NotDefined:
            return 'NotDefined'

        elif self.Success:
            return 'Success'

        elif self.Error:
            return 'Error'

        elif self.Timeout:
            return 'Timeout'

        elif self.Simulated:
            return 'Simulated'