#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2020/11/1 11:17
@Author : chenzhixu
@Email : 1195733026@qq.com
@File : __init__.py
@Project : AutoTestPlatform
"""

from selenium.webdriver.common.by import By


class B:
    hwmconf_welcome_login_btn = By.ID, "hwmconf_welcome_login_btn"
    login_choice_title = By.ID, "login_choice_title"
    hwmconf_login_account_input = By.ID, "hwmconf_login_account_input"
    hwmconf_login_password_input = By.ID, "hwmconf_login_password_input"
    hwmconf_login_login_btn = By.ID, "hwmconf_login_login_btn"
    privacy_dialog_title = By.ID, "privacy_dialog_title"
    hwmconf_dialog_button_right = By.ID, "hwmconf_dialog_button_right"
    hwmconf_mine_mine_tab = By.ID, "hwmconf_mine_mine_tab"
    hwmconf_mine_settings = By.ID, "hwmconf_mine_settings"
    hwmconf_minesetting_call_setting = By.ID, "hwmconf_minesetting_call_setting"
    hwmconf_minesetting_log_out = By.ID, "hwmconf_minesetting_log_out"
    base_dialog_title = By.ID, "base_dialog_title"
    hwmconf_dialog_button_left = By.ID, "hwmconf_dialog_button_left"
    hwmconf_conflist_meetings_tab = By.ID, "hwmconf_conflist_meetings_tab"
    hwmconf_conflist_conf_schedule = By.ID, "hwmconf_conflist_conf_schedule"
    conf_input_edittext = By.ID, "conf_input_edittext"
    hwmconf_conf_media_type_btn = By.ID, "hwmconf_conf_media_type_btn"
    hwmconf_meeting_ID_type = By.ID, "hwmconf_meeting_ID_type"
    set_conf_pwd_layout = By.ID, "set_conf_pwd_layout"
    hwmconf_open_password = By.ID, "hwmconf_open_password"
    hwmconf_password_input = By.ID, "hwmconf_password_input"
    conf_btn_one = By.ID, "conf_btn_one"
    hwmconf_advanced_settings = By.ID, "hwmconf_advanced_settings"
    hwmconf_conf_recording_switch = By.ID, "hwmconf_conf_recording_switch"
    hwmconf_confadvancesetting_email_notify = By.ID, "hwmconf_confadvancesetting_email_notify"
    hwmconf_confadvancesetting_sms_notify = By.ID, "hwmconf_confadvancesetting_sms_notify"
    hwmconf_confadvancesetting_email_calendar = By.ID, "hwmconf_confadvancesetting_email_calendar"
    hwmconf_confadvancesetting_time_zone = By.ID, "hwmconf_confadvancesetting_time_zone"
    navigation_back = By.ID, "navigation_back"
    hwmconf_participants_add = By.ID, "hwmconf_participants_add"
    conf_search_wrap = By.CSS_SELECTOR, "input[data-testid^='mSelectBoxSearchInput']"
    conf_search_content_item0 = By.CSS_SELECTOR, "div[data-testid^='mSelectBoxContactItem0Warp']"
    conf_search_content_expand_btn = By.CSS_SELECTOR, "div[data-testid^='mSelectBoxContactItem0Warp'] div.m-select-box-item-line div.m-select-box-item-btn"
    conf_search_attendees = By.CSS_SELECTOR, "div[data-testid^='mSelectBoxItemNumberListItem'] div.m-select-box-item-nl-item-content span"
    conf_search_add_confirm_btn = By.CSS_SELECTOR, "div[data-testid^='mSelectBoxCompleteBtn']"
