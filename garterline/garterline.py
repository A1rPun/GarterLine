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

  # TODO: Implement self.getAttribute(self.attribute)
  def tie(self, delimiter=""):
    fmt = self.background + self.foreground
    if isinstance(delimiter, GarterLine):
      delimiter = delimiter.tie()
    garter = []
    for g in self.garter:
      if isinstance(g, GarterLine):
        garter.append(g.tie())
      else:
        garter.append(fmt + g)
    return fmt + delimiter.join(garter)
