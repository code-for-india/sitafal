from google.appengine.api import users
import webapp2

from utils import *

from models import User

class BaseHandler(webapp2.RequestHandler):
	"""
	Base class for view functions, which provides basic rendering 
	funtionalities
	"""

	def render(self, template, **kw):
		"""
		Render a template with the given keyword arguments
		"""

		self.response.out.write(render_str(template, **kw))

	def set_secure_cookie(self, name, val):
		"""
		Set an encrypted cookie on client's machine
		"""

		cookie_val = make_secure_val(val)
		self.response.headers.add_header(
			'Set-Cookie',
			'%s=%s; Path=/' % (name, cookie_val)
			)

	def read_secure_cookie(self, name):
		"""
		Read a cookie and check it's integrity
		"""

		cookie_val = self.request.cookies.get(name)
		return cookie_val and check_secure_val(cookie_val)

	def initialize(self, *a, **kw):
		"""
		Override the constuctor for adding user information
		when a request comes
		"""

		webapp2.RequestHandler.initialize(self, *a, **kw)
		user_id = self.read_secure_cookie('user')
		self.user = user_id and User.get_by_id(int(user_id))

class Home(BaseHandler):
	"""
	Render the homepage.
	"""

	def get(self):
		"""
		For a GET request, render the homepage.
		"""

		self.render("home.html")

class New(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))