import sys

def append_namespace(namespace):
    file_path = 'aws-eks-test-cluster1/namespaces.txt'
    with open(file_path, 'a+') as file:
        file.seek(0)
        lines = file.readlines()
        if lines and not lines[-1].endswith('\n'):
            file.write('\n')
        file.write(namespace + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 append_namespace.py <namespace>")
        sys.exit(1)
    namespace = sys.argv[1]
    append_namespace(namespace)
