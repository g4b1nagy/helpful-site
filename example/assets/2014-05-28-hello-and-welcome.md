===========================================================================
categories: 'getting started, examples'
date: 2014-05-28 09:10
description: ''
icon: ''
ogimage: ''
script: ''
style: ''
template: post.html
title: !!python/unicode 'Hello and welcome'
===========================================================================

You're live! Nice. The great people at [Ghost](https://ghost.org/) wrote a great post showcasing their Casper theme (the one we're also using) and since I probably won't be able to do a better job at showcasing their work, I'm providing the original post (with adjustments) bellow.

If you're looking for documentation on how to use the site generator, feel free to check out the project's [GitHub page](https://github.com/g4b1nagy/helpful-site).

## Getting Started

Helpful Site uses something called Markdown for writing. Essentially, it's a shorthand way to manage your post formatting as you write!

Writing in Markdown is really easy. Inside every .md file, you simply write as you normally would. Where appropriate, you can use _shortcuts_ to **style** your content. For example, a list:

*   Item number one
*   Item number two

    *   A nested item
*   A final item

or with numbers!

1.  Remember to buy some milk
2.  Drink the milk
3.  Tweet that I remembered to buy the milk, and drank it

### Links

Want to link to a source? No problem. If you paste in url, like [http://ghost.org](http://ghost.org) - it'll automatically be linked up. But if you want to customise your anchor text, you can do that too! Here's a link to [the Ghost website](http://ghost.org). Neat.

### What about Images?

Images work too! Already know the URL of the image you want to include in your article? Simply paste it in like this to make it show up:

![The Ghost Logo](https://ghost.org/images/ghost.png)

Not sure which image you want to use yet? That's ok too. Leave yourself a descriptive placeholder and keep writing. Come back later and drag and drop the image in to upload:

### Quoting

Sometimes a link isn't enough, you want to quote someone on what they've said. It was probably very wisdomous. Is wisdomous a word? Find out in a future release when we introduce spellcheck! For now - it's definitely a word.

> Wisdomous - it's definitely a word.

### Working with Code

Got a streak of geek? We've got you covered there, too. You can write inline `<code>` blocks really easily with back ticks. Want to show off something more comprehensive? Writing your code between  
`∕∕code syntax` and  
`∕∕code`  
gets you there.

//code python
@cli.command()
@click.option('--all', is_flag=True)
def reset(all):
  """Reset site by removing all files."""

  click.confirm('Reset site and remove all files?', abort=True)
  if os.path.isdir(config['dist_dir']):
    shutil.rmtree(config['dist_dir'])
  if all:
    click.confirm('Remove source files as well?', abort=True)
    for file_name in os.listdir(config['src_dir']):
      file_path = os.path.join(config['src_dir'], file_name)
      if os.path.isfile(file_path):
        os.remove(file_path)
      elif os.path.isdir(file_path):
        shutil.rmtree(file_path)
//code

### Ready for a Break?

Throw 3 or more dashes down on any new line and you've got yourself a fancy new divider. Aw yeah.

* * *

### Advanced Usage

There's one fantastic secret about Markdown. If you want, you can  write plain old HTML and it'll still work! Very flexible.

<input type="text" placeholder="I'm an input field!">

That should be enough to get you started. Have fun! :)