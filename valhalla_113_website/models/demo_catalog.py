"""Owner-requested showcase products using native Odoo catalogue records."""
import base64

from odoo import api, fields, models
from odoo.tools import file_open


class Website(models.Model):
    _inherit = "website"

    valhalla_demo_catalog_done = fields.Boolean(copy=False)

    @api.model
    def _setup_valhalla_demo_catalog(self):
        website = self.env.ref("valhalla_113_website.page_valhalla_113").website_id
        if not website or website.valhalla_demo_catalog_done:
            return
        env = self.with_company(website.company_id).env

        def owned_record(model, name, values):
            xmlid = "valhalla_113_website." + name
            existing = env.ref(xmlid, raise_if_not_found=False)
            if existing:
                return existing
            record = env[model].create(values)
            env["ir.model.data"].create({
                "module": "valhalla_113_website", "name": name,
                "model": model, "res_id": record.id, "noupdate": True,
            })
            return record

        categories = {}
        for key, name in [("food", "Grill & Bites"), ("drinks", "Drinks")]:
            public = owned_record("product.public.category", "demo_web_category_" + key,
                                  {"name": name, "website_id": website.id})
            pos = owned_record("pos.category", "demo_pos_category_" + key, {"name": name})
            categories[key] = (public, pos)

        # Prices are illustrative in the website company's existing currency.
        # Native company sales-tax defaults apply; no tax or payment setup is changed.
        products = [
            ("wings", "BBQ Wings", 65, "food", "menu_wings.jpg", "Chicken wings with BBQ sauce."),
            ("burger", "Classic Beef Burger", 75, "food", "menu_burger.jpg", "Beef burger with cheese, lettuce, and fries."),
            ("ribs", "BBQ Ribs", 110, "food", "menu_ribs.jpg", "Grilled ribs finished with BBQ sauce."),
            ("fries", "Loaded Fries", 45, "food", "menu_fries.jpg", "Golden fries with cheese and savoury toppings."),
            ("chicken", "Grilled Chicken", 80, "food", "grill-editorial.jpg", "Grilled chicken with herbs and dipping sauce."),
            ("spritz", "Citrus Spritz", 55, "drinks", "cocktails-editorial.jpg", "A refreshing citrus cocktail served over ice."),
        ]
        for sequence, (key, name, price, category, image, description) in enumerate(products, 1):
            public, pos = categories[category]
            with file_open("valhalla_113_website/static/src/img/" + image, "rb") as source:
                image_data = base64.b64encode(source.read())
            values = {
                "name": name, "default_code": "V113-DEMO-" + key.upper(),
                "type": "consu", "is_storable": False,
                "sale_ok": True, "purchase_ok": False,
                "list_price": price, "description_sale": description,
                "website_description": "<p>" + description + "</p>",
                "company_id": website.company_id.id, "website_id": website.id,
                "is_published": True, "available_in_pos": True,
                "public_categ_ids": [(6, 0, [public.id])],
                "pos_categ_ids": [(6, 0, [pos.id])],
                "website_sequence": sequence * 10, "image_1920": image_data,
            }
            if "self_order_available" in env["product.template"]._fields:
                values["self_order_available"] = True
            owned_record("product.template", "demo_product_" + key, values)
        # Later upgrades preserve edits, prices, publication state and deletions.
        website.valhalla_demo_catalog_done = True
