import random
import win32clipboard

themes = [
    'kindness',
    'discipline',
    'focus',
    'resiliance',
    'skill vs talent',
    'productivity',
    'humility',
    'arrogance',
    'growth',
]

templates = [
    'Be ___ with the ___, not the___.',
    'Be ___, not ___.',
    'If ___, ___.',
    'Funny how ___.',
    '___ is a skill, not a talent.',
    'You grow when ___, not ___.',
    "Psychology says: ___.",
    "[x] and [y] are worst enemies.",
    "[x] is a sign of [y].",
    "[x] wihtou [y] is ___.",
    "Never trade [x] for [y].",
    "[x] is the key to [y].",
    "[x] is ok. [y] is not.",
    "[x] is good, but [y] is better.",
    "Become a master in the art of [x].",
    "Be addicted to [x].",
    "Be obsessed with [x].",
    "Be very selective with [x].",
    "The more [x], the less [y].",
    "___ is when ___.",
    "",
]


templates_mindtendencies2 = [
    'Avoid people who ___.',
    'Be someone you ___.',
    'Don\'t lose people ___. They are so rare.',
    'Heal so ___.',
    'If you are serious about ___, be serious about ___.',
    '___ is a superpower.',
    'Normalize ___.',
    'The right person ___.',
    "___ without ___ is incomplete",
    "Your soul is ___.",
    "",
    "",
    "",
    "",
    "",
    "",
    
]

templates_mindtendencies2 = [
    "A healed person wouldn't ___.",
    "A person who is ___.",
    "___ accelerates ___.",
    "Admitting ___.",
    "Always ___ especially when ___.",
    "Always trust that ___ is ___.",
    "___ and ___.",
    "___ and ___ go together.",
    "Any ___ that requires you to ___ is not the ___.",
    "Anyone who ___ you will ___.",
    "___ are angels in disguise.",
    "As ___, things around your change.",
    "Avoid ___ who ___.",
    "Be at peace with the fact ___.",
    "Be ___ enough to ___.",
    "___ be like ___.",
    "Be loyal to ___.",
    "Be someone ___.",
    "Be the reason someone ___.",
    "Be very ___.",
    "Be with people who ___.",
    "___ become 10 times more ___ when ___.",
    "Being with someone ___ >>>",
    "Beware of ___.",
    "Can't fuck with anyone who ___.",
    "Choose people ___.",
    "Choose to ___ instead of ___.",
    "___ CPR ___.",
    "Detach from ___.",
    "___ different when you ___.",
    "___ does not mean ___.",
    "Don't let ___.",
    "Don't let someone live rent-free in your head if __.",
    "Don't lose people ___. They are so rare.",
    "Due to personal reasons, I ___.",
    "Everything shifts when you ___.",
    "Fall in love with someone who ___.",
    "Free yourself from ___.",
    "Get comfortable with ___.",
    "Hang out with ___.",
    "Heal so ___.",
    "Heavy on the “___” ___.",
    "___ how ___.",
    "Idk who needs to hear this but ___.",
    "If ___, ___.",
    "___ if ___.",
    "If you are serious about ___, be serious about ___.",
    " If you do not address your childhood trauma, ___.",
    "I love when ___.",
    "I'm at a place in my life where ___.",
    "I only want ___ around me.",
    "I've so much ___.",
    "I've ___ to know ___.",
    "I won't ___ because ___.",
    "I would rather ___ than ___.",
    "In case you didn't know, ___.",
    "“___” is ___.",
    "___ is a form of manipulation.",
    "___ is a ___, not ___.",
    "___ is a ___ of ___.",
    "___ is a reflection of ___.",
    "___ is a revolution.",
    "___ is a sign ___.",
    "___ is a sign that something inside ___ needs fixing.",
    "___ is a trauma response.",
    "___ is a whole vibe",
    "___ is attractive.",
    "___ is divine ___.",
    "___ is high emotional intelligence.",
    "___ is high spiritual intelligence.",
    "___ is ___ in disguise.",
    "___ is not the reason why you ___, ___.",
    "___ is self-care.",
    "___ is sexy af.",
    "___ is so ___.",
    "___ is such a huge part of ___.",
    "___ is the ___ form of ___.",
    "___ is the foundation of ___.",
    "___ is the new grind.",
    "___ is worth the wait.",
    "It's a red flag ___.",
    "It's all fun and games until ___",
    "It's beautiful seeing ___.",
    "It's crazy ___.",
    "It's not your job to ___. It's your job to ___.",
    "It's ok to ___.",
    "It's ___ than ___.",
    "Just because ___.",
    "Keep ___.",
    "Keep trusting ___.",
]



theme = random.choice(themes)
template = random.choice(templates_mindtendencies2)

theme = 'burnout'

prompt = f'''write 10 short tweets with the following theme and template:

Theme: {theme}

Template: {template}
'''


print(prompt)

win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(prompt, win32clipboard.CF_TEXT)
win32clipboard.CloseClipboard()

