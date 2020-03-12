from odoo import api, fields, models


class Book(models.Model):
    
    _name = 'library.book'
    _description = 'Book'
    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    active = fields.Boolean('Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary('Cover')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')

    @api.multi
    def _check_isbn(self):
        """Check one Book's ISBN"""
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        print(digits)

        if len(digits) == 13:
            ponderators = [1, 3] * 6
            print(ponderators)

            total = sum(a * b for a, b in zip(digits[:12], ponderators))

            print(total)

            remain = total % 10
            print(remain)

            check = 10 - remain if remain != 0 else 0
            print(check)
            return digits[-1] == check