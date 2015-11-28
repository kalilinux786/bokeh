''' Provide a subcommand to generate serialized JSON output from a Bokeh
application.

'''
from __future__ import print_function

from ..subcommand import Subcommand
from ..util import build_single_handler_application

class JSON(Subcommand):
    ''' Subcommand to output applications as serialized JSON

    '''

    name = "json"

    help = "Emit serialized JSON for one application"

    def __init__(self, **kwargs):
        super(JSON, self).__init__(**kwargs)

        self.parser.add_argument(
            'file',
            metavar='DIRECTORY-OR-SCRIPT',
            help="The app directory or script to generate JSON for",
            default=None
        )

        self.parser.add_argument(
            '--indent',
            metavar='LEVEL',
            type=int,
            help="indentation to use when printing",
            default=None
        )

    def invoke(self, args):
        application = build_single_handler_application(args.file)

        doc = application.create_document()
        print(doc.to_json_string(indent=args.indent))