from __future__ import print_function
import re, sys, glob, getopt, os

def usage():
    print('aspx2url v1.0')
    print('Usage:')
    print(sys.argv[0]+' -d -h filename(s)') 
    print('-d : Delete original file')
    print('-h : This help')

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd")
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)
    deleteOriginal = False
    for option,value in opts:
        if option == '-h':
            usage()
            sys.exit()
        elif option == '-d':
            deleteOriginal = True
    for origFilename in args:
        with open(origFilename, "r") as f:
            html_doc = f.read()
        prog = re.compile('\<mso\:URL.*?\>(.*?),.*?\<\/mso\:URL\>', re.M)    
        result = prog.search(html_doc)
        url = result.group(1);
        filename = re.search('(.*?)\.aspx',origFilename).group(1)
        fullFilename = filename+'.url'
        with open(fullFilename, 'w') as out:
            out.write('[InternetShortcut]\n')
            out.write('URL='+url)
            out.write('\n')
        if deleteOriginal:
            os.remove(origFilename)
        
if __name__ == '__main__':
    main()
