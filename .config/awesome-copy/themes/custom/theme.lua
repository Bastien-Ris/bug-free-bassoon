--[[

     Vertex Awesome WM theme
     github.com/lcpz

--]]

local gears = require("gears")
local lain  = require("lain")
local awful = require("awful")
local wibox = require("wibox")
local dpi   = require("beautiful.xresources").apply_dpi

local math, string, tag, tonumber, type, os = math, string, tag, tonumber, type, os
local my_table = awful.util.table or gears.table -- 4.{0,1} compatibility





local theme                                     = {}

theme.default_dir                               = require("awful.util").get_themes_dir() .. "default"
theme.icon_dir                                  = os.getenv("HOME") .. "/.config/awesome/themes/custom/icons"
theme.wallpaper                                 = os.getenv("HOME") .. "/.config/awesome/themes/custom/wall.png"

-- define a gruvbox-palette
theme.bg                                        = "#282828"
theme.fg                                        = "#ebdbb2"
theme.red                                       = "#cc241d"
theme.green                                     = "#98971a"
theme.yellow                                    = "#d79921"
theme.blue                                      = "#458588"
theme.purple                                    = "#b16286"
theme.aqua                                      = "#689d6a"


theme.fg_focus                                  = theme.aqua
theme.bg_focus                                  = theme.bg
theme.bg_focus2                                 = theme.blue
theme.fg_urgent                                 = theme.red
theme.bg_urgent                                 = theme.yellow
theme.tasklist_fg_normal                        = theme.fg
theme.tasklist_fg_focus                         = theme.yellow
theme.tasklist_fg_urgent                        = theme.aqua
theme.tasklist_bg_normal                        = theme.bg
theme.tasklist_bg_focus                         = theme.bg
theme.tasklist_bg_urgent                        = theme.bg
theme.border_normal                             = theme.fg
theme.border_focus                              = theme.red
theme.tooltip_border_color                      = theme.fg_focus
theme.tooltip_border_width                      = theme.border_width


theme.menu_height                               = dpi(24)
theme.menu_width                                = dpi(140)
theme.awesome_icon                              = theme.icon_dir .. "/awesome.png"

theme.taglist_squares_sel                       = gears.surface.load_from_shape(dpi(15), dpi(3), gears.shape.rectangle, theme.fg_focus)
theme.taglist_squares_unsel                     = gears.surface.load_from_shape(dpi(15), dpi(3), gears.shape.rectangle, theme.bg_focus2)

theme.border_width                              = dpi(4)
theme.font                                      = "FuraCode Nerd Font 12"
theme.taglist_font                              = "FuraCode Nerd Font 14"

theme.layout_fairh                              = theme.default_dir.."/layouts/fairhw.png"
theme.layout_fairv                              = theme.default_dir.."/layouts/fairvw.png"
theme.layout_floating                           = theme.default_dir.."/layouts/floatingw.png"
theme.layout_magnifier                          = theme.default_dir.."/layouts/magnifierw.png"
theme.layout_max                                = theme.default_dir.."/layouts/maxw.png"
theme.layout_fullscreen                         = theme.default_dir.."/layouts/fullscreenw.png"
theme.layout_tilebottom                         = theme.default_dir.."/layouts/tilebottomw.png"
theme.layout_tileleft                           = theme.default_dir.."/layouts/tileleftw.png"
theme.layout_tile                               = theme.default_dir.."/layouts/tilew.png"
theme.layout_tiletop                            = theme.default_dir.."/layouts/tiletopw.png"
theme.layout_spiral                             = theme.default_dir.."/layouts/spiralw.png"
theme.layout_dwindle                            = theme.default_dir.."/layouts/dwindlew.png"
theme.layout_cornernw                           = theme.default_dir.."/layouts/cornernww.png"
theme.layout_cornerne                           = theme.default_dir.."/layouts/cornernew.png"
theme.layout_cornersw                           = theme.default_dir.."/layouts/cornersww.png"
theme.layout_cornerse                           = theme.default_dir.."/layouts/cornersew.png"
theme.tasklist_plain_task_name                  = true
theme.tasklist_disable_icon                     = true
theme.useless_gap                               = dpi(4)

-- http://fontawesome.io/cheatsheet
awful.util.tagnames = { "", "", "", "", "", "", "", "" }

local markup = lain.util.markup

-- Clock
local mytextclock = wibox.widget.textclock(markup(theme.yellow, "%a %d %b, %H:%M"))
mytextclock.font = theme.font

-- Launcher
local mylauncher = awful.widget.button({image = theme.awesome_icon})
mylauncher:connect_signal("button::press", function() awful.util.mymainmenu:toggle() end)

-- Separators
local rspace = wibox.widget.textbox(" ")
rspace.forced_width = dpi(21)







local barcolor = gears.color({
    type  = "linear",
    from  = { 0, dpi(46) },
    to    = { dpi(46), dpi(46) },
    stops = { {0, theme.bg}, {0.9, theme.bg} }
})


local dockshape = function(cr, width, height)
    gears.shape.partially_rounded_rect(cr, width, height, true, true, true, true, 8)
end

--[[function theme.vertical_wibox(s)
    -- Create the vertical wibox
    s.dockwidth = s.workarea.width / 8

    s.mytagswibox = wibox({ screen = s, x= s.workarea.width * (7/16)  , y=4, width = s.dockwidth, height = 36, fg = theme.fg, bg = theme.bg, ontop = true, visible = true, type = "dock" })

    if s.index > 1 and s.mytagswibox.y == 0 then
        s.mytagswibox.y = screen[1].mytagswibox.y
    end

    -- Add widgets to the vertical wibox
    s.mytagswibox:setup {
        layout = wibox.layout.align.horizontal,
        {
            layout = wibox.layout.fixed.horizontal,
            rspace,
            s.mytaglist,
            rspace,
            s.mylayoutbox,
            rspace
        },
    }

    -- Add toggling functionalities
    s.docktimer = gears.timer{ timeout = 2 }
    s.docktimer:connect_signal("timeout", function()
        local s = awful.screen.focused()
        s.mytagswibox.height = dpi(2)
        s.mylayoutbox.visible = false
        if s.docktimer.started then
            s.docktimer:stop()
        end
    end)
    tag.connect_signal("property::selected", function(t)
        local s = t.screen or awful.screen.focused()
        s.mytagswibox.height = dpi(36)
        s.mylayoutbox.visible = true
        gears.surface.apply_shape_bounding(s.mytagswibox, dockshape)
        if not s.docktimer.started then
            s.docktimer:start()
        end
    end)

    s.mytagswibox:connect_signal("mouse::leave", function()
        local s = awful.screen.focused()
        s.mytagswibox.height = dpi(2)
        s.mylayoutbox.visible = false
    end)

    s.mytagswibox:connect_signal("mouse::enter", function()
        local s = awful.screen.focused()
        s.mytagswibox.height = dpi(36)
        s.mylayoutbox.visible = true
        gears.surface.apply_shape_bounding(s.mytagswibox, dockshape)
    end)
end
]]

-- ALSA volume bar
local volumelabel = wibox.widget.textbox("vol: ")
theme.volume = lain.widget.alsabar({
    ticks = false, width = dpi(67),
    notification_preset = { font = theme.font },
    colors = {
        background   = theme.bg,
        mute         = theme.red,
        unmute       = theme.aqua
    }
})
theme.volume.tooltip.wibox.fg = theme.aqua
theme.volume.tooltip.wibox.font = theme.font
theme.volume.bar:buttons(my_table.join (
          awful.button({}, 1, function()
            awful.spawn(string.format("%s -e alsamixer", terminal))
          end),
          awful.button({}, 2, function()
            os.execute(string.format("%s set %s 100%%", theme.volume.cmd, theme.volume.channel))
            theme.volume.update()
          end),
          awful.button({}, 3, function()
            os.execute(string.format("%s set %s toggle", theme.volume.cmd, theme.volume.togglechannel or theme.volume.channel))
            theme.volume.update()
          end),
          awful.button({}, 4, function()
            os.execute(string.format("%s set %s 2%%+", theme.volume.cmd, theme.volume.channel))
            theme.volume.update()
          end),
          awful.button({}, 5, function()
            os.execute(string.format("%s set %s 2%%-", theme.volume.cmd, theme.volume.channel))
            theme.volume.update()
        end)

))
local volumebg = wibox.container.background(theme.volume.bar, theme.blue, gears.shape.rectangle)
local volumewidget = wibox.container.margin(volumebg, dpi(7), dpi(7), dpi(5), dpi(5))

-- CPU 


-- CPU
local cpuicon = wibox.widget.textbox('cpu: ')
local cpu = lain.widget.cpu({
    settings = function()
        widget:set_markup(markup.fontfg(theme.font, theme.blue, cpu_now.usage .. "% "))
    end
})

-- Coretemp
local temp = lain.widget.temp({
    settings = function()
        widget:set_markup(markup.fontfg(theme.font, theme.purple, coretemp_now .. "°C "))
    end
})


-- RAM


-- MEM
local memicon = wibox.widget.textbox('ram: ')
local memory = lain.widget.mem({
    settings = function()
        widget:set_markup(markup.fontfg(theme.font, theme.green, mem_now.used .. "M "))
    end
})

-- Clipmenu




function theme.at_screen_connect(s)
    -- Quake application
    s.quake = lain.util.quake({ app = awful.util.terminal, border = theme.border_width })

    -- If wallpaper is a function, call it with the screen
    local wallpaper = theme.wallpaper
    if type(wallpaper) == "function" then
        wallpaper = wallpaper(s)
    end
    gears.wallpaper.maximized(wallpaper, s, true)

    -- Tags
    awful.tag(awful.util.tagnames, s, awful.layout.layouts[1])

    -- Create a promptbox for each screen
    s.mypromptbox = awful.widget.prompt()
    s.mypromptbox.bg = theme.bg 

    -- Create an imagebox widget which will contains an icon indicating which layout we're using.
    -- We need one layoutbox per screen.
    s.mylayoutbox = awful.widget.layoutbox(s)
    s.mylayoutbox:buttons(my_table.join(
                           awful.button({}, 1, function () awful.layout.inc(-1) end),
                           awful.button({}, 2, function () awful.layout.set(awful.layout.layouts[1] ) end),
                           awful.button({}, 3, function () awful.layout.inc(-1) end),
                           awful.button({}, 4, function () awful.layout.inc(-1) end),
                           awful.button({}, 5, function () awful.layout.inc(-1) end)))

    -- Create a taglist widget
    s.mytaglist = awful.widget.taglist(s, awful.widget.taglist.filter.all, awful.util.taglist_buttons)

    -- Create a tasklist widget
    s.mytasklist = awful.widget.tasklist(
        s,
        awful.widget.tasklist.filter.currenttags, 
        awful.util.tasklist_buttons)


    -- Create the wibox
    s.mywibox = awful.wibar({ position = "bottom", screen = s, height = dpi(25), bg = theme.bg })

    -- Add widgets to the wibox
    s.mywibox:setup {
        layout = wibox.layout.align.horizontal,
        expand = "none",
        { -- Left widgets
            layout = wibox.layout.fixed.horizontal,
            mylauncher, 
            tspace1,
            s.mylayoutbox,
            tspace1,
        },
        { -- Middle widgets
            layout = wibox.layout.flex.horizontal,
            s.mytasklist
            
            
        },
        { -- Right widgets
            layout = wibox.layout.fixed.horizontal,
            memicon,
            memory,
            cpuicon,
            cpu,
            temp,
            volumelabel,
            volumewidget,
            mytextclock
        },
    }

   -- gears.timer.delayed_call(theme.vertical_wibox, s)
end

return theme
