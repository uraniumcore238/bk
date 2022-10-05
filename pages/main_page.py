from selene.support.shared.jquery_style import s


class MainPage:

    header_element = s("[class*='wrapperDesktop']")
    mobile_header_element = s("[class*='wrapperMobile']")
    logo = header_element.s("[class*='logoLink']")
    mobile_logo = mobile_header_element.s("[class*='logoLink']")
    download = s("[data-link-id='download']")
    nitro = s("[data-link-id='nitro']")
    discover = s("[data-link-id='discover']")
    safety = s("[data-link-id='safetycenter']")
    support = s("[data-link-id='helpandsupport']")
    blog = s("[data-link-id='blog']")
    careers = s("[data-link-id='careers']")
    login_btn = header_element.s(".gtm-click-class-login-button")
    mobile_login_btn = mobile_header_element.s(".gtm-click-class-login-button")

    # Side menu
    side_menu_button = mobile_header_element.s("[class*='menuIcon']")
    side_menu = s("[class*='panelThemed']")
    home_side_menu = side_menu.s("//span[.='Home']")
    download_side_menu = side_menu.s("[href='/download']")
    nitro_side_menu = side_menu.s("[href='/nitro']")
    discover_side_menu = side_menu.s("[href='/servers']")
    safety_side_menu = side_menu.s("//span[.='Safety']")
    mod_academy_side_menu = side_menu.s("//span[.='Mod Academy']")
    support_side_menu = side_menu.s("[href='//support.discord.com/hc/en-us']")
    blog_side_menu = side_menu.s("[href='/blog']")
    careers_side_menu = side_menu.s("[href='/jobs']")
    download_button = s("[class*='downloadButtonWrapper']")
