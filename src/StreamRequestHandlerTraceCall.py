# coding: utf-8
from __future__ import absolute_import

import aoiktracecall.config
import aoiktracecall.trace
import aoiktracecall.wrap


aoiktracecall.config.set_config('FIGLET_WIDTH', 200)


trace_specs = [
    ('aoiktracecall([.].+)?', False),

    ('.+[.]copy', False),

    ('.+[.]__setattr__', True),

    ('socket.IntEnum', False),

    ('socket._intenum_converter', False),

    ('socket[.].+[.]getsockname', False),

    ('socket[.].+[.]getpeername', False),

    ('(socket|SocketServer)[.].+[.]fileno', False),

    ('socket._realsocket', False),

    ('socket[.](socket|_socketobject|SocketType)[.]__init__', {'highlight'}),

    ('socket[.](socket|_socketobject|SocketType)[.]bind', {'highlight'}),

    ('socket[.](socket|_socketobject|SocketType)[.]listen', {'highlight'}),

    ('socket[.](socket|_socketobject|SocketType)[.]accept', {'highlight'}),

    ('socket[.](socket|_socketobject|SocketType)[.]makefile', {'highlight'}),

    ('socket[.](socket|_socketobject|SocketType)[.]close', {'highlight'}),

    ('socket.SocketIO.__init__', {'highlight'}),

    ('socket[.].+[.]__[^.]+__', False),

    ('socket([.].+)?', True),

    ('selectors.ABCMeta', False),

    ('selectors.Mapping', False),

    ('selectors.SelectSelector', False),

    ('selectors.DefaultSelector.__init__', {'highlight'}),

    ('selectors.DefaultSelector.select', 'hide_tree'),

    ('selectors.DefaultSelector.register', {'highlight'}),

    ('selectors[.].+[.]__[^.]+__', False),

    ('selectors([.].+)?', True),

    ('(socketserver|SocketServer)._eintr_retry', False),

    ('(socketserver|SocketServer)._ServerSelector', False),

    ('(socketserver|SocketServer).BaseServer.__init__', {'highlight'}),

    ('(socketserver|SocketServer).TCPServer.__init__', {'highlight'}),

    ('(socketserver|SocketServer).TCPServer.server_bind', {'highlight'}),

    ('(socketserver|SocketServer).TCPServer.setup_environ', {'highlight'}),

    ('(socketserver|SocketServer).TCPServer.server_activate', {'highlight'}),

    ('(socketserver|SocketServer).TCPServer.serve_forever', {'highlight'}),

    ('(socketserver|SocketServer).TCPServer._handle_request_noblock',
        {'highlight'}),

    ('(socketserver|SocketServer).TCPServer.set_app', {'highlight'}),

    ('(socketserver|SocketServer).TCPServer.get_request', {'highlight'}),

    ('(socketserver|SocketServer).TCPServer.verify_request', {'highlight'}),

    ('(socketserver|SocketServer).TCPServer.process_request', {'highlight'}),

    ('(socketserver|SocketServer).TCPServer.finish_request', {'highlight'}),

    ('(socketserver|SocketServer).TCPServer.shutdown_request', {'highlight'}),

    ('(socketserver|SocketServer).TCPServer.close_request', {'highlight'}),

    ('(socketserver|SocketServer)[.].+[.]service_actions', False),

    ('(socketserver|SocketServer)[.].+[.]__[^.]+__', False),

    ('(socketserver|SocketServer)([.].+)?', True),

    ('__main__.CustomHandler', True),

    ('__main__.CustomHandler.__init__', {'highlight'}),

    ('__main__.CustomHandler.setup', {'highlight'}),

    ('__main__.CustomHandler.handle', {'highlight'}),

    ('__main__.CustomHandler.finish', {'highlight'}),

    ('__main__.main', {'highlight'}),

    ('__main__[.].+[.]__[^.]+__', False),

    ('__main__([.].+)?', True),
]


aoiktracecall.trace.trace_calls_in_specs(specs=trace_specs)


try:
    # Python 3
    import socketserver
except ImportError:
    # Python 2
    import SocketServer as socketserver


class CustomHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline(65535)

        self.wfile.write(data)


def main():
    try:
        server = socketserver.TCPServer(
            ('127.0.0.1', 8000), CustomHandler
        )

        server.serve_forever()

    except KeyboardInterrupt:
        pass


aoiktracecall.trace.trace_calls_in_this_module()


if __name__ == '__main__':
    exit(main())
