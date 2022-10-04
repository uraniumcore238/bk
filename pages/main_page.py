from selene.support.shared.jquery_style import s


class MainPage:

    logo = s("[class*='wrapperDesktop'] [class*='logoLink']")
    download = s("[data-link-id='download']")
    nitro = s("[data-link-id='nitro']")
    discover = s("[data-link-id='discover']")
    safety = s("[data-link-id='safetycenter']")
    support = s("[data-link-id='helpandsupport']")
    blog = s("[data-link-id='blog']")
    careers = s("[data-link-id='careers']")
    login_btn = s("[class*='wrapperDesktop'] .gtm-click-class-login-button")