from keysender import pressKey, releaseKey
from time import sleep

VK_SHIFT = 0x10

# Map characters to (VK_CODE, requires_SHIFT)
char_map = {
    'a': (0x41, False), 'b': (0x42, False), 'c': (0x43, False), 'd': (0x44, False), 'e': (0x45, False),
    'f': (0x46, False), 'g': (0x47, False), 'h': (0x48, False), 'i': (0x49, False), 'j': (0x4A, False),
    'k': (0x4B, False), 'l': (0x4C, False), 'm': (0x4D, False), 'n': (0x4E, False), 'o': (0x4F, False),
    'p': (0x50, False), 'q': (0x51, False), 'r': (0x52, False), 's': (0x53, False), 't': (0x54, False),
    'u': (0x55, False), 'v': (0x56, False), 'w': (0x57, False), 'x': (0x58, False), 'y': (0x59, False),
    'z': (0x5A, False),

    '0': (0x30, False), '1': (0x31, False), '2': (0x32, False), '3': (0x33, False), '4': (0x34, False),
    '5': (0x35, False), '6': (0x36, False), '7': (0x37, False), '8': (0x38, False), '9': (0x39, False),

    ' ': (0x20, False),
    '\n': (0x0D, False),  # Enter
    '\r': (0x0D, False),
    '\t': (0x09, False),

    '.': (0xBE, False),
    ',': (0xBC, False),
    '/': (0xBF, False),
    '-': (0xBD, False),
    ';': (0xBA, False),
    ':': (0xBA, True),    # Shift + ;
    '"': (0xDE, True),    # Shift + '
    '[': (0xDB, False),
    ']': (0xDD, False),
    '{': (0xDB, True),    # Shift + [
    '}': (0xDD, True),    # Shift + ]
}

def sendCharAsVK(ch):
    # Attempt direct mapping
    if ch in char_map:
        vk, shift = char_map[ch]
    else:
        # If character isn't directly mapped, try lowercase fallback
        low = ch.lower()
        if low in char_map:
            vk, shift = char_map[low]
            # If original char is uppercase
            if ch.isupper():
                shift = True
        else:
            # Character not mapped at all, skip it
            return

    # Press SHIFT if needed
    if shift:
        pressKey(VK_SHIFT)
        sleep(0.01)

    # Press & release actual key
    pressKey(vk)
    sleep(0.01)
    releaseKey(vk)
    sleep(0.01)

    # Release SHIFT if used
    if shift:
        releaseKey(VK_SHIFT)
        sleep(0.01)

def sendStringAsVK(string):
    for letter in string:
        sendCharAsVK(letter)
        sleep(0.01)

