===========================================================================
date: 2014-05-26 16:05
description: ''
icon: ''
ogimage: ''
script: ''
style: ''
template: post.html
title: !!python/unicode 'Counting Sheep In JavaScript'
===========================================================================

Dramatization

It was 2 am. None of us were sleeping. The beast wouldn’t allow it. This couldn’t go on. We were getting weaker every day. The lack of sleep was getting to us. We desperately needed to do something. But what ? There was no solution in sight. I had been thinking about this for days. Then, when all hope seemed to be gone, it dawned upon me ! If we were going to battle the monster, we needed to use its own weapons against it. I jumped up, grabbed my trusty HTML armor, put on my CSS and drew my JavaScript sword and yelled:
“INTERNET, release us from your evil spells and give us back our sleep !!!” 
The beast roared ferociously. It did not like people rebelling against it. It waved its spidery arms around and it started raining funny pictures and videos. This was not good. Every drop of procrastination in my body started boiling. But I had to resist. I had to be strong. My weapons didn’t stand a chance. I needed help. And fast. I needed something that could keep me focused. I looked around. There was nothing on the vast Desktopian plains that could help me. I was slowly loosing the battle. Then I remembered !
Nothing keeps people focused more than small fluffy creatures ! I remembered people staring at pictures of cats for hours on end ! With a desperate attempt at fighting back, I pulled myself together and with all my strength, I called out to the Helpful Sheep sheep.
The beast was stunned ! It did not expect this. I raised my sword and charged at it like a raging bull on a bad hair day. I only had one chance. I was aiming for its heart. Time seemed to slow down.
I could feel the impact as it resonated through my body. There was a terrible roar as the monster came crushing down. Then there was nothing. Silence filled the air like a good barkeep on a late Sunday night. It had been done. I looked back one more time at the beast’s stricken body and then slowly headed to bed. I had the rest of the night to think about this.

Artist’s depiction



Behind the scenes

As you might expect, the whole thing is really simple, but there are a few things that would be worth explaining. Firstly, the page structure and CSS.

Notice that the #title, #content and #sheep elements are given absolute positioning. This alone is not enough though. The absolute position is relative to the first positioned (not static) ancestor element. By default, all elements are static. So the elements would end up sticking to the viewport and would escape outside the parent div. To prevent this from happening, we set the #page div position to relative. That being said and done, let’s get things moving with JavaScript.

Congratulations ! I didn't think anyone would make it all the way down here. Since you did, please feel free to DOWNLOAD the whole thing. Backgrounds courtesy of Background Labs.