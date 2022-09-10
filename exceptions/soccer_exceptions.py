class MissingInformationTeam(Exception):
    """
    Exception raised when a match is incomplete
    """

    def __init__(self, str_match, message="Missing team information."):
        self.str_match = str_match
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'In the match "{self.str_match}" is {self.message}'


class IncorrectMatchFormat(Exception):
    """
    Exception raised when the match is .

    Attributes:
        str_match: string that was tried to regex
    """

    def __init__(self, str_match, message="Match format is incorrect."):
        self.str_match = str_match
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.str_match} -> {self.message}'
