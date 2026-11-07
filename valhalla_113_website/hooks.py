def uninstall_hook(env):
    websites = env["website"].search([
        ("valhalla_branding_enabled", "=", True),
        ("homepage_url", "=", "/valhalla-113"),
    ])
    websites.write({"homepage_url": False})
