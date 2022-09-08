#! /usr/bin/python
import cmd
import sys
from model.league_stats import Rank


class SoccerShell(cmd.Cmd):
    """
    Shell using CMD library
    """
    intro = '\n'.join([
        "\t" + "*" * 41,
        "\t\t***  Soccer Stats Simple CLI  ***",
        "\t" + "*" * 41,
        "\tType help or ? to list commands,",
        "\t or help command to get help about a command."
    ])
    prompt = "#: "
    rank = Rank()
    def do_load(self, arg):
        """
        Load file with the result of the matches
            command: load [FILE] | l [FILE]
            args:
                -FILE: Location of the TXT file
        """
        arg = arg.split()
        if len(arg) == 1:
            file = arg
            print(f"Loading file {file}")
            # self.rank.record_result(file)
        else:
            print("no argus load")
            self.rank.record_result('inputs/input2.txt')
            self.rank.print_ranking()

    def do_quit(self, arg):
        """
        Quit Soccer CLI
            command: quit | q
        """
        print("exiting ...")
        return True  # Exit of the cmd loop

    def do_results(self, arg):
        """
        Show last results
            command: results | r
        """
        if arg:
            league = arg[0]
            print(self.rank.print_ranking())

        else:
            print('leagues ...')

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.

        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    # shortcuts
    do_l = do_load
    do_q = do_quit
    do_r = do_results


if __name__ == "__main__":
    SoccerShell().cmdloop()
