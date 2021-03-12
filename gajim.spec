Summary:	Jabber Client written in PyGTK
Name:		gajim
Version:	1.3.1.2
Release:	1
Source:		http://www.gajim.org/downloads/1.3/gajim-1.3.1-2.tar.gz
URL:		http://www.gajim.org
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
%setup -q -n %{name}-1.3.1

%build
%py_build


%install
%py_install

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="GNOME" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

find %{buildroot} -name '*.la' -delete

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING
%{_bindir}/gajim
%{_bindir}/gajim-remote
%{_bindir}/gajim-history-manager
%{_datadir}/applications/org.gajim.Gajim.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gajim.Gajim.svg
%{_iconsdir}/hicolor/scalable/apps/org.gajim.Gajim-symbolic.svg
%{_datadir}/metainfo/org.gajim.Gajim.appdata.xml
%{_mandir}/man1/gajim.1*
%{_mandir}/man1/gajim-remote.1*
%{_mandir}/man1/gajim-history-manager.1*
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-*.*.*-py3.9.egg-info/



%changelog
* Thu Oct 20 2011 Andrey Bondrov <abondrov@mandriva.org> 0.14.4-1mdv2011.0
+ Revision: 705526
- New version 0.14.4

* Sun Jun 19 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.14.2-1
+ Revision: 686021
- new version 0.14.2

* Sat Nov 27 2010 Michael Scherer <misc@mandriva.org> 0.14.1-1mdv2011.0
+ Revision: 601761
- version 0.14.1

* Wed Sep 08 2010 Michael Scherer <misc@mandriva.org> 0.14-2mdv2011.0
+ Revision: 576790
- add a Suggest on spellchecker, asked by mikala

* Mon Sep 06 2010 Michael Scherer <misc@mandriva.org> 0.14-1mdv2011.0
+ Revision: 576265
- update to 0.14

* Mon Apr 12 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.13.4-1mdv2010.1
+ Revision: 533701
- update to 0.13.4

* Sat Feb 27 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.13.3-1mdv2010.1
+ Revision: 512439
- up to 0.13.3

* Thu Feb 04 2010 Michael Scherer <misc@mandriva.org> 0.13.2-1mdv2010.1
+ Revision: 500614
- new version

* Sun Jan 03 2010 Michael Scherer <misc@mandriva.org> 0.13.1-1mdv2010.1
+ Revision: 486010
- update to 0.13.1

* Fri Nov 27 2009 Michael Scherer <misc@mandriva.org> 0.13-1mdv2010.1
+ Revision: 470705
- upgrade to 0.13
- remove patch applied upstream
- fix license

* Thu Sep 17 2009 Michael Scherer <misc@mandriva.org> 0.12.5-1mdv2010.0
+ Revision: 443920
- new version 0.12.5

* Thu Jul 23 2009 Frederik Himpe <fhimpe@mandriva.org> 0.12.3-1mdv2010.0
+ Revision: 399119
- update to new version 0.12.3

  + Michael Scherer <misc@mandriva.org>
    - new version

* Wed Apr 15 2009 Michael Scherer <misc@mandriva.org> 0.12.1-2mdv2009.1
+ Revision: 367266
- fix kde4 notification, patch adapted from upstream

* Sun Dec 21 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.1-1mdv2009.1
+ Revision: 317119
- update to new version 0.12.1

* Wed Dec 17 2008 Michael Scherer <misc@mandriva.org> 0.12-1mdv2009.1
+ Revision: 315379
- update to new version 0.12

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.11.4-1mdv2009.0
+ Revision: 140733
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.11.4-1mdv2008.1
+ Revision: 116206
- new version

* Sat Nov 17 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.11.3-1mdv2008.1
+ Revision: 109629
- New release 0.11.3

* Sun Sep 23 2007 Michael Scherer <misc@mandriva.org> 0.11.2-1mdv2008.0
+ Revision: 92338
- update to final version

* Mon Sep 10 2007 Michael Scherer <misc@mandriva.org> 0.11.2-0.pre1mdv2008.0
+ Revision: 83997
-upgrade to latest 0.11.2 prerelease, bugfixs only release


* Mon Feb 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.11.1-2mdv2007.0
+ Revision: 122646
- build system honoury bump

  + Michael Scherer <misc@mandriva.org>
    - upgrade to 0.11.1

* Tue Dec 19 2006 Michael Scherer <misc@mandriva.org> 0.11-1mdv2007.1
+ Revision: 100205
- add expat-devel to work around a strange building problem
- fix BuildRequires

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - new version
    - fix build and installation

* Tue Dec 12 2006 Michael Scherer <misc@mandriva.org> 0.10.1-5mdv2007.1
+ Revision: 95696
- rebuild for new python
- Requires bind-utils, for SRV record support ( used among other by google talk )
- Import gajim

* Wed Jun 21 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.10.1-4mdv2007.0
- Use X-MandrivaLinux-* category

* Wed Jun 14 2006 Götz Waschk <waschk@mandriva.org> 0.10.1-3mdv2007.0
- fix menu entry
- fix buildrequires

* Wed Jun 07 2006 Götz Waschk <waschk@mandriva.org> 0.10.1-2mdv2007.0
- fix buildrequires

* Tue Jun 06 2006 Jerome Soyer <saispo@mandriva.org> 0.10.1-1mdv2007.0
- New release 0.10.1

* Tue May 09 2006 Götz Waschk <waschk@mandriva.org> 0.10-2mdk
- update deps

* Wed May 03 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.10-1mdk
- New release 0.10

* Thu Jan 26 2006 Götz Waschk <waschk@mandriva.org> 0.9.1-3mdk
- fix deps

* Thu Dec 29 2005 Michael Scherer <misc@mandriva.org> 0.9.1-2mdk
- fix x86_64 build

* Tue Dec 27 2005 Michael Scherer <misc@mandriva.org> 0.9.1-1mdk
- New release 0.9.1

* Mon Dec 26 2005 Michael Scherer <misc@mandriva.org> 0.9-3mdk
- fix Requires

* Sat Dec 24 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9-2mdk
- Add BuildRequires: intltool

* Sat Dec 24 2005 Michael Scherer <misc@mandriva.org> 0.9-1mdk
- New release 0.9

* Wed Sep 07 2005 Michael Scherer <misc@mandriva.org> 0.8.2-1mdk
- New release 0.8.2
- remove patch, applied upstream

* Wed Sep 07 2005 Michael Scherer <misc@mandriva.org> 0.8.1-1mdk
- New release 0.8.1
- fix #18273 ( thanks michael reinsh )

* Thu Aug 25 2005 Michael Scherer <misc@mandriva.org> 0.8-2mdk
- add a menu ( thanks michael reinsh )
- fix #17898
- fix error in requires

* Wed Aug 24 2005 Michael Scherer <misc@mandriva.org> 0.8-1mdk
- from Matthieu Milan <matthieu.milan@gmail.com>
  - new package

