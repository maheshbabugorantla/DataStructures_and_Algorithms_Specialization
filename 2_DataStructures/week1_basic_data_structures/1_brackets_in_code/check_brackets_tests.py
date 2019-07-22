import os

from check_brackets import find_mismatch

def main():
    for filename in os.listdir('{}/tests'.format(os.getcwd())):
        if filename.endswith('.a'):
            continue
        fp = open('./tests/{}'.format(filename), 'r')
        output_fp = open('./tests/{}.a'.format(filename), 'r')
        snippet = fp.readlines()[0].strip()
        # print("Filename: {}".format(filename))
        solution = output_fp.readlines()[0].strip()

        code_output = find_mismatch(snippet)

        if not str("Success" if code_output==-1 else code_output) == solution:
            print("tests/{} Failed:".format(filename))
            print("\tExpected Output: {}".format(solution))
            print("\tYour Output: {}\n\n".format(code_output))
        else:
            print("tests/{} Success".format(filename))

if __name__ == "__main__":
    main()
