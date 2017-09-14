from .bash import BashPrompt

class Garter(object):
  def __init__(self, text="", foreground="", background="", attribute=""):
    self.text = text
    self.foreground = foreground
    self.background = background
    self.attribute = attribute
  def tie(self):
    fmtSet = BashPrompt.format(self.foreground, self.background, self.attribute)
    fmtReset = BashPrompt.reset(self.attribute)
    return fmtSet + self.text + fmtReset
    
class GarterLine(object):
  def __init__(self, text="", foreground="", background="", attribute=""):
    self.garters = []
    self.foreground = foreground
    self.background = background
    self.attribute = attribute
    self.append(text, foreground, background, attribute)

  def append(self, text="", foreground="", background="", attribute=""):
    if isinstance(text, list):
      for g in text:
        if g:
          self.append(g, foreground, background, attribute)
    elif isinstance(text, GarterLine):
      self.garters += text.garters
    elif isinstance(text, Garter):
      self.garters.append(text)
    elif text:
      self.garters.append(Garter(text, foreground, background, attribute))
    return self

  def tie(self, delimiter="", blend=False):
    result = ""
    if delimiter and not isinstance(delimiter, (Garter, GarterLine)):
      delimiter = Garter(delimiter)
    lastIndex = len(self.garters) - 1
    i=0
    for g in self.garters:
      g.foreground = g.foreground or self.foreground
      g.background = g.background or self.background
      g.attribute = g.attribute or self.attribute
      result += g.tie()
      if delimiter and i < lastIndex:
        if blend:
          delimiter.foreground = g.background
          delimiter.background = self.garters[i+1].background
        result += delimiter.tie()
      i=i+1
    return result
