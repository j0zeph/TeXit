"""Command-line utility that takes a file as input, and adds TeX syntax to
it, based on markers specified in the inputted file"""

import os
import re
import sys
import typing


# content types
ctt_type = {
    'text': r'\text',
    }

size = {
    'large': r'\large',
    }

brace = {
    'open': '{',
    'close': '}',
    }

# commonly used TeX syntax
common = {
    'tex_dollars': '$$',
    'large_txt': f"{size['large']}" + f"{ctt_type['text']}" +
                 f"{brace['open']}",
    'end_slash': f"{brace['close']}" + r'\\',
    }

# markers and their TeX translations
mapping = {
    '-bp': r'\bullet' + f"{common['large_txt']}",
    '-bf': f"{size['large']}" + r'\textbf{',
    '-br': '$$$$',
    '-bbr': '$$ $$',
    }

# generate regex from the keys of the mappings dict
starts = ''.join(['^' + str(x) + '|' for x in mapping.keys()])
possible_starts = r'(?P<marker>' + starts + r')?'
rest_of_string = r'([ ]*)?(?P<text>.*)?(?P<nln>\n)?'

PATTERN = possible_starts + rest_of_string

infile_name = ''


def main():

    # check the correct number of arguments
    if not len(sys.argv) == 2:
        print(show_error('usage'))
        sys.exit(1)
    else:
        global infile_name
        infile_name = sys.argv[1]

    if not os.path.exists(infile_name):
        print(show_error('file_nonexistent'))
        print()
        print(show_error('usage'))
        exit(2)

    # save the output file in the same location as the input file
    infile_pattern = r'^(?P<origin>.*?)?(?P<name>[\w\.]*)(?P<ext>\.[\w]*)$'
    infile_match = re.match(infile_pattern, infile_name)

    outfile_location = infile_match.group('origin')
    outfile_name = infile_match.group('name')
    outfile_path = outfile_location + outfile_name + '_texit_out.txt'

    # prepare for writing
    outfile = open(outfile_path, 'a', encoding='utf8')

    # open the input file, and process each line
    with open(infile_name, 'r', encoding='utf-8') as infile:
        process_files(infile, outfile)

    outfile.close()


def process_files(infile: typing.TextIO, outfile: typing.TextIO) -> None:
    """Processes each line in the input file provided, and writes the
    results of processing onto the output file provided"""

    while True:
        line = infile.readline().strip()

        # at end of file
        if not line:
            break

        # start the TeX
        if line in '-start' or line in '-begin':
            outfile.write(f"{common['tex_dollars']}\n")

        # end the TeX
        elif line in '-end':
            outfile.write(f"{common['tex_dollars']}\n")

        else:
            match = re.match(PATTERN, line)
            marker = match.group('marker')
            text = match.group('text')
            end_slash = common['end_slash']
            large_text = common['large_txt']

            # for a normal line of text
            if marker is None:
                outfile.write(f'{large_text}{text}{end_slash}\n')
            else:
                # special case for standalone -br and -bbr markers
                if marker == '-br':
                    outfile.write(f"{mapping['-br']}\n")

                elif marker == '-bbr':
                    outfile.write(f"{mapping['-bbr']}\n")

                else:
                    if marker == '':
                        outfile.write(f"{common['large_txt']}{text}{end_slash}\n")
                    else:
                        outfile.write(f'{mapping[marker]}{text}{end_slash}\n')


def show_error(message_type: str) -> str:
    """Returns an error message based on the type provided"""

    errors = {
        'usage': 'Usage: python3 texit.py "<filepath>"|filename',
        'file_nonexistent': f'`{infile_name}` does not exist.',
        }

    return errors[message_type]


if __name__ == "__main__":
    main()
