#!/usr/bin/env python

#Application global vars
#TODO Set global vars.
VERSION = "0.1"
PROG_NAME = "template"
PROG_DESC = "TheTwitchy standard Python template."
PROG_EPILOG = "Written by TheTwitchy. Source available at github.com/TheTwitchy/pytemplate"

#Application imports.
import sys,signal
#TODO Insert additional imports here.

#Try to import argparse, not available until Python 2.7
try:
    import argparse
except ImportError:
    print_err("Failed to import argparse module. Needs python 2.7+.")
    quit()
#Try to import termcolor, ignore if not available.
DO_COLOR = True
try:
    import termcolor
except ImportError:
    DO_COLOR = False
def try_color(string, color):
    if DO_COLOR:
        return termcolor.colored(string, color)
    else:
        return string
#Print some info to stdout
def print_info(*args):
    sys.stdout.write(try_color(PROG_NAME + ": info: ", "green"))
    sys.stdout.write(try_color(" ".join(map(str,args)) + "\n", "green"))
#Print an error to stderr
def print_err(*args):
    sys.stderr.write(try_color(PROG_NAME + ": error: ", "red"))
    sys.stderr.write(try_color(" ".join(map(str,args)) + "\n", "red"))
#Print a debug statement to stdout
def print_debug(*args):
    sys.stderr.write(try_color(PROG_NAME + ": debug: ", "blue"))
    sys.stderr.write(try_color(" ".join(map(str,args)) + "\n", "blue"))
#Handles early quitters.
def signal_handler(signal, frame):
    print ""
    quit(0)

#Because.
#TODO Generator is found at http://patorjk.com/software/taag/#p=display&f=Big&t=template
def print_header():
    print " _                       _       _       "
    print "| |                     | |     | |      "
    print "| |_ ___ _ __ ___  _ __ | | __ _| |_ ___ "
    print "| __/ _ \ '_ ` _ \| '_ \| |/ _` | __/ _ \\"
    print "| ||  __/ | | | | | |_) | | (_| | ||  __/"
    print " \__\___|_| |_| |_| .__/|_|\__,_|\__\___|"
    print "                  | |                    "
    print "                  |_|                    "
    print "                             version " + VERSION
    print ""

#Main application entry point.
def main():
    #Signal handler to catch CTRL-C (quit immediately)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    #Setup the argparser and all args
    parser = argparse.ArgumentParser(prog=PROG_NAME, description=PROG_DESC, epilog=PROG_EPILOG)
    parser.add_argument("-v", "--version", action="version", version="%(prog)s " + VERSION)
    parser.add_argument("-q", "--quiet", help="surpress extra output", action="store_true", default=False)
    #TODO Insert additional application args.
    parser.add_argument("-i", "--int", help="an optional int", type=int, default=100)
    parser.add_argument("-y", "--yes", help="a 'yes' switch (default)", dest="switch", action="store_true")
    parser.add_argument("-n", "--no", help="a 'no' switch", dest="switch", action="store_false")
    parser.set_defaults(switch=True)
    parser.add_argument("string", help="a required string", nargs="+")
    args = parser.parse_args()

    #TODO Retrieve arg values for application use.
    var_quiet = args.quiet
    var_int = args.int
    var_switch = args.switch
    var_string_args = args.string

    #Print out some sweet ASCII art.
    if not var_quiet:
        print_header()

    #TODO Begin application logic.
    print_debug("int    = %d" % var_int)
    print_debug("switch = %r" % var_switch)
    print_debug("string = '%s'" % var_string_args)
    print_info("Preparing to exit non-gracefully...")
    print_err("Now exiting.")


if __name__ == "__main__":
    main()
    quit(0)
