
"""
def find_or_run(app, classes=(), group="", processes=()):
    if not processes:
        processes = [regex(app.split('/')[-1])]

    def __inner(qtile):
        if classes:
            for window in qtile.windowMap.values():
                for c in classes:
                    if window.group and window.match(wmclass=c):
                        qtile.currentScreen.setGroup(window.group)
                        window.group.focus(window, False)
                        return
        if group:
            lines = subprocess.check_output(["/usr/bin/ps", "axw"]).decode("utf-8").splitlines()
            ls = [line.split()[4:] for line in lines][1:]
            ps = [' '.join(l) for l in ls]
            for p in ps:
                for process in processes:
                    if re.match(process, p):
                        qtile.groupMap[group].cmd_toscreen()
                        return
        subprocess.Popen(app.split())

    return __inner

#to implement? Usage = Key([mod], "e", lazy.function(find_or_run("/usr/bin/leafpad")))
"""

