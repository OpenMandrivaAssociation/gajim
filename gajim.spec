Summary:	Jabber Client written in PyGTK
Name:		gajim
Version:	1.7.3
Release:	4
Source:		http://www.gajim.org/downloads/1.7/gajim-%{version}.tar.gz
URL:		https://www.gajim.org
Group:		Networking/Instant messaging
License:	GPLv3

BuildRequires:	intltool
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)

Requires:	glib-networking
Requires:	python3dist(pycurl)
Requires:	python3dist(dbus-python)
Requires:	python3dist(pygobject)
Requires:	python3dist(pyopenssl)
Requires:	python3dist(nbxmpp)
Requires:	python-pkg-resources
Requires:	python3dist(pyasn1)
Requires:	python3dist(keyring)

Recommends:	python-axolotl
Recommends:	python-gnupg
Recommends:	python3dist(idna)
Recommends:	python3dist(pillow)
Recommends:	typelib(Farstream) == 0.2
Recommends:	typelib(GUPnP) == 1.0
Recommends:	typelib(GstAudio) == 1.0
Recommends:	typelib(Geoclue) == 2.0
Recommends:	typelib(Gspell) == 1
Recommends:	typelib(Secret) == 1
Recommends:	typelib(NetworkManager) == 1.0

%define debug_package %{nil}

%description
Gajim is a jabber client written in PyGTK. The goal of Gajim's developers is
to provide a full featured and easy to use xmpp client for the GTK+
users. Gajim does not require GNOME to run, eventhough it exists with it
nicely. Gajim is released under the GNU General Public License

Features:
- Tabbed chat windows
- Groupchat support (with MUC protocol)
- Emoticons, URL grabber
- Systray icon
- TLS & GPG support
- Transport Registration support
- Service Discovery including Nodes
- Multiple accounts support

%prep
%setup -q -n %{name}-%{version}

%build
%py_build

%install
%py_install

find %{buildroot} -name '*.la' -delete

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/gajim
%{_bindir}/gajim-remote
#{_datadir}/applications/org.gajim.Gajim.desktop
#{_iconsdir}/hicolor/scalable/apps/*.svg
#{_datadir}/metainfo/org.gajim.Gajim.appdata.xml
%{python_sitelib}/%{name}
#{python_sitelib}/%{name}-*.egg-info
#{_mandir}/man1/*.1*
