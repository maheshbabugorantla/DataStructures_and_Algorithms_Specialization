import sys
import threading
import os
from tree_height import TreeHeight


def main():

    for filename in os.listdir('{}/tests'.format(os.getcwd())):

        # if filename.endswith('21') or filename.endswith('22') or filename.endswith('23') or filename.endswith('24'):
        #     continue

        if filename.endswith('.a'):
            continue
        try:
            fp = open('./tests/{}'.format(filename), 'r')
            output_fp = open('./tests/{}.a'.format(filename), 'r')
            lines = fp.readlines()
            len_parents = int(lines[0].strip())
            parents = list(map(int, lines[1].strip().split()))
            assert(len(parents) == len_parents)
            # print("Filename: {}".format(filename, len_parents))
            solution = int(output_fp.readlines()[0].strip())
            # print(parents)
            tree_height = TreeHeight(parents)
            code_output = tree_height.get_tree_max_height()

            if code_output == solution:
                print("Test {} Success".format(filename))
            else:
                print("Test {} Failed: ".format(filename))
                print()
                print("\tSolution: {}".format(solution))
                print("\tOutput: {}\n".format(code_output))
        except Exception:
            print("Exception Occurred: {}".format(filename))
    print("Done")

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()
