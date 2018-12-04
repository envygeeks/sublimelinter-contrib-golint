from SublimeLinter.lint import util, Linter, WARNING
from os import path


class GoLint(Linter):
    tempfile_suffix = "-"
    default_type = WARNING
    error_stream = util.STREAM_STDOUT
    regex = r'(?:[^:]+):(?P<line>\d+):(?P<col>\d+)?(:(?:(?P<warning>warning)|(?P<error>error)))?:\s*(?P<message>.*)'
    defaults = {
        'selector': 'source.go'
    }

    def cmd(self):
      """Gives back the command with a relative path."""
      f, e = path.basename(self.filepath), self.which("gometalinter")
      if e is not None:
        return (
          e,
          "--fast", "--concurrency=12",
          "${args}", f
        )

      return None
