# Copyright 2025 Sam Jamsh
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



def isprintable_(byte):
    if byte.isprintable():
        return chr(byte)   # printable
    else:
        return UNKNOWN_SYMBOL


def isprintable(byte):
    if 31 < byte < 127 or 159 < byte < 256:
        return chr(byte)   # printable
    else:
        return f"{cu_color}{UNKNOWN_SYMBOL}{reset_color}"


def convertInt2(system, integer):
    if system == "hex":
        return f"{integer:x}"

    elif system == "oct":
        return f"{integer:o}"

    elif system == "dec":
        return f"{integer:d}"

    elif system == "bin":
        return f"{integer:b}"


def view_hex(filename, offset_system, BYTESLEN, output):

    RUN = True
    O = False
    DATA = None
    chunked_bytes = None
    asciiData = ''


    offset = entry_address # 0

    try:
        if output != None:
            O = True  # unnecessary (delete line)
            output_file = open(output, 'a')
            sys.stdout = output_file


        with open(filename, 'rb') as file_bytes:
            file_bytes.seek(entry_address)

            while RUN:


                chunked_bytes = file_bytes.read(BYTESLEN)

                if offset == exit_address:
                    #BYTESLEN = x #
                    chunked_bytes = chunked_bytes[:X + 1]
                    RUN = False

                if not chunked_bytes:
                    if O == True:
                        output_file.close()
                    break


                chunkLen = len(chunked_bytes)

                str_offset = convertInt2(offset_system, offset)

                _offset_ = '0' * (offsetLim - len(str_offset)) + str_offset

                for asciiByte in chunked_bytes:  asciiData += isprintable(asciiByte)

                _ascii_data_ = asciiData + (' ' * (asciiLim - len(asciiData)))
                _ascii_data_ = f"|{_ascii_data_}|"

                chunked_bytes = [f"{byte:02x}" for byte in chunked_bytes]
                chunked_bytes = ' '.join(chunked_bytes)
                _chunked_bytes_ = chunked_bytes + (' ' * (bytesLim - len(chunked_bytes)))

                if hideOFFSET == True:
                    _offset_ = ''

                if hideASCII == True:
                    _ascii_data_ = ''

                if hideBOTH == True:
                    _offset_, _ascii_data_ = '', ''


                DATA = f"{_offset_}  {_chunked_bytes_}  {_ascii_data_}"

                print(DATA)
                offset += chunkLen
                asciiData = ''

                # offset += chunkLen

    except Exception as err:
        exit(err)


def str2int(value):
    try:
        return int(value)
    except Exception as err:
        exit(err)




import sys

ALLOWEDS = ["-cu", "--colour-unknown", "-ho", "--hide-offset", "-ha", "--hide-ascii", "-hb", "--hide-both", "-offset", "-O", "--output", "-io", "--initial-offset", "-fo", "--final-offset", "-bl", "--bytes-length", "-us", "--unknown-symbol", "-or", "--offset-range", "--version", "--help"]

offsetNumericalSystems = ["dec", "hex", "oct", "bin"]

argsLen = len(sys.argv)
file = sys.argv[-1] # filename
output_filename = None  # sys.stdout
UNKNOWN_SYMBOL = '.'
RUN = True
X = None

hideOFFSET = False
hideASCII = False
hideBOTH = False

entry_address = 0
exit_address = -1  # the default must be negative

CU = False
reset_color = "\033[0m"
invert_color = "\033[7m"
cu_color = reset_color

offset_system = "dec"
bytesLen = 16
offsetLim = 10
bytesLim = 47 # 16 x 2 + 16 - 1 = N x 2 + N - 1
asciiLim = 16

i = 1

if argsLen == 2:
        arg = sys.argv[1]
        if arg == "--version":
            exit(f"Hd version 1.0\nThis is a hexadecimal viewer software used to view files data in hex format\nThis program was created by Sam Jamsh the cyb3rguy and it was created in 15/07/2025 and published in 20/07/2025\nYou can modify and do whatever you want with this program and source code because its a free and open source software also available on github\nContacts: instagram> @sam.jamsh, email> thecyb3rguy@protonmail.com")


        elif arg == "--help":
            print(f"Usage: {sys.argv[0]} [OPTION]... [FILE]\nView FILE(S) Data in Hexadecimal.\n")
            exit("-O, --output            redirects the output to a specific file\n-ho, --hide-offset       hides the offset section\n-ha, --hide-ascii       hides the ascii section\n-hb, --hide-both        hides both offset and ascii sections\n-cu, --colour-unknown   highlights the unknown characters symbols with colors\n-io, --initial-offset    sets the initial offset address\n-fo, --final-offset       sets the final offset address\n-or, --offset-range      specifies an range of initial and final offsets\n-us, --unknown-symbol   specifies the symbol to be used for unknown characters on ascii section\n     available symbols:          dot, at, star, and hash\n-bl, --bytes-length     specifies the number of bytes per line\n-offset                  specifies the offset numeric system\n     available numeric systems:  dec, hex, oct and bin \n-v, --version           shows version\n-h, --help              shows this message\n")

        else:
            file = arg # comment it




elif argsLen >= 3:

    argsLen -= 1  # delete/remove file (filename)
    while (i < argsLen):
        arg = sys.argv[i]

        if arg[0] == '-' and arg not in ALLOWEDS: # param starts with - or -- & not in list
            exit(f"parameter error: invalid parameter {arg}")
        # else: pass

        if arg == "-cu" or arg == "--colour-unknown":
            cu_color = invert_color
            print("ARG = -cu (--colour-unknown)")
            i += 1
            continue


        elif arg == "-ho" or arg == "--hide-offset":
            hideOFFSET = True
            print("ARG = -ho (--hide-offset)")
            i += 1
            continue


        elif arg == "-ha" or arg == "--hide-ascii":
            hideASCII = True
            print("ARG = -ha (--hide-ascii)")
            i += 1
            continue


        elif arg == "-hb" or arg == "--hide-both":
            hideBOTH = True
            print("ARG = -hb (--hide-both)")
            i += 1
            continue




        elif arg == "-offset":
            if (argsLen > (i+1)):
                #["dec", "hex", "oct", "bin"]
                value = sys.argv[i + 1] #
                if value in offsetNumericalSystems:
                    if value == "dec":
                        offset_system = "dec"

                    elif value == "hex":
                        offset_system = "hex"

                    elif value == "oct":
                        offset_system = "oct"

                    elif value == "bin":
                        offset_system = "bin"


                else:
                    exit(f"parameter value error: value {value} is invalid for -offset option")

                i += 1
                continue

            else:
                exit("parameter error: unsufficient parameters given, no value found for -offset option")





        elif arg == "-O" or arg == "--output":
            if (argsLen > (i+1)):
                
                output_filename = sys.argv[i + 1]
                i += 1
                continue
            else:
                exit("parameter error: unsufficient parameters given, no value found for -O option")





        elif arg == "-io" or arg == "--initial-offset":
            if (argsLen > (i+1)):
                entry_address = str2int(sys.argv[i + 1])

                if entry_address < 0:
                    exit("parameter error: initial offset address must be a posivite number")

                i += 1
                continue

            else:
                exit("parameter error: unsufficient parameters given, no value found for -io option")





        elif arg == "-fo" or arg == "--final-offset":
            if (argsLen > (i+1)):
                exit_address = str2int(sys.argv[i + 1])

                if exit_address < 0:
                    exit("parameter error: final offset address must be a posivite number")

                lim = bytesLen * int(exit_address / bytesLen)
                #rest = exit_address - lim
                rest = exit_address - int(exit_address / bytesLen) * bytesLen

                exit_address = lim
                X = rest

                i += 1
                continue

            else:
                exit("parameter error: unsufficient parameters given, no value found for -fo option")





        elif arg == "-bl" or arg == "--bytes-length":
            if (argsLen > (i+1)):

                # bytesLen must be >= 4
                bytesLen = str2int(sys.argv[i + 1])
                bytesLim = bytesLen * 2 + bytesLen - 1
                asciiLim = bytesLen

                i += 1
                continue

            else:
                exit("parameter error: unsufficient parameters given, no value found for -bl option")





        elif arg == "-us" or arg == "--unknown-symbol":
            unknown_symbols = {'dot':'.', 'at':'@', 'star':'*', 'hash':'#'}
            # allowed_values = ['dot', 'at', 'star', 'hash']

            if (argsLen > (i+1)):
                argvalue = sys.argv[i + 1]
                if argvalue  not in ['dot', 'at', 'star', 'hash']:
                    exit(f"parameter error: invalid unknown symbol {argvalue}")
                else:
                    UNKNOWN_SYMBOL = unknown_symbols[argvalue]

                i += 1
                continue

            else:
                exit("parameter error: unsufficient parameters given, no value found for -us option")






        elif arg == "-or" or arg == "--offset-range":
            if (argsLen > (i+1)):

                entry_address = str2int(sys.argv[i + 1])

                if entry_address < 0:
                    exit("parameter error: initial offset address must be a posivite number")

                exit_address = str2int(sys.argv[i + 2]) - entry_address

                if exit_address < 0:
                    exit("parameter error: final offset address must be a posivite number")

                lim = bytesLen * int(exit_address / bytesLen)
                #rest = exit_address - int(exit_address / bytesLen) * bytesLen
                rest = exit_address - lim
                exit_address = lim + entry_address
                X = rest

                i += 1
                continue

            else:
                exit("parameter error: unsufficient parameters given, no value found for -or option")



        i+=1
    # else: parameter exists but is not supported yet (still being developed)

else:
    print("parameter error: invalid argument!")
    exit(f"try: python3 {sys.argv[0]} filename")
#-----------------------------------------------

#-----------------------------------------------

#_______________________________________________
view_hex(file, offset_system, bytesLen, output_filename)

