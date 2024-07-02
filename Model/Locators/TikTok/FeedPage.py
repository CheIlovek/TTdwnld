CURRENT_VIDEO       = R"//div[contains(@class,'e1yey0rl2')]/div" #get ID video xgwrapper-0-7332342275151760642 -> 7332342275151760642
CURRENT_CHANNEL     = CURRENT_VIDEO + R"/../../../../../../div[1]//h3" #get text
PREVIEW_IMG         = CURRENT_VIDEO + R"/../../../../../..//img[@imagex-type='react']" #get src
CURRENT_VIDEO_URL   = R"//video[1]"
LIKE_BUTTON         = R"//div[contains(@class,'e1yey0rl2')]/../../../../..//button[contains(@aria-label, 'Поставить лайк')]"
