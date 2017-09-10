from .ansi import Ansi

class GarterLine(object):
  def __init__(self, text="", foreground="", background="", attribute="", delimiter=" "):
    self.text = [text]
    self.foreground = Ansi.foreground(foreground)
    self.background = Ansi.background(background)
    self.attribute = attribute
    self.delimiter = delimiter

  # TODO: Add support for own class
  # TODO: Implement self.getAttribute(attribute)  
  def append(self, text="", foreground="", background="", attribute=""):
    fg = Ansi.foreground(foreground)
    bg = Ansi.background(background)
    text = bg + fg + text
    self.text.append(text)
    return self

  # TODO: Implement self.getAttribute(self.attribute)
  def tie(self):
    text = self.background + self.foreground
    text += (self.delimiter + text).join(self.text)
    return text
