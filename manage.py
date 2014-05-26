#!/usr/bin/env python
# -*- coding: utf-8 -*-

import atexit
import datetime
import os
import shutil
import subprocess
import sys
import time

import click
import jinja2
import markdown
import slugify
import yaml


@click.group()
def cli():
  pass


@cli.command()
def new():
  """Create a new page."""

  date = datetime.datetime.now()
  page_attributes['title'] = click.prompt('Title', default='New page')
  page_attributes['date'] = date.strftime(config['date_format'])
  page_attributes['template'] = config['default_template']
  file_name = (date.strftime(config['link_prefix_format']) +
                slugify.slugify(page_attributes['title']) + '.md')
  file_path = os.path.join(config['src_dir'], file_name)
  if os.path.isfile(file_path):
    click.echo('A page with the same name already exists.')
  else:
    with open(file_path, 'w') as f:
      f.write(config['delimiter'])
      f.write(yaml.dump(page_attributes, default_flow_style=False))
      f.write(config['delimiter'])
      f.write('\n')


@cli.command()
def mini():
  """Minify CSS and JS."""

  click.echo('Processing CSS')
  subprocess.call(['crammit', '-c', 'config/css.yaml'])
  click.echo('Processing JS')
  subprocess.call(['crammit', '-c', 'config/js.yaml'])


@cli.command()
def build():
  """Build pages."""

  click.echo('Building pages')
  posts = []
  pages = []
  link_prefix_len = len(config['link_prefix_format'])
  # read the files from the src directory
  for file_name in os.listdir(config['src_dir']):
    file_path = os.path.join(config['src_dir'], file_name)
    if os.path.isfile(file_path):

      with open(file_path, 'r') as f:
        data = f.read().split(config['delimiter'])
        page_attributes = yaml.load(data[1])
        page_attributes['content'] = markdown.markdown(data[2], output_format='html5')
      page_attributes['date'] = datetime.datetime.strptime(page_attributes['date'], config['date_format'])
      page_attributes['file_name'] = file_name.replace('.md', '')
      page_attributes['link'] = '/' + file_name.replace('.md', '') + '/'
      try:
        # files that start with 'link_prefix_format' are considered posts
        datetime.datetime.strptime(file_name[:link_prefix_len + 2], config['link_prefix_format'])
        posts.append(page_attributes)
      except ValueError:
        # the rest of them are considered pages
        pages.append(page_attributes)

  # sort posts from newest to oldest
  posts = sorted(posts, key=lambda x: x['date'], reverse=True)

  # add prev and next links to posts
  if config['prev_next_links']:
    for i in range(0, len(posts)):
      if i + 1 <= len(posts) - 1:
        posts[i]['prev_post'] = '/' + posts[i + 1]['file_name'] + '/'
      if i - 1 >= 0:
        posts[i]['next_post'] = '/' + posts[i - 1]['file_name'] + '/'

  environment = jinja2.Environment(loader=jinja2.FileSystemLoader(config['template_dir']))
  # write the .html files
  for page in posts + pages:
    import pprint
    pprint.pprint(page.keys())
    dir_path = os.path.join(config['dist_dir'], page['file_name'])
    if not os.path.exists(dir_path):
      os.makedirs(dir_path)
    template = environment.get_template(page['template'])
    render = template.render(page)
    file_path = os.path.join(dir_path, 'index.html')
    with open(file_path, 'w') as f:
      f.write(render)

  # write the index.html
  template = environment.get_template(config['home_template'])
  render = template.render({'posts': posts})
  file_path = os.path.join(config['dist_dir'], 'index.html')
  with open(file_path, 'w') as f:
    f.write(render)


@cli.command()
@click.pass_context
def update(context):
  """Minify + build."""

  context.invoke(mini)
  context.invoke(build)


@cli.command()
def runserver():
  """Run local server."""

  os.chdir(config['dist_dir'])
  process = subprocess.call(['python', '-m', 'SimpleHTTPServer',
            config['port']])
  # kill child process i.e. http server on exit
  atexit.register(process.terminate)


@cli.command()
def reset():
  """Reset site by removing all files."""

  click.confirm('Reset site and remove all files?', abort=True)
  if os.path.isdir(config['dist_dir']):
    shutil.rmtree(config['dist_dir'])
  for file_name in os.listdir(config['src_dir']):
    file_path = os.path.join(config['src_dir'], file_name)
    if os.path.isfile(file_path):
      os.remove(file_path)


if __name__ == '__main__':
  config_path = os.path.join('config', 'config.yaml')
  with open(config_path, 'r') as config_file:
    config = yaml.load(config_file)
  page_attributes_path = os.path.join('config', 'page_attributes.yaml')
  with open(page_attributes_path, 'r') as page_attributes_file:
    page_attributes = yaml.load(page_attributes_file)
  cli()