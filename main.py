import argparse
import sys, subprocess

sys.path.append("../src")

from AES import *

if __name__ == "__main__" :

    AES_Instance = AES()

    parser = argparse.ArgumentParser(prog="AES")

    subParserMode =   parser.add_argument_group("MODE", "Choose one of the following modes")

    subParserMode.add_argument('-T', help="Testing mode", action='store_true')

    subParserMode.add_argument('-E', help="Encryption mode", action='store_true')
    subParserMode .add_argument('-D', help="Decryption mode", action='store_true')

    subParserKey = parser.add_argument_group("KEY", "Choose one of the following commands to insert the key")
    
    subParserKey.add_argument('-kr', help="Key from size of a randomly generated byte array (size >= 16)", type=int, metavar="size")
    subParserKey.add_argument('-kb', help="Key from bytes in hexadecimal format", type = str, metavar="hex")
    subParserKey.add_argument('-kt', help="Key from text", type=str, metavar="text")

    subParserData = parser.add_argument_group("DATA", "Choose one of the following commands to insert the data to be encrypted / decrypted")

    subParserData.add_argument('-dr', help="Data from size of a randomly generated byte array", type=int, metavar= "size")
    subParserData.add_argument('-dt', help="Data from text", type = str, metavar="text")
    subParserData.add_argument('-df', help="Data from file using a path", type = str, metavar="path")

    subParserOut = parser.add_argument_group("OUTPUT", "Choose on of the following commands to output / save the result")

    subParserOut.add_argument('-ob', help="Output bytes", action='store_true')
    subParserOut.add_argument('-ot', help="Output text", action='store_true')
    subParserOut.add_argument('-of', help="Output file to a path", type = str, metavar="path")

    # Get the arguments as a list
    args = sys.argv[1:]
    
    # Print help if no arguments are passed
    if len(args) == 0:
    
        parser.print_help()
        sys.exit(0)

    # Parse the arguments
    else :

        parse = parser.parse_args(args)

    # Run test
    if parse.T :

        subprocess.run(["python", "../tests/test_unittest.py"])
        sys.exit()


    # Select key 
    if (parse.kb != None and parse.kt != None) \
            or (parse.kr != None and parse.kt != None) \
            or (parse.kr != None and parse.kb != None) :
        
        print("You can't have multiple keys use : -kr or -kb or -kt")
        sys.exit(0)

    if (parse.kb == None and parse.kt == None and parse.kr == None):
    
        print("You should insert a key using : -kr or -kb or -kt")
        sys.exit(0)

    # Load the key value
    if parse.kr != None :

        AES_Instance.UseRandomKey(parse.kr)
        
    elif parse.kb != None :

        AES_Instance.UseBytesKey(parse.kb)
    
    elif parse.kt != None :

        AES_Instance.UseTextKey(parse.kt)

    # Select data
    if (parse.dt != None and parse.dr != None) \
        or (parse.dt != None and parse.df != None) \
        or (parse.df != None and parse.dr != None) :
    
        print("You can't have multiple data inputs use : -dr or -dt or -df")
        sys.exit(0)

    if (parse.dr == None and parse.dt == None and parse.df == None):
    
        print("You sould have a data input using : -dr or -dt or -db")
        sys.exit(0)

    # Load the data  
    if parse.dr != None :

        AES_Instance.FromRandomByte(parse.dr)

    elif parse.dt != None :

        AES_Instance.FromText(parse.dt)

    elif parse.df != None :

        AES_Instance.FromFile(parse.df)

    # Select the mode
    if parse.E and parse.D :

        print("You can't select both modes : -E or -D")
        sys.exit(0)

    if not(parse.E) and not(parse.D) :

        print("You should select a mode : -E or -D")
        sys.exit(0)

    # Select output 
    if (parse.ob != False and parse.ot != False) \
        or (parse.ot != False and parse.of != None) \
        or (parse.of != None and parse.ob != False) :
    
        print("You can't have multiple data outputs use : -ob or -ot or -of")
        sys.exit(0)

    if (parse.ob == False and parse.ot == False and parse.of == None):
    
        print("You sould have a data output using : -ob or -ot or -of")
        sys.exit(0)

    # Run the selected mode
        
    if parse.E :

        AES_Instance.Cipher()

    elif parse.D :

        AES_Instance.UnCipher()

    # Run ouput
        
    if parse.ob :

        AES_Instance.ToBytes()

    elif parse.ot :

        AES_Instance.ToText()

    elif parse.of != None :

        AES_Instance.ToFile(parse.of)
         
