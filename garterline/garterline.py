from .bash import BashPrompt

class GarterLine(object):
  def __init__(self, text="", foreground="", background="", attribute=""):
    self.garter = []
    self.text(text)
    self.foreground = foreground
    self.background = background
    self.attribute = attribute

  def append(self, text="", foreground="", background="", attribute=""):
    self.text(GarterLine(text, foreground, background, attribute))
    return self

  def text(self, text):
    if isinstance(text, list):
      self.garter = self.garter + text
    elif text:
      self.garter.append(text)

  def tie(self, delimiter="", blend=False):
    result = ""
    fmtSet = BashPrompt.format(self.foreground, self.background, self.attribute)
    fmtReset = BashPrompt.reset(self.attribute)
    if delimiter and not isinstance(delimiter, GarterLine):
      delimiter = GarterLine(delimiter)
    lastIndex = len(self.garter) - 1
    i=0
    for g in self.garter:
      bg = self.background
      if isinstance(g, GarterLine):
        bg = g.background
        g = g.tie()
      result += fmtSet + g + fmtReset
      if delimiter and i < lastIndex:
        if blend:
          delimiter.foreground = bg
          delimiter.background = self.garter[i+1].background
        result += delimiter.tie()
      i=i+1
    return result
