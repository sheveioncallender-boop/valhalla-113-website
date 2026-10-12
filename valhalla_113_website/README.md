# Valhalla 113 Website — Odoo 19

Version **19.0.2.0.0**. Preserves the original sports-bar homepage layout, imagery and black/red/silver identity while restoring Odoo's native website header and eCommerce flow.

## Install fresh through Cloudpepper

1. Synchronize the **main** branch of this repository with Cloudpepper's addons path and rebuild/restart Odoo.
2. Update the Apps List and install **Valhalla 113 Website**. Its `website_sale` dependency installs native eCommerce.
3. Install **Valhalla 113 QR Table Ordering** from the companion repository if table ordering is required. Either module can be installed first; neither requires the other.
4. The website module assigns the landing page to the existing page's website, or the default website on a fresh installation. The root homepage opens Valhalla automatically. Its original `/valhalla-113` URL is retained.
5. For an existing installation, upgrade the module after rebuilding. The first upgrade configures native navigation and branding; subsequent upgrades preserve website logo, homepage selection, menus and the newly added page edits.

## Pages and native destinations

| Page | URL |
| --- | --- |
| Home | `/` (landing page also at `/valhalla-113`) |
| Menu & Order | `/shop` — native Odoo shop |
| What's On | `/whats-on` |
| About | `/about-valhalla` |
| Gallery | `/gallery` |
| Visit Us | `/visit-us` |
| Ordering help | `/ordering` |
| Contact enquiry | `/contactus` — native Odoo form |
| Cart / Checkout | `/shop/cart` / `/shop/checkout` |
| Customer orders | `/my/orders` — native customer portal |

Edit page content with Odoo Website's editor. Manage navigation with its native menu editor. The logo and the **Valhalla 113 Branding** switch are on the native Website record. Branding is limited to the selected website, including its shop/cart/checkout/portal; the backend and other websites retain their own styling. The default native footer receives Valhalla content; alternative footers remain selectable in Odoo.

## One product catalogue, Odoo's normal flows

No custom cart, checkout, payment controller or order model is added. Homepage highlights read up to five published products in the current website/company, ordered by Odoo's website sequence. Images, names and links come from the product records. Displayed prices use Odoo's pricelist, currency, tax and fiscal-position calculation. Selecting an item opens its native product page for variants/options. Zero-price restrictions remain native.

No placeholder prices, products, inventory quantities, tax rates, payment providers, delivery charges or accounting entries are created. If no products are published, the homepage provides a contact/menu message.

| Channel | Product settings | Order flow |
| --- | --- | --- |
| Website | Sales enabled, published, assigned to the appropriate website | Shop → cart → checkout/payment → native Sales order |
| Table QR / POS | Same product, Available in POS and Available in Self Order, allowed POS categories | Table QR → native self-order app → matching POS table/session → native preparation/payment |

Online Sales orders are **not automatically turned into POS/kitchen orders** by these modules. Native POS Sales-order settlement can be configured separately where appropriate. Table tokens, kitchen routing, payment rules, tax calculations and stock behavior remain Odoo-managed. Do not duplicate products to serve each channel.

## Complete in Odoo before accepting real orders

- Publish the real menu, images, prices, taxes and variants; confirm the website company/currency and pricelist.
- Configure and test the intended payment provider and checkout fulfilment options in Odoo. The module does not activate a provider or promise delivery/pickup services.
- Check the native Contact Us recipient/company details and outbound email configuration.
- For QR ordering, configure the POS products/categories, floors/tables and printer/preparation settings; open its session and scan an actual table QR.
- Test a website checkout and a separate table order, including the correct totals, payment state and resulting order type.

## Validation for this release

Python syntax, Odoo XML schema, data/asset paths, QWeb expressions and references, native inheritance targets and native API names were checked against Odoo 19 source. No running Odoo/PostgreSQL instance was available here: installation, compiled frontend rendering, live checkout/payment and table/kitchen processing require validation on the deployed database.
