# Valhalla 113 Website — Odoo 19

Version **19.0.3.2.0**. Redesigns the homepage and all five supporting pages with Valhalla’s black/red/silver identity, licensed food/drink photography and authentic past-event artwork. The social-led direction puts food, drinks, Caribbean music and the lime first. Odoo’s native header and commerce flow remain intact. See [image provenance](IMAGE_SOURCES.md).

## Install fresh through Cloudpepper

1. Synchronize the **main** branch of this repository with Cloudpepper's addons path and rebuild/restart Odoo.
2. Update the Apps List and install **Valhalla 113 Website**. Its `website_sale` dependency installs native eCommerce.
3. Install **Valhalla 113 QR Table Ordering** from the companion repository if table ordering is required. Either module can be installed first; neither requires the other.
4. The website module assigns the landing page to the existing page's website, or the default website on a fresh installation. The root homepage opens Valhalla automatically. Its original `/valhalla-113` URL is retained.
5. For an existing installation, upgrade the module after rebuilding. The first upgrade configures native navigation and branding; this redesign includes a one-time migration that replaces the five original supporting-page layouts. It preserves website logo, homepage selection and menus. Later upgrades preserve supporting-page editor changes. Independently duplicated/website-specific views are not overwritten; use Odoo’s view reset on a customized copy if you want this new layout there.

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

No custom cart, checkout, payment controller or order model is added. Homepage highlights read up to four published products in the current website/company, ordered by Odoo's website sequence. Images, names and links come from the product records. Displayed prices use Odoo's pricelist, currency, tax and fiscal-position calculation. Selecting an item opens its native product page for variants/options. Zero-price restrictions remain native.

Six owner-requested demo products with illustrative prices and images are created once on installation/upgrade. No inventory quantities, tax rates, payment providers, delivery charges or accounting entries are created. If no products are published, the homepage provides a contact/menu message.

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

Python syntax, Odoo XML schema, data/asset paths, QWeb expressions and references, native inheritance targets and native API names were checked against Odoo 19 source. Presentation-only Chromium fixtures for all six page bodies passed image-loading and horizontal-overflow checks at 1440, 768, 390 and 320 pixels; desktop/mobile screenshots were reviewed. These fixtures use a representative header shell and do not exercise Odoo rendering or header behaviour. No running Odoo/PostgreSQL instance was available here: installation, compiled frontend rendering, live checkout/payment and table/kitchen processing require validation on the deployed database.


## Design changes in 19.0.3.0.0

- Larger editorial photography, a mobile layout, clear ordering calls to action, and social links.
- Past promotions are labelled with their historical dates; current announcements link to official social pages.
- Optional native header contact text uses the real Valhalla phone number on the branded website. Native menu/cart/search/account/mobile interactions are retained.
- Native primary actions use red; secondary actions use charcoal; footer links have explicit readable contrast.
- No online-to-POS conversion, order models, payment behaviour, table tokens or QR backend settings changed in this release.

The addon is an application (`application=True`) and appears in the Apps filter after Cloudpepper has loaded this revision and the Apps List has been refreshed. Search **Valhalla 113 Website**; upgrade it if already installed.

## Update 19.0.3.1.0

The top banner now cycles through three photographs every six seconds using Odoo’s native carousel, with arrows, indicators and touch support. Odoo supplies pause on hover/focus and reduced-motion handling. The footer shows the current year and Valhalla 113 Bar & Grill, and omits Odoo promotional attribution on the branded website. Upgrade the module after syncing Cloudpepper.


## Update 19.0.3.2.0

- Banner controls are bottom indicators only; native touch and automatic rotation remain.
- Homepage and What’s On show up to three published, public, upcoming/ongoing native Odoo events for this website/company, excluding cancelled and ended events. Manage dates, event cover images, visibility and publication in **Events**. Event details and registration use Odoo’s native flow. No fictitious upcoming events are created.
- Native `website_event` and `point_of_sale` dependencies install as needed.
- Six showcase products: BBQ Wings (65), Classic Beef Burger (75), BBQ Ribs (110), Loaded Fries (45), Grilled Chicken (80), Citrus Spritz (55). Prices use the existing company currency and its native tax defaults; verify before live sales. Product references start `V113-DEMO-` for easy cleanup. Names have no demo label on the storefront.
- Products are published to the Valhalla website, available in POS, and enabled for Self Order when that app is installed. Its native default also enables products if Self Order is installed later. POS categories are **Grill & Bites** and **Drinks**; website categories use the same names. Reload an open POS after upgrading. If its configuration restricts available categories, include these categories using the native POS settings.
- The same product/variant records serve website and POS. No duplicate catalogue, stock adjustment or transaction is created. Subsequent upgrades do not recreate deleted demo products or overwrite changes.
- Primary buttons are red, secondary buttons charcoal, light buttons silver, and outline/link actions use matching brand colors. Status-specific warning/success/danger controls retain their native meaning.

Validation for this update: Odoo 19 source field/template checks, Python/XML/CSS validation, isolated catalogue setup checks with/without Self Order (including repeat-upgrade preservation), and a Bootstrap desktop/mobile fixture for automatic cycling and bottom indicator navigation passed. A live Odoo installation, event registration, website checkout and POS sale have not been run here.
