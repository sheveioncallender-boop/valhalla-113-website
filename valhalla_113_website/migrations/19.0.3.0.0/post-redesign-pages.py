"""Apply the requested redesign once to the five protected supporting views."""
from copy import deepcopy

from lxml import etree

from odoo import SUPERUSER_ID, api
from odoo.tools import file_open


def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # These records are noupdate so subsequent upgrades retain Website editor
    # changes. This release intentionally refreshes only our original views.
    # Independently created/duplicated website views are not rewritten.
    with file_open("valhalla_113_website/views/valhalla_pages.xml", "rb") as source:
        document = etree.parse(source)
    for template in document.xpath("/odoo/data/template"):
        view = env.ref("valhalla_113_website." + template.get("id"), raise_if_not_found=False)
        if view and view.type == "qweb":
            root = etree.Element("t", {"t-name": view.key})
            for child in template:
                root.append(deepcopy(child))
            architecture = etree.tostring(root, encoding="unicode")
            view.with_context(lang="en_US").write({"arch_db": architecture})
