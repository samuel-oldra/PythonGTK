#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# BIBLIOTECAS
import gtk
import gtk.glade

# GLADE FILE
gladefile = gtk.glade.XML('PyToy.glade')

# WIDGETS
PyToy = gladefile.get_widget('PyToy')
txtTeste = gladefile.get_widget('txtTeste')


# FUNÇÕES ICONE BANDEJA
def notification_clicked(*args):
    if PyToy.get_property('visible'):
        PyToy.hide()
    else:
        PyToy.present()


# FUNÇÕES CLIQUE DO BOTÃO
def on_btnOK_clicked(*args):
    gtk.rc_parse('%s\gtk-2.0\gtkrc' % txtTeste.get_text())
    screen = PyToy.get_screen()
    settings = gtk.settings_get_for_screen(screen)
    gtk.rc_reset_styles(settings)


# CRIAÇÃO ICONE NA BANDEJA
icon = 'critical.png'
notificationIcon = gtk.StatusIcon()
notificationIcon.set_from_file(icon)
notificationIcon.connect("activate", notification_clicked)

events = {
    "on_PyToy_activate_default": notification_clicked,
    "on_PyToy_destroy": gtk.main_quit,
    "on_btnOK_clicked": on_btnOK_clicked
}
gladefile.signal_autoconnect(events)

gtk.main()
