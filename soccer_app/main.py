#! /usr/bin/python
import cmd
from controller.league_stats import Rank


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
        Example:
            - l inputs/input1.txt
        """
        arg = arg.split()
        if len(arg) == 1:
            file = arg[0]
            print(f"Loading file {file}")
            try:
                self.rank.record_result(file)
            except (IOError, OSError) as e:
                print(e.args) 
        else:
            print("Using default file (inputs/input1.txt) ... ")
            self.rank.record_result('inputs/input1.txt')

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
        if len(self.rank.rank_teams):
            print(self.rank.table_ranking())

        else:
            print('Please load first a file with matches....')

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
