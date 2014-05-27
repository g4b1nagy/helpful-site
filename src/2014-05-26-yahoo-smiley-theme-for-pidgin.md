===========================================================================
categories: 'yahoo, smiley'
date: 2014-05-26 16:06
description: ''
icon: ''
ogimage: ''
script: ''
style: ''
template: post.html
title: !!python/unicode 'Yahoo Smiley Theme For Pidgin'
===========================================================================

If you’re sick of the way Yahoo Messenger sucks the living daylight out of your computer, fills your screen with conversation windows and pokes you in the eye with advertisements, Pidgin might just be the replacement for you. It’s sleek, fast, easy to use, features a nifty tabbed interface and it runs on Windows, Linux, and other UNIX operating systems. While the lack of Voice calls, Video calls or Photo sharing in Pidgin might not be all that bad, one can not help but feel the great void caused by the absence of the original Yahoo smileys. And this is where this little pack comes in. The smiley theme comes in two versions:


//code python

@cli.command()
def new():
  """Create a new post or page."""

  date = datetime.now()
  file_type = click.prompt('Create new post/page', type=click.Choice(['post', 'page']), default='post')
  page_attributes['title'] = click.prompt('Title', default='New ' + file_type)
  page_attributes['date'] = date.strftime(config['date_format'])
  page_attributes['template'] = config['default_template']
  if file_type == 'post':
    file_name = (date.strftime(config['link_prefix_format']) +
                  slugify(page_attributes['title']) + '.md')
  else:
    file_name = slugify(page_attributes['title']) + '.md'
  file_path = os.path.join(config['src_dir'], file_name)
  if os.path.isfile(file_path):
    click.echo('A page with the same name already exists.')
  else:
    with open(file_path, 'w') as f:
      f.write(config['delimiter'])
      f.write(yaml.dump(page_attributes, default_flow_style=False))
      f.write(config['delimiter'])
      f.write('\n')

  //code


Please note that the last two smileys: pirate and transformer are only available in Yahoo Messenger for the web. A list of all Yahoo smileys and their respective codes can be found here.

Installation

To install a smiley theme, click Tools -> Preferences -> Themes. Then drag and drop the theme file onto the Smiley Theme drop down list. Check the list for your newly added theme, select it and press close. Visual instructions below:

Removal

The smiley themes are installed in
/home/user/.purple/smileys – on Linux
C:\Documents and Settings\user\Application Data\.purple\smileys – on Windows XP
C:\Users\user\Application Data\.purple\smileys – on Windows 7
To remove a theme, simply delete the respective directory. The change will take effect after you restart Pidgin.