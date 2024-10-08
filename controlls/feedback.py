from odoo import http
from odoo.http import request

class FeedbackController(http.Controller):

    # Route, die für jedes Element eine dynamische URL erzeugt (z.B. anhand der ID)
    @http.route(['/feedback/<model("workshop.session"):session>'], type='http', auth='public', website=True)
    def feedback_form(self, session, **kwargs):
        """
        Diese Route generiert eine spezielle URL für jedes Produkt (oder ein anderes Element).
        Die Produkt-ID wird als Parameter übergeben.
        """
        # Render die Bewertungsformular-Vorlage mit dem spezifischen Produkt
        return request.render('workshop_management.feedback_template', {
            'session': session,
        })

    # POST-Route, um das Feedback zu speichern
    @http.route(['/feedback/submit'], type='http', auth='public', methods=['POST'], website=True)
    def feedback_submit(self, **post):
        """
        Diese Route verarbeitet das abgesendete Bewertungsformular.
        """
        feedback = post.get("feedback_text")
        session_id = int(post.get('session') ) # Produkt-ID aus dem POST-Daten

        # Erstelle einen neuen Eintrag im Feedback-Modell
        request.env['workshop.session.feedback'].sudo().create({
            'session_id': session_id,
            'feedback_text': feedback,
        })

        # Weiterleitung nach dem Absenden (z.B. auf eine Danke-Seite)
        return request.redirect('/thank-you')
    
    @http.route(['/thank-you'], type='http', auth='public', website=True)
    def thank_you(self,  **kwargs):
        """
        Diese Route generiert eine spezielle URL für jedes Produkt (oder ein anderes Element).
        Die Produkt-ID wird als Parameter übergeben.
        """
        # Render die Bewertungsformular-Vorlage mit dem spezifischen Produkt
        return request.render('workshop_management.thank_you')
