import base64

from odoo import api, fields, models
from odoo.tools import file_open
from odoo.fields import Domain


class Website(models.Model):
    _inherit = "website"

    valhalla_branding_enabled = fields.Boolean(string="Valhalla 113 Branding")
    valhalla_setup_done = fields.Boolean(copy=False)

    def _valhalla_menu_products(self):
        self.ensure_one()
        if not self.has_ecommerce_access():
            return self.env["product.template"]
        # No sudo: retain public access rules, website/company restrictions and
        # Odoo's product eligibility rules. Never create a second catalogue.
        return self.env["product.template"].search(
            Domain.AND([self.sale_product_domain(), [("is_published", "=", True)]]),
            order="website_sequence, id", limit=5,
        )

    @api.model
    def _setup_valhalla_website(self):
        """Run on fresh installation and first upgrade; retain later editor changes."""
        page = self.env.ref("valhalla_113_website.page_valhalla_113")
        website = page.website_id or self.env.ref("website.default_website")
        if website.valhalla_setup_done:
            return
        with file_open("valhalla_113_website/static/src/img/logo_official.png", "rb") as logo:
            website.write({
                "name": "Valhalla 113 Bar & Grill",
                "valhalla_branding_enabled": True,
                "homepage_url": "/valhalla-113",
                "logo": base64.b64encode(logo.read()),
            })
        for xmlid in ["page_valhalla_113", "page_about", "page_whats_on", "page_gallery", "page_visit", "page_ordering"]:
            self.env.ref("valhalla_113_website." + xmlid).website_id = website
        # Retire only our obsolete extra home link. Preserve other user menus.
        legacy_menu = self.env.ref("valhalla_113_website.menu_valhalla_113", raise_if_not_found=False)
        if legacy_menu:
            legacy_menu.unlink()
        for name, url, sequence in [
            ("Home", "/", 10), ("Menu & Order", "/shop", 20),
            ("What's On", "/whats-on", 30), ("About", "/about-valhalla", 40),
            ("Gallery", "/gallery", 50), ("Visit Us", "/visit-us", 60),
        ]:
            menu = self.env["website.menu"].search([
                ("parent_id", "=", website.menu_id.id), ("url", "=", url),
            ], limit=1)
            if menu:
                menu.write({"name": name, "sequence": sequence})
            else:
                menu = self.env["website.menu"].create({
                    "name": name, "url": url, "sequence": sequence,
                    "website_id": website.id, "parent_id": website.menu_id.id,
                })
                self.env["ir.model.data"].create({
                    "module": "valhalla_113_website",
                    "name": "native_menu_%s_%s" % (website.id, sequence),
                    "model": "website.menu", "res_id": menu.id, "noupdate": True,
                })
        website.valhalla_setup_done = True
