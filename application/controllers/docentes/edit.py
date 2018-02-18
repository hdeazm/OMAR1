import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_docente, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_docente) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/docentes') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_docente, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_docente) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/docentes') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_docente, **k):
        message = None # Error message
        id_docente = config.check_secure_val(str(id_docente)) # HMAC id_docente validate
        result = config.model.get_docentes(int(id_docente)) # search for the id_docente
        result.id_docente = config.make_secure_val(str(result.id_docente)) # apply HMAC for id_docente
        return config.render.edit(result, message) # render docentes edit.html

    @staticmethod
    def POST_EDIT(id_docente, **k):
        form = config.web.input()  # get form data
        form['id_docente'] = config.check_secure_val(str(form['id_docente'])) # HMAC id_docente validate
        # edit user with new data
        result = config.model.edit_docentes(
            form['id_docente'],form['nombre'],form['telefono'],form['direccion'],
        )
        if result == None: # Error on udpate data
            id_docente = config.check_secure_val(str(id_docente)) # validate HMAC id_docente
            result = config.model.get_docentes(int(id_docente)) # search for id_docente data
            result.id_docente = config.make_secure_val(str(result.id_docente)) # apply HMAC to id_docente
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/docentes') # render docentes index.html
