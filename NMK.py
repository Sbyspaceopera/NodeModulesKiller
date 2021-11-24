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


# Keep the node_modules count
deletedNodeModulesCount = {"value": 0}

# DRY function
def delete_node_modules_where(path, deletedNodeModulesCount):
    if os.path.isabs(path) and os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for name in dirs:
                if name == "node_modules":
                    shutil.rmtree(os.path.join(root, name))
                    print(
                        f"{bcolors.OKGREEN}[SUCCESS]{bcolors.ENDC}{root}\{name} has been successfully deleted."
                    )
                    deletedNodeModulesCount["value"] += 1
    else:
        print(
            f"{bcolors.FAIL}[NMK FAILED]{bcolors.ENDC}: {path} is not a valid or existing absolute path.\n"
            f"{bcolors.FAIL}[NMK FAILED]{bcolors.ENDC}: Please enter a valid absolute path instead."
        )


# Core code
if len(sys.argv) == 1:
    path = input(
        f"{bcolors.OKCYAN}Please enter the absolute path where you want to delete all node_modules :{bcolors.ENDC}\n"
    )
    delete_node_modules_where(path, deletedNodeModulesCount)
else:
    paths = sys.argv[1:]
    for path in paths:
        delete_node_modules_where(path, deletedNodeModulesCount)

finalCount = deletedNodeModulesCount.get("value")
print(f"{bcolors.OKCYAN}JOB DONE!{bcolors.ENDC}")
print(
    f"{bcolors.OKCYAN}{finalCount} node_modules folders has been deleted.{bcolors.ENDC}"
)

