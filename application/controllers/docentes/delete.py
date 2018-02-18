import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_docente, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_docente) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_docente, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_docente) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_docente, **k):
        message = None # Error message
        id_docente = config.check_secure_val(str(id_docente)) # HMAC id_docente validate
        result = config.model.get_docentes(int(id_docente)) # search  id_docente
        result.id_docente = config.make_secure_val(str(result.id_docente)) # apply HMAC for id_docente
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_docente, **k):
        form = config.web.input() # get form data
        form['id_docente'] = config.check_secure_val(str(form['id_docente'])) # HMAC id_docente validate
        result = config.model.delete_docentes(form['id_docente']) # get docentes data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_docente = config.check_secure_val(str(id_docente))  # HMAC user validate
            id_docente = config.check_secure_val(str(id_docente))  # HMAC user validate
            result = config.model.get_docentes(int(id_docente)) # get id_docente data
            result.id_docente = config.make_secure_val(str(result.id_docente)) # apply HMAC to id_docente
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/docentes') # render docentes delete.html 
