def count_character_appearances(letter, target_string):
    if not _inputs_are_valid(letter, target_string):
        return False
    return len([l for l in target_string if l == letter])

def find_character_appearances(letter, target_string):
    if not _inputs_are_valid(letter, target_string):
        return False
    appearances = []
    for i in range(0, len(target_string)):
        if target_string[i] != letter: continue
        appearances.append(i)
    return appearances

def _inputs_are_valid(letter, target_string):
    arguments_valid = True
    if not isinstance(target_string, str):
        arguments_valid = False
    if len(target_string) == 0:
        arguments_valid = False
    if not isinstance(letter, str):
        arguments_valid = False
    if len(letter) != 1:
        arguments_valid = False
    return arguments_valid

if __name__ == '__main__':
    print(count_character_appearances('a', 'aardvark'))
    print(find_character_appearances('a', 'aardvark'))
