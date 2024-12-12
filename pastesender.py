from time import sleep
import argparse
from keymapper import sendStringAsVK

defaultFile = "./clipboard.txt"

def init():
    parser = argparse.ArgumentParser(
                    prog='Send From File',
                    description='can\'t copy paste to an rdp ? say no more!')
    parser.add_argument(
                    'filepath',
                    nargs="?",
                    type=str,
                    help="Path to the file, if empty then use the default path (./clipboard.txt)",
                    default=defaultFile)
    args = parser.parse_args()
    return args

def getFileContent(filePath):
    with open(filePath, "r") as file:
        content = file.read()
    return content

def main():
    # Wait 10 seconds so user can focus on the target window
    sleep(10)
    args = init()
    content = getFileContent(args.filepath)
    sendStringAsVK(content)  # Use our helper from keymapper.py
    return

if __name__ == "__main__":
    main()
