%global glib2_version 2.55.0

Name:           libdazzle
Version:        3.28.5
Release:        3%{?dist}
Summary:        Experimental new features for GTK+ and GLib

License:        GPLv3+
URL:            https://git.gnome.org/browse/libdazzle/
Source0:        https://download.gnome.org/sources/%{name}/3.28/%{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gmodule-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

# for tests
BuildRequires:  dbus
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  words

Requires:       glib2%{?_isa} >= %{glib2_version}

%description
libdazzle is a collection of fancy features for GLib and Gtk+ that aren't quite
ready or generic enough for use inside those libraries. This is often a proving
ground for new widget prototypes. Applications such as Builder tend to drive
development of this project.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# https://bugzilla.redhat.com/show_bug.cgi?id=1972097
%ifarch x86_64
Conflicts:      %{name}-devel(x86-32) <= %{version}-%{release}
%else
%ifarch i686
Conflicts:      %{name}-devel(x86-64) <= %{version}-%{release}
%endif
%endif

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson -D enable_gtk_doc=true
%meson_build


%install
%meson_install


%check
dbus-run-session -- xvfb-run -w 10 ninja test %{__ninja_common_opts} -C %{_vpath_builddir}


%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/dazzle-list-counters
%{_libdir}/libdazzle-1.0.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Dazzle-1.0.typelib

%files devel
%doc CONTRIBUTING.md examples
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Dazzle-1.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libdazzle
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libdazzle-1.0.*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libdazzle-1.0.pc


%changelog
* Wed May 24 2023 Kalev Lember <klember@redhat.com> - 3.28.5-3
- Add Conflicts for i686/x86_64 devel subpackage
- Resolves: #1972097

* Mon Feb 01 2021 Kalev Lember <klember@redhat.com> - 3.28.5-2
- Rebuild to ship libdazzle-devel in CRB
- Resolves: #1919429

* Sat Jul 28 2018 Kalev Lember <klember@redhat.com> - 3.28.5-1
- Update to 3.28.5

* Fri Jul 27 2018 Kalev Lember <klember@redhat.com> - 3.28.4-1
- Update to 3.28.4

* Tue Jun 26 2018 Kalev Lember <klember@redhat.com> - 3.28.3-1
- Update to 3.28.3

* Thu May 24 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Tue Apr 10 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Wed Mar 14 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Sat Mar 03 2018 Kalev Lember <klember@redhat.com> - 3.27.91-1
- Update to 3.27.91

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Kalev Lember <klember@redhat.com> - 3.27.90-1
- Update to 3.27.90
- Drop ldconfig scriptlets

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.5-2
- Switch to %%ldconfig_scriptlets

* Sun Jan 28 2018 Kalev Lember <klember@redhat.com> - 3.27.5-1
- Update to 3.27.5

* Tue Dec 19 2017 Kalev Lember <klember@redhat.com> - 3.27.3-1
- Update to 3.27.3
- Set minimum required glib version

* Tue Oct  3 2017 Yanko Kaneti <yaneti@declera.com> - 3.26.1-1
- Update to 3.26.1

* Tue Sep 12 2017 Yanko Kaneti <yaneti@declera.com> - 3.26.0-1
- Update to 3.26.0

* Tue Sep  5 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.92-1
- Update to 3.25.92
- Reenable test-fuzzy-index, should be fixed upstream

* Sun Aug 27 2017 Kalev Lember <klember@redhat.com> - 3.25.91-1
- Update to 3.25.91

* Tue Aug  8 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.90-1
- Update to 3.25.90

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.5-1
- Update to 3.25.5

* Wed Jul 19 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.4-1
- Update to 3.25.4. Add tests, BR: xorg-x11-server-Xvfb, words, dbus

* Tue Jul 18 2017 Kalev Lember <klember@redhat.com> - 3.25.3-3
- Drop the workaround as meson is now fixed

* Thu Jun 22 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.3-2
- Add temporary workaround for meson 0.41.1 breakage

* Mon Jun 19 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.3-1
- Initial spec
