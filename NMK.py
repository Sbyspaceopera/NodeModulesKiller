import shutil
import os
import sys

# bcolors = Prompt styling
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
# https://en.wikipedia.org/wiki/ANSI_escape_code
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


deletedNodeModulesCount = 0
if len(sys.argv) == 1:
    print(
        f"{bcolors.FAIL}[NMK FAILED]{bcolors.ENDC}: Please enter at least 1 absolute path as an argument when running NMK."
    )
else:
    paths = sys.argv[1:]
    for path in paths:
        if os.path.isabs(path) and os.path.isdir(path):
            for root, dirs in os.walk(path):
                for name in dirs:
                    if name == "node_modules":
                        shutil.rmtree(os.path.join(root, name))
                        print(
                            f"{bcolors.OKGREEN}[SUCCESS]{bcolors.ENDC}{root}\{name} has been successfullydeleted."
                        )
                        deletedNodeModulesCount += 1
        else:
            print(
                f"{bcolors.FAIL}[NMK FAILED]{bcolors.ENDC}: {path} is not a valid or existing absolute path.\n"
                f"{bcolors.FAIL}[NMK FAILED]{bcolors.ENDC}: Please enter a valid absolute path instead."
            )
    print(f"{bcolors.OKCYAN}JOB DONE!{bcolors.ENDC}")
    print(
        f"{bcolors.OKCYAN}{deletedNodeModulesCount} node_modules folders has been deleted.{bcolors.ENDC}"
    )
