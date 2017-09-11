from .ansi import Ansi

class GarterLine(object):
  def __init__(self, text="", foreground="", background="", attribute=""):
    self.garter = []
    self.text(text)
    self.foreground = Ansi.foreground(foreground)
    self.background = Ansi.background(background)
    self.attribute = Ansi.attribute(attribute)

  def append(self, text="", foreground="", background="", attribute=""):
    self.text(GarterLine(text, foreground, background, attribute))
    return self

  def text(self, text):
    if isinstance(text, list):
      self.garter = self.garter + text
    elif text:
      self.garter.append(text)

  def tie(self, text="", foreground="", background="", attribute="", blend=False):
    fmtSet = self.background + self.foreground + self.attribute["apply"]
    fmtReset = self.attribute["reset"]
    if text:
      if isinstance(text, GarterLine):
        text = text.tie()
      else:
        text = GarterLine(text, foreground, background, attribute).tie()
    garter = []
    for g in self.garter:
      if isinstance(g, GarterLine):
        garter.append(fmtSet + g.tie() + fmtReset)
      else:
        garter.append(fmtSet + g + fmtReset)
    return text.join(garter)
