#!/usr/bin/env python
import click
import os

@click.command()
@click.option("--preferred", "-p", 'preferred',
              help="Preferred file extension",
              required=True,
)
def process(preferred):
    """ Processes the input STDIN and stores the result to
    STDOUT.
    """
    stdout = click.get_text_stream('stdout')
    stdin = click.get_text_stream('stdin')
    files = dict()
    for line in stdin:
      filename, file_extension = os.path.splitext(line)
      current_ext = files.get(filename)
      if current_ext is None:
          files[filename] = file_extension
      elif file_extension == preferred:
          files[filename] = file_extension

    for filename, file_extension in files.items():
        stdout.write(filename + file_extension)

if __name__ =="__main__":
    process()
