from odoo import http
from odoo.addons.library_app.controllers.main import Books


class BookExtend(Books):
    @http.route()
    def list(self, **kwargs):
        if kwargs.get('available'):
            Book = http.request.env['library.book']
            books = Book.search([('is_available', '=', True)])
            response.qcontext['books'] = books
            return response