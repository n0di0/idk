from anvil.js.window import jQuery
from anvil.js import get_dom_node
from ._anvil_designer import Form2Template
from anvil import *
import anvil.server

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    iframe = jQuery("<iframe width='392px' margin-top: 100px; height='450px'>").attr("src","https://studio.code.org/projects/applab/NONz21j9-O9OI-2j9E-zT9F-b1j69EFO6vzz/embed?nosource")
    iframe.appendTo(get_dom_node(self.content_panel))
    # Any code you write here will run when the form opens.
