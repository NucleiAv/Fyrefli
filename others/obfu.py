# The following is the script/code for the FyreFli Obfuscator, written in python.



import urllib.parse, sys
import hashlib
import fileinput
from argparse import ArgumentParser

lackofart = '''
________________________________________________________________________________________________________________________________________
      
        FyreFli Obfuscator
........................................................................................................................................
'''

def paramEncode(params="", charset="", encodeEqualSign=False, encodeAmpersand=False, urlDecodeInput=True, urlEncodeOutput=True,hashType="", fileInput=False):

    equalSign = "="
    ampersand = "&"

# Incase of File Input we will be using Buffer.

    buffer = '\n'

# If there is a File Input i.e. "fileInput" is TRUE.

    if(fileInput):
        for line in fileinput.input(files = params, encoding="ascii"):
            buffer += line + '\n'
        buffer = buffer[:len(buffer)-1]
        print('')
        print(f"Buffer: {buffer}")
        print('')
        params = buffer

# If there is a Hash Input, hence there has to be a Hash Type i.e. "hashType" is TRUE. There may/may not be any file.
# It supports md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'blake2b', 'blake2s'.
# It also supports 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'shake_128', 'shake_256.

    if(hashType):
        if(hashType == "md5"):
            m = hashlib.md5()
        if(hashType == "sha1"):
            m = hashlib.sha1()
        if(hashType == "sha256"):
            m = hashlib.sha256()
        if(hashType == "sha224"):
            m = hashlib.sha224()
        if(hashType == "sha384"):
            m = hashlib.sha384()
        if(hashType == "sha512"):
            m = hashlib.sha512()
        if(hashType == "blake2b"):
            m = hashlib.blake2b()
        if(hashType == "blake2s"):
            m = hashlib.blake2s()
        if(hashType == "sha3_224"):
            m = hashlib.sha3_224()
        if(hashType == "sha3_256"):
            m = hashlib.sha3_256()
        if(hashType == "sha3_384"):
            m = hashlib.sha3_384()
        if(hashType == "sha3_512"):
            m = hashlib.sha3_512()
        if(hashType == "shake_128"):
            m = hashlib.shake_128()
        if(hashType == "shake_256"):
            m = hashlib.shake_256()
        m.update(params.encode('ascii'))
        return m.hexdigest()
    
# If we don't use Hashing but Encoding. There may/may not be any file.
# It supports UTF8 ,UTF16, UTF32.
# It also supports IBM037, IBM039, IBM424, etc.

    if '=' and '&' in params:
        if encodeEqualSign:
            equalSign = equalSign.encode(charset)
        if encodeAmpersand:
            ampersand = ampersand.encode(charset)
        params_list = params.split("&")
        for param_pair in params_list:
            param, value = param_pair.split("=")
            if urlDecodeInput:
                param = urllib.parse.unquote(param)
                value = urllib.parse.unquote(value)
            param = param.encode(charset)
            value = value.encode(charset)
            if urlEncodeOutput:
                param = urllib.parse.quote_plus(param)
                value = urllib.parse.quote_plus(value)
            if result:
                result += ampersand
            result += param + equalSign + value

    else:
        if urlDecodeInput:
            params = urllib.parse.unquote(params)
        result = params.encode(charset)
        if urlEncodeOutput:
            result = urllib.parse.quote_plus(result)
    return result

# The Main Function

def main():
    
    print(lackofart)

    parser = ArgumentParser('python obfu.py')
    parser._action_groups.pop()

    # A simple hack/way to have required arguments and optional arguments separately

    required = parser.add_argument_group('Required Arguments')
    optional = parser.add_argument_group('Optional Arguments')

    # Required Options

    # A string must be there independent of the presence of file.
    # If file is present then string is the file name, else it can be any artbitrary string provided by the user.

    required.add_argument('-s', help='String to obfuscate', dest='str')
    
    # Optional Arguments (main stuff and necessary)

    optional.add_argument('-ueo', help='URL Encode Output', dest='ueo', action='store_true')
    optional.add_argument('-udi', help='URL Decode Input', dest='udi', action='store_true')
    optional.add_argument('-e', help='Encoding type. eg: ibm037 , utf8 , utf16 , utf32 , etc', dest='enc')
    optional.add_argument('-hash', help='Enable Hash Input', dest='hash')
    optional.add_argument('-f', help='Enable File Input', dest='fi', action = "store_true")
    
    print('\n')

    args = parser.parse_args()

    if not len(sys.argv) > 1:
        parser.print_help()
        quit()

    print('Input: %s' % (args.str))
    print('Output: %s' % (paramEncode(params=args.str, charset=args.enc, urlDecodeInput=args.udi, urlEncodeOutput=args.ueo, hashType=args.hash, fileInput=args.fi)))
    print('')
    print('_________________________________________________________________________________________________________________________________________')
    print('')

if __name__ == '__main__':
    main()