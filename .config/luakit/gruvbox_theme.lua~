--------------------------
-- Default luakit theme --
--------------------------

-- get color tables from pywal
function getColors()
  local colorTable = {}
 local home = os.getenv("HOME")
  local pywal_colors  = home .. "/.cache/wal/colors"
  file = io.open(pywal_colors, "r")
  for line in file:lines() do
    table.insert(colorTable,line) 
  end
  return colorTable
end

local colors = getColors()


local theme = {}

-- Default settings
theme.font = "15px Luxi Mono Regular"
theme.fg   = colors[8]
theme.bg   = colors[4]

-- General colours
theme.success_fg = colors[8]
theme.loaded_fg  = colors[8]
theme.error_fg = colors[8]
theme.error_bg = colors[4]

-- Warning colours
theme.warning_fg = colors[8]
theme.warning_bg = colors[6]

-- Notification colours
theme.notif_fg = colors[8]
theme.notif_bg = colors[3]

-- Menu colours
theme.menu_fg                   = colors[8]
theme.menu_bg                   = colors[1]
theme.menu_selected_fg          = colors[8]
theme.menu_selected_bg          = colors[4]
theme.menu_title_bg             = colors[3]
theme.menu_primary_title_fg     = colors[8]
theme.menu_secondary_title_fg   = colors[2]

theme.menu_disabled_fg = colors[8]
theme.menu_disabled_bg = theme.menu_bg
theme.menu_enabled_fg = theme.menu_fg
theme.menu_enabled_bg = theme.menu_bg
theme.menu_active_fg = colors[8]
theme.menu_active_bg = theme.menu_bg

-- Proxy manager
theme.proxy_active_menu_fg      = colors[8]
theme.proxy_active_menu_bg      = colors[3]
theme.proxy_inactive_menu_fg    = colors[9]
theme.proxy_inactive_menu_bg    = colors[4]

-- Statusbar specific
theme.sbar_fg         = colors[8]
theme.sbar_bg         = colors[3]

-- Downloadbar specific
theme.dbar_fg         = colors[8]
theme.dbar_bg         = colors[4]
theme.dbar_error_fg   = colors[6]

-- Input bar specific
theme.ibar_fg           = colors[8]
theme.ibar_bg           = colors[1]

-- Tab label
theme.tab_fg            = colors[8]
theme.tab_bg            = colors[1]
theme.tab_hover_bg      = colors[6]
theme.tab_ntheme        = colors[7]
theme.selected_fg       = colors[1]
theme.selected_bg       = colors[3]
theme.selected_ntheme   = colors[3]
theme.loading_fg        = colors[8]
theme.loading_bg        = colors[5]

theme.selected_private_tab_bg = "#3d295b"
theme.private_tab_bg    = "#22254a"

-- Trusted/untrusted ssl colours
theme.trust_fg          = colors[4]
theme.notrust_fg        = colors[5]

-- Follow mode hints
theme.hint_font = "15px Luxi Mono Regular"
theme.fg   = colors[8]
theme.bg   = colors[3]
theme.hint_fg = colors[1]
theme.hint_bg = colors[2]
theme.hint_border = "1px solid color[1]"
theme.hint_opacity = 0.4
theme.hint_overlay_bg = colors[5]
theme.hint_overlay_border = "0px dotted #888"
theme.hint_overlay_selected_bg = colors[6]
-- theme.hint_overlay_selected_border = theme.hint_overlay_border

-- General colour pairings
theme.ok = { fg = colors[8], bg = colors[1] }
theme.warn = { fg = colors[8], bg = colors[3] }
theme.error = { fg = colors[8] , bg = colors }

-- Gopher page style (override defaults)
theme.gopher_light = { bg = colors[8], fg = colors[1], link = colors[4] }
theme.gopher_dark  = { bg = colors[1], fg = colors[8], link = colors[6] }

return theme

-- vim: et:sw=4:ts=8:sts=4:tw=88
