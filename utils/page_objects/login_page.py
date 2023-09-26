from selenium.webdriver.common.by import By


class LoginPagePageObject:
    """Login form"""
    login_form = (By.CSS_SELECTOR, ".passp-auth-content")
    back_button = (By.CSS_SELECTOR, "[data-t='backpane']")
    ya_id_logo = (By.CSS_SELECTOR, ".IdLogo")
    login_form_title = (By.CSS_SELECTOR, "[data-t='title']")
    login_by_email_button = (By.CSS_SELECTOR, ".AuthLoginInputToggle-type")
    login_by_phone_button = (By.CSS_SELECTOR, ".AuthLoginInputToggle-type")
    login_by_qr_button = (By.CSS_SELECTOR, ".AuthPasswordForm-qr-button")
    email_input = (By.CSS_SELECTOR, "[data-t='field:input-login']")
    password_input = (By.CSS_SELECTOR, "[data-t='field:input-passwd']")
    phone_input = (By.CSS_SELECTOR, "[id='passp-field-phone']")
    forgot_password_button = (By.CSS_SELECTOR, "[id='field:link-passwd']")
    auth_error_label = (By.CSS_SELECTOR, "[data-t='field:input-passwd:hint']")
    back_to_email_button = (By.CSS_SELECTOR, ".CurrentAccount")
    sign_in_button = (By.CSS_SELECTOR, "[id='passp:sign-in']")
    create_id_button = (By.CSS_SELECTOR, "[id='passp:exp-register']")
    auth_social_title = (By.CSS_SELECTOR, ".AuthSocialBlock-title")
    auth_by_vk_button = (By.CSS_SELECTOR, "[data-t='provider:primary:vk']")
    auth_by_gg_button = (By.CSS_SELECTOR, "[data-t='provider:primary:gg']")
    auth_by_qr_button = (By.CSS_SELECTOR, "[data-t='provider:primary:qr']")
    auth_by_fb_button = (By.CSS_SELECTOR, "[data-t='provider:primary:fb']")
    auth_social_more_button = (By.CSS_SELECTOR, "[data-t='provider:more']")
    auth_by_mr_button = (By.CSS_SELECTOR, "[data-t='provider:primary:mr']")
    auth_by_ok_button = (By.CSS_SELECTOR, "[data-t='provider:primary:ok']")
    auth_by_tw_button = (By.CSS_SELECTOR, "[data-t='provider:primary:tw']")
