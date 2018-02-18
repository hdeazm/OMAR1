import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_alumno, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_alumno) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_alumno, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_alumno) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_alumno, **k):
        message = None # Error message
        id_alumno = config.check_secure_val(str(id_alumno)) # HMAC id_alumno validate
        result = config.model.get_alumnos(int(id_alumno)) # search  id_alumno
        result.id_alumno = config.make_secure_val(str(result.id_alumno)) # apply HMAC for id_alumno
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_alumno, **k):
        form = config.web.input() # get form data
        form['id_alumno'] = config.check_secure_val(str(form['id_alumno'])) # HMAC id_alumno validate
        result = config.model.delete_alumnos(form['id_alumno']) # get alumnos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_alumno = config.check_secure_val(str(id_alumno))  # HMAC user validate
            id_alumno = config.check_secure_val(str(id_alumno))  # HMAC user validate
            result = config.model.get_alumnos(int(id_alumno)) # get id_alumno data
            result.id_alumno = config.make_secure_val(str(result.id_alumno)) # apply HMAC to id_alumno
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/alumnos') # render alumnos delete.html 
