from .bash import BashPrompt

class GarterLine(object):
  def __init__(self):
    self.garters = []

  def __str__(self):
    return "".join(self.garters)

  def text(self, text=""):
    if isinstance(text, list):
      for g in text:
        if g:
          self.text(g)
    elif isinstance(text, GarterLine):
      self.garters += text.garters
    elif text:
      self.garters.append(text)
    return self

  def color(self,  foreground="", background="", attribute=""):
    self.text(BashPrompt.color(foreground, background, attribute))
    return self

  def escape(self,  escape=""):
    self.text(BashPrompt.escape(escape))
    return self
