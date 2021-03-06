
#########################################
##  ____ ____   ___  _   _ ____  ____  ##
## / ___|  _ \ / _ \| | | |  _ \/ ___| ##
##| |  _| |_) | | | | | | | |_) \___ \ ##
##| |_| |  _ <| |_| | |_| |  __/ ___) |##
## \____|_| \_\\___/ \___/|_|   |____/ ##
#########################################
import os
from libqtile import layout
from libqtile.config import Group, Match, ScratchPad, DropDown 
from appearance import layout_theme, floating_layout_theme, treetab_layout_theme


groups= [
    Group("1",
          label= "",
          #label= "",
          layouts=[
            layout.MonadTall(**layout_theme, ratio=0.5),
   	        layout.MonadThreeCol(**layout_theme, ),
            layout.Bsp(**layout_theme, fair=True),
            layout.Floating(**floating_layout_theme),
                ] 
          ),

    Group("2",
          label="",
          #label= "",
          persist=True,
          init=True,
          layouts=[
            layout.MonadTall(**layout_theme,  ratio=0.5 ),
   	        layout.MonadThreeCol(**layout_theme),
            layout.Bsp(**layout_theme, fair=True),
            layout.Floating(**floating_layout_theme),
                ] 
          ),

    Group("3",
          label= "",
          #label= "",
          persist=True,
          init=True,
          layouts=[
            layout.MonadTall(**layout_theme, ratio=0.5),
   	        layout.MonadThreeCol(**layout_theme),
            layout.Bsp(**layout_theme, fair=True),
            layout.Floating(**floating_layout_theme),
                ]   
          ),

    Group("4",
          label= "", 
          #label="",
          persist=True,
          init=True,
          layouts=[
            layout.MonadTall(**layout_theme, ratio=0.5),
   	        layout.MonadThreeCol(**layout_theme),
            layout.Bsp(**layout_theme, fair=True),
            layout.Floating(**floating_layout_theme),
                ] 
          ),

    Group("5",
          label = "", 
          #label="",
          persist=True,
          init=True,
          layouts=[
            layout.MonadTall(**layout_theme, ratio=0.5),
   	        layout.MonadThreeCol(**layout_theme),
            layout.Bsp(**layout_theme, fair=True),
            layout.Floating(**floating_layout_theme),
                ]
          ),

    Group("6",
          label= "", 
          #label="",
          persist=True,
          init=True,
          layouts=[
            layout.MonadTall(**layout_theme, ratio=0.5),
   	        layout.MonadThreeCol(**layout_theme),
            layout.Bsp(**layout_theme, fair=True),
            layout.Floating(**floating_layout_theme),
                ]
          ),

    Group("7",
          label="",
          #label="",
          persist=True,
          init=True,
          layouts=[
            layout.MonadTall(**layout_theme, ratio=0.5),
   	        layout.MonadThreeCol(**layout_theme),
            layout.Bsp(**layout_theme, fair=True),
            layout.Floating(**floating_layout_theme),
                ]
          ),

    Group("8",
          label = "",
          #label="",
          persist=True,
          init=True,
          layouts=[
            layout.MonadTall(**layout_theme, ratio=0.5),
   	        layout.MonadThreeCol(**layout_theme),
            layout.Bsp(**layout_theme, fair=True),
            layout.Floating(**floating_layout_theme),
                ],
          ),

    Group("9",
          label="",
          persist=True,
          init=True,
          layouts=[
            layout.MonadTall(**layout_theme, ratio=0.5),
   	        layout.MonadThreeCol(**layout_theme),
            layout.Bsp(**layout_theme, fair=True),
            layout.Floating(**floating_layout_theme),
                ]
          ),

   Group("e",
          label="𝓔",
          matches=Match(wm_class=["emacs", "Emacs"]),
          persist=False,
          init=False,
          layouts=[
            layout.Max(**layout_theme),
            layout.TreeTab(**treetab_layout_theme),
            layout.MonadTall(**layout_theme, ratio=0.66),
            layout.Floating(**floating_layout_theme),
                ] 
          ),


    Group("f",
          label="",
          matches=Match(wm_class=["firefox", "Firefox"]),
          persist=False,
          init=False,
          layouts=[
            layout.Max(**layout_theme),
            layout.TreeTab(**treetab_layout_theme),
            layout.MonadTall(**layout_theme, ratio=0.66),
            layout.Floating(**floating_layout_theme),
               ]
            ),

    Group("o",
          label="",
          matches=Match(wm_class=["libreoffice", "LibreOffice"]),
          persist=False,
          init=False,
          layouts=[
              layout.Max(**layout_theme),
              layout.TreeTab(**treetab_layout_theme),
              layout.MonadTall(**layout_theme, ratio=0.66),
              layout.Floating(**floating_layout_theme),
                ]
          ),

    Group("i",
          label="",
          matches=Match(wm_class=[
                "gimp", "Gimp"
                "org.inkscape.Inkscape", "Inkscape",
                "geeqie", "Geeqie"
                ]),
          persist=False,
          init=False,
          layouts=[
              layout.Max(**layout_theme), 
              layout.TreeTab(**treetab_layout_theme ),
              layout.Floating(**floating_layout_theme),
                ]
    ),

    Group("g",
          label="",
          matches=Match(wm_class=[
                "steam", "Steam"
                ]),
          persist=False,
          init=False,
          layouts=[
              layout.Max(**layout_theme), 
              layout.Floating(**floating_layout_theme),
                ]
    ),

    Group("v",
       label="",
       matches=Match(wm_class=[
            "vmware-view", "Vmware-view",
            "virt-manager", "Virt-manager"
            ]),
        persist=False,
        init=False,
        layouts=[
            layout.MonadThreeCol(**layout_theme), 
            layout.TreeTab(**treetab_layout_theme ),
            layout.Floating(**floating_layout_theme),
               ]
    ),
]
###############################################################################
########   ScratchPad:
###############################################################################

groups.append(ScratchPad("scratch", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "kitty",
           x=0.6, y=0, width=0.4, height=0.8, opacity = 1, 
            on_focus_lost_hide=True),
        DropDown("web", "kitty -e lynx 'www.duckduckgo.com'",
           x=0.6, y=0, width=0.4, height=0.8, opacity = 1, 
            on_focus_lost_hide=True),
        DropDown("mails", "thunderbird",
            x=0.5, y=0, width=0.5, height=0.8, opacity = 1, 
           on_focus_lost_hide=False), 
        DropDown("music", "spotify",
           x=0.5, y=0, width=0.5, height=0.8, opacity = 1, 
           on_focus_lost_hide=True), 
        DropDown("files", "kitty -e ranger",
           x=0.5, y=0, width=0.5, height=0.8, opacity =1, 
           on_focus_lost_hide=True), 
        DropDown("math", "galculator",
            x=0.4, y=0.4, width=0.2, height=0.2, opacity = 1, 
           on_focus_lost_hide=True) 
        ]))
 
