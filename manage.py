#!/usr/bin/env python
# -*- coding: utf-8 -*-

import atexit
import datetime
import os
import sys
import subprocess
import time

import click
import jinja2
import slugify
import yaml


def get_files(path):
  """Returns the list of files that reside at the given path."""

  files = []
  for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)
    if os.path.isfile(file_path):
      files.append(file_name)
  return files


@click.group()
def cli():
  pass


@cli.command()
def new():
  """Create a new page."""

  page_data['title'] = click.prompt('Title', default='New page')
  date = datetime.datetime.now()
  page_data['timestamp'] = time.mktime(date.timetuple())
  page_data['template'] = config['default_template']
  page_filename = '{0}-{1}'.format(date.strftime('%Y-%m-%d'),
                                   slugify.slugify(page_data['title']))
  page_path = os.path.join(config['src_dir'], page_filename)
  if os.path.isfile(page_path):
    click.echo('A page with this name already exists.')
  else:
    with open(page_path, 'w') as page:
      page.write(config['delimiter'])
      page.write(yaml.dump(page_data, default_flow_style=False))
      page.write(config['delimiter'])
      page.write('\n')


@cli.command()
def mini():
  """Minify CSS and JS."""

  click.echo('Processing CSS')
  subprocess.call(['crammit', '-c', 'config/css.yaml'])
  click.echo('Processing JS')
  subprocess.call(['crammit', '-c', 'config/js.yaml'])


@cli.command()
def compile():
  """Compile pages."""

  click.echo('Compiling pages')
  for page_name in get_files(config['src_dir']):
    page_path = os.path.join(config['src_dir'], page_name)
    with open(page_path, 'r') as page:
      data = page.read().split(config['delimiter'])
      page_data = yaml.load(data[1])
      page_data['content'] = data[2]
    page_data['date'] = datetime.datetime.fromtimestamp(
                                                      page_data['timestamp'])
    page_dist_path = os.path.join(config['dist_dir'], page_name)
    if not os.path.exists(page_dist_path):
      os.makedirs(page_dist_path)
    page_dist_path = os.path.join(page_dist_path, 'index.html')
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(
                                                      config['template_dir']))
    template = env.get_template(page_data['template'])
    render = template.render(page_data)
    with open(page_dist_path, 'w') as page:
      page.write(render)


@cli.command()
@click.pass_context
def update(context):
  """Minify + compile."""

  context.invoke(mini)
  context.invoke(compile)


@cli.command()
def runserver():
  """Run local server."""

  os.chdir(config['dist_dir'])
  process = subprocess.call(['python', '-m', 'SimpleHTTPServer',
            config['port']])
  atexit.register(process.terminate)


if __name__ == '__main__':
  config_path = os.path.join('config', 'config.yaml')
  with open(config_path, 'r') as config_file:
    config = yaml.load(config_file)
  page_data_path = os.path.join('config', 'page_data.yaml')
  with open(page_data_path, 'r') as page_data_file:
    page_data = yaml.load(page_data_file)
  cli()