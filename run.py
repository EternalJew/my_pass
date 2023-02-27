from api import app
from api.routes import it_college, ns_members

if __name__ == '__main__':

    app.register_blueprint(it_college.main, url_prefix='/api/student')
    app.register_blueprint(ns_members.main, url_prefix='/api/ns_member')

    app.run(debug=True)