from keysender import pressKey, releaseKey
from time import sleep
import argparse
import binascii

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

def letterToHex(letter):
    hexStringValue = hex(ord(letter))
    cleanedUp = format(ord("c"), "x")

def sendString(string):
    for letter in string:
        decvalue = ord(letter)
        pressKey(decvalue)
        sleep(1)
        releaseKey(decvalue)

def getFileContent(filePath):
    with open(filePath, "r") as file:
        content = file.read()
        file.close
    return content

def main():
    sleep(10)
    args = init()
    content = getFileContent(args.filepath)
    sendString(content)
    return


if __name__ == "__main__":
    main()
 
