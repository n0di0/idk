from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    list_of_decodes = anvil.server.call('read_barcodes', file)

    for code in list_of_decodes:
      self.content_panel.add_component(Label(text=code, align="center"))

