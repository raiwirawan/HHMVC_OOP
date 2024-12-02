class BaseController:
    def __init__(self, model=None, view=None):
        self.model = model
        self.view = view
    
    def set_model(self, model):
        self.model = model
    
    def set_view(self, view):
        self.view = view