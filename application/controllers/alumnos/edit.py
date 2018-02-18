import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_alumno, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_alumno) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/alumnos') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_alumno, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_alumno) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/alumnos') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_alumno, **k):
        message = None # Error message
        id_alumno = config.check_secure_val(str(id_alumno)) # HMAC id_alumno validate
        result = config.model.get_alumnos(int(id_alumno)) # search for the id_alumno
        result.id_alumno = config.make_secure_val(str(result.id_alumno)) # apply HMAC for id_alumno
        return config.render.edit(result, message) # render alumnos edit.html

    @staticmethod
    def POST_EDIT(id_alumno, **k):
        form = config.web.input()  # get form data
        form['id_alumno'] = config.check_secure_val(str(form['id_alumno'])) # HMAC id_alumno validate
        # edit user with new data
        result = config.model.edit_alumnos(
            form['id_alumno'],form['nombre'],form['telefono_alum'],form['telefono_tutor'],form['direccion'],
        )
        if result == None: # Error on udpate data
            id_alumno = config.check_secure_val(str(id_alumno)) # validate HMAC id_alumno
            result = config.model.get_alumnos(int(id_alumno)) # search for id_alumno data
            result.id_alumno = config.make_secure_val(str(result.id_alumno)) # apply HMAC to id_alumno
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/alumnos') # render alumnos index.html
