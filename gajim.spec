%define name	gajim
%define version	0.11.2
%define rel 0.pre1
%define Summary	Jabber Client written in PyGTK


Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Source:		http://www.gajim.org/downloads/gajim-%{version}-pre1.tar.bz2
URL:		http://www.gajim.org
Group:		Networking/Instant messaging
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	python >= %{pyver}
Requires:       pygtk2.0-libglade python-sqlite2
Requires:       gnome-python-gconf
Requires:       gnome-python-extras
Requires:       dbus-python bind-utils
BuildRequires:	gnome-python-extras
BuildRequires:	gtkspell-devel gtk2-devel pygtk2.0-devel
BuildRequires:  libxscrnsaver-devel
BuildRequires:  libexpat-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  dbus-devel
# required, or we see 
#  creating gtkspell.la
#  /bin/sed: can't read /usr/lib/libexpat.la: No such file or directory
#  libtool: link: `/usr/lib/libexpat.la' is not a valid libtool archive
#  make[3]: *** [gtkspell.la] Error 1
# on x86 ( and not on x86_64 )
# may have to be removed in the future, when the real problem is fixed
BuildRequires:  expat-devel

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
# (misc) yes, weird tarball
%setup -q -n %{name}-0.11.1.4 
# (misc) rapid fix, need to be changed upstream
perl -pi -e 's/Icon=gajim.png/Icon=gajim/' data/gajim.desktop.in.in
perl -pi -e 's/Version=.*/Version=0.9.5/'  data/gajim.desktop.in.in

%build
%configure2_5x
%make 

%install
rm -rf $RPM_BUILD_ROOT installed-docs
%makeinstall_std
mv %buildroot%_datadir/doc/gajim installed-docs

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GNOME" \
  --add-category="X-MandrivaLinux-Internet-InstantMessaging" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

mkdir -p %buildroot/%_iconsdir
mkdir -p %buildroot/%_liconsdir
mkdir -p %buildroot/%_miconsdir

convert $RPM_BUILD_ROOT/%_datadir/%name/data/pixmaps/gajim.png -resize 32x32 %buildroot/%_iconsdir/%name.png
convert $RPM_BUILD_ROOT/%_datadir/%name/data/pixmaps/gajim.png -resize 16x16 %buildroot/%_miconsdir/%name.png
convert $RPM_BUILD_ROOT/%_datadir/%name/data/pixmaps/gajim.png -resize 48x48 %buildroot/%_liconsdir/%name.png

rm -f %buildroot%_libdir/%name/*.la


%find_lang %{name} 
%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root)
%doc installed-docs/*
%{_bindir}/gajim
%{_bindir}/gajim-remote
%{_datadir}/applications/gajim.desktop
%{_datadir}/gajim
%{_datadir}/pixmaps/gajim.png
%{_datadir}/pixmaps/gajim_about.png
%dir %{_libdir}/gajim
%{_libdir}/gajim/gtkspell.so
%{_libdir}/gajim/idle.so
%{_libdir}/gajim/trayicon.so
%doc %{_mandir}/man1/gajim.1*
%doc %{_mandir}/man1/gajim-remote.1*
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png


